import discord
from discord import Message

import aiess
from aiess import Event
from aiess.logger import log

from settings import API_KEY
import receiver
from subscriptions import Subscription
from cmd_modules import _all


class Client(discord.Client):
    def __init__(self, reader):
        super().__init__()
        self.reader = reader
        self.reader.client = self

    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")

        if not self.reader.running:
            await self.reader.run()

    async def on_message(self, message: Message) -> None:
        await receiver.receive(message)

class Reader(aiess.Reader):
    client: Client = None
    
    async def on_event(self, event: Event):
        log(event, postfix="bot")

reader = Reader("bot")

client = Client(reader)
client.run(API_KEY)