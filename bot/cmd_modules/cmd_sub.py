from commands import Command, register
from subscriber import subscribe

@register("sub")
async def cmd_ping(command: Command):
    if len(command.args) == 0:
        await command.respond("✗ missing arg")
        return
    
    # We only take one argument, so let's combine all whitespace splits back together.
    # TODO: Make this implicit by registering the argument amount, after which whitespace no longer splits.
    combined_arg = " ".join(command.args)

    # TODO: Ensure our filter argument is actually a valid filter (e.g. doesn't throw on parenthesis inequality).
    # TODO: Improve feedback by ecapsulating our input and its expansion in an embed.

    subscribe(command.context.channel, combined_arg)
    await command.respond("✓ subbed")