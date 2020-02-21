from discord import Message

def receive(message: Message) -> None:
    print(f"Message from {message.author}: {message.content}")