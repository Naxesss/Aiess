from typing import Generator, Dict, List

import aiess
from aiess import Event, Beatmapset, User
from aiess.reader import merge_concurrent

from subscriptions import Subscription

class Database(aiess.Database):
    """Creates an aiess_bot database connection, with methods to insert and retrieve subscriptions."""

    def __init__(self, _db_name:str="aiess_bot"):
        self.beatmapset_event_cache: Dict[int, List[Event]] = {}
        self.last_type_cache: Dict[str, Event] = {}
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
        self.delete_table_data("subscriptions",
            where_str=f"guild_id={sub.guild_id} AND channel_id={sub.channel_id}")
    
    def retrieve_beatmapset_events(self, beatmapset: Beatmapset) -> List[Event]:
        """Retrieves all events which have the given beatmapset id associated in
        descending order (i.e. newer events first), from the database, then stores
        the result in a cache used for any consecutive call. Concurrent events
        are merged together using the same method as on_event.
        
        The cache must be cleared manually before new information can be obtained,
        see `clear_cache`."""
        if beatmapset.id not in self.beatmapset_event_cache:
            # Retriving events from the database will give us non-merged events (e.g.
            # user nominates -> system qualifies, instead of user qualifies), hence merge.
            raw_events = list(self.retrieve_events(f"beatmapset_id = {beatmapset.id} ORDER BY time DESC"))
            self.beatmapset_event_cache[beatmapset.id] = merge_concurrent(raw_events)

        return self.beatmapset_event_cache[beatmapset.id]
    
    def retrieve_last_type(self, user: User, beatmapset: Beatmapset, _type: str) -> Event:
        """Retrieves the last event of the given type made by the given user on the given beatmapset.
        This is first done from the database, and then from a cache for any consecutive call.
        
        The cache must be cleared manually before new information can be obtained,
        see `clear_cache`."""
        args_id = f"{user.id}-{beatmapset.id}-{_type}"
        if args_id not in self.last_type_cache:
            event = self.retrieve_event(f"""
                beatmapset_id = {beatmapset.id} AND
                user_id = {user.id} AND
                type = \"{_type}\"
                ORDER BY time DESC
                LIMIT 1""")
            self.last_type_cache[args_id] = event

        return self.last_type_cache[args_id]

    def clear_cache(self) -> None:
        """Clears any cache the database may be using, allowing new info to be obtained
        (e.g. for retrieving all events related to a beatmapset)."""
        self.beatmapset_event_cache.clear()
        self.last_type_cache.clear()

database = Database()