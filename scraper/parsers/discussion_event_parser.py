import sys
sys.path.append('..')

from bs4 import BeautifulSoup
from typing import Generator
from bs4.element import Tag
import json

from aiess.objects import Event, Beatmapset, User, Discussion
from aiess.errors import ParsingError, DeletedContextError
from aiess import timestamp
from aiess.logger import log_err
from aiess import event_types as types

from scraper.parsers.event_parser import EventParser

class DiscussionEventParser(EventParser):

    def parse(self, discussion_jsons: object, user_jsons: object=None, discussion_jsons_for_replies: object=None) -> Generator[Event, None, None]:
        """Returns a generator of BeatmapsetEvents, from the given disussions and user jsons."""
        for discussion_json in discussion_jsons:
            event = self.parse_event_json(discussion_json, user_jsons, discussion_jsons_for_replies)
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

            content = self.parse_discussion_message(event)

            # Reconstruct objects
            beatmapset = Beatmapset(beatmapset_id)
            user = User(user_id, user_name) if user_id is not None else None
            if _type == "reply":
                # Replies should look up the discussion they are posted on.
                discussion = Discussion(discussion_id, beatmapset) if discussion_id is not None else None
            else:
                tab = self.parse_discussion_tab(event)
                difficulty = self.parse_discussion_diff(event)

                discussion = Discussion(discussion_id, beatmapset, user, content, tab, difficulty) if discussion_id is not None else None
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
    
    def parse_event_json(self, event_json: object, user_jsons: object=None, discussion_jsons_for_replies: object=None) -> Event:
        """Returns a BeatmapsetEvent reflecting the given event json object.
        Ignores any event with an incomplete context (e.g. deleted beatmaps).

        Requests user names from the api unless supplied with the corresponding user json from the discussion page."""
        if not event_json:
            # Seems to occur when the respective beatmapset has been deleted. However, it's there when
            # viewing the page source manually for some reason, regardless of login status.
            log_err("WARNING | An event is missing; the beatmapset was probably deleted.")
            return None
        
        try:
            # Scrape object data
            _type = event_json["message_type"] if "message_type" in event_json else types.REPLY
            time = timestamp.from_string(event_json["created_at"])

            # This part only matters in case `event_json` is a post, as we would then be missing some context.
            respective_discussion_json = None
            if discussion_jsons_for_replies:
                for discussion_json in discussion_jsons_for_replies:
                    if discussion_json["id"] == event_json["beatmapset_discussion_id"]:
                        respective_discussion_json = discussion_json
                        break
                
                if respective_discussion_json is None:
                    log_err("WARNING | The parent discussion for a reply is missing; it was probably deleted.")
                    return None

            beatmapset_id = event_json["beatmapset_id"] if "beatmapset_id" in event_json else respective_discussion_json["beatmapset_id"]
            if discussion_jsons_for_replies:
                discussion_id = event_json["beatmapset_discussion_id"]
            else:
                discussion_id = event_json["starting_post"]["beatmapset_discussion_id"] if "starting_post" in event_json else None

            user_id = event_json["user_id"]
            # The user name is either provided by a user json from the discussion page, or queried through the api.
            user_json = self.__lookup_user_json(user_id, user_jsons)
            user_name = user_json["username"] if user_json else None
            
            if discussion_jsons_for_replies:
                content = event_json["message"]
            else:
                content = event_json["starting_post"]["message"] if discussion_id else None


            difficulty = event_json["beatmap"]["version"] if "beatmap" in event_json and "version" in event_json["beatmap"] else None
            tab = None
            if "timestamp" in event_json:
                if event_json["timestamp"] is not None: tab = "timeline"
                elif difficulty:                        tab = "general"
                else:                                   tab = "generalAll"

            # Reconstruct objects
            beatmapset = Beatmapset(beatmapset_id)
            user = User(user_id, user_name) if user_id is not None else None
            # TODO: This portion is missing handling for replies, see the other method.
            # Still unclear which message_type replies use; will need to find out if/when replies get json formats.
            discussion = Discussion(discussion_id, beatmapset, user, content, tab, difficulty) if discussion_id is not None else None
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
        """Returns the type of the given event (e.g. "suggestion", "problem", "hype")."""
        event_class = "beatmap-discussion-message-type"
        class_prefix = "beatmap-discussion-message-type--"
        try:
            return super().parse_event_type(
                event,
                event_class=event_class,
                class_prefix=class_prefix
            )
        except ParsingError:
            if event:
                is_discussion_message = event.find(attrs={"class": event_class})
                has_type = event.find(attrs={"class": class_prefix})
                # Replies have no explicit type.
                if is_discussion_message and not has_type:
                    return "reply"
            raise
    
    def parse_event_author_id(self, event: Tag) -> str:
        """Returns the user id associated with the given event, if applicable (e.g. the user starting a discussion, "1314547")."""
        return super().parse_event_author_id(
            event,
            href_class="beatmap-discussion-user-card__user-link",
            must_find=True
        )
    
    def parse_event_author_name(self, event: Tag) -> str:
        """Returns the user name associated the given event, if applicable (e.g. the user starting a discussion, 5129592)."""
        return super().parse_event_author_name(
            event,
            name_class="beatmap-discussion-user-card__user-text",
            must_find=True
        )

    def parse_discussion_message(self, event: Tag) -> str:
        """Parses the raw message content of a discussion post."""
        message_class = "beatmap-discussion-post__message"
        return event.find("div", {"class": message_class}).contents[0]
    
    def parse_discussion_tab(self, event: Tag) -> str:
        """Parses the tab which a discussion post is on (e.g. "general" / "generalAll" / "timeline")."""
        active_tab_class = "page-mode-link--is-active"
        return event.find_previous("a", {"class": active_tab_class})["data-mode"]
    
    def parse_discussion_diff(self, event: Tag) -> str:
        """Parses the difficulty which a discussion post is on (e.g. "Expert").
        This may return some default difficulty if we're in the General tab."""
        active_diff_class = "beatmap-list__item--selected"
        active_diff_tag = event.find_previous("a", {"class": active_diff_class})
        if not active_diff_tag:
            raise ValueError("Could not parse the difficulty associated with a discussion.")

        return active_diff_tag.find("div", {"data-beatmap-title": True})["data-beatmap-title"]

# Only need one instance since it's always the same.
discussion_event_parser = DiscussionEventParser()