import sys
sys.path.append('..')

import os

import discord
from discord import Status

from aiess import logger

from bot import subscriber
from bot.settings import API_KEY

logger.init()
subscriber.load()

bot = discord.Bot(status=Status.do_not_disturb)

for filename in os.listdir("./bot/cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'bot.cogs.{filename[:-3]}')

bot.run(API_KEY)