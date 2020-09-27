import sys
sys.path.append('..')

import asyncio
from datetime import datetime, timedelta

from discord import Client, Activity, Game, Status

from aiess.logger import log_err
from aiess import Reader

from bot.prefixes import DEFAULT_PREFIX

async def loop(client: Client, reader: Reader) -> None:
    """Updates the client activity ("Playing" indicator), and status (Online indicator), every minute."""
    try:
        while True:
            await client.change_presence(
                activity = get_activity(client),
                status   = get_status(reader)
            )
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

def get_status(reader: Reader) -> Status:
    """Returs online / idle / do not disturb, depending on how long ago the last event batch was."""
    time_since_heartbeat = datetime.utcnow() - reader.last_heartbeat
    if   time_since_heartbeat > timedelta(hours=1):    return Status.do_not_disturb
    elif time_since_heartbeat > timedelta(minutes=30): return Status.idle
    else:                                              return Status.online