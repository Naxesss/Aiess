import sys
sys.path.append('..')

from collections import defaultdict
from typing import Generator, Dict, List

import aiess
from aiess import Event, Beatmapset, User
from aiess.reader import merge_concurrent

from bot.subscriptions import Subscription

BOT_DB_NAME      = "aiess_bot"
BOT_TEST_DB_NAME = "aiess_bot_test"

beatmapset_event_cache: Dict[str, Dict[int, List[Event]]] = defaultdict(dict)  # [db_name][beatmapset_id]
last_type_cache:        Dict[str, Dict[str, Event]]       = defaultdict(dict)  # [db_name][{user.id}-{beatmapset.id}-{where_type_str}]

class Database(aiess.Database):
    """Creates an aiess_bot database connection, with methods to insert and retrieve subscriptions."""

    def __init__(self, _db_name: str):
        super().__init__(_db_name)
    
    def insert_subscription(self, subscription: Subscription):
        """Inserts/updates the given subscription into the subscriptions table."""
        self.insert_table_data(
            "subscriptions",
            dict(
                guild_id=subscription.guild_id,
                channel_id=subscription.channel_id,
                filter=subscription.filter))
    
    def retrieve_subscriptions(self, where_str: str=None) -> Generator[Subscription, None, None]:
        """Returns a generator of all subscriptions from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data("subscriptions", where_str, selection="guild_id, channel_id, filter")
        for row in (fetched_rows or []):
            guild_id = row[0]
            channel_id = row[1]
            _filter = row[2]
            yield Subscription(guild_id, channel_id, _filter)
    
    def delete_subscription(self, sub: Subscription) -> None:
        """Deletes the given subscription from the subscriptions table.
        
        The filter of the given subscription does not matter, as there is only one in each channel anyway."""
        self.delete_table_data(
            "subscriptions",
            where_str=f"guild_id={sub.guild_id} AND channel_id={sub.channel_id}"
        )
    
    def retrieve_beatmapset_events(self, beatmapset: Beatmapset) -> List[Event]:
        """Retrieves all events which have the given beatmapset id associated in descending
        order (i.e. newer events first), from the database, then stores the result in a cache
        used for any consecutive call. Concurrent events are merged together using the same
        method as on_event.
        
        The cache must be cleared before new information can be obtained, see `clear_cache`."""
        if beatmapset.id not in beatmapset_event_cache[self.db_name]:
            # Retriving events from the database will give us non-merged events (e.g.
            # user nominates -> system qualifies, instead of user qualifies), hence merge.
            raw_events = list(self.retrieve_events(f"beatmapset_id = {beatmapset.id} ORDER BY time DESC"))
            beatmapset_event_cache[self.db_name][beatmapset.id] = merge_concurrent(raw_events)

        return beatmapset_event_cache[self.db_name][beatmapset.id]
    
    def retrieve_last_type(self, user: User, beatmapset: Beatmapset, where_type_str: str) -> Event:
        """Retrieves the last event made by the given user on the given beatmapset, satisfying the
        additional where clause for types (e.g. `type = \"praise\" OR type = \"hype\"`). This is
        first done from the database, and then from a cache for any consecutive call.
        
        The cache must be cleared before new information can be obtained, see `clear_cache`."""
        args_id = f"{user.id}-{beatmapset.id}-{where_type_str}"
        if args_id not in last_type_cache[self.db_name]:
            event = self.retrieve_event(f"""
                beatmapset_id = {beatmapset.id} AND
                user_id = {user.id} AND
                ({where_type_str})
                ORDER BY time DESC
                LIMIT 1""")
            last_type_cache[self.db_name][args_id] = event

        return last_type_cache[self.db_name][args_id]

def clear_cache(db_name: str) -> None:
    """Clears any cache the database may be using, allowing new info to be obtained
    (e.g. for retrieving all events related to a beatmapset)."""
    beatmapset_event_cache[db_name].clear()
    last_type_cache[db_name].clear()