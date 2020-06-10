import sys
sys.path.append('..')

from bot.commands import Command, register
from bot import subscriber
from bot.subscriber import unsubscribe

@register("unsub")
async def cmd_unsub(command: Command):
    if not any(sub.channel_id == command.context.channel.id for sub in subscriber.cache):
        # End result is what caller expected (clearing subs in the channel), hence success.
        # Should still let them know that we didn't do anything, though, e.g. in case of wrong channel.
        await command.respond("✓ nothing to unsub")
        return

    unsubscribe(command.context.channel)
    await command.respond("✓ unsubbed")