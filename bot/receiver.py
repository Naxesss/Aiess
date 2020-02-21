from discord import Message

def receive(message: Message) -> None:
    print(f"({message.guild} > #{message.channel}) {message.author}: {message.content}")
