import asyncio
import mysql.connector
from mysql.connector.errors import Error, OperationalError
from typing import List, Generator, Tuple, Callable
from enum import Enum
from datetime import datetime, timedelta
from contextlib import suppress

from aiess.objects import User, Beatmapset, BeatmapsetStatus, Beatmap, Discussion, Event, NewsPost, Usergroup
from aiess.settings import DB_CONFIG
from aiess.logger import log
from aiess.common import anext
from aiess.errors import DeletedContextError
from aiess import event_types as types

SCRAPER_DB_NAME      = "aiess"
SCRAPER_TEST_DB_NAME = "aiess_test"

class InterpolationDict(dict):
    def __missing__(self, key):
        return "%(" + key + ")s"

class Database:
    """Creates an aiess database connection."""
    class Table(Enum):
        # External code should be able to refer to specific tables,
        # while not breaking if we change anything in the actual database.
        EVENTS             = "events"
        BEATMAPSETS        = "beatmapsets"
        DISCUSSIONS        = "discussions"
        DISCUSSION_REPLIES = "discussion_replies"
        USERS              = "users"

    def __init__(self, _db_name: str, timeout_ms: float=20000):
        self.db_name    = _db_name
        self.timeout_ms = timeout_ms
        db_config = {
            "host":     DB_CONFIG["host"],
            "port":     int(DB_CONFIG["port"]),
            "database": self.db_name,
            "user":     DB_CONFIG["user"],
            "password": DB_CONFIG["password"]
        }
        
        try:
            self.connection = mysql.connector.connect(**db_config)
        except Error as error:
            raise ValueError(f"Could not connect to MySQL; {error}")

        # Prevents DoS from complex SELECT queries.
        # See https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_max_execution_time.
        self._execute(f"SET SESSION MAX_EXECUTION_TIME={timeout_ms}")
    
    def __get_cursor(self):
        attempts = 0
        while(attempts < 3):
            attempts += 1
            try:
                return self.connection.cursor()
            except OperationalError as error:
                log(f"WARNING | {error}")
                self.__init__(self.db_name)

    def __del__(self):
        """Clears up allocated resources such as memory upon destruction."""
        if (hasattr(self, "connection") and self.connection.is_connected()):
            self.connection.cursor().close()
            self.connection.close()
    
    def __fetch(self, cursor: object) -> List[tuple]:
        """Attempts to return fetch all from a cursor object. Does not throw if nothing to fetch.
        Returns the fetched result sets as a list of tuples, or None if no result."""
        try:
            # Fetch entire result set so nothing carries over to the next query.
            return cursor.fetchall()
        except mysql.connector.errors.InterfaceError as error:
            if error.msg == "No result set to fetch from.":
                return None  # Reached end of result set, not an issue.
            raise

    def _check_for_timeout(self, func: Callable, args: List[object], timeout: float) -> None:
        """Runs function `func` with arguments `args` until it ends. If this took more than `timeout`
        milliseconds, `TimeoutError` is raised."""
        start_time = datetime.utcnow()
        func(*args)
        delta_time = datetime.utcnow() - start_time
        if delta_time > timedelta(milliseconds=self.timeout_ms):
            raise TimeoutError("database execution time exceeded")

    def _execute(self, query: str, values: tuple=None) -> List[tuple]:
        """Executes the given SQL query with the given argument values, if any. Use like "%s" in query
        and ("name",) in values. Returns the fetched result sets as a list of tuples, or None if no result."""
        cursor = self.__get_cursor()
        cursor.nextset()
        self._check_for_timeout(
            func    = cursor.execute,
            args    = [query, values],
            timeout = self.timeout_ms
        )

        fetch = self.__fetch(cursor)
        cursor.close()
        self.connection.commit()
        return fetch
    
    def __execute_dict(self, query: str, **values: object) -> List[tuple]:
        """Executes the given SQL query with the given argument values, if any. Use like "%(name)s" in query
        and name=name in values. Returns the fetched result sets as a list of tuples, or None if no result."""
        return self._execute(query, values)
    
    def __executemany(self, query: str, values: List[tuple]) -> List[tuple]:
        """Executes the given SQL query over multiple values (e.g. list or array of tuples).
        Use like "%s, %s" in query and array of (id, name) in values.
        Returns the fetched result sets as a list of tuples, or None of no result."""
        cursor = self.connection.cursor()
        cursor.nextset()
        cursor.executemany(query, values)

        fetch = self.__fetch(cursor)
        self.connection.commit()
        return fetch

    def __raise_missing(self, message: str):
        raise ValueError(f"""
            Could not insert incomplete record; {message}. Only insert complete objects
            into the database to prevent partial information from being outdated or missing.
            """)

    def insert_table_data(self, table: str, new_column_dict: dict) -> List[tuple]:
        """Inserts the dictionary into the table, or if already present, updates the columns.
        Keys in the dictionary are column names, values are their respective value to assign.
        Returns the result from the query."""
        keys = new_column_dict.keys()
        key_string = ", ".join(keys)
        key_format_string = ", ".join(f"%({key})s" for key in keys)
        keyword_format_string = ", ".join(f"{key}=%({key})s" for key in keys)
        
        query = """
            INSERT INTO %(db_name)s.%(table)s (%(key_string)s)
            VALUES (%(key_format_string)s)
            ON DUPLICATE KEY
            UPDATE %(keyword_format_string)s
            """ % InterpolationDict(
                db_name               = self.db_name,
                table                 = table,
                key_string            = key_string,
                key_format_string     = key_format_string,
                keyword_format_string = keyword_format_string
            )

        return self.__execute_dict(query, **new_column_dict)

    def retrieve_table_data(
            self, table: str, where: str=None, where_values: tuple=None, selection: str="*",
            group_by: str=None, order_by: str=None, limit: int=None
        ) -> List[tuple]:
        """Returns all rows from the table where the WHERE clause applies (e.g. `where` as "type=%s AND id=%s" and 
        `where_values` as ("nominate", 5)), if specified, otherwise any data present in the table."""
        group_by = f"\nGROUP BY {group_by}" if group_by else ""
        order_by = f"\nORDER BY {order_by}" if order_by else ""
        limit    = f"\nLIMIT {limit}" if limit else ""

        if where and ("ORDER BY" in where or "LIMIT" in where):
            log("WARNING | Found special in `where` variable. This should probably be in `order_by`/`limit` variables.")

        return self._execute("""
            SELECT %(selection)s FROM %(db_name)s.%(table)s
            WHERE %(where)s
            """ % InterpolationDict(
                selection = selection,
                db_name   = self.db_name,
                table     = table,
                where     = where if where else "TRUE"
            ) +
            (
                group_by +
                order_by +
                limit
            ),
            where_values
        )

    def delete_table_data(self, table: str, where: str, where_values: tuple=None, ignore_exception: bool=False) -> List[tuple]:
        """Deletes all rows from the table where the WHERE clause applies (e.g. `where` as "type=%s AND id=%s" and 
        `where_values` as ("nominate", 5)). Can optionally allow failure by ignoring any thrown exception from the query.
        Returns the result of the query."""
        return self._execute("""
            DELETE %(ignore)sFROM %(db_name)s.%(table)s
            WHERE %(where)s
            """ % InterpolationDict(
                ignore  = "IGNORE " if ignore_exception else "",
                db_name = self.db_name,
                table   = table,
                where   = where
            ),
            where_values
        )
    
    def clear_table_data(self, table: str) -> None:
        """Deletes all rows from the table. Ignores the foreign key check, meaning this
        will disconnect keys from values. As such use with care."""
        self._execute("SET FOREIGN_KEY_CHECKS = 0")
        self._execute("""
            TRUNCATE %(db_name)s.%(table)s
            """ % InterpolationDict(
                db_name = self.db_name,
                table   = table
            )
        )
        self._execute("SET FOREIGN_KEY_CHECKS = 1")
    
    def delete_group_user(self, group: Usergroup, user: User) -> None:
        """Deletes the given user to group relation from the group_users table."""
        self.delete_table_data(
            table        = "group_users",
            where        = "group_id=%s AND user_id=%s",
            where_values = (group.id, user.id)
        )
    
    def delete_beatmap(self, beatmap: Beatmap) -> None:
        """Deletes the given beatmap from the beatmaps table."""
        self.delete_table_data(
            table        = "beatmaps",
            where        = "id=%s",
            where_values = (beatmap.id,)
        )

    def insert_user(self, user: User) -> None:
        """Inserts/updates the given user object into the users table."""
        self.insert_table_data(
            "users",
            dict(
                id   = user.id,
                name = user.name
            )
        )
    
    def insert_beatmapset_modes(self, beatmapset: Beatmapset) -> None:
        """Inserts/updates the beatmapset-modes relation of the given beatmapset.
        Equivalent to storing an array of modes for the beatmapset."""
        beatmapset_ids = []
        beatmapset_mode_pairs = []
        for mode in beatmapset.modes:
            beatmapset_ids.append((beatmapset.id,))
            beatmapset_mode_pairs.append((beatmapset.id, mode))
        
        # Ensures any mode no longer present in the set is not included.
        self.__executemany("""
            DELETE IGNORE FROM {db_name}.beatmapset_modes
            WHERE beatmapset_id=%s
            """.format(db_name=self.db_name),
            beatmapset_ids
        )
        
        self.__executemany("""
            INSERT IGNORE INTO {db_name}.beatmapset_modes (beatmapset_id, mode)
            VALUES (%s, %s)
            """.format(db_name=self.db_name),
            beatmapset_mode_pairs
        )
    
    def insert_beatmapset(self, beatmapset: Beatmapset) -> None:
        """Inserts/updates the given beatmapset object into the beatmapsets table and modes into the beatmapset_modes table.
        Also inserts/updates the creator into the users table."""
        self.insert_user(beatmapset.creator)
        self.insert_beatmapset_modes(beatmapset)
        for beatmap in beatmapset.beatmaps:
            self.insert_beatmap(beatmap)
        self.insert_table_data(
            "beatmapsets",
            dict(
                id         = beatmapset.id,
                title      = beatmapset.title,
                artist     = beatmapset.artist,
                creator_id = beatmapset.creator.id,
                genre      = beatmapset.genre,
                language   = beatmapset.language,
                tags       = str.join(" ", beatmapset.tags)
            )
        )
    
    def insert_beatmap(self, beatmap: Beatmap) -> None:
        """Inserts/updates the given beatmap object into the beatmaps table."""
        if beatmap is None:
            # Can happen in cases where a beatmap is removed and can no longer have properties be retrieved.
            return
        
        self.insert_table_data(
            "beatmaps",
            dict(
                id            = beatmap.id,
                beatmapset_id = beatmap.beatmapset_id,
                version       = beatmap.version,
                draintime     = beatmap.draintime,
                sr_total      = beatmap.sr_total,
                favourites    = beatmap.favourites,
                userrating    = beatmap.userrating,
                playcount     = beatmap.playcount,
                passcount     = beatmap.passcount,
                updated_at    = datetime.utcnow()
            )
        )
    
    def insert_discussion(self, discussion: Discussion) -> None:
        """Inserts/updates the given discussion into the discussions table.
        Also inserts/updates other values (e.g. beatmapset and user)."""
        if discussion.beatmapset: self.insert_beatmapset(discussion.beatmapset)
        if discussion.user: self.insert_user(discussion.user)
        
        # These will be missing when scraped from /events (e.g. disqualify, nomination_reset),
        # but should then be filled in through the respective /beatmap-discussions events before
        # being inserted into the database.
        if discussion.user is None: self.__raise_missing("User is missing from discussion")
        if discussion.content is None: self.__raise_missing("Content is missing from discussion")

        self.insert_table_data(
            "discussions",
            dict(
                id            = discussion.id,
                beatmapset_id = discussion.beatmapset.id,
                user_id       = discussion.user.id,
                content       = discussion.content,
                tab           = discussion.tab,
                difficulty    = discussion.difficulty
            )
        )
    
    def insert_beatmapset_status(self, status: BeatmapsetStatus) -> None:
        """Inserts/updates the given status object into the beatmapset status table.
        Also inserts/updates the associated nominators and beatmapset."""
        if status.beatmapset: self.insert_beatmapset(status.beatmapset)
        self.insert_table_data(
            "beatmapset_status",
            dict(
                beatmapset_id = status.beatmapset.id,
                status        = status.status,
                time          = status.time
            )
        )
        # Reason we're retrieving the event here is because we need the `status_id` field.
        retrieved_status = self.retrieve_beatmapset_status(
            "beatmapset_id=%s AND status=%s AND time=%s",
            (status.beatmapset.id, status.status, status.time)
        )
        for nominator in status.nominators: self.insert_beatmapset_status_nominator(retrieved_status.id, nominator)
    
    def insert_beatmapset_status_nominator(self, status_id: int, nominator: User) -> None:
        """Inserts/updates the given status object into the beatmapset status table.
        Also inserts/updates the associated nominators and beatmapset."""
        self.insert_user(nominator)
        self.insert_table_data(
            "status_nominators",
            dict(
                status_id    = status_id,
                nominator_id = nominator.id
            )
        )
    
    def insert_obv_sev_event(self, event: Event) -> None:
        """Inserts/updates the given SEV type event data into the SEV table.
        Parses the obv/sev from the content of the event (e.g. "2/1")."""
        if event.type != types.SEV:
            raise ValueError("Cannot insert an event as obv/sev without being of SEV type.")
        
        splits = event.content.split("/")
        obv = int(splits[0]) if splits[0] != "?" else None
        sev = int(splits[1]) if splits[1] != "?" else None
        self.insert_obv_sev(event.discussion, obv, sev)

    def insert_obv_sev(self, discussion: Discussion, obv: int, sev: int) -> None:
        """Inserts/updates the given obv/sev and associates it to the given
        discussion in the SEV table."""
        self.insert_table_data(
            "discussion_obv_sev",
            dict(
                discussion_id = discussion.id,
                obv           = obv,
                sev           = sev
            )
        )
    
    def insert_newspost(self, newspost: NewsPost) -> None:
        """Inserts/updates the given newspost object into the newsposts table.
        Also inserts/updates the associated user (i.e. author of the newspost)."""
        # Specifically checks `author.id`, as the id may be None in case of e.g. "The Spotlight Team".
        if newspost.author.id: self.insert_user(newspost.author)
        self.insert_table_data(
            "newsposts",
            dict(
                id          = newspost.id,
                title       = newspost.title,
                preview     = newspost.preview,
                author_id   = newspost.author.id,
                author_name = newspost.author.name,
                slug        = newspost.slug,
                image_url   = newspost.image_url
            )
        )

    def insert_group_user(self, group: Usergroup, user: User) -> None:
        """Inserts/updates the given user to group relation into the group_users table.
        Also inserts/updates the associated user (i.e. whoever got added/removed)."""
        self.insert_user(user)
        self.insert_table_data(
            "group_users",
            dict(
                group_id = group.id,
                user_id  = user.id
            )
        )

    def insert_event(self, event: Event) -> None:
        """Inserts/updates the given event into the events table, along with any other values
        (e.g. beatmapset, discussion, user) into their respective tables."""
        if event.beatmapset:        self.insert_beatmapset(event.beatmapset)
        if event.user:              self.insert_user(event.user)
        if event.type == types.SEV: self.insert_obv_sev_event(event)
        if event.discussion:        self.insert_discussion(event.discussion)
        if event.newspost:          self.insert_newspost(event.newspost)
        if event.group:
            if event.type == types.ADD:    self.insert_group_user(event.group, event.user)
            if event.type == types.REMOVE: self.delete_group_user(event.group, event.user)
        
        if event.type in [types.NOMINATE, types.QUALIFY, types.RESET, types.DISQUALIFY, types.RANK, types.LOVE] and event.beatmapset:
            self.update_beatmapset_status(event)

        self.insert_table_data(
            "events",
            dict(
                insert_time   = datetime.utcnow(),
                time          = event.time,
                type          = event.type,
                beatmapset_id = event.beatmapset.id if event.beatmapset is not None else None,
                discussion_id = event.discussion.id if event.discussion is not None else None,
                user_id       = event.user.id if event.user is not None else None,
                group_id      = event.group.id if event.group is not None else None,
                group_mode    = event.group.mode if event.group is not None else None,
                news_id       = event.newspost.id if event.newspost is not None else None,
                content       = event.content if event.content is not None else None
            )
        )
    
    def update_beatmapset_status(self, event: Event) -> None:
        """Inserts/updates the given status object into the beatmapset status table.
        Also inserts/updates the associated nominators and beatmapset."""
        if event.type not in [types.NOMINATE, types.QUALIFY, types.RESET, types.DISQUALIFY, types.RANK, types.LOVE]:
            raise ValueError("Cannot update status from an event not being of nom/reset/rank type.")

        status = self.retrieve_beatmapset_status(
            where        = "beatmapset_id=%s",
            where_values = (event.beatmapset.id,),
            order_by     = "time DESC",
            beatmapset   = event.beatmapset
        )
        is_reset = event.type in [types.RESET, types.DISQUALIFY]

        new_status = status.status if status else "pending"
        if is_reset:                     new_status = "pending"
        if event.type == types.NOMINATE: new_status = "nominated" if new_status == "pending" else new_status
        if event.type == types.QUALIFY:  new_status = "qualified" if new_status in ["pending", "nominated"] else new_status
        if event.type == types.RANK:     new_status = "ranked"
        if event.type == types.LOVE:     new_status = "loved"

        new_nominators = status.nominators if status else []
        valid_user = event.user and event.user not in new_nominators
        if is_reset or event.type == types.LOVE: new_nominators = []
        if event.type in [types.NOMINATE, types.QUALIFY]:
            if valid_user: new_nominators.append(event.user)
            else:          return  # Earliest qualify events are system qualifies (no user associated), we skip those.
                                   # They'd be ranked by now anyway if they weren't dqed.

        self.insert_beatmapset_status(
            BeatmapsetStatus(
                _id        = 0,  # Will be auto-generated, so doesn't matter.
                beatmapset = event.beatmapset,
                status     = new_status,
                time       = event.time,
                nominators = new_nominators
            )
        )

    def retrieve_user(self, where: str, where_values: tuple=None, group_by: str=None, order_by: str=None) -> User:
        """Returns the first user from the database matching the given WHERE clause, or None if no such user is stored."""
        return next(
            self.retrieve_users(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1
            ),
            None
        )
    
    def retrieve_users(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None
        ) -> Generator[User, None, None]:
        """Returns a generator of all users from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "users",
            where        = where,
            where_values = where_values,
            selection    = "id, name",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )
        for row in (fetched_rows or []):
            _id  = row[0]
            name = row[1]
            yield User(_id, name, allow_api=False)
    
    def retrieve_beatmapset_modes(self, beatmapset_id: int) -> List[str]:
        """Returns an array of modes corresponding to the given beatmapset id.
        Returned array is empty when no such beatmapset is stored."""
        fetched_rows = self.retrieve_table_data(
            table        = "beatmapset_modes",
            where        = "beatmapset_id=%s",
            where_values = (beatmapset_id,),
            selection    = "mode"
        )
        modes = []
        for row in (fetched_rows or []):
            modes.append(row[0])
        return modes
    
    def retrieve_beatmapset(self, where: str, where_values: tuple=None, group_by: str=None, order_by: str=None) -> Beatmapset:
        """Returns the first beatmapset from the database matching the given WHERE clause, or None if no such beatmapset is stored."""
        return next(
            self.retrieve_beatmapsets(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1
            ),
            None
        )
    
    def retrieve_beatmapsets(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None
        ) -> Generator[Beatmapset, None, None]:
        """Returns a generator of all beatmapsets from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "beatmapsets",
            where        = where,
            where_values = where_values,
            selection    = "id, title, artist, creator_id, genre, language, tags",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )
        for row in (fetched_rows or []):
            _id      = row[0]
            title    = row[1]
            artist   = row[2]
            creator  = self.retrieve_user("id=%s", (row[3],))
            modes    = self.retrieve_beatmapset_modes(_id)
            genre    = row[4]
            language = row[5]
            tags     = row[6].split(" ") if row[6] else None
            beatmaps = list(self.retrieve_beatmaps("beatmapset_id=%s", (_id,), allow_api=False))

            beatmapset = Beatmapset(_id, artist, title, creator, modes, genre, language, tags, beatmaps, allow_api=False)
            if beatmapset.is_incomplete():
                # The retrieved beatmapset is incomplete, and should be updated.
                api_beatmapset = Beatmapset(_id, allow_api=True)
                self.insert_beatmapset(api_beatmapset)
                for beatmap in beatmaps:
                    # Ensure any deleted beatmap gets cleared out before we repopulate it.
                    self.delete_beatmap(beatmap)
                for api_beatmap in api_beatmapset.beatmaps:
                    self.insert_beatmap(api_beatmap)
                beatmapset = api_beatmapset
            
            yield beatmapset

    def retrieve_beatmap(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None
        ) -> Beatmap:
        """Returns the first beatmap from the database matching the given WHERE clause, or None if no such beatmap is stored."""
        return next(
            self.retrieve_beatmaps(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1
            ),
            None
        )
    
    def retrieve_beatmaps(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None, allow_api: bool=True
        ) -> Generator[Beatmap, None, None]:
        """Returns a generator of all beatmaps from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "beatmaps",
            where        = where,
            where_values = where_values,
            selection    = "id, beatmapset_id, version, draintime, sr_total, favourites, userrating, playcount, passcount, updated_at",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )
        for row in (fetched_rows or []):
            beatmap = Beatmap.from_raw(
                _id           = row[0],
                beatmapset_id = row[1],
                version       = row[2],
                draintime     = row[3],
                sr_total      = row[4],
                favourites    = row[5],
                userrating    = row[6],
                playcount     = row[7],
                passcount     = row[8],
                updated_at    = row[9]
            )

            if allow_api:
                updated_at     = row[9]
                needs_updating = updated_at is None or (updated_at - datetime.utcnow()) > timedelta(days=30)

                if not beatmap or beatmap.is_incomplete() or needs_updating:
                    # The retrieved beatmap is incomplete, and should be updated.
                    retrieved_beatmap = Beatmap.from_api(_id=row[0], beatmapset_id=row[1])
                    #if retrieved_beatmap is None:
                        # Beatmap was likely deleted.
                        #self.delete_beatmap(beatmap)
                    
                    beatmap = retrieved_beatmap
                    self.insert_beatmap(beatmap)
            
            if beatmap:
                yield beatmap

    def retrieve_discussion(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, beatmapset: Beatmapset=None
        ) -> Discussion:
        """Returns the first discussion from the database matching the given WHERE clause, or None if no such discussion is stored.
        Also retrieves the associated beatmapset from the database if not supplied."""
        return next(
            self.retrieve_discussions(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1,
                beatmapset   = beatmapset
            ),
            None
        )
    
    def retrieve_discussions(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None, beatmapset: Beatmapset=None
        ) -> Generator[Discussion, None, None]:
        """Returns a generator of all discussions from the database matching the given WHERE clause.
        Also retrieves the associated beatmapset from the database if not supplied."""
        fetched_rows = self.retrieve_table_data(
            table        = "discussions", 
            where        = where,
            where_values = where_values,
            selection    = "id, beatmapset_id, user_id, content, tab, difficulty",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )
        for row in (fetched_rows or []):
            _id     = row[0]
            if not beatmapset:
                beatmapset = self.retrieve_beatmapset("id=%s", (row[1],))
            user       = self.retrieve_user("id=%s", (row[2],))
            content    = row[3]
            tab        = row[4]
            difficulty = row[5]
            yield Discussion(_id, beatmapset, user, content, tab, difficulty)

    def retrieve_beatmapset_status(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, beatmapset: Beatmapset=None
        ) -> BeatmapsetStatus:
        """Returns the first status from the database matching the given WHERE clause, or None if no such status is stored.
        Also retrieves the associated beatmapset from the database if not supplied."""
        return next(
            self.retrieve_beatmapset_statuses(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1,
                beatmapset   = beatmapset
            ),
            None
        )

    def retrieve_beatmapset_statuses(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None, beatmapset: Beatmapset=None
        ) -> Generator[BeatmapsetStatus, None, None]:
        """Returns a generator of all statuses from the database matching the given WHERE clause.
        Also retrieves the associated beatmapset from the database if not supplied."""
        fetched_rows = self.retrieve_table_data(
            table        = "beatmapset_status", 
            where        = where,
            where_values = where_values,
            selection    = "id, beatmapset_id, status, time",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )
        for row in (fetched_rows or []):
            _id        = row[0]
            if not beatmapset:
                beatmapset = self.retrieve_beatmapset("id=%s", (row[1],))
            status     = row[2]
            time       = row[3]
            nominators = list(self.retrieve_beatmapset_status_nominators(status_id=_id))
            yield BeatmapsetStatus(_id, beatmapset, status, time, nominators)

    def retrieve_beatmapset_status_nominators(self, status_id: int) -> Generator[User, None, None]:
        """Returns a generator of all users who are nominators on the given beatmapset status instance."""
        fetched_rows = self.retrieve_table_data(
            table        = "status_nominators",
            where        = "status_id=%s",
            where_values = (status_id,),
            selection    = "nominator_id"
        )
        for row in (fetched_rows or []):
            yield self.retrieve_user("id=%s", (row[0],))

    def retrieve_obv_sev(self, discussion_id: int) -> Tuple[int, int]:
        """Returns a tuple of the obviousness and severity from the database associated
        with the given discussion id, or `(None, None)` if no such obv/sev is stored."""
        fetched_rows = self.retrieve_table_data(
            table        = "discussion_obv_sev", 
            where        = "discussion_id=%s",
            where_values = (discussion_id,),
            selection    = "obv, sev"
        )
        for row in (fetched_rows or []):
            obv = row[0]
            sev = row[1]
            return (obv, sev)
        return (None, None)

    def retrieve_newspost(self, where: str, where_values: tuple=None, group_by: str=None, order_by: str=None) -> NewsPost:
        """Returns the first newspost from the database matching the given WHERE clause, or None if no such newspost is stored."""
        return next(
            self.retrieve_newsposts(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1
            ),
            None
        )
    
    def retrieve_newsposts(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None
        ) -> Generator[NewsPost, None, None]:
        """Returns a generator of all newsposts from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "newsposts",
            where        = where,
            where_values = where_values,
            selection    = "id, title, preview, author_id, author_name, slug, image_url",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )
        for row in (fetched_rows or []):
            _id         = row[0]
            title       = row[1]
            preview     = row[2]
            author      = self.retrieve_user("id=%s", (row[3],))
            author_name = row[4]
            if not author:
                author = User(_id=None, name=author_name)
            slug        = row[5]
            image_url   = row[6]
            yield NewsPost(_id, title, preview, author, slug, image_url)

    def retrieve_group_user(self, where: str, where_values: tuple=None, group_by: str=None, order_by: str=None) -> Tuple[Usergroup, User]:
        """Returns the first group user relation from the database matching the given WHERE clause,
        or None if no such group user relation is stored."""
        return next(
            self.retrieve_group_users(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1
            ),
            None
        )

    def retrieve_group_users(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None
        ) -> Generator[Tuple[Usergroup, User], None, None]:
        """Returns a generator of all group user relations from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "group_users",
            where        = where,
            where_values = where_values,
            selection    = "group_id, user_id",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )
        for row in (fetched_rows or []):
            group = Usergroup(row[0])
            user  = self.retrieve_user("id=%s", (row[1],))
            yield (group, user)

    async def retrieve_event(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, extensive: bool=False
        ) -> Event:
        """Returns the first event from the database matching the given WHERE clause, or None if no such event is stored."""
        return await anext(
            self.retrieve_events(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1,
                extensive    = extensive
            ),
            default_value = None
        )
    
    async def retrieve_events(
            self, where: str, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None, extensive: bool=False
        ) -> Generator[Event, None, None]:
        """Returns an asynchronous generator of all events from the database matching the given WHERE clause.
        Optionally retrieve extensively so that more can be queried (e.g. user name, beatmap creator/artist/title)."""
        if not extensive:
            fetched_rows = self.__fetch_events(where, where_values, order_by, limit)
        else:
            fetched_rows = self.__fetch_events_extensive(where, where_values, order_by, limit)
        
        for row in (fetched_rows or []):
            await asyncio.sleep(0)  # Return control back to the event loop, granting other tasks a window to start/resume.
            
            # Treat deleted beatmapsets/discussions as if not stored.
            with suppress(DeletedContextError):
                _type      = row[0]
                time       = row[1]
                beatmapset = self.retrieve_beatmapset("id=%s", (row[2],)) if row[2] else None
                discussion = self.retrieve_discussion("id=%s", (row[3],), beatmapset=beatmapset) if row[3] else None
                user       = self.retrieve_user("id=%s", (row[4],)) if row[4] else None
                group      = Usergroup(row[5], mode=row[6] if row[6] else None) if row[5] else None
                newspost   = self.retrieve_newspost("id=%s", (row[7],)) if row[7] else None
                content    = row[8]

                if beatmapset:
                    status_time = time
                    if _type == types.SEV:
                        reset_event = await self.retrieve_event(
                            where        = "(type=%s OR type=%s) AND discussion_id=%s",
                            where_values = ("disqualify", "nomination_reset", discussion.id)
                        )
                        if reset_event:
                            status_time = reset_event.time

                    # Dependent on when the event happened, hence why this is here and not in `retrieve_beatmapset`.
                    beatmapset.status = self.retrieve_beatmapset_status(
                        where        = "beatmapset_id=%s AND time < %s",
                        where_values = (beatmapset.id, status_time),
                        order_by     = "time DESC"
                    )

                yield Event(_type, time, beatmapset, discussion, user, group, newspost, content=content)

    def __fetch_events(self, where: str, where_values: tuple=None, order_by: str=None, limit: int=None):
        return self.retrieve_table_data(
            table        = "events",
            where        = where,
            where_values = where_values,
            selection    = "type, time, beatmapset_id, discussion_id, user_id, group_id, group_mode, news_id, content",
            group_by     = "events.id",
            order_by     = order_by,
            limit        = limit
        )

    def __fetch_events_extensive(self, where: str, where_values: tuple=None, order_by: str=None, limit: int=None):
        return self.retrieve_table_data(
            table        = f"""events
                LEFT JOIN {self.db_name}.discussions AS discussion ON events.discussion_id=discussion.id
                LEFT JOIN {self.db_name}.beatmapsets AS beatmapset ON events.beatmapset_id=beatmapset.id
                LEFT JOIN {self.db_name}.newsposts AS newspost ON events.news_id=newspost.id
                LEFT JOIN {self.db_name}.users AS author ON discussion.user_id=author.id
                LEFT JOIN {self.db_name}.users AS creator ON beatmapset.creator_id=creator.id
                LEFT JOIN {self.db_name}.users AS user ON events.user_id=user.id
                LEFT JOIN {self.db_name}.beatmapset_modes AS modes ON beatmapset.id=modes.beatmapset_id""",
                #LEFT JOIN {self.db_name}.beatmapset_status AS status ON events.beatmapset_id=status.beatmapset_id
                #LEFT JOIN {self.db_name}.status_nominators AS status_nominator ON status.id=status_nominator.status_id
                #LEFT JOIN {self.db_name}.users AS nominator ON status_nominator.nominator_id=nominator.id""",
            where        = where,
            where_values = where_values,
            selection    = "events.type, events.time, events.beatmapset_id, events.discussion_id, events.user_id, events.group_id, events.group_mode, events.news_id, events.content",
            group_by     = "events.id",  # Ensures we don't return the same event more than once.
            order_by     = order_by,
            limit        = limit
        )

class CachedDatabase(Database):
    """Creates an aiess database connection. Stores any query results in a cache and retrieves from it whenever available."""
    def __init__(self, _db_name: str):
        self.cache = {}
        super().__init__(_db_name=_db_name)
    
    def _execute(self, query: str, values: tuple=None) -> List[tuple]:
        """Executes the given SQL query with the given argument values, if any. Use like "%s" in query
        and ("name",) in values. Returns the fetched result sets as a list of tuples, or None if no result.
        
        Returns from cache, if available, otherwise caches the result."""
        cache_line = f"Q:{query}, V:{values}"
        if cache_line in self.cache and self.cache[cache_line]:
            return self.cache[cache_line]
        
        self.cache[cache_line] = super()._execute(
            query  = query,
            values = values
        )
        
        return self.cache[cache_line]