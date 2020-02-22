import re as regex

from discord import Message

from commands import Command

def receive(message: Message) -> None:
    print(f"({message.guild} > #{message.channel}) {message.author}: {message.content}")

    command = parse_command(message.content, message)
    if command:
        receive_command(command)

def parse_command(content: str, context: Message=None) -> Command:
    match = regex.search(r"^\+([A-Za-z]+) ?(.+)?", content)
    if match:
        name = match.group(1)
        args = match.group(2)

        if args: return Command(name, *args.split(" "), context=context)
        else:    return Command(name, context=context)
    
    return None

def receive_command(command: Command) -> None:
    pass