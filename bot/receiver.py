import re as regex

from discord import Message

from commands import Command, registered_commands

async def receive(message: Message) -> None:
    """Handles logic ran upon receiving a discord message (e.g. printing and parsing potential commands)."""
    print(f"({message.guild} > #{message.channel}) {message.author}: {message.content}")

    command = await parse_command(message.content, message)
    if command:
        await receive_command(command)

async def parse_command(content: str, context: Message=None) -> Command:
    """Returns the given content string as a command, optionally with the given message as context."""
    match = regex.search(r"^\+([A-Za-z]+) ?(.+)?", content)
    if match:
        name = match.group(1)
        args = match.group(2)

        if args: return Command(name, *args.split(" "), context=context)
        else:    return Command(name, context=context)
    
    return None

async def receive_command(command: Command) -> bool:
    """Returns whether the received command was recognized and executed."""
    if command.name in registered_commands:
        await registered_commands[command.name](command)
        return True
    return False