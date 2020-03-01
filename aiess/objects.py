from datetime import datetime
from typing import List

from aiess.web import api
from aiess.errors import DeletedContextError

class User:
    """Contains the user data either requested from the api or directly supplied (i.e. id, name)."""
    def __init__(self, _id: str, name: str=None):
        self.id = str(_id)
        if name != None:
            self.name = name
        else:
            user_json = api.request_user(_id)
            if user_json != None:
                self.name = user_json["username"]
            else:
                # User doesn't exist, likely restricted.
                self.name = None
    
    def __str__(self) -> str:
        return self.name if self.name != None else self.id
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return self.id == other.id and self.name == other.name

class Beatmapset:
    """Contains the beatmapset data requested from the api or supplied as a json object (e.g. artist, title, creator)."""
    MODES = {
        "0": "osu",
        "1": "taiko",
        "2": "catch",
        "3": "mania"
    }

    def __init__(self,
    _id: str, artist: str=None, title: str=None, creator: User=None, modes: List[str]=None,
    beatmapset_json: object=None):
        if _id == None:
            raise ValueError("Beatmapset id should not be None.")

        # No need to get the beatmap json if we already have all the data.
        if artist == None or title == None or creator == None or modes == None:
            if not beatmapset_json:
                beatmapset_json = api.request_beatmapset(_id)
                if not beatmapset_json:
                    raise DeletedContextError(f"Could not retrieve any api response for a beatmapset with id {_id}.")
            if str(beatmapset_json) == "[]":
                raise DeletedContextError(f"No beatmapset with id {_id} exists.")
            beatmap_json = beatmapset_json[0]  # Assumes metadata is the same across the entire set.

        self.id = str(_id)
        self.artist = artist if artist != None else beatmap_json["artist"]
        self.title = title if title != None else beatmap_json["title"]
        self.creator = creator if creator != None else User(
            beatmap_json["creator_id"],
            beatmap_json["creator"])
        
        self.modes = modes if modes != None else self.__get_modes(beatmapset_json)
    
    def __str__(self) -> str:
        return f"{self.artist} - {self.title} (mapped by {self.creator}) {self.mode_str()}"

    def mode_str(self) -> str:
        string = ""
        for mode in self.modes:
            string += f"[{mode}]"
        return string

    def __get_modes(self, beatmapset_json: object) -> List[str]:
        """Returns a list of the game modes by name included in the given beatmapset json (e.g. ["osu", "taiko", "mania"])."""
        mode_names = []
        for beatmap_json in beatmapset_json:
            mode_id = beatmap_json["mode"]
            mode_name = self.MODES[mode_id]
            if mode_name not in mode_names:
                mode_names.append(mode_name)
        return mode_names
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return (
            self.id == other.id and
            self.artist == other.artist and
            self.title == other.title and
            self.creator == other.creator and
            self.modes == other.modes
        )

class Discussion:
    """Contains the discussion data either supplied or further scraped (latter in case of e.g. disqualify or nomination_reset events)."""
    def __init__(self, _id: str, beatmapset: Beatmapset, user: User=None, content: str=None):
        self.id = str(_id)
        self.beatmapset = beatmapset
        self.user = user if user != None else None
        self.content = content if content != None else None
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return (
            self.id == other.id and
            self.beatmapset == other.beatmapset and
            self.user == other.user and
            self.content == other.content
        )

class Usergroup:
    """Contains the usergroup data (i.e id, name). Name is implied from id if not supplied."""
    GROUP_NAMES = {
        "4": "Global Moderation Team",
        "7": "Nomination Assessment Team",
        "11": "Development Team",
        "16": "Alumni",
        "22": "Support Team",
        "28": "Beatmap Nominators",
        "32": "Beatmap Nominators (Probationary)"
    }

    def __init__(self, _id: str, name: str=None):
        self.id = str(_id)
        self.name = name if name != None else self.__get_name(_id)

    def __get_name(self, _id: str) -> str:
        """Returns the name of the given group id, or None if unrecognized."""
        return self.GROUP_NAMES[_id] if _id in self.GROUP_NAMES else None
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return (
            self.id == other.id and
            self.name == other.name
        )

class Event:
    """Contains the event data (i.e. type, time, mapset, discussion, user, group, content). 
    Some of these properties will be None depending on type."""
    def __init__(self, _type: str, time: datetime,
            beatmapset: Beatmapset=None, discussion: Discussion=None, user: User=None, group: Usergroup=None, content: str=None):
        self.type = _type
        self.time = time.replace(microsecond=0)  # Simplify precision to database-level
        self.beatmapset = beatmapset
        self.discussion = discussion
        self.user = user
        self.group = group
        self.content = content

        # Occurs in cases where the event should not be logged.
        # e.g. discussion deleted but we don't have the discussion cached (no relevant information).
        self.marked_for_deletion = False
    
    def __str__(self) -> str:
        string = f"{self.time} | {self.type}"
        string += f" ({self.user})" if self.user else ""
        string += f" on {self.beatmapset}" if self.beatmapset else ""
        string += f" to/from {self.group}" if self.group else ""
        string += f" \"{self.content}\"" if self.content else ""
        
        return string
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return (
            self.type == other.type and
            self.time == other.time and
            self.beatmapset == other.beatmapset and
            self.discussion == other.discussion and
            self.user == other.user and
            self.group == other.group and
            self.content == other.content
        )