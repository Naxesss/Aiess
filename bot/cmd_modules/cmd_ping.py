import sys
sys.path.append('..')

from bot.formatter import TimeUnit
from bot.formatter import format_time
from bot.commands import Command, register
from bot.commands import GENERAL_CATEGORY

@register(
    category    = GENERAL_CATEGORY,
    names       = ["ping"],
    description = "Returns the bot latency (e.g. \"134 ms\")."
)
async def cmd_ping(command: Command):
    await command.respond(
        format_time(
            delta_time=command.client.latency,  # `client.latency` is a second representation.
            min_unit=TimeUnit.MILLISECONDS
        )
    )