import sys
sys.path.append('..')

import asyncio
from datetime import datetime, timedelta

from discord import Client, Activity, Game, Status

from aiess.logger import log_err
from aiess import Reader

from bot.formatter import format_time

async def loop(client: Client, reader: Reader) -> None:
    """Updates the client activity ("Playing" indicator), and status (Online indicator), every minute."""
    try:
        while True:
            await client.change_presence(
                activity = get_activity(client, reader),
                status   = get_status(client, reader)
            )
            # Presence updates are ratelimited at 1 update / 15s.
            await asyncio.sleep(60)
    except Exception as ex:
        log_err(f"WARNING | Discord presence raised \"{ex}\"")

def get_activity(client: Client, reader: Reader) -> Activity:
    """Returns the "Playing +help | x servers" indicator for the bot."""
    if not client.is_ready():
        return Game(f"/subscribe | Starting...")

    time_since_event = (datetime.utcnow() - reader.latest_event_time) if reader.latest_event_time else None
    guild_n = len(client.guilds)
    return Game(
        f"/subscribe" +
        f" | {guild_n} server" + ("s" if guild_n != 1 else "") +
        (f" | {format_time(time_since_event, max_units=1, long=True)} delay"
            if time_since_event and time_since_event > timedelta(minutes=30)
            else "")
    )

def get_status(client: Client, reader: Reader) -> Status:
    """Returs online / idle / do not disturb, depending on how long ago the last event batch was."""
    if not client.is_ready():
        return Status.do_not_disturb

    time_since_event = (datetime.utcnow() - reader.latest_event_time) if reader.latest_event_time else None
    if  (time_since_event is None or
         time_since_event > timedelta(hours=2)):   return Status.do_not_disturb
    elif time_since_event > timedelta(minutes=30): return Status.idle
    else:                                          return Status.online