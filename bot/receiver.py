import sys
sys.path.append('..')

import re as regex

from discord import Message, Client
from typing import List

from bot.commands import Command
from bot.commands import registered_commands, registered_aliases
from bot.prefixes import get_prefix
from bot import permissions
from bot.filterer import unescape
from bot.logic import split_unescaped
from bot.cmdcommon import permissions_embed

async def receive(message: Message, client: Client) -> None:
    """Handles logic ran upon receiving a discord message (e.g. printing and parsing potential commands)."""
    if message.author and message.author.id == client.user.id:
        print_message(message)

    if not message.author or message.author.bot:
        # Ignore messages from bots, prevents weird loopholes like
        # changing permissions through making another bot invoke commands.
        return

    command = parse_command(message.content, context=message, client=client)
    if command:
        print_message(message)
        await receive_command(command)

def print_message(message: Message) -> None:
    """Prints the given message."""
    print(f"({message.guild} > #{message.channel}) {message.author}: {message.content}")

def parse_command(content: str, context: Message=None, client: Client=None) -> Command:
    """Returns the given content string as a command, if it's formatted as one, else None.
    Optionally with the given message as context."""
    match = regex.search(r"^" + regex.escape(get_prefix(context)) + r"([A-Za-z]+) ?(.+)?", content)
    if match:
        name = match.group(1)
        args = match.group(2)

        if args:
            args_respecting_quotes = [unescape(arg) for arg, _ in split_unescaped(args, (" ",))]
            return Command(name, *args_respecting_quotes, context=context, client=client)
        return Command(name, context=context, client=client)
    return None

async def receive_command(command: Command) -> bool:
    """Returns whether the received command was recognized and executed."""
    if command.name not in registered_aliases:
        return False
    
    name = registered_aliases[command.name]
    func_wrapper = registered_commands[name]
    
    # Let the user know the command was recognized, and that a response should follow.
    await command.trigger_typing()

    if not permissions.can_execute(command):
        await command.respond(
            response = f"✗ Lacking permission.",
            embed = permissions_embed(
                # Can only lack permission in a guild.
                guild_id         = command.guild_id(),
                command_wrappers = [func_wrapper]
            )
        )
        return False

    if len(func_wrapper.required_args) > len(command.args):
        missing_args = func_wrapper.required_args[len(command.args):]
        missing_arg_str = "`<" + "`>, <`".join(missing_args) + ">`"
        await command.respond_err(f"Missing required argument(s) {missing_arg_str}.")
        return False

    parsed_args = parse_args(command.args, arg_count=len(func_wrapper.required_args) + len(func_wrapper.optional_args))
    await func_wrapper.execute(command, *parsed_args)

    return True

def parse_args(args: List[str], arg_count: int) -> List[str]:
    """Returns an argument list with a length of the given count or less. If the amount of arguments
    are greater than the count, the last returned argument is a combination of the remaining ones.
    
    E.g. `+tell <user> <text>` with "+tell someone hello there" gives <text> = "hello there"."""
    if not arg_count:
        # Takes no args, so ignore any given.
        return []

    parsed_args = []
    for index, arg in enumerate(args):
        if index >= arg_count:
            parsed_args[-1] += " " + arg
        else:
            parsed_args.append(arg)
    return parsed_args