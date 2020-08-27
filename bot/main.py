import sys
sys.path.append('..')

import asyncio
from contextlib import suppress

import discord
from discord import Message, Game
from discord.errors import Forbidden

import aiess
from aiess import Event
from aiess import logger
from aiess.logger import log
from aiess.database import SCRAPER_DB_NAME

from bot.settings import API_KEY
from bot import receiver, subscriber, prefixes
from bot.objects import Subscription
from bot import database
from bot.formatter import format_link, format_embed
from bot.cmd_modules import *
from bot import activity
from bot import permissions

logger.init()
subscriber.load()
prefixes.load()
permissions.load()

class Client(discord.Client):
    def __init__(self, reader):
        super().__init__()
        self.reader = reader
        self.reader.client = self

    async def on_ready(self) -> None:
        log(f"Logged in as {self.user}!", postfix="bot")
        asyncio.create_task(activity.loop(self))

        if not self.reader.running:
            await self.reader.run()

    async def on_message(self, message: Message) -> None:
        await receiver.receive(message, client=self)
    
    async def send_event(self, event: Event, subscription: Subscription):
        channel = self.get_channel(subscription.channel_id)
        if not channel:
            # Ignore channels we no longer have access to (e.g. deleted / power outage).
            return

        with suppress(Forbidden):
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