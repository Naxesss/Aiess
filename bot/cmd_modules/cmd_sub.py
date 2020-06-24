import sys
sys.path.append('..')

from discord import Embed, Colour

from bot.commands import Command, register
from bot.commands import COMMAND_PREFIX
from bot.subscriber import subscribe
from bot.filterer import expand, get_invalid_keys, get_invalid_filters, get_invalid_words
from bot.formatter import escape_markdown

@register(
    name          = "sub",
    required_args = ["filter"],
    description   = f"""
        Subscribes this channel to events matching `<filter>`.

        See also `{COMMAND_PREFIX}unsub`.
        """,
    example_args  = [
        "type:(rank or love)",
        "user:\"space in name\"",
        "(user or creator):someone and not type:reply"
    ])
async def cmd_sub(command: Command, _filter: str):

    try:
        expansion = expand(_filter)
    except ValueError as err:
        # E.g. parenthesis inequality.
        await command.respond_err(f"{str(err)}")
        return

    invalid_keys = set(get_invalid_keys(_filter))
    if invalid_keys:
        invalids_formatted = "`" + "`, `".join(invalid_keys) + "`"
        await command.respond_err(f"Invalid key(s) {invalids_formatted}.")
        return

    invalid_filters = set(get_invalid_filters(_filter))
    if invalid_filters:
        invalids_strs = (f"{key}:{value}" for key, value in invalid_filters)
        invalids_formatted = "`" + "`, `".join(invalids_strs) + "`"
        await command.respond_err(f"Invalid value(s) for key(s) {invalids_formatted}.") # TODO: Show valid values.
        return

    invalid_words = set(get_invalid_words(_filter))
    if invalid_words:
        invalids_formatted = "`" + "`, `".join(invalid_words) + "`"
        await command.respond_err(f"Invalid word(s) {invalids_formatted}.")
        return

    if not hasattr(command.context.channel, "guild"):
        # Prevents excessive discord rate limiting (5 DMs per second globally).
        await command.respond_err(f"Cannot subscribe in DM channels.")
        return

    subscribe(command.context.channel, _filter)

    embed = Embed()
    embed.colour = Colour.from_rgb(255, 170, 50)
    embed.add_field(
        name="🔔 Subscribed",
        value=f"""
            {escape_markdown(_filter)}
            `{expansion}`
            """
    )

    await command.respond("✓", embed=embed)