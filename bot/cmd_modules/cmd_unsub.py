import sys
sys.path.append('..')

from discord import Embed
from discord import Colour

from bot.commands import Command, register
from bot import subscriber
from bot.subscriber import unsubscribe
from bot.formatter import escape_markdown
from bot.filterer import expand
from bot.commands import EVENTS_CATEGORY

@register(
    category    = EVENTS_CATEGORY,
    names       = ["unsub", "unsubscribe"],
    description = """
        Unsubscribes this channel from any event subscriptions.

        See also `{0}sub`.
        """
)
async def cmd_unsub(command: Command):
    subscription = subscriber.get_subscription(command.context.channel)
    if not subscription:
        await command.respond_err("Nothing to unsubscribe")
        return

    unsubscribe(subscription)

    embed = Embed()
    embed.colour = Colour.from_rgb(255, 170, 50)
    embed.add_field(
        name="🔕\u2000Unsubscribed from",
        value=f"""
            {escape_markdown(subscription.filter)}
            `{expand(subscription.filter)}`
            """
    )

    await command.respond("✓", embed=embed)