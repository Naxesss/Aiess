import sys
sys.path.append('..')

from bs4.element import Tag
from datetime import datetime
import re as regex

from aiess.errors import ParsingError, DeletedContextError
from aiess import timestamp

class EventParser():

    def parse_event_type(self, event: Tag, event_class: str, class_prefix: str) -> str:
        """Returns the type of the given event (e.g. "suggestion", "problem", "hype", "nominate", "issue-resolve", "disqualify").
        Only use this function if you know what you're doing, use child classes for maintainability (e.g. BeatmapsetEventParser)."""
        event_type = None
        event_tag = event and event.find(attrs={"class": event_class})
        if event_tag:
            for class_name in event_tag.attrs["class"]:
                if class_name.startswith(class_prefix):
                    # CSS class types use -, whereas json types use _, we should standardize this.
                    event_type = class_name[len(class_prefix):].replace("-", "_")
                    break
        
        # Failure to parse event type should be met with an exception, as this is abnormal and will likely cause further issues if silent.
        if not event_type:
            raise ParsingError(f"""
                The type of an event could not be parsed. Expected some class starting with \"{class_prefix}\":\r\n{event}""")

        return event_type

    def parse_event_time(self, event: Tag) -> datetime:
        """Returns the datetime of the given event (e.g. "2019-10-12T02:19:27+00:00" into its datetime equivalent)."""
        event_time = None
        time = event and event.find(attrs={"class": "js-timeago"})
        if time:
            event_time = time.attrs["datetime"]
        
        # Failure to parse event time should be met with an exception for the same reason as failing to parse event type.
        if event_time is None:
            raise ParsingError(f"""
                The time of an event could not be parsed. Expected some time object with class \"timeago\":\r\n{event}""")

        return timestamp.from_string(event_time)

    def parse_event_link(self, event: Tag) -> str:
        """Returns the beatmapset/discussion link from the thumbnail of a given event
        (e.g. "https://osu.ppy.sh/beatmapsets/818013/discussion#/1211219")."""
        thumb = event and event.find("a", {"href": regex.compile(r"^https:\/\/osu\.ppy\.sh\/beatmapsets\/")})
        href = thumb and thumb.attrs["href"]

        if not href:
            self.raise_if_deleted(event)
            raise ParsingError("""
                The thumbnail link of an event could not be found. Expected some <a> tag with attribute href.""")

        return href

    def parse_event_author_id(self, event: Tag, href_class: str, must_find: bool=False) -> str:
        """Returns the user id associated with the given event, if applicable (e.g. the user nominating or starting a discussion, "1314547").
        Only use this function if you know what you're doing, see child classes for abstracted versions (e.g. BeatmapsetEventParser)."""
        user_id = None
        user_a = event and event.find(attrs={"class": href_class})
        if user_a:
            if user_a.has_attr("data-user-id"):
                user_id = str(user_a["data-user-id"])
            
            if not user_id and user_a.has_attr("href"):
                user_id = self.parse_id_from_user_link(user_a["href"])
        
        if must_find and not user_id:
            self.raise_if_deleted(event)
            raise ParsingError(f"""
                The user id of the author of an event could not be parsed. Expected some <a> tag with class \"user-name\"
                and attr \"data-user-id\":\r\n{event}""")

        return user_id

    def parse_event_author_name(self, event: Tag, name_class: str, must_find: bool=False) -> str:
        """Returns the user name associated the given event, if applicable (e.g. the user nominating or starting a discussion, 5129592).
        Only use this function if you know what you're doing, see child classes for abstracted versions (e.g. BeatmapsetEventParser)."""
        user_name = None
        user_href = event and event.find(attrs={"class": name_class})
        if user_href:
            user_name = user_href.getText()
        
        if must_find and not user_name:
            self.raise_if_deleted(event)
            raise ParsingError(f"""
                The user name of the author of an event could not be parsed. Expected some href object with class \"user-name\"
                and attr \"data-user-id\":\r\n{event}""")
        
        return user_name

    def parse_id_from_user_link(self, link: str) -> str:
        """Returns the user id from the given user link (assuming the link contains the id, otherwise None)
        (i.e. link following this format https://osu.ppy.sh/users/5129592)."""
        if not link:
            return None
        match = regex.search(r"https:\/\/osu\.ppy\.sh\/users\/(\d+)", link)
        if not match:
            return None
        return match.group(1)

    def parse_id_from_discussion_link(self, link: str) -> str:
        """Returns the discussion id from the given discussion link (assuming the link contains the id, otherwise None)
        (i.e. link following this format https://osu.ppy.sh/beatmapsets/1016042/discussion#/1294751)."""
        if not link:
            return None
        match = regex.search(r"https:\/\/osu\.ppy\.sh\/beatmapsets\/\d+\/discussion#\/(\d+)", link)
        if not match:
            return None
        return match.group(1)

    def parse_id_from_beatmapset_link(self, link: str) -> str:
        """Returns the beatmapset id from the given beatmapset link (assuming the link contains the id, otherwise None)
        (i.e. link following this format https://osu.ppy.sh/beatmapsets/1016042)."""
        if not link:
            return None
        match = regex.search(r"https:\/\/osu\.ppy\.sh\/beatmapsets\/(\d+)", link)
        if not match:
            return None
        return match.group(1)
    
    def is_beatmap_deleted(self, event: Tag) -> bool:
        """Returns whether the event includes some span containing "deleted",
        as any deleted beatmap will include "<span>deleted<br>beatmap</span>"."""
        span = event and event.find("span")
        return span and "deleted" in span.text
    
    def raise_if_deleted(self, event: Tag) -> bool:
        if self.is_beatmap_deleted(event):
            raise DeletedContextError()