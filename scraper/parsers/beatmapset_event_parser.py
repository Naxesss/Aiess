import sys
sys.path.append('..')

from typing import Generator
from bs4 import BeautifulSoup
from bs4.element import Tag
import json

from aiess.objects import Event, Beatmapset, Discussion, User
from aiess.errors import DeletedContextError
from aiess.logger import log_err
from aiess import timestamp
from aiess import event_types as types

from scraper.parsers.event_parser import EventParser

class BeatmapsetEventParser(EventParser):

    def parse(self, events: BeautifulSoup) -> Generator[Event, None, None]:
        """Returns a generator of BeatmapsetEvents, from the given /events BeautifulSoup response, parsed top-down."""
        json_events = events.find("script", {"id": "json-events"})
        json_users = events.find("script", {"id": "json-users"})

        if not json_events or not json_users:
            # In case the jsons for some reason fail to appear, we can always
            # parse the HTML tags instead.
            event_tags = events.findAll("div", {"class": "beatmapset-event"})
            if not event_tags:
                raise ValueError("Neither json nor HTML tags available for parsing beatmapset events.")

            for event_tag in event_tags:
                event = self.parse_event(event_tag)
                if event:
                    yield event
            return

        event_jsons = json.loads(json_events.string)
        user_jsons = json.loads(json_users.string)

        for event_json in event_jsons:
            event = self.parse_event_json(event_json, user_jsons)
            if event:
                yield event
    
    def parse_event(self, event: Tag) -> Event:
        """Returns a BeatmapsetEvent reflecting the given event html Tag object.
        Ignores any event with an incomplete context (e.g. deleted beatmaps)."""
        try:
            # Scrape object data
            _type = self.parse_event_type(event)
            time = self.parse_event_time(event)

            link = self.parse_event_link(event)
            beatmapset_id = self.parse_id_from_beatmapset_link(link)
            discussion_id = self.parse_id_from_discussion_link(link)

            user_id = self.parse_event_author_id(event)
            user_name = self.parse_event_author_name(event)

            # Reconstruct objects
            beatmapset = Beatmapset(beatmapset_id)
            user = User(user_id, user_name) if user_id is not None else None
            discussion = Discussion(discussion_id, beatmapset) if discussion_id is not None else None
        except DeletedContextError as err:
            log_err(err)
        else:
            return Event(
                _type = _type,
                time = time,
                beatmapset = beatmapset,
                discussion = discussion,
                user = user)
        
        return None
    
    def parse_event_json(self, event_json: object, user_jsons: object=None) -> Event:
        """Returns a BeatmapsetEvent reflecting the given event json object.
        Ignores any event with an incomplete context (e.g. deleted beatmaps).

        Requests user names from the api unless supplied with the corresponding user json from the discussion page."""
        if not event_json:
            # Seems to occur when the respective beatmapset has been deleted.
            log_err("WARNING | An event is missing; the beatmapset was probably deleted.")
            return None
        
        try:
            # Scrape object data
            _type = event_json["type"]
            time = timestamp.from_string(event_json["created_at"])

            if "beatmapset" not in event_json or not event_json["beatmapset"]:
                raise DeletedContextError("No beatmapset was found in this event. It was likely deleted.")

            beatmapset_id = event_json["beatmapset"]["id"]
            discussion_id = event_json["discussion"]["id"] if "discussion" in event_json and event_json["discussion"] else None

            user_id = event_json["user_id"] if "user_id" in event_json else None
            user_json = self.__lookup_user_json(user_id, user_jsons)
            user_name = user_json["username"] if user_json else None

            content = None
            if _type in [types.LANGUAGE_EDIT, types.GENRE_EDIT]:
                # Language/genre edits always have "old" and "new" fields, which no other type has.
                old = event_json["comment"]["old"]
                new = event_json["comment"]["new"]
                content = f"{old} -> {new}"
            
            if _type in [types.UNLOVE]:
                # E.g. "Mapper has asked for it to be removed from Loved".
                content = event_json["comment"]["reason"]

            # Reconstruct objects
            beatmapset = Beatmapset(beatmapset_id)
            user = User(user_id, user_name) if user_id is not None else None
            discussion = Discussion(discussion_id, beatmapset) if discussion_id is not None else None
        except DeletedContextError as err:
            log_err(err)
        else:
            return Event(
                _type = _type,
                time = time,
                beatmapset = beatmapset,
                discussion = discussion,
                user = user,
                content = content)
        
        return None
    
    def __lookup_user_json(self, user_id: str, user_jsons: object):
        if not user_jsons:
            return None

        for user_json in user_jsons:
            if user_json["id"] == user_id:
                return user_json
        
        return None

    def parse_event_type(self, event: Tag) -> str:
        """Returns the type of the given event (e.g. nominate", "issue_resolve", "disqualify")."""
        return super().parse_event_type(
            event,
            event_class="beatmapset-event__icon",
            class_prefix="beatmapset-event__icon--"
        )
    
    def parse_event_author_id(self, event: Tag) -> str:
        """Returns the user id associated with the given event, if applicable (e.g. the user nominating, "1314547")."""
        return super().parse_event_author_id(event, href_class="user-name")
    
    def parse_event_author_name(self, event: Tag) -> str:
        """Returns the user name associated the given event, if applicable (e.g. the user nominating, 5129592)."""
        return super().parse_event_author_name(event, name_class="user-name")

# Only need one instance since it's always the same.
beatmapset_event_parser = BeatmapsetEventParser()