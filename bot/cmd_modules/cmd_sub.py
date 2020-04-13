from commands import Command, register
from subscriber import subscribe

@register("sub")
async def cmd_ping(command: Command):
    if len(command.args) == 0:
        await command.respond("✗ missing arg")
        return
    
    # We only take one argument, so let's combine all whitespace splits back together.
    combined_arg = " ".join(command.args)

    subscribe(command.context.channel, combined_arg)
    await command.respond("✓ subbed")