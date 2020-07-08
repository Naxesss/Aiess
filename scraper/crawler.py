import sys
sys.path.append('..')

from datetime import datetime
from typing import Generator, Callable

from aiess.web import api
from aiess.objects import Event

from scraper.requester import get_discussion_events, get_reply_events, get_beatmapset_events
from scraper import populator

async def get_all_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of all events within the given time frame."""
    # Ensures name changes, beatmap updates, etc are considered.
    # Updates once for each pass (more than that isn't necessary considering time is locked).
    api.clear_response_cache()
    populator.cached_discussions_json = {}

    async for event in __get_discussion_events_between(start_time, end_time): yield event
    async for event in __get_reply_events_between(start_time, end_time):      yield event
    async for event in __get_beatmapset_events_between(start_time, end_time): yield event

async def __get_discussion_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of discussion events (from /beatmap-disussions) within the given time frame."""
    for event in __get_event_generations_between(get_discussion_events, start_time, end_time):
        yield event

async def __get_reply_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of discussion events (from /beatmap-disussions) within the given time frame."""
    for event in __get_event_generations_between(get_reply_events, start_time, end_time):
        await populator.populate_event(event)
        if not event.marked_for_deletion:
            yield event

async def __get_beatmapset_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of beatmapset events (from /events) within the given time frame.
    Should be run after discussion events so that discussion contexts are available."""
    for event in __get_event_generations_between(get_beatmapset_events, start_time, end_time):
        await populator.populate_event(event)
        if not event.marked_for_deletion:
            yield event

def __get_event_generations_between(
        generator_function: Callable[[int], Generator[Event, None, None]],
        start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns the same generator as the generation function argument, but within the given time
    frame and across multiple pages rather than just one."""
    current_time = start_time
    page = 1

    while current_time > end_time:
        event_generator = generator_function(page)
        
        for event in event_generator:
            if event.time > current_time:
                continue

            current_time = event.time
            if current_time <= end_time:
                # Since events are sorted, any remaining element time is also <= `end_time`.
                break
            
            yield event
        
        page += 1
        if page > 500:
            # Assuming 60 s / page, this would take 8 hours to hit, but that's within acceptable bounds for this purpose.
            raise ValueError("""
                The page index has exceeded 500, we're probably stuck in a loop.""")