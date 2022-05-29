import asyncio

import discord
from discord.ext import commands

import aiess
from aiess import Event
from aiess import logger
from aiess.database import SCRAPER_DB_NAME

from bot import activity
from bot import database
from bot import subscriber

class Reader(aiess.Reader):
    def __init__(self, reader_id: str, db_name: str, bot: discord.Bot):
        super().__init__(reader_id, db_name)
        self.bot = bot
    
    async def on_events(self, _):
        # This is called before any on_event for each batch.
        database.clear_cache(SCRAPER_DB_NAME)

    async def on_event(self, event: Event):
        logger.log(event, postfix=self.reader_id)
        await subscriber.forward(event, self.bot)

class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reader = Reader("bot", db_name=SCRAPER_DB_NAME, bot=bot)

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        logger.log(f"Connected as {self.bot.user}!", postfix="bot")
        asyncio.create_task(activity.loop(self.bot, self.reader))

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        logger.log("Ready!", postfix="bot")

        if not self.reader.running:
            await self.reader.run()

def setup(bot):
    bot.add_cog(Ready(bot))