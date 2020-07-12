import sys
sys.path.append('..')

from bot.formatter import TimeUnit
from bot.formatter import format_time
from bot.commands import Command, register, COMMAND_PREFIX
from bot.commands import help_embed, general_help_embed

@register(
    name          = "help",
    optional_args = ["command"],
    description   = "Returns a list of commands, optionally the usage of `[command]`."
)
async def cmd_help(command: Command, name: str=None):
    if name:
        embed = help_embed(name)
        content = f"Type `{COMMAND_PREFIX}help` for a list of commands."
    else:
        embed = general_help_embed()
        content = f"Type `{COMMAND_PREFIX}help <command>` for usage."

    await command.respond(content, embed=embed)