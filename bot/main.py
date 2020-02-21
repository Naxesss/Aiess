import discord
from discord import Message

import receiver
from settings import API_KEY

class Client(discord.Client):
    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")

    async def on_message(self, message: Message) -> None:
        receiver.receive(message)

client = Client()
client.run(API_KEY)