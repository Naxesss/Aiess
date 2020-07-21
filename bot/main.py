import sys
sys.path.append('..')

import discord
from discord import Message, Game

import aiess
from aiess import Event
from aiess.logger import log
from aiess.database import SCRAPER_DB_NAME

from bot.settings import API_KEY
from bot import receiver, subscriber, prefixes
from bot.objects import Subscription
from bot import database
from bot.formatter import format_link, format_embed
from bot.cmd_modules import *
from bot.prefixes import DEFAULT_PREFIX

subscriber.load()
prefixes.load()

class Client(discord.Client):
    def __init__(self, reader):
        super().__init__()
        self.reader = reader
        self.reader.client = self

    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")
        await self.change_presence(activity=Game(f"{DEFAULT_PREFIX}help"))

        if not self.reader.running:
            await self.reader.run()

    async def on_message(self, message: Message) -> None:
        await receiver.receive(message, client=self)
    
    async def send_event(self, event: Event, subscription: Subscription):
        channel = self.get_channel(subscription.channel_id)

        await channel.send(content=format_link(event), embed=await format_embed(event))

class Reader(aiess.Reader):
    client: Client = None
    
    async def on_events(self, events):
        # This is called before any on_event for each batch.
        database.clear_cache(SCRAPER_DB_NAME)

    async def on_event(self, event: Event):
        log(event, postfix=self.reader_id)
        await subscriber.forward(event, self.client)

reader = Reader("bot", db_name=SCRAPER_DB_NAME)

client = Client(reader)
client.run(API_KEY)