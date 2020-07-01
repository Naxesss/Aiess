import sys
sys.path.append('..')

import asyncio
from datetime import datetime
from time import sleep

from aiess import timestamp, logger
from aiess import Event
from aiess.logger import log, colors, fmt
from aiess.database import Database, SCRAPER_DB_NAME
from aiess.reader import merge_concurrent

from scraper.crawler import get_all_events_between

init_time_str = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

async def gather_loop() -> None:
    """Gathers new events every 60 seconds."""
    while(True):
        await gather_new_events()
        await asyncio.sleep(60)

async def gather_new_events() -> None:
    """Iterates over new events since the last time, inserts them into the database, and then updates the last time."""
    current_time = datetime.utcnow().replace(microsecond=0)
    last_time = timestamp.get_last("events").replace(microsecond=0)

    await push_events(get_all_events_between, current_time, last_time)

    last_updated(current_time)

async def push_events(async_event_generator, current_time, last_time) -> None:
    """Parses and inserts events generated by the given function over the timeframe."""
    events = []
    await parse_events(events, async_event_generator, current_time, last_time)
    insert_db(merge_concurrent(events))

async def parse_events(event_list, async_event_generator, current_time, last_time) -> None:
    """Parses events generated by the given function over the timeframe and appends them to the event list."""
    log(f"--- Parsing Events from {last_time} to {current_time} ---")
    async for event in async_event_generator(current_time, last_time):
        progress_ratio = (current_time - event.time).total_seconds() / (current_time - last_time).total_seconds()
        progress_str = (
            fmt(" " * int(progress_ratio       * 20), colors.LOADING_FILLED) +
            fmt(" " * int((1 - progress_ratio) * 20), colors.LOADING_EMPTY )
        )
        
        log(f"{progress_str} | {format_event_log(event)}")
        event_list.append(event)

def format_event_log(event: Event) -> str:
    return "".join([
        f"{fmt(event.type, colors.EVENT)}",
        f" ({fmt(event.user, colors.AUTHOR)})" if event.user else "",
        f" on {fmt(event.beatmapset, colors.CONTEXT)}" if event.beatmapset else "",
        f" to/from {fmt(event.group, colors.CONTEXT)}" if event.group else "",
        f" \"{event.content}\"" if event.content else ""
    ])

def insert_db(events) -> None:
    """Inserts the given event list into the database in reversed order."""
    if not events:
        return
    
    events.sort(key=lambda event: event.time)

    log(f"--- Inserting {len(events)} Events into the Database ---")
    for event in events:
        log(".", newline=False)
        database.insert_event(event)
    log()

def last_updated(current_time) -> None:
    """Updates the last updated file to reflect the given time."""
    log(f"--- Last Updated {current_time} ---")
    timestamp.set_last(current_time, "events")

logger.init(init_time_str)
database = Database(SCRAPER_DB_NAME)

loop = asyncio.get_event_loop()
loop.run_until_complete(gather_loop())