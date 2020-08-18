import sys
sys.path.append('..')

from bot.commands import Command, register
from bot.filterers.event_filterer import filter_context
from bot.commands import EVENTS_CATEGORY
from bot.cmdcommon import filters_embed, filter_embed
from bot.filterers.event_filterer import filter_context

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
        tag = filter_context.get_tag(key)
        keys = tag.names if tag else None

        if not tag or not keys:
            await command.respond_err(f"No filter key `{key}` exists.")
            return

        await command.respond(
            response = f"Type `{command.prefix()}filters` for a list of keys and gates.",
            embed    = filter_embed(key, filter_context)
        )
        return

    await command.respond(
        response = f"Type `{command.prefix()}filters <key>` for usage.",
        embed    = filters_embed(filter_context)
    )