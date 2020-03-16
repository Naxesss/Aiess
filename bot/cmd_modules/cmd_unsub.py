from commands import Command, register
from subscriber import unsubscribe

@register("unsub")
async def cmd_ping(command: Command):
    unsubscribe(command.context.channel)
    await command.respond("✓ unsubbed")