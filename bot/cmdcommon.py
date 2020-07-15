import sys
sys.path.append('..')

from discord import Embed

from bot.commands import Command
from bot.filterer import expand, get_invalid_keys, get_invalid_filters, get_invalid_words
from bot.filterer import get_tag, get_tag_keys
from bot.filterer import TAGS, AND_GATES, OR_GATES, NOT_GATES

async def validate_filter(command: Command, _filter: str):
    """Returns whether the filter was considered valid. If invalid, an appropriate response is sent
    where the command was called."""
    try:
        expansion = expand(_filter)
    except ValueError as err:
        # E.g. parenthesis inequality.
        await command.respond_err(f"{str(err)}")
        return False

    invalid_keys = set(get_invalid_keys(_filter))
    if invalid_keys:
        invalids_formatted = "`" + "`, `".join(invalid_keys) + "`"
        await command.respond_err(f"Invalid key(s) {invalids_formatted} in expansion `{expansion}`.")
        return False

    invalid_filters = set(get_invalid_filters(_filter))
    if invalid_filters:
        invalids_strs = (f"{key}:{value}" for key, value in invalid_filters)
        invalids_formatted = "`" + "`, `".join(invalids_strs) + "`"
        await command.respond_err(f"Invalid value(s) for key(s) {invalids_formatted} in expansion `{expansion}`.") # TODO: Show valid values.
        return False

    invalid_words = set(get_invalid_words(_filter))
    if invalid_words:
        invalids_formatted = "`" + "`, `".join(invalid_words) + "`"
        await command.respond_err(f"Invalid word(s) {invalids_formatted} in expansion `{expansion}`.")
        return False

    if not hasattr(command.context.channel, "guild"):
        # Prevents excessive discord rate limiting (5 DMs per second globally).
        await command.respond_err(f"Cannot subscribe in DM channels.")
        return False
    
    return True

def filters_embed():
    embed = Embed()
    embed.title = "The **`<filter>`** Argument"
    embed.description = """
            A string of key:value pairs (e.g. `type:(nominate or qualify) and user:lasse`).
            Keys and values are always case insensitive.
            """
    embed.add_field(
        name = "Keys (`/` denotes aliases)",
        value = "\u2000".join("/".join(f"**`{key}`**" for key in keys) for keys in TAGS.keys()),
        inline = True
    )
    embed.add_field(
        name = "Gates",
        value = (
            "**AND**\u2000" + "\u2000".join(f"**`{gate.strip()}`**" for gate in AND_GATES) + "\r\n" +
            "**OR**\u2000"  + "\u2000".join(f"**`{gate.strip()}`**" for gate in OR_GATES)  + "\r\n" +
            "**NOT**\u2000" + "\u2000".join(f"**`{gate.strip()}`**" for gate in NOT_GATES)
        ),
        inline = True
    )
    return embed

def filter_embed(key: str):
    key = key.lower().strip()
    tag = get_tag(key)
    keys = get_tag_keys(key)

    embed = Embed()
    embed.add_field(
        name = "/".join(f"**`{key}`**" for key in keys),
        value = tag.description,
        inline = True
    )
    embed.add_field(
        name = "Value(s)",
        value = tag.validation.hint,
        inline = True
    )
    embed.add_field(
        name = "Example(s)",
        value = "\r\n".join(f"∙ `{key}:{value}`" for value in tag.example_values),
        inline = True
    )
    return embed