import sys
sys.path.append('..')

import asyncio

from discord import Client, Activity, Game

from bot.prefixes import DEFAULT_PREFIX

async def loop(client: Client) -> None:
    while True:
        await client.change_presence(activity=get_activity(client))
        # Presence updates are ratelimited at 1 update / 15s.
        await asyncio.sleep(15)

def get_activity(client: Client) -> Activity:
    guild_n = len(client.guilds)
    return Game(
        f"{DEFAULT_PREFIX}help | " +
        f"{guild_n} server" + ("s" if guild_n != 1 else "")
    )