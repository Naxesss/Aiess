import sys
sys.path.append('..')

from bot.prefixes import DEFAULT_PREFIX
from bot.prefixes import set_prefix
from bot.commands import Command, register
from bot.commands import GENERAL_CATEGORY

@register(
    category      = GENERAL_CATEGORY,
    names         = ["prefix"],
    required_args = ["symbol"],
    description   = f"""
        Changes the command prefix to `<symbol>` for this server.
        Current is `{{0}}`, default is `{DEFAULT_PREFIX}`.
        `<symbol>` cannot include whitespace.
        """,
    example_args  = ["&", "a!", DEFAULT_PREFIX]
)
async def cmd_prefix(command: Command, symbol: str):
    if not command.guild_id():
        await command.respond_err(f"Cannot change prefix in DM channels.")
        return
    
    if " " in symbol:
        await command.respond_err(f"`<symbol>` cannot include whitespace.")
        return
    
    # The discord message character limit is 2000.
    # Need enough characters to write `{prefix}prefix +` to reset it.
    len_limit = 2000 - len("prefix +")
    if len(symbol) > len_limit:
        await command.respond_err(f"`<symbol>` cannot exceed {len_limit} characters.")
        return

    old_prefix = command.prefix()
    set_prefix(command.guild_id(), symbol)
    await command.respond(f"✓ Command prefix changed from `{old_prefix}` to `{command.prefix()}`.")