import discord
from discord import Message
import asyncio

import aiess
from aiess import Event
from aiess.logger import log

from settings import API_KEY
import receiver
import subscriber
from subscriptions import Subscription
from cmd_modules import *

subscriber.load()

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
    
    async def send_event(self, event: Event, subscription: Subscription):
        channel = self.get_channel(subscription.channel_id)
        await channel.send(str(event))

        asyncio.sleep(2)  # TODO: Figure out how to ratelimit discord messages.

class Reader(aiess.Reader):
    client: Client = None
    
    async def on_event(self, event: Event):
        log(event, postfix="bot")
        subscriber.forward(event, self.client)

reader = Reader("bot")

client = Client(reader)
client.run(API_KEY)