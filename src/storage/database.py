import mysql.connector
from mysql.connector.errors import Error, OperationalError
from typing import List, Tuple
from enum import Enum
from datetime import datetime

from storage.settings import DB_CONFIG
from objects import User, Beatmapset, Discussion, Event
from storage.logger import log

class InterpolationDict(dict):
    def __missing__(self, key):
        return "%(" + key + ")s"

class Database:
    """Creates an aiess database connection."""

    db_name = None

    class Table(Enum):
        # External code should be able to refer to specific tables,
        # while not breaking if we change anything in the actual database.
        EVENTS = "events"
        BEATMAPSETS = "beatmapsets"
        DISCUSSIONS = "discussions"
        DISCUSSION_REPLIES = "discussion_replies"
        USERS = "users"

    def __init__(self, _db_name="aiess"):
        global db_name
        db_name = _db_name
        db_config = {
            "host": DB_CONFIG["host"],
            "database": db_name,
            "user": DB_CONFIG["user"],
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
                self.__init__()

    def __del__(self):
        """Clears up allocated resources such as memory upon destruction."""
        if (hasattr(self, "connection") and self.connection.is_connected()):
            self.connection.cursor().close()
            self.connection.close()
    
    def __fetch(self, cursor: object) -> List[Tuple]:
        """Attempts to return fetch all from a cursor object. Does not throw if nothing to fetch.
        Returns the fetched result sets as a list of tuples, or None if no result."""
        try:
            # Fetch entire result set so nothing carries over to the next query.
            return cursor.fetchall()
        except mysql.connector.errors.InterfaceError as error:
            if error.msg == "No result set to fetch from.":
                return None  # Reached end of result set, not an issue. 
            else:
                raise

    def __execute(self, query: str, **values: str) -> List[Tuple]:
        """Executes the given SQL query with the given argument values, if any. Use like "%(name)s" in query
        and name=name in values. Returns the fetched result sets as a list of tuples, or None if no result."""
        cursor = self.__get_cursor()
        cursor.nextset()
        cursor.execute(query, values)

        fetch = self.__fetch(cursor)
        self.connection.commit()
        return fetch
    
    def __executemany(self, query: str, values: List[Tuple]) -> List[Tuple]:
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

    def insert_table_data(self, table: str, where_dict: dict) -> List[Tuple]:
        """Inserts the dictionary into the table, or if already present, updates the columns.
        Keys in the dictionary are column names, values are their respective value to assign.
        Returns the result from the query."""
        keys = where_dict.keys()
        key_string = ", ".join(keys)
        key_format_string = ", ".join(f"%({key})s" for key in keys)
        keyword_format_string = ", ".join(f"{key}=%({key})s" for key in keys)
        
        return self.__execute("""
            INSERT INTO %(db_name)s.%(table)s (%(key_string)s)
            VALUES (%(key_format_string)s)
            ON DUPLICATE KEY
            UPDATE %(keyword_format_string)s
            """ % InterpolationDict(
                db_name=db_name,
                table=table,
                key_string=key_string,
                key_format_string=key_format_string,
                keyword_format_string=keyword_format_string),
            **where_dict)

    def retrieve_table_data(self, table: str, where_dict: dict=None, selection: str="*") -> List[Tuple]:
        """Returns all rows from the table where the dictionary conditions apply (e.g. dict(type="nominate")),
        if specified, otherwise any data present in the table."""
        if where_dict:
            where_str = " and ".join(f"{key}=%({key})s" for key in where_dict.keys())
        else:
            where_str = "TRUE"
        
        query = """
            SELECT %(selection)s FROM %(db_name)s.%(table)s
            WHERE %(where_str)s
            """ % InterpolationDict(
                selection=selection,
                db_name=db_name,
                table=table,
                where_str=where_str)
        
        if where_dict:
            return self.__execute(query, **where_dict)
        return self.__execute(query)

    
    def fetchone_table_data(self, table: str, where_dict: dict, selection: str="*") -> List[Tuple]:
        """Returns the first row from the table where the dictionary conditions apply (e.g. dict(id=1))."""
        keyword_format_string = ", ".join(f"{key}=%({key})s" for key in where_dict.keys())
        
        return self.__execute("""
            SELECT %(selection)s FROM %(db_name)s.%(table)s
            WHERE %(keyword_format_string)s
            LIMIT 1
            """ % InterpolationDict(
                selection=selection,
                db_name=db_name,
                table=table,
                keyword_format_string=keyword_format_string),
            **where_dict)

    def delete_table_data(self, table: str, where_dict: dict, ignore_exception: bool=False) -> List[Tuple]:
        """Deletes all rows from the table where the dictionary conditions apply (e.g. dict(type="kudosu-deny")).
        Can optionally allow failure by ignoring any thrown exception from the query. Returns the result of the query."""
        keyword_format_string = ", ".join(f"{key}=%({key})s" for key in where_dict.keys())

        return self.__execute("""
            DELETE %(ignore)sFROM %(db_name)s.%(table)s
            WHERE %(keyword_format_string)s
            """ % InterpolationDict(
                ignore="IGNORE " if ignore_exception else "",
                db_name=db_name,
                table=table,
                keyword_format_string=keyword_format_string),
            **where_dict)

    def insert_user(self, user: User) -> None:
        """Inserts/updates the given user object into the users table."""
        self.insert_table_data(
            "users",
            dict(
                id=user.id,
                name=user.name))
    
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
            """.format(db_name=db_name),
            beatmapset_ids)
        
        self.__executemany("""
            INSERT IGNORE INTO {db_name}.beatmapset_modes (beatmapset_id, mode)
            VALUES (%s, %s)
            """.format(db_name=db_name),
            beatmapset_mode_pairs)
    
    def insert_beatmapset(self, beatmapset: Beatmapset) -> None:
        """Inserts/updates the given beatmapset object into the beatmapsets table and modes into the beatmapset_modes table.
        Also inserts/updates the creator into the users table."""
        self.insert_user(beatmapset.creator)
        self.insert_beatmapset_modes(beatmapset)
        self.insert_table_data(
            "beatmapsets",
            dict(
                id=beatmapset.id,
                title=beatmapset.title,
                artist=beatmapset.artist,
                creator_id=beatmapset.creator.id))
    
    def insert_discussion(self, discussion: Discussion) -> None:
        """Inserts/updates the given discussion into the discussions table.
        Also inserts/updates other values (e.g. beatmapset and user)."""
        if discussion.beatmapset: self.insert_beatmapset(discussion.beatmapset)
        if discussion.user: self.insert_user(discussion.user)
        
        # These will be missing when scraped from /events (e.g. disqualify, nomination_reset),
        # but should then be filled in through the respective /beatmap-discussions events before
        # being inserted into the database.
        if discussion.user == None: self.__raise_missing("User is missing from discussion")
        if discussion.content == None: self.__raise_missing("Content is missing from discussion")

        self.insert_table_data(
            "discussions",
            dict(
                id=discussion.id,
                beatmapset_id=discussion.beatmapset.id,
                user_id=discussion.user.id,
                content=discussion.content))
    
    def insert_event(self, event: Event) -> None:
        """Inserts/updates the given event into the events table, along with any other values
        (e.g. beatmapset, discussion, user) into their respective tables."""
        if event.beatmapset: self.insert_beatmapset(event.beatmapset)
        if event.user: self.insert_user(event.user)
        if event.discussion: self.insert_discussion(event.discussion)
        self.insert_table_data(
            "events",
            dict(
                insert_time=datetime.utcnow(),
                time=event.time,
                type=event.type,
                beatmapset_id=event.beatmapset.id if event.beatmapset != None else None,
                discussion_id=event.discussion.id if event.discussion != None else None,
                user_id=event.user.id if event.user != None else None,
                content=event.content if event.content != None else None))
    
    def retrieve_user(self, where_dict: dict) -> User:
        """Returns the first user with the given column data from the database, or None if no such user is stored."""
        if not where_dict:
            return None

        fetched_rows = self.fetchone_table_data("users", where_dict, selection="id, name")
        for row in (fetched_rows or []):
            _id = row[0]
            name = row[1]
            return User(_id, name)
        return None
    
    def retrieve_beatmapset_modes(self, beatmapset_id: str) -> List[str]:
        """Returns an array of modes corresponding to the given beatmapset id.
        Returned array is empty when no such beatmapset is stored."""
        if not beatmapset_id:
            return None

        fetched_rows = self.retrieve_table_data(
            "beatmapset_modes", dict(beatmapset_id=beatmapset_id), selection="mode")
        modes = []
        for row in (fetched_rows or []):
            modes.append(row[0])
        return modes
    
    def retrieve_beatmapset(self, where_dict: dict) -> Beatmapset:
        """Returns the first beatmapset with the given column data from the database, or None if no such beatmapset is stored."""
        if not where_dict:
            return None

        fetched_rows = self.fetchone_table_data("beatmapsets", where_dict, selection="id, title, artist, creator_id")
        for row in (fetched_rows or []):
            _id = row[0]
            title = row[1]
            artist = row[2]
            creator = self.retrieve_user(dict(id=row[3]))
            modes = self.retrieve_beatmapset_modes(_id)
            return Beatmapset(_id, artist, title, creator, modes)
        return None

    def retrieve_discussion(self, where_dict: dict, beatmapset: Beatmapset=None) -> Discussion:
        """Returns the first discussion with the given column data from the database, or None if no such discussion is stored.
        Also retrieves the associated beatmapset from the database if not supplied."""
        if not where_dict:
            return None

        fetched_rows = self.fetchone_table_data("discussions", where_dict, selection="id, beatmapset_id, user_id, content")
        for row in (fetched_rows or []):
            _id = row[0]
            if not beatmapset:
                beatmapset = self.retrieve_beatmapset(dict(id=row[1]))
            user = self.retrieve_user(dict(id=row[2]))
            content = row[3]

            return Discussion(_id, beatmapset, user, content)
        return None
    
    def retrieve_event(self, where_dict: dict) -> Event:
        """Returns the first event with the given column data from the database, or None if no such event is stored."""
        if not where_dict:
            return None

        fetched_rows = self.fetchone_table_data(
            "events", where_dict, selection="type, time, beatmapset_id, discussion_id, user_id, content")
        for row in (fetched_rows or []):
            _type = row[0]
            time = row[1]
            beatmapset = self.retrieve_beatmapset(dict(id=row[2]))
            discussion = self.retrieve_discussion(dict(id=row[3]))
            user = self.retrieve_user(dict(id=row[4]))
            content = row[5]
            return Event(_type, time, beatmapset, discussion, user, content=content)
        return None

database = Database()