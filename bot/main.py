import discord
from discord import Message

import aiess
from aiess import Event

import receiver
from settings import API_KEY

class Reader(aiess.Reader):
    async def on_event(self, event: Event):
        pass

reader = Reader("bot")

class Client(discord.Client):
    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")

        global reader
        if not reader.running:
            await reader.run()

    async def on_message(self, message: Message) -> None:
        await receiver.receive(message)

client = Client()
client.run(API_KEY)