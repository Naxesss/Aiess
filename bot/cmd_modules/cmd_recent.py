import sys
sys.path.append('..')

from discord import Embed

from aiess.database import SCRAPER_DB_NAME

from bot.commands import Command, register
from bot.commands import COMMAND_PREFIX
from bot.filterer import passes_filter, filter_to_sql
from bot.cmdcommon import validate_filter
from bot.formatter import format_link, format_embed, format_timeago
from bot.database import Database
from bot.commands import EVENTS_CATEGORY

@register(
    category      = EVENTS_CATEGORY,
    names         = ["recent", "r"],
    optional_args = ["filter"],
    description   = f"""
        Returns the most recent event gathered, optionally matching `[filter]`.
        
        See also `{COMMAND_PREFIX}sub`.
        """,
    example_args  = [
        "type:(rank or love)",
        "user:\"space in name\"",
        "(user or creator):someone and not type:reply"
    ]
)
async def cmd_recent(command: Command, _filter: str=None):
    if _filter and not await validate_filter(command, _filter):
        return  # `validate_filter` will respond for us.

    filter_query, filter_values = filter_to_sql(_filter)
    database = Database(SCRAPER_DB_NAME)
    event = database.retrieve_event_extensive(
        where        = f"""
            {filter_query}
            ORDER BY time DESC
            LIMIT 1
            """,
        where_values = filter_values
    )
    
    matching_filter_str = f" matching `{_filter}`" if _filter else ""

    if not event:
        await command.respond_err(f"No event{matching_filter_str} could be found.")
        return
    
    await command.respond(
        response = f"✓ Most recent event{matching_filter_str}\r\n{format_link(event)}",
        embed = await format_embed(event)
    )