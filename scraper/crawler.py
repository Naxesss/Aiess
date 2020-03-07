from bs4 import BeautifulSoup
from datetime import datetime
from typing import Generator, Callable, List

from aiess.web import api
from aiess.objects import Event, Discussion
from aiess.database import database

from scraper import get_discussion_events, get_reply_events, get_beatmapset_events
from scraper import request_discussions_json, get_map_page_discussions, get_map_page_event_jsons
import populator
from parsers.discussion_parser import discussion_parser

def get_all_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of all events within the given time frame."""
    # Ensures name changes, beatmap updates, etc are considered.
    # Updates once for each pass (more than that isn't necessary considering time is locked).
    api.clear_response_cache()
    populator.cached_discussions_json = {}

    for event in __get_discussion_events_between(start_time, end_time): yield event
    for event in __get_reply_events_between(start_time, end_time): yield event
    for event in __get_beatmapset_events_between(start_time, end_time): yield event

def __get_discussion_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of discussion events (from /beatmap-disussions) within the given time frame."""
    for event in __get_event_generations_between(get_discussion_events, start_time, end_time):
        yield event

def __get_reply_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of discussion events (from /beatmap-disussions) within the given time frame."""
    for event in __get_event_generations_between(get_reply_events, start_time, end_time):
        populator.populate_event(event)
        if not event.marked_for_deletion:
            yield event

def __get_beatmapset_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of beatmapset events (from /events) within the given time frame.
    Should be run after discussion events so that discussion contexts are available."""
    for event in __get_event_generations_between(get_beatmapset_events, start_time, end_time):
        populator.populate_event(event)
        if not event.marked_for_deletion:
            yield event

def __get_event_generations_between(
    generator_function: Callable[[int], Generator[Event, None, None]],
    start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns the same generator as the generation function argument, but within the given time
    frame and across multiple pages rather than just one."""
    current_time = start_time
    page = 1
    noEntriesTries = 0

    while current_time > end_time:
        event_generator = generator_function(page)
        had_value = False
        
        for event in event_generator:
            had_value = True

            # Skip any event earlier than our current time, as we'll either handle them during the next pass,
            # or have already done so in the current (e.g. new event pushed old event into next page as we were reading the first).
            if current_time >= event.time:
                current_time = event.time

                # Once we reach an event later than our end time, we stop knowing any further events will also be later.
                if current_time <= end_time:
                    break
                
                yield event
        
        # In case the generator for some reason is empty (e.g. site changed routes, class names, or end time is later than events
        # were logged for).
        if not had_value:
            noEntriesTries += 1
            if noEntriesTries >= 3:
                raise ValueError("""
                    No events were returned from the generator. Are we parsing the events properly? Are we looking too far back in time?""")
        else:
            page += 1