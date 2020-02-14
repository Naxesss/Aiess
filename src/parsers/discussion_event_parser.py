from bs4 import BeautifulSoup
from typing import Generator
from bs4.element import Tag

from objects import Event, Beatmapset, User, Discussion
from parsers.event_parser import EventParser
from exceptions import DeletedContextError
from storage.logger import log_err

class DiscussionEventParser(EventParser):

    def parse(self, events: BeautifulSoup) -> Generator[Event, None, None]:
        """Returns a generator of BeatmapsetEvents, from the given /beatmapset-discussions BeautifulSoup response, parsed top-down."""
        for event in events.findAll("div", {"class": "beatmapset-activities__discussion-post"}):
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

            content = self.parse_discussion_message(event)

            # Reconstruct objects
            beatmapset = Beatmapset(beatmapset_id)
            user = User(user_id, user_name) if user_id != None else None
            discussion = Discussion(discussion_id, beatmapset, user, content) if discussion_id != None else None
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
    
    def parse_event_type(self, event: Tag) -> str:
        """Returns the type of the given event (e.g. "suggestion", "problem", "hype")."""
        return super().parse_event_type(event,
            event_class="beatmap-discussion-message-type",
            class_prefix="beatmap-discussion-message-type--")
    
    def parse_event_author_id(self, event: Tag) -> str:
        """Returns the user id associated with the given event, if applicable (e.g. the user starting a discussion, "1314547")."""
        return super().parse_event_author_id(event,
            href_class="beatmap-discussion-user-card__user-link",
            must_find=True)
    
    def parse_event_author_name(self, event: Tag) -> str:
        """Returns the user name associated the given event, if applicable (e.g. the user starting a discussion, 5129592)."""
        return super().parse_event_author_name(event,
            name_class="beatmap-discussion-user-card__user-text",
            must_find=True)

    def parse_discussion_message(self, event: Tag) -> str:
        """Parses the raw message content of a discussion post."""
        message_class = "beatmap-discussion-post__message"
        return event.find("div", {"class": message_class}).contents[0]

# Only need one instance since it's always the same.
discussion_event_parser = DiscussionEventParser()