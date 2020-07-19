import sys
sys.path.append('..')

from bot.commands import Command, register
from bot.commands import help_embed, general_help_embed
from bot.commands import GENERAL_CATEGORY

@register(
    category      = GENERAL_CATEGORY,
    names         = ["help", "commands"],
    optional_args = ["command"],
    description   = "Returns a list of commands, or optionally the usage of `[command]`.",
    example_args  = [None, "help"]
)
async def cmd_help(command: Command, name: str=None):
    if name:
        # Clean up the argument so that `+help +ping` works, as the user would expect.
        name = name.replace("+", "")

        embed = help_embed(name, prefix=command.prefix())
        content = f"Type `{command.prefix()}help` for a list of commands."
    else:
        embed = general_help_embed(prefix=command.prefix())
        content = f"Type `{command.prefix()}help <command>` for usage."

    if not embed:
        await command.respond_err(f"No command `{name}` exists.")
        return
    
    await command.respond(content, embed=embed)