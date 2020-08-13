import sys
sys.path.append('..')

from bot.objects import CommandPermission
from bot.commands import FunctionWrapper
from bot.database import Database, BOT_DB_NAME
from bot.filterers.perms_filterer import filter_context

cache = {}  # 2d-dict, `cache[guild_id][command_wrapper.names[0]] = permission_filter`

def load():
    """Loads the guild-specific command permissions from the database into the cache."""
    cache.clear()
    for perm_obj in Database(BOT_DB_NAME).retrieve_permissions():
        cache[perm_obj.guild_id] = { perm_obj.command_name : perm_obj.permission_filter }

def get_permission_filter(guild_id: int, command_wrapper: FunctionWrapper):
    """Returns the permission filter used for this command type in this guild, or None if no such filter exists."""
    if guild_id not in cache or command_wrapper.names[0] not in cache[guild_id]:
        return None
    
    return cache[guild_id][command_wrapper.names[0]]

def set_permission_filter(guild_id: int, command_wrapper: FunctionWrapper, permission_filter: str):
    """Updates the permission filter in this guild for this command to the given value."""
    if permission_filter is None:
        Database(BOT_DB_NAME).delete_permission(guild_id, command_wrapper.names[0])
    else:
        Database(BOT_DB_NAME).insert_permission(CommandPermission(guild_id, command_wrapper.names[0], permission_filter))
    load()