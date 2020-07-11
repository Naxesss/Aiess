import sys
sys.path.append('..')

from discord import Embed, Colour

from bot.commands import Command, register
from bot.commands import COMMAND_PREFIX
from bot.cmdcommon import validate_filter
from bot.subscriber import get_subscription
from bot.subscriber import subscribe
from bot.filterer import expand
from bot.formatter import escape_markdown

@register(
    name          = "sub",
    optional_args = ["filter"],
    description   = f"""
        Subscribes this channel to events matching `[filter]`, if specified, otherwise shows the current channel subscription.

        See also `{COMMAND_PREFIX}unsub`.
        """,
    example_args  = [
        "type:(rank or love)",
        "user:\"space in name\"",
        "(user or creator):someone and not type:reply"
    ])
async def cmd_sub(command: Command, _filter: str=None):
    if not _filter:
        subscription = get_subscription(command.context.channel)

        embed = Embed()
        embed.colour = Colour.from_rgb(255, 170, 50)
        embed.add_field(
            name="🔔\u2000Current Subscription",
            value=f"""
                {escape_markdown(subscription.filter)}
                `{expand(subscription.filter)}`
                """
        )

        await command.respond("", embed=embed)
        return

    if not await validate_filter(command, _filter):
        return  # `validate_filter` will respond for us.

    subscribe(command.context.channel, _filter)

    embed = Embed()
    embed.colour = Colour.from_rgb(255, 170, 50)
    embed.add_field(
        name="🔔\u2000Subscribed",
        value=f"""
            {escape_markdown(_filter)}
            `{expand(_filter)}`
            """
    )

    await command.respond("✓", embed=embed)