import sys
sys.path.append('..')

import re as regex

from discord import Message
from typing import List

from bot.commands import Command, FunctionWrapper
from bot.commands import registered_commands

async def receive(message: Message) -> None:
    """Handles logic ran upon receiving a discord message (e.g. printing and parsing potential commands)."""
    print(f"({message.guild} > #{message.channel}) {message.author}: {message.content}")

    command = parse_command(message.content, message)
    if command:
        await receive_command(command)

def parse_command(content: str, context: Message=None) -> Command:
    """Returns the given content string as a command, optionally with the given message as context."""
    match = regex.search(r"^\+([A-Za-z]+) ?(.+)?", content)
    if match:
        name = match.group(1)
        args = match.group(2)

        if args:
            return Command(name, *args.split(" "), context=context)
        return Command(name, context=context)
    return None

async def receive_command(command: Command) -> bool:
    """Returns whether the received command was recognized and executed."""
    if command.name not in registered_commands:
        return False
    
    func_wrapper = registered_commands[command.name]
    
    if len(func_wrapper.required_args) > len(command.args):
        missing_args = func_wrapper.required_args[len(command.args):]
        missing_arg_str = "`<" + "`>, <`".join(missing_args) + ">`"
        await command.respond(f"✗ Missing required argument(s) {missing_arg_str}.")
        return False

    parsed_args = parse_args(command.args, arg_count=len(func_wrapper.required_args) + len(func_wrapper.optional_args))

    await func_wrapper.execute(command, *parsed_args)
    return True

def parse_args(args: List[str], arg_count: int) -> List[str]:
    """Returns an argument list with a length of the given count or less. If the amount of arguments
    are greater than the count, the last returned argument is a combination of the remaining ones.
    
    E.g. `+tell <user> <text>` with "+tell someone hello there" gives <text> = "hello there"."""
    parsed_args = []
    for index, arg in enumerate(args):
        if index > arg_count:
            parsed_args[-1] += " " + arg
        else:
            parsed_args.append(arg)
    return parsed_args