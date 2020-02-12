from bs4 import BeautifulSoup
from datetime import datetime
from typing import Generator, Callable, List

from web.scraper import get_beatmapset_events, get_discussion_events
from web.scraper import request_discussions_json, get_map_page_discussions, get_map_page_event_jsons
from web import api
from storage import event_time
from objects import Event, Discussion
from storage.database import database
from parsers import time_parser
from parsers.discussion_parser import discussion_parser

cached_discussions_json = {}

def get_all_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of all events within the given time frame."""
    # Ensures name changes, beatmap updates, etc are considered.
    api.clear_response_cache()

    for event in __get_discussion_events_between(start_time, end_time): yield event
    for event in __get_beatmapset_events_between(start_time, end_time): yield event

def __get_discussion_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of discussion events (from /beatmap-disussions) within the given time frame."""
    for event in __get_event_generations_between(get_discussion_events, start_time, end_time):
        yield event

def __get_beatmapset_events_between(start_time: datetime, end_time: datetime) -> Generator[Event, None, None]:
    """Returns a generator of beatmapset events (from /events) within the given time frame.
    Should be run after discussion events so that discussion contexts are available."""
    global cached_discussions_json
    cached_discussions_json = {}  # Update once for each pass (more than that isn't necessary considering time is locked).

    for event in __get_event_generations_between(get_beatmapset_events, start_time, end_time):
        populate_event(event)
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
        noEntriesTries = 0
        if not had_value:
            noEntriesTries += 1
            if noEntriesTries >= 3:
                raise ValueError("""
                    No events were returned from the generator. Are we parsing the events properly? Are we looking too far back in time?""")
        else:
            page += 1

def populate_event(event: Event) -> None:
    """Populates the given event using the beatmapset discussion json
    (e.g. missing discussion info and additional details like who did votes)."""
    discussions_json = None
    if event.beatmapset.id not in cached_discussions_json:
        discussions_json = request_discussions_json(event.beatmapset)
        cached_discussions_json[event.beatmapset.id] = discussions_json
    else:
        discussions_json = cached_discussions_json[event.beatmapset.id]

    if discussions_json == None:
        raise ValueError("Could not get a discussion")

    __populate_missing_discussion_info(event, discussions_json)
    __populate_additional_details(event, discussions_json)

def __populate_missing_discussion_info(event: Event, discussions_json: object) -> None:
    """Populates missing discussion information in the given event from the beatmapset discussion json (e.g. user, content)."""
    if not event.discussion:
        return  # Event doesn't care about discussions.
    
    # Some events rely on prior discussions, so we need to make sure these are accessible by caching them.
    # Eventually all discussions should be tracked, but in the beginning this part is necessary.
    if event.discussion.user == None or event.discussion.content == None:
        for discussion in get_map_page_discussions(event.beatmapset, discussions_json):
            if discussion.id == event.discussion.id:
                event.discussion = discussion

def __populate_additional_details(event: Event, discussions_json: object) -> None:
    """Populates additional details in the given event from the beatmapset discussion json (e.g. who voted)."""
    if event.discussion and (not event.discussion.user or not event.discussion.content):
        if not __complete_discussion_context(event):
            # After being deleted, many properties of discussions are inaccessible without referring to cached information.
            # Without cached information, we skip the event, since this its context is no longer visible to the public anyway.
            event.marked_for_deletion = True
            return

    beatmapset_json = discussions_json["beatmapset"]
    for page_event in get_map_page_event_jsons(event, discussions_json):
        # Likelihood that two same type of events happen in the same second is very unlikely,
        # so this'll work as identification (we have no access to actual event ids on scraping side, so can't use that).
        same_time = event.time == time_parser.from_ISO_8601_to_datetime(page_event["created_at"])
        same_type = event.type == page_event["type"].replace("_", "-")
        if same_time and same_type:
            if event.type == "disqualify" or event.type == "nomination_reset":  # Content is discussion content.
                event.content = event.discussion.content

            if event.type == "issue-resolve":  # User is resolver, not discussion creator.
                post_author = discussion_parser.parse_discussion_post_author(
                    page_event["comment"]["beatmap_discussion_post_id"],
                    beatmapset_json)
                if post_author != None:
                    event.user = post_author
            
            if event.type == "kudosu-gain":  # User is giver, not discussion creator.
                kudosu_giver = discussion_parser.parse_user(
                    page_event["comment"]["new_vote"]["user_id"],
                    beatmapset_json)
                if kudosu_giver != None:
                    event.user = kudosu_giver
            
            if event.type == "kudosu-lost":  # User is remover, not discussion creator.
                kudosu_remover = discussion_parser.parse_user(
                    page_event["comment"]["new_vote"]["user_id"],
                    beatmapset_json)
                if kudosu_remover != None:
                    event.user = kudosu_remover
            
            if event.type == "issue-reopen":  # User is reopener, not discussion creator.
                issue_reopener = discussion_parser.parse_discussion_post_author(
                    page_event["comment"]["beatmap_discussion_post_id"],
                    beatmapset_json)
                if issue_reopener != None:
                    event.user = issue_reopener
            
            if event.type == "discussion-delete":  # User is discussion creator (which we would normally not have access to).
                event.user = event.discussion.user
            
            if event.type == "discussion_post_delete":  # User is discussion post creator, to which we would no longer have access.
                event.marked_for_deletion = True  # TODO: Not yet supported.

def __complete_discussion_context(event: Event) -> bool:
    """Completes the context of the discussion from prior database entries, if present. Returns true if succeeded."""
    cached_discussion = database.retrieve_discussion(dict(id=event.discussion.id))
    if not cached_discussion:
        return False
    
    if cached_discussion.user == None or cached_discussion.content == None:
        raise ValueError("""
            Retrieved an incomplete discussion instance. This should not be possible when
            preventing input of incomplete instances.""")

    event.discussion = cached_discussion
    return True