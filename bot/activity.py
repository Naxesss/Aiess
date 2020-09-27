import sys
sys.path.append('..')

import asyncio

from discord import Client, Activity, Game

from aiess.logger import log_err

from bot.prefixes import DEFAULT_PREFIX

async def loop(client: Client) -> None:
    """Updates the client activity ("Playing" indicator) every minute."""
    try:
        while True:
            await client.change_presence(activity=get_activity(client))
            # Presence updates are ratelimited at 1 update / 15s.
            await asyncio.sleep(60)
    except Exception as ex:
        log_err(f"WARNING | Discord presence raised \"{ex}\"")

def get_activity(client: Client) -> Activity:
    """Returns the "Playing +help | x servers" indicator for the bot."""
    guild_n = len(client.guilds)
    return Game(
        f"{DEFAULT_PREFIX}help | " +
        f"{guild_n} server" + ("s" if guild_n != 1 else "")
    )