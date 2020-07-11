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
    if not any(sub.channel_id == command.context.channel.id for sub in subscriber.cache):
        await command.respond_err("Nothing to unsubscribe")
        return

    unsubscribe(command.context.channel)
    await command.respond("✓ Unsubscribed")