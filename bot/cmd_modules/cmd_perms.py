import sys
sys.path.append('..')

from typing import Optional, List

from bot import commands
from bot.commands import register
from bot.commands import Command, FunctionWrapper
from bot.commands import PERMISSIONS_CATEGORY
from bot.cmdcommon import validate_filter, permissions_embed, get_command_wrappers
from bot import permissions
from bot.filterers.perms_filterer import filter_context

@register(
    category      = PERMISSIONS_CATEGORY,
    names         = ["perms", "permissions"],
    optional_args = ["command(s)"],
    description   = """
        Shows all command permissions in the server. Optionally only `[command(s)]`.

        See also `{0}enable` and `{0}disable`.
        """,
    example_args  = [
        None,
        "recent",
        "\"help, ping, info\""
    ]
)
async def cmd_perms(command: Command, commands_str: Optional[str]=None):
    if not command.guild_id():
        await command.respond_err("Permissions unavailable in DM channels.")
        return

    command_wrappers = get_command_wrappers(commands_str)
    await command.respond(
        response = f"See `{command.prefix()}enable` and `{command.prefix()}disable` for changing permissions.",
        embed    = permissions_embed(
            guild_id         = command.guild_id(),
            command_wrappers = command_wrappers
        )
    )