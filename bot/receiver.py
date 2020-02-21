from discord import Message

def Receive(message: Message) -> None:
    print(f"Message from {message.author}: {message.content}")