import discord
from discord import Message

import receiver
from settings import API_KEY

import aiess
from aiess import Event

class Reader(aiess.Reader):
    async def on_event(self, event: Event):
        pass

class Client(discord.Client):
    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")

    async def on_message(self, message: Message) -> None:
        await receiver.receive(message)

client = Client()
client.run(API_KEY)