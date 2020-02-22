import re as regex

from discord import Message

from commands import Command

def receive(message: Message) -> None:
    print(f"({message.guild} > #{message.channel}) {message.author}: {message.content}")

    command = parse_command(message.content)
    if command:
        receive_command(command)

def parse_command(content: str) -> Command:
    match = regex.search(r"^\+([A-Za-z]+) ?(.+)?", content)
    if match:
        name = match.group(1)
        args = match.group(2)

        if args: return Command(name, *args.split(" "))
        else:    return Command(name)
    
    return None

def receive_command(command: Command) -> None:
    pass