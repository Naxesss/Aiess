import sys
sys.path.append('..')

from bot.objects import CommandPermission
from bot import commands
from bot.commands import FunctionWrapper, Command
from bot.database import Database, BOT_DB_NAME
from bot.filterers.perms_filterer import filter_context

DEFAULT_DB_NAME = BOT_DB_NAME

cache = {}  # 2d-dict, `cache[guild_id][command_wrapper.names[0]] = permission_filter`

def load() -> None:
    """Loads the guild-specific command permissions from the database into the cache."""
    cache.clear()
    for perm_obj in Database(DEFAULT_DB_NAME).retrieve_permissions():
        if perm_obj.guild_id not in cache:
            cache[perm_obj.guild_id] = { perm_obj.command_name : perm_obj.permission_filter }
        else:
            cache[perm_obj.guild_id][perm_obj.command_name] = perm_obj.permission_filter

def get_permission_filter(guild_id: int, command_wrapper: FunctionWrapper) -> str:
    """Returns the permission filter used for this command type in this guild, or None if no such filter exists."""
    if guild_id not in cache or command_wrapper.names[0] not in cache[guild_id]:
        return None
    
    return cache[guild_id][command_wrapper.names[0]]

def set_permission_filter(guild_id: int, command_wrapper: FunctionWrapper, permission_filter: str) -> None:
    """Updates the permission filter in this guild for this command to the given value.
    If given `None`, the permission entry is deleted."""
    if permission_filter is None:
        Database(DEFAULT_DB_NAME).delete_permission(guild_id, command_wrapper.names[0])
    else:
        Database(DEFAULT_DB_NAME).insert_permission(CommandPermission(guild_id, command_wrapper.names[0], permission_filter))
    load()

async def can_execute(command: Command) -> bool:
    """Returns whether the given command has permissions to execute within its current context
    (channel/author/roles of that guild). Administrators bypass any permission."""
    command_wrapper = commands.get_wrapper(command.name)
    perm_filter = get_permission_filter(command.guild_id(), command_wrapper)
    has_permission = filter_context.test(perm_filter, command.context) if perm_filter else False

    caller = command.context.author
    # The `guild_permissions` attribute is only available in guilds, for DM channels we skip this.
    is_admin_or_dm = not hasattr(caller, "guild_permissions") or caller.guild_permissions.administrator

    if not command_wrapper.wip:
        return has_permission or is_admin_or_dm
    else:
        # Only the owner of the bot should be able to use WIP commands.
        app_info = await command.client.application_info()
        return caller.id == app_info.owner.id