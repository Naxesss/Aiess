import sys
sys.path.append('..')

from bot.commands import Command, register
from bot.subscriber import unsubscribe

@register("unsub")
async def cmd_ping(command: Command):
    unsubscribe(command.context.channel)
    await command.respond("✓ unsubbed")