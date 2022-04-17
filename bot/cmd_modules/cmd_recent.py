import sys
sys.path.append('..')

from aiess.database import SCRAPER_DB_NAME

from bot.commands import Command, register
from bot.filterers.event_filterer import filter_to_sql
from bot.cmdcommon import validate_filter
from bot.formatter import format_link, format_embed
from bot.database import Database
from bot.commands import EVENTS_CATEGORY
from bot.filterers.event_filterer import filter_context

@register(
    category      = EVENTS_CATEGORY,
    names         = ["recent", "r"],
    optional_args = ["filter"],
    description   = """
        Returns the most recent event gathered, optionally matching `[filter]`.
        
        See also `{0}sub`.
        """,
    example_args  = [
        "type:(rank or love)",
        "user:\"space in name\"",
        "(user or creator):someone and not type:reply"
    ]
)
async def cmd_recent(command: Command, _filter: str=None):
    if _filter and not await validate_filter(command, _filter, filter_context):
        return  # `validate_filter` will respond for us.

    matching_filter_str = f" matching `{_filter}`" if _filter else ""

    filter_query, filter_values = filter_to_sql(_filter)
    database = Database(SCRAPER_DB_NAME)
    try:
        event = await database.retrieve_event(
            where        = filter_query,
            where_values = filter_values,
            order_by     = "time DESC",
            extensive    = True if _filter else False
        )
    except TimeoutError:
        await command.respond_err(f"Took too long to find an event{matching_filter_str}.")
        return

    if not event:
        await command.respond_err(f"No event{matching_filter_str} could be found.")
        return
    
    await command.respond(
        response = f"✓ Most recent event{matching_filter_str}:\r\n{format_link(event)}",
        embed = await format_embed(event)
    )