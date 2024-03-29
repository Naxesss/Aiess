import sys
sys.path.append('..')

from collections import defaultdict
from typing import Generator, Dict, List

import aiess
from aiess import Event, Beatmapset, Usergroup

from bot.objects import Subscription, Prefix, CommandPermission

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
    
    def retrieve_subscription(self, where: str=None, where_values: tuple=None, group_by: str=None, order_by: str=None) -> Subscription:
        """Returns the first subscription matching the given WHERE clause, if any, otherwise None."""
        return next(
            self.retrieve_subscriptions(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1
            ),
            None
        )

    def retrieve_subscriptions(
            self, where: str=None, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None
        ) -> Generator[Subscription, None, None]:
        """Returns a generator of all subscriptions from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "subscriptions",
            where        = where,
            where_values = where_values,
            selection    = "guild_id, channel_id, filter",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
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
    
    def retrieve_prefix(self, where: str=None, where_values: tuple=None, group_by: str=None, order_by: str=None) -> Prefix:
        """Returns the first command prefix matching the given WHERE clause, if any, otherwise None."""
        return next(
            self.retrieve_prefixes(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1
            ),
            None
        )

    def retrieve_prefixes(
            self, where: str=None, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None
        ) -> Generator[Prefix, None, None]:
        """Returns a generator of all command prefixes from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "prefixes",
            where        = where,
            where_values = where_values,
            selection    = "guild_id, prefix",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
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

    def insert_permission(self, permission: CommandPermission):
        """Inserts/updates the given command permission into the permissions table."""
        self.insert_table_data(
            "permissions",
            dict(
                guild_id=permission.guild_id,
                command_name=permission.command_name,
                permission_filter=permission.permission_filter))
    
    def retrieve_permission(self, where: str=None, where_values: tuple=None, group_by: str=None, order_by: str=None) -> CommandPermission:
        """Returns the first command permission matching the given WHERE clause, if any, otherwise None."""
        return next(
            self.retrieve_permissions(
                where        = where,
                where_values = where_values,
                group_by     = group_by,
                order_by     = order_by,
                limit        = 1
            ),
            None
        )

    def retrieve_permissions(
            self, where: str=None, where_values: tuple=None, group_by: str=None,
            order_by: str=None, limit: int=None
        ) -> Generator[CommandPermission, None, None]:
        """Returns a generator of all command permissions from the database matching the given WHERE clause."""
        fetched_rows = self.retrieve_table_data(
            table        = "permissions",
            where        = where,
            where_values = where_values,
            selection    = "guild_id, command_name, permission_filter",
            group_by     = group_by,
            order_by     = order_by,
            limit        = limit
        )
        for row in (fetched_rows or []):
            guild_id = row[0]
            command_name = row[1]
            permission_filter = row[2]
            yield CommandPermission(guild_id, command_name, permission_filter)
    
    def delete_permission(self, guild_id: int, command_name: str) -> None:
        """Deletes the command permission of the given guild id from the permissions table."""
        self.delete_table_data(
            table        = "permissions",
            where        = "guild_id=%s AND command_name=%s",
            where_values = (guild_id, command_name)
        )
    
    async def retrieve_beatmapset_events(self, beatmapset: Beatmapset) -> List[Event]:
        """Retrieves all events which have the given beatmapset id associated in descending
        order (i.e. newer events first), from the database, then stores the result in a cache
        used for any consecutive call.
        
        The cache must be cleared before new information can be obtained, see `clear_cache`."""
        if beatmapset.id not in beatmapset_event_cache[self.db_name]:
            raw_event_generator = self.retrieve_events(
                where        = "beatmapset_id=%s",
                where_values = (beatmapset.id,),
                order_by     = "time DESC"
            )
            beatmapset_event_cache[self.db_name][beatmapset.id] = [event async for event in raw_event_generator]

        return beatmapset_event_cache[self.db_name][beatmapset.id]

def clear_cache(db_name: str) -> None:
    """Clears any cache the database may be using, allowing new info to be obtained
    (e.g. for retrieving all events related to a beatmapset)."""
    beatmapset_event_cache[db_name].clear()