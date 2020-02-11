from bs4 import BeautifulSoup
from typing import Generator
from bs4.element import Tag

from objects import Event, Beatmapset, Discussion, User
from parsers.event_parser import EventParser
from parsers.discussion_parser import discussion_parser
from parsers.exceptions import DeletedContextError
from storage.database import database
from storage.logger import log_err

class BeatmapsetEventParser(EventParser):

    def parse(self, events: BeautifulSoup) -> Generator[Event, None, None]:
        """Returns a generator of BeatmapsetEvents, from the given /events BeautifulSoup response, parsed top-down."""
        for event in events.findAll("div", {"class": "beatmapset-event"}):
            parsed_event = self.parse_event(event)
            if parsed_event:
                yield parsed_event
    
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
            user = User(user_id, user_name) if user_id != None else None
            discussion = Discussion(discussion_id, beatmapset) if discussion_id != None else None
        except DeletedContextError as err:
            log_err(err)
        else:
            return Event(
                _type = _type,
                time = time,
                beatmapset = beatmapset,
                discussion = discussion,
                user = user)
    
    def parse_event_type(self, event: Tag) -> str:
        """Returns the type of the given event (e.g. nominate", "issue-resolve", "disqualify")."""
        return super().parse_event_type(event,
            event_class="beatmapset-event__icon",
            class_prefix="beatmapset-event__icon--")
    
    def parse_event_author_id(self, event: Tag) -> str:
        """Returns the user id associated with the given event, if applicable (e.g. the user nominating, "1314547")."""
        return super().parse_event_author_id(event,
            href_class="user-name")
    
    def parse_event_author_name(self, event: Tag) -> str:
        """Returns the user name associated the given event, if applicable (e.g. the user nominating, 5129592)."""
        return super().parse_event_author_name(event,
            name_class="user-name")

# Only need one instance since it's always the same.
beatmapset_event_parser = BeatmapsetEventParser()