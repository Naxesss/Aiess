import sys
sys.path.append('..')

from collections import defaultdict
from typing import Generator, Dict, List

import aiess
from aiess import Event, Beatmapset, User
from aiess.reader import merge_concurrent

from bot.objects import Subscription, Prefix

BOT_DB_NAME      = "aiess_bot"
BOT_TEST_DB_NAME = "aiess_bot_test"

beatmapset_event_cache: Dict[str, Dict[int, List[Event]]] = defaultdict(dict)  # [db_name][beatmapset_id]

class Database(aiess.Database):
    """Creates an aiess_bot database connection, with methods to insert and retrieve subscriptions."""

    def __init__(self, _db_name: str):
        super().__init__(_db_name)
    
    def insert_subscription(self, subscription: Subscription):
        """Inserts/updates the given subscription into the subscriptions table."""
        if not subscription.filter:
            raise ValueError("Subscription filter cannot be falsy.")
        self.insert_table_data(
            "subscriptions",
            dict(
                guild_id=subscription.guild_id,
                channel_id=subscription.channel_id,
                filter=subscription.filter))
    
    def retrieve_subscription(self, where: str=None, where_values: tuple=None) -> Subscription:
        """Returns the first subscription matching the given WHERE clause, if any, otherwise None."""
        return next(self.retrieve_subscriptions(where + " LIMIT 1", where_values), None)

    def retrieve_subscriptions(self, where: str=None, where_values: tuple=None) -> Generator[Subscription, None, None]:
        """Returns a generator of all subscriptions from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "subscriptions",
            where        = where,
            where_values = where_values,
            selection    = "guild_id, channel_id, filter"
        )
        for row in (fetched_rows or []):
            guild_id = row[0]
            channel_id = row[1]
            _filter = row[2]
            yield Subscription(guild_id, channel_id, _filter)
    
    def delete_subscription(self, sub: Subscription) -> None:
        """Deletes the given subscription from the subscriptions table.
        
        The filter of the given subscription does not matter, as there is only one in each channel anyway."""
        self.delete_table_data(
            table        = "subscriptions",
            where        = "guild_id=%s AND channel_id=%s",
            where_values = (sub.guild_id, sub.channel_id)
        )
    
    def insert_prefix(self, prefix: Prefix):
        """Inserts/updates the given command prefix into the prefixes table."""
        self.insert_table_data(
            "prefixes",
            dict(
                guild_id=prefix.guild_id,
                prefix=prefix.prefix))
    
    def retrieve_prefix(self, where: str=None, where_values: tuple=None) -> Prefix:
        """Returns the first command prefix matching the given WHERE clause, if any, otherwise None."""
        return next(self.retrieve_prefixes(where + " LIMIT 1", where_values), None)

    def retrieve_prefixes(self, where: str=None, where_values: tuple=None) -> Generator[Prefix, None, None]:
        """Returns a generator of all command prefixes from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "prefixes",
            where        = where,
            where_values = where_values,
            selection    = "guild_id, prefix"
        )
        for row in (fetched_rows or []):
            guild_id = row[0]
            prefix = row[1]
            yield Prefix(guild_id, prefix)
    
    def delete_prefix(self, guild_id: int) -> None:
        """Deletes the prefix of the given guild id from the prefixes table."""
        self.delete_table_data(
            table        = "prefixes",
            where        = "guild_id=%s",
            where_values = (guild_id,)
        )
    
    async def retrieve_beatmapset_events(self, beatmapset: Beatmapset) -> List[Event]:
        """Retrieves all events which have the given beatmapset id associated in descending
        order (i.e. newer events first), from the database, then stores the result in a cache
        used for any consecutive call. Concurrent events are merged together using the same
        method as on_event.
        
        The cache must be cleared before new information can be obtained, see `clear_cache`."""
        if beatmapset.id not in beatmapset_event_cache[self.db_name]:
            # Retriving events from the database will give us non-merged events (e.g.
            # user nominates -> system qualifies, instead of user qualifies), hence merge.
            raw_event_generator = self.retrieve_events(where="beatmapset_id=%s ORDER BY time DESC", where_values=(beatmapset.id,))
            raw_events = [event async for event in raw_event_generator]
            beatmapset_event_cache[self.db_name][beatmapset.id] = merge_concurrent(raw_events)

        return beatmapset_event_cache[self.db_name][beatmapset.id]

    def retrieve_event_extensive(self, where: str, where_values: tuple=None) -> Event:
        """Returns the first event from the database matching the given WHERE clause, or None if no such event is stored."""
        return next(self.retrieve_events_extensive(where + " LIMIT 1", where_values), None)

    def retrieve_events_extensive(self, where: str, where_values: tuple=None) -> Generator[Event, None, None]:
        """Returns a generator of all events from the database matching the given WHERE clause.
        Includes the properties of objects (e.g. beatmapset artist/title and username)."""
        fetched_rows = self.retrieve_table_data(
            # `LEFT JOIN`s allow for querying e.g. usernames and beatmapset artists/titles.
            table        = f"""events
                LEFT JOIN {self.db_name}.discussions AS discussion ON events.discussion_id=discussion.id
                LEFT JOIN {self.db_name}.beatmapsets AS beatmapset ON events.beatmapset_id=beatmapset.id
                LEFT JOIN {self.db_name}.newsposts AS newspost ON events.news_id=newspost.id
                LEFT JOIN {self.db_name}.users AS author ON discussion.user_id=author.id
                LEFT JOIN {self.db_name}.users AS creator ON beatmapset.creator_id=creator.id
                LEFT JOIN {self.db_name}.users AS user ON events.user_id=user.id
                LEFT JOIN {self.db_name}.beatmapset_modes AS modes ON beatmapset.id=modes.beatmapset_id""",
            where        = where,
            where_values = where_values,
            selection    = "events.type, events.time, events.beatmapset_id, events.discussion_id, events.user_id, events.news_id, events.content"
        )
        for row in (fetched_rows or []):
            _type = row[0]
            time = row[1]
            beatmapset = self.retrieve_beatmapset("id=%s", (row[2],)) if row[2] else None
            discussion = self.retrieve_discussion("id=%s", (row[3],)) if row[3] else None
            user = self.retrieve_user("id=%s", (row[4],)) if row[4] else None
            newspost = self.retrieve_newspost("id=%s", (row[5],)) if row[5] else None
            content = row[6]
            yield Event(_type, time, beatmapset, discussion, user, newspost=newspost, content=content)

def clear_cache(db_name: str) -> None:
    """Clears any cache the database may be using, allowing new info to be obtained
    (e.g. for retrieving all events related to a beatmapset)."""
    beatmapset_event_cache[db_name].clear()