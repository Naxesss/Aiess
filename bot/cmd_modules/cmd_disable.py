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
    names         = ["disable"],
    required_args = ["command(s)"],
    description   = """
        Disables the given `<command(s)>` such that only admins can use it.
        Optionally only enable for certain roles/channels/users, using a logical `[filter]`.

        See also `{0}enable` and `{0}permissions`.
        """,
    example_args  = [
        "recent",
        "\"help, ping, info\""
    ]
)
async def cmd_disable(command: Command, commands_str: str):
    if not command.guild_id():
        await command.respond_err("Cannot change permissions in DM channels.")
        return

    command_wrappers = get_command_wrappers(commands_str)
    for command_wrapper in command_wrappers:
        permissions.set_permission_filter(
            guild_id          = command.guild_id(),
            command_wrapper   = command_wrapper,
            permission_filter = None
        )
    
    await command.respond(
        response = "✓ Command permissions changed.",
        embed    = permissions_embed(
            guild_id         = command.guild_id(),
            command_wrappers = command_wrappers
        )
    )