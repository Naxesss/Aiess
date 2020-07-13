import sys
sys.path.append('..')

from bot.commands import Command, register, COMMAND_PREFIX
from bot.commands import help_embed, general_help_embed

@register(
    name          = "help",
    optional_args = ["command"],
    description   = "Returns a list of commands, or optionally the usage of `[command]`.",
    example_args  = [None, "help"]
)
async def cmd_help(command: Command, name: str=None):
    if name:
        # Clean up the argument so that `+help +ping` works, as the user would expect.
        name = name.replace("+", "")

        embed = help_embed(name)
        content = f"Type `{COMMAND_PREFIX}help` for a list of commands."
    else:
        embed = general_help_embed()
        content = f"Type `{COMMAND_PREFIX}help <command>` for usage."

    if not embed:
        await command.respond_err(f"No command `{name}` exists.")
        return
    
    await command.respond(content, embed=embed)