from datetime import datetime
from typing import List

from aiess.web import api
from aiess.errors import DeletedContextError

class User:
    """Contains the user data either requested from the api or directly supplied (i.e. id, name)."""
    def __init__(self, _id: str, name: str=None):
        self.id = str(_id)
        if name is not None:
            # Cast for ease-of-use, e.g. with names consisting of just digits.
            self.name = str(name)
        else:
            user_json = api.request_user(_id)
            if user_json is not None:
                self.name = str(user_json["username"])
            else:
                # User doesn't exist, likely restricted.
                self.name = None
    
    def __str__(self) -> str:
        return self.name if self.name is not None else str(self.id)
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.name
        )
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

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
        if _id is None:
            raise ValueError("Beatmapset id should not be None.")

        # No need to get the beatmap json if we already have all the data.
        if artist is None or title is None or creator is None or modes is None:
            if not beatmapset_json:
                beatmapset_json = api.request_beatmapset(_id)
                if not beatmapset_json:
                    raise DeletedContextError(f"Could not retrieve any api response for a beatmapset with id {_id}.")
            if str(beatmapset_json) == "[]":
                raise DeletedContextError(f"No beatmapset with id {_id} exists.")
            beatmap_json = beatmapset_json[0]  # Assumes metadata is the same across the entire set.

        self.id = str(_id)
        self.artist = str(artist) if artist is not None else beatmap_json["artist"]
        self.title = str(title) if title is not None else beatmap_json["title"]
        self.creator = creator if creator is not None else User(
            beatmap_json["creator_id"],
            beatmap_json["creator"])
        
        self.modes = modes if modes is not None else self.__get_modes(beatmapset_json)
    
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
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.artist,
            self.title,
            self.creator,
            tuple(self.modes)  # Cannot hash mutable types; list is mutable, tuple is immutable.
        )
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

class Discussion:
    """Contains the discussion data either supplied or further scraped (latter in case of e.g. disqualify or nomination_reset events)."""
    def __init__(self, _id: str, beatmapset: Beatmapset, user: User=None, content: str=None):
        self.id = str(_id)
        self.beatmapset = beatmapset
        self.user = user if user is not None else None
        self.content = str(content) if content is not None else None
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.beatmapset,
            self.user,
            self.content
        )
    
    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

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
        self.name = name if name is not None else self.__get_name(str(_id))

    def __get_name(self, _id: str) -> str:
        """Returns the name of the given group id, or None if unrecognized."""
        return self.GROUP_NAMES[_id] if _id in self.GROUP_NAMES else None
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.name
        )

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

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
        self.content = str(content) if content is not None else None

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
    
    def __key(self) -> tuple:
        return (
            self.type,
            self.time,
            self.beatmapset,
            self.discussion,
            self.user,
            self.group,
            self.content
        )

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())