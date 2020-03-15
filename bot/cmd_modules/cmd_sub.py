from commands import Command, register
from subscriber import subscribe

@register("sub")
async def cmd_ping(command: Command):
    if len(command.args) == 0:
        await command.respond("✗ missing arg")
        return

    subscribe(command.context.channel, command.args[0])
    await command.respond("✓ subbed")