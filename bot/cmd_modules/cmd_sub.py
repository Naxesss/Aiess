import sys
sys.path.append('..')

from bot.commands import Command, register
from bot.subscriber import subscribe

@register("sub", required_args=["filter"])
async def cmd_sub(command: Command, _filter: str):
        return
    

    # TODO: Ensure our filter argument is actually a valid filter (e.g. doesn't throw on parenthesis inequality).
    # TODO: Improve feedback by ecapsulating our input and its expansion in an embed.

    subscribe(command.context.channel, _filter)
    await command.respond("✓ subbed")