import sys
sys.path.append('..')

from bot.commands import Command, register
from bot import subscriber
from bot.subscriber import unsubscribe

@register(
    name         = "unsub",
    description  = "Unsubscribes this channel from any events."
)
async def cmd_unsub(command: Command):
    subscription = subscriber.get_subscription(command.context.channel)
    if not subscription:
        await command.respond_err("Nothing to unsubscribe")
        return

    unsubscribe(subscription)
    await command.respond("✓ Unsubscribed")