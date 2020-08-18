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
    names         = ["enable"],
    required_args = ["command(s)"],
    optional_args = ["filter"],
    description   = """
        Enables the given `<command(s)>` for everyone anywhere in the server.
        Optionally only enable for certain roles/channels/users, using a logical `[filter]`.

        See also `{0}disable` and `{0}permissions`.
        """,
    example_args  = [
        "recent",
        "\"help, ping, info\"",
        "recent channel:#bot",
        "\"recent, info\" \"role:@verified and channel:#bot or role:@moderators\""
    ]
)
async def cmd_enable(command: Command, commands_str: str, perms_filter: Optional[str]=None):
    if not command.guild_id():
        await command.respond_err("Cannot change permissions in DM channels.")
        return
    
    if perms_filter and not await validate_filter(command, perms_filter, filter_context):
        # `validate_filter` responds for us.
        return

    command_wrappers = get_command_wrappers(commands_str)
    for command_wrapper in command_wrappers:
        permissions.set_permission_filter(
            guild_id          = command.guild_id(),
            command_wrapper   = command_wrapper,
            permission_filter = perms_filter or f"role:<@&{command.context.guild.default_role.id}>"
        )
    
    await command.respond(
        response = "✓ Command permissions changed.",
        embed    = permissions_embed(
            guild_id         = command.guild_id(),
            command_wrappers = command_wrappers
        )
    )