from typing import Generator

import aiess

from subscriptions import Subscription

class Database(aiess.Database):
    """Creates an aiess_bot database connection, with methods to insert and retrieve subscriptions."""
    
    def __init__(self, _db_name:str="aiess_bot"):
        super().__init__(_db_name)
    
    def insert_channel_sub(self, subscription: Subscription):
        """Inserts/updates the given channel subscription into the channel subscriptions table."""
        self.insert_table_data(
            "channel_subscriptions",
            dict(
                guild_id=subscription.guild_id,
                channel_id=subscription.channel_id,
                filter=subscription.filter))
    
    def retrieve_channel_subs(self, where_str: str=None) -> Generator[Subscription, None, None]:
        """Returns a generator of all channel subscriptions from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data("channel_subscriptions", where_str, selection="guild_id, channel_id, filter")
        for row in (fetched_rows or []):
            guild_id = row[0]
            channel_id = row[1]
            _filter = row[2]
            yield Subscription(guild_id, channel_id, _filter)

database = Database()