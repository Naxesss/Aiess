import sys
sys.path.append('..')

from bot.commands import Command, register

@register(
    name        = "ping",
    description = "Returns \"pong\"."
)
async def cmd_ping(command: Command):
    await command.respond("pong")