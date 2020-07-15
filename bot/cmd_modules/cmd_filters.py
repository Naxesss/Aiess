import sys
sys.path.append('..')

from discord import Embed

from bot.commands import Command, register, COMMAND_PREFIX
from bot.filterer import AND_GATES, OR_GATES, NOT_GATES, TAGS
from bot.filterer import get_tag, get_tag_keys
from bot.formatter import truncate
from bot.commands import EVENTS_CATEGORY
from bot.cmdcommon import filters_embed, filter_embed

@register(
    category      = EVENTS_CATEGORY,
    names         = ["filters", "filter"],
    optional_args = ["key"],
    description   = "Returns a list of filter keys and gates, or optionally the usage of `[key]`.",
    example_args  = [None, "type"]
)
async def cmd_filters(command: Command, key: str=None):
    if key:
        key = key.lower().strip()
        tag = get_tag(key)
        keys = get_tag_keys(key)

        if not tag or not keys:
            await command.respond_err(f"No filter key `{key}` exists.")
            return

        await command.respond(f"Type `{COMMAND_PREFIX}filters` for a list of keys and gates.", embed=filter_embed(key))
        return

    await command.respond(f"Type `{COMMAND_PREFIX}filters <key>` for usage.", embed=filters_embed())