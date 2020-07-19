import sys
sys.path.append('..')

from discord import Embed, Colour

from bot.commands import Command, register
from bot.cmdcommon import validate_filter
from bot.subscriber import get_subscription
from bot.subscriber import subscribe
from bot.filterer import expand
from bot.formatter import escape_markdown
from bot.commands import EVENTS_CATEGORY

@register(
    category      = EVENTS_CATEGORY,
    names         = ["sub", "subscribe"],
    optional_args = ["filter"],
    description   = """
        Subscribes this channel to events matching `[filter]`, if specified, otherwise shows the current channel subscription.

        See also `{0}unsub` and `{0}recent`.
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
                """ if subscription else "None"
        )

        content = (
            f"Type `{command.prefix()}sub <filter>` to change subscription" +
            (f", or `{command.prefix()}unsub` to unsubscribe" if subscription else "") +
            "."
        )
        await command.respond(content, embed=embed)
        return

    if not await validate_filter(command, _filter):
        return  # `validate_filter` will respond for us.

    subscribe(command.context.channel, _filter)

    embed = Embed()
    embed.colour = Colour.from_rgb(255, 170, 50)
    embed.add_field(
        name="🔔\u2000Subscribed to",
        value=f"""
            {escape_markdown(_filter)}
            `{expand(_filter)}`
            """
    )

    await command.respond("✓", embed=embed)