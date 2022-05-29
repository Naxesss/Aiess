import sys
sys.path.append('..')

import os

import discord
from discord import Status

from aiess import logger

from bot import subscriber
from bot import prefixes
from bot import permissions
from bot.settings import API_KEY

logger.init()
subscriber.load()
prefixes.load()
permissions.load()

bot = discord.Bot(status=Status.do_not_disturb)

for filename in os.listdir("./bot/cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'bot.cogs.{filename[:-3]}')

bot.run(API_KEY)