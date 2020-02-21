from discord import Message

def receive(message: Message) -> None:
    print(f"({message.guild} > #{message.channel}) {message.author}: {message.content}")
    if qualifies_as_command(message):
        receive_command(message)

def qualifies_as_command(message: Message) -> None:
    pass

def receive_command(command: str) -> None:
    pass