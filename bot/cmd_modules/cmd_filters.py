import sys
sys.path.append('..')

from discord import Embed

from bot.commands import Command, register, COMMAND_PREFIX
from bot.filterer import AND_GATES, OR_GATES, NOT_GATES, TAGS
from bot.filterer import get_tag, get_tag_keys
from bot.formatter import truncate
from bot.commands import EVENTS_CATEGORY

@register(
    category      = EVENTS_CATEGORY,
    name          = "filters",
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

        await command.respond(f"Type `{COMMAND_PREFIX}filters` for a list of keys and gates.", embed=embed)
        return

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

    await command.respond(f"Type `{COMMAND_PREFIX}filters <key>` for usage.", embed=embed)