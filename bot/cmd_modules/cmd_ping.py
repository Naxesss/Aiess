from commands import Command, register

@register("ping")
async def cmd_ping(command: Command):
    await command.respond("pong")