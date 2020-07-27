import asyncio
import mysql.connector
from mysql.connector.errors import Error, OperationalError
from typing import List, Generator
from enum import Enum
from datetime import datetime
from collections import defaultdict

from aiess.objects import User, Beatmapset, Discussion, Event, NewsPost
from aiess.settings import DB_CONFIG
from aiess.logger import log
from aiess.common import anext

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

    def __init__(self, _db_name: str):
        self.db_name = _db_name
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

    def __execute(self, query: str, values: tuple=None) -> List[tuple]:
        """Executes the given SQL query with the given argument values, if any. Use like "%s" in query
        and ("name",) in values. Returns the fetched result sets as a list of tuples, or None if no result."""
        cursor = self.__get_cursor()
        cursor.nextset()
        cursor.execute(query, values)

        fetch = self.__fetch(cursor)
        self.connection.commit()
        return fetch
    
    def __execute_dict(self, query: str, **values: object) -> List[tuple]:
        """Executes the given SQL query with the given argument values, if any. Use like "%(name)s" in query
        and name=name in values. Returns the fetched result sets as a list of tuples, or None if no result."""
        return self.__execute(query, values)
    
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

    def retrieve_table_data(self, table: str, where: str=None, where_values: tuple=None, selection: str="*") -> List[tuple]:
        """Returns all rows from the table where the WHERE clause applies (e.g. `where` as "type=%s AND id=%s" and 
        `where_values` as ("nominate", 5)), if specified, otherwise any data present in the table."""
        return self.__execute("""
            SELECT %(selection)s FROM %(db_name)s.%(table)s
            WHERE %(where)s
            """ % InterpolationDict(
                selection = selection,
                db_name   = self.db_name,
                table     = table,
                where     = where if where else "TRUE"
            ),
            where_values
        )

    def delete_table_data(self, table: str, where: str, where_values: tuple=None, ignore_exception: bool=False) -> List[tuple]:
        """Deletes all rows from the table where the WHERE clause applies (e.g. `where` as "type=%s AND id=%s" and 
        `where_values` as ("nominate", 5)). Can optionally allow failure by ignoring any thrown exception from the query.
        Returns the result of the query."""
        return self.__execute("""
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
        self.__execute("SET FOREIGN_KEY_CHECKS = 0")
        self.__execute("""
            TRUNCATE %(db_name)s.%(table)s
            """ % InterpolationDict(
                db_name = self.db_name,
                table   = table
            )
        )
        self.__execute("SET FOREIGN_KEY_CHECKS = 1")

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
        self.insert_table_data(
            "beatmapsets",
            dict(
                id         = beatmapset.id,
                title      = beatmapset.title,
                artist     = beatmapset.artist,
                creator_id = beatmapset.creator.id
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
                content       = discussion.content
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

    def insert_event(self, event: Event) -> None:
        """Inserts/updates the given event into the events table, along with any other values
        (e.g. beatmapset, discussion, user) into their respective tables."""
        if event.beatmapset: self.insert_beatmapset(event.beatmapset)
        if event.user:       self.insert_user(event.user)
        if event.discussion: self.insert_discussion(event.discussion)
        if event.newspost:   self.insert_newspost(event.newspost)
        self.insert_table_data(
            "events",
            dict(
                insert_time   = datetime.utcnow(),
                time          = event.time,
                type          = event.type,
                beatmapset_id = event.beatmapset.id if event.beatmapset is not None else None,
                discussion_id = event.discussion.id if event.discussion is not None else None,
                user_id       = event.user.id if event.user is not None else None,
                news_id       = event.newspost.id if event.newspost is not None else None,
                content       = event.content if event.content is not None else None
            )
        )
    
    def retrieve_user(self, where: str, where_values: tuple=None) -> User:
        """Returns the first user from the database matching the given WHERE clause, or None if no such user is stored."""
        return next(self.retrieve_users(where + " LIMIT 1", where_values), None)
    
    def retrieve_users(self, where: str, where_values: tuple=None) -> Generator[User, None, None]:
        """Returns a generator of all users from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "users",
            where        = where,
            where_values = where_values,
            selection    = "id, name"
        )
        for row in (fetched_rows or []):
            _id  = row[0]
            name = row[1]
            yield User(_id, name)
    
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
    
    def retrieve_beatmapset(self, where: str, where_values: tuple=None) -> Beatmapset:
        """Returns the first beatmapset from the database matching the given WHERE clause, or None if no such beatmapset is stored."""
        return next(self.retrieve_beatmapsets(where + " LIMIT 1", where_values), None)
    
    def retrieve_beatmapsets(self, where: str, where_values: tuple=None) -> Generator[Beatmapset, None, None]:
        """Returns a generator of all beatmapsets from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "beatmapsets",
            where        = where,
            where_values = where_values,
            selection    = "id, title, artist, creator_id"
        )
        for row in (fetched_rows or []):
            _id     = row[0]
            title   = row[1]
            artist  = row[2]
            creator = self.retrieve_user("id=%s", (row[3],))
            modes   = self.retrieve_beatmapset_modes(_id)
            yield Beatmapset(_id, artist, title, creator, modes)

    def retrieve_discussion(self, where: str, where_values: tuple=None, beatmapset: Beatmapset=None) -> Discussion:
        """Returns the first discussion from the database matching the given WHERE clause, or None if no such discussion is stored.
        Also retrieves the associated beatmapset from the database if not supplied."""
        return next(self.retrieve_discussions(where + " LIMIT 1", where_values), None)
    
    def retrieve_discussions(self, where: str, where_values: tuple=None, beatmapset: Beatmapset=None) -> Generator[Discussion, None, None]:
        """Returns a generator of all discussions from the database matching the given WHERE clause.
        Also retrieves the associated beatmapset from the database if not supplied."""
        fetched_rows = self.retrieve_table_data(
            table        = "discussions", 
            where        = where,
            where_values = where_values,
            selection    = "id, beatmapset_id, user_id, content"
        )
        for row in (fetched_rows or []):
            _id     = row[0]
            if not beatmapset:
                beatmapset = self.retrieve_beatmapset("id=%s", (row[1],))
            user    = self.retrieve_user("id=%s", (row[2],))
            content = row[3]

            yield Discussion(_id, beatmapset, user, content)
    
    def retrieve_newspost(self, where: str, where_values: tuple=None) -> NewsPost:
        """Returns the first newspost from the database matching the given WHERE clause, or None if no such newspost is stored."""
        return next(self.retrieve_newsposts(where + " LIMIT 1", where_values), None)
    
    def retrieve_newsposts(self, where: str, where_values: tuple=None) -> Generator[NewsPost, None, None]:
        """Returns a generator of all newsposts from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "newsposts", 
            where        = where,
            where_values = where_values,
            selection    = "id, title, preview, author_id, author_name, slug, image_url"
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

    async def retrieve_event(self, where: str, where_values: tuple=None) -> Event:
        """Returns the first event from the database matching the given WHERE clause, or None if no such event is stored."""
        return await anext(self.retrieve_events(where + " LIMIT 1", where_values), None)
    
    async def retrieve_events(self, where: str, where_values: tuple=None) -> Generator[Event, None, None]:
        """Returns an asynchronous generator of all events from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "events",
            where        = where,
            where_values = where_values,
            selection    = "type, time, beatmapset_id, discussion_id, user_id, news_id, content"
        )
        for row in (fetched_rows or []):
            await asyncio.sleep(0)  # Return control back to the event loop, granting other tasks a window to start/resume.
            _type      = row[0]
            time       = row[1]
            beatmapset = self.retrieve_beatmapset("id=%s", (row[2],)) if row[2] else None
            discussion = self.retrieve_discussion("id=%s", (row[3],)) if row[3] else None
            user       = self.retrieve_user("id=%s", (row[4],)) if row[4] else None
            newspost   = self.retrieve_newspost("id=%s", (row[5],)) if row[5] else None
            content    = row[6]
            yield Event(_type, time, beatmapset, discussion, user, newspost=newspost, content=content)