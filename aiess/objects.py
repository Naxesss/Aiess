from datetime import datetime
from typing import List

from aiess import timestamp
from aiess.web import api
from aiess.errors import DeletedContextError

class User:
    """Contains the user data either requested from the api or directly supplied (i.e. id, name)."""
    def __init__(self, _id: int=None, name: str=None, allow_api: bool=True):
        if _id is None and name is None:
            raise ValueError("Cannot create a User object with neither id nor name provided.")

        if not allow_api:
            if _id  is None: _id  = 1
            if name is None: name = "name"

        self.id = int(_id) if _id is not None else None
        self.name = str(name) if name is not None else None

        if name is None or _id is None:
            if name is None: user_json = api.request_user(_id)
            if _id is None:  user_json = api.request_user(name)
            # Otherwise user doesn't exist, either restricted or renamed a long time ago.
            if user_json is not None:
                self.id = int(user_json["user_id"])
                self.name = str(user_json["username"])
    
    def __str__(self) -> str:
        return self.name if self.name is not None else str(self.id)
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.name
        )
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

class Beatmap:
    """Contains the beatmap data given a json representation (e.g. diff name, star rating, and draintime)."""
    def __init__(self):
        # Default initialize all values to None. This faciliates __eq__,
        # __hash__, etc. to function even if not all values are specified.
        self.id            = None
        self.beatmapset_id = None
        self.version       = None
        self.totaltime     = None
        self.draintime     = None
        self.cs            = None
        self.od            = None
        self.ar            = None
        self.hp            = None
        self.mode          = None
        self.circles       = None
        self.sliders       = None
        self.spinners      = None
        self.submit_date   = None
        self.approved_date = None
        self.artist        = None
        self.title         = None
        self.creator_name  = None
        self.bpm           = None
        self.source        = None
        self.tags          = None
        self.genre         = None
        self.language      = None
        self.favourites    = None
        self.userrating    = None
        self.playcount     = None
        self.passcount     = None
        self.max_combo     = None
        self.sr_aim        = None
        self.sr_speed      = None
        self.sr_total      = None
        self.updated_at    = None
    
    @classmethod
    def from_json(self, beatmap_json: str):
        beatmap = self()
        beatmap.id            = int(beatmap_json["beatmap_id"])
        beatmap.beatmapset_id = int(beatmap_json["beatmapset_id"])
        beatmap.version       = str(beatmap_json["version"])
        beatmap.totaltime     = float(beatmap_json["total_length"])
        beatmap.draintime     = float(beatmap_json["hit_length"])
        beatmap.cs            = float(beatmap_json["diff_size"])
        beatmap.od            = float(beatmap_json["diff_overall"])
        beatmap.ar            = float(beatmap_json["diff_approach"])
        beatmap.hp            = float(beatmap_json["diff_drain"])
        beatmap.mode          = api.MODES[beatmap_json["mode"]]
        beatmap.circles       = int(beatmap_json["count_normal"])
        beatmap.sliders       = int(beatmap_json["count_slider"])
        beatmap.spinners      = int(beatmap_json["count_spinner"])
        beatmap.submit_date   = timestamp.from_string(beatmap_json["submit_date"])
        beatmap.approved_date = timestamp.from_string(beatmap_json["approved_date"]) if beatmap_json["approved_date"] else None  # None if not ranked.
        beatmap.artist        = str(beatmap_json["artist"])
        beatmap.title         = str(beatmap_json["title"])
        beatmap.creator_name  = str(beatmap_json["creator"])
        beatmap.bpm           = float(beatmap_json["bpm"]) if beatmap_json["bpm"] else None  # None if no timing lines.
        beatmap.source        = str(beatmap_json["source"])
        beatmap.tags          = str(beatmap_json["tags"])
        beatmap.genre         = api.GENRES[beatmap_json["genre_id"]]
        beatmap.language      = api.LANGUAGES[beatmap_json["language_id"]]
        beatmap.favourites    = int(beatmap_json["favourite_count"])
        beatmap.userrating    = float(beatmap_json["rating"])
        beatmap.playcount     = int(beatmap_json["playcount"])
        beatmap.passcount     = int(beatmap_json["passcount"])
        beatmap.max_combo     = int(beatmap_json["max_combo"])    if beatmap_json["max_combo"]  else None  # None for taiko maps.
        beatmap.sr_aim        = float(beatmap_json["diff_aim"])   if beatmap_json["diff_aim"]   else None
        beatmap.sr_speed      = float(beatmap_json["diff_speed"]) if beatmap_json["diff_speed"] else None
        beatmap.sr_total      = float(beatmap_json["difficultyrating"])
        beatmap.updated_at    = datetime.utcnow()

        return beatmap

    @classmethod
    def from_raw(
            self, _id: int, beatmapset_id: int, version: str, draintime: float, sr_total: float,
            favourites: int, userrating: float, playcount: int, passcount: int, updated_at: object
        ):
        """Returns the beatmap object with the given attributes. This is
        used by the database to reconstruct beatmaps when retrieved."""
        beatmap = self()
        beatmap.id            = int(_id)
        beatmap.beatmapset_id = int(beatmapset_id)
        beatmap.version       = str(version)
        beatmap.draintime     = float(draintime)
        beatmap.sr_total      = float(sr_total)
        beatmap.favourites    = int(favourites)   if favourites is not None else None  # Following were added later, so old entries have these as None.
        beatmap.userrating    = float(userrating) if userrating is not None else None 
        beatmap.playcount     = int(playcount)    if playcount  is not None else None
        beatmap.passcount     = int(passcount)    if passcount  is not None else None
        beatmap.updated_at    = updated_at

        return beatmap

    @classmethod
    def from_api(self, _id: int, beatmapset_id: int):
        """Returns the beatmap with the given id and beatmapset id from the osu!api, if any, else None."""
        beatmapset_json = api.request_beatmapset(beatmapset_id=beatmapset_id)
        beatmapset = Beatmapset(beatmapset_json=beatmapset_json)
        for beatmap in beatmapset.beatmaps:
            if beatmap.id == _id:
                return beatmap
        
        return None

    def is_incomplete(self):
        return (
            self.id            is None or
            self.beatmapset_id is None or
            self.version       is None or
            self.draintime     is None or
            self.sr_total      is None or
            self.favourites    is None or
            self.userrating    is None or
            self.playcount     is None or
            self.passcount     is None or
            self.updated_at    is None
        )

    def __str__(self) -> str:
        return f"{self.artist} - {self.title} (mapped by {self.creator_name}) [{self.mode}] \"{self.version}\""
    
    def __key(self) -> tuple:
        # Only checks the most distinctive attributes, as these are the only ones we store in the database.
        return (
            self.beatmapset_id,
            self.id,
            self.version,
            self.draintime,
            self.sr_total,
            self.favourites,
            self.userrating,
            self.playcount,
            self.passcount
        )
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Beatmap):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

class Beatmapset:
    """Contains the beatmapset data requested from the api or supplied as a json object (e.g. artist, title, creator)."""
    def __init__(
            self, _id: int=None, artist: str=None, title: str=None, creator: User=None,
            modes: List[str]=None, genre: str=None, language: str=None, tags: List[str]=None,
            beatmaps: List[Beatmap]=None, beatmapset_json: object=None, allow_api: bool=True):

        self.incomplete = False
        
        self.id       = _id
        self.artist   = artist
        self.title    = title
        self.creator  = creator
        self.modes    = modes
        self.genre    = genre
        self.language = language
        self.tags     = tags
        self.beatmaps = beatmaps
        self.status   = None

        if self.is_incomplete():
            # Not all information was provided in the constructor.
            # We need this information populated.
            if beatmapset_json:
                self.from_json(beatmapset_json)
                self.incomplete = False
            elif allow_api and _id is not None:
                beatmapset_json = api.request_beatmapset(_id)
                if not beatmapset_json:
                    raise DeletedContextError(f"Could not retrieve any api response for a beatmapset with id {_id}.")
                self.from_json(beatmapset_json)
                self.incomplete = False
            else:
                # With no access to the API, we can only mock the attributes.
                self.id       = int(_id)      if _id      else 1
                self.artist   = str(artist)   if artist   else "artist"
                self.title    = str(title)    if title    else "title"
                self.creator  = creator       if creator  else User(_id=1, name="creator")
                self.modes    = modes         if modes    else ["osu"]
                self.genre    = str(genre)    if genre    else "genre"
                self.language = str(language) if language else "language"
                self.tags     = tags          if tags     else ["tags"]
                self.beatmaps = beatmaps      if beatmaps else []

                # Show that the beatmapset is not truly complete, as we have simply mocked some attributes.
                self.incomplete = True
    
    def from_json(self, beatmapset_json: str):
        if str(beatmapset_json) == "[]":
            raise DeletedContextError(f"A beatmapset did not exist.")
        beatmap_json = beatmapset_json[0]

        self.beatmaps = [Beatmap.from_json(json) for json in beatmapset_json]
        ref_beatmap = self.beatmaps[0]  # Assumes metadata is the same across the entire set.

        self.id       = int(beatmap_json["beatmapset_id"])
        self.artist   = ref_beatmap.artist
        self.title    = ref_beatmap.title
        self.creator  = User(
            beatmap_json["creator_id"],
            beatmap_json["creator"]
        )
        self.modes    = self.__get_modes()
        self.genre    = ref_beatmap.genre
        self.language = ref_beatmap.language
        self.tags     = ref_beatmap.tags.split(" ")

    def is_incomplete(self):
        return self.incomplete or (
            self.artist   is None or
            self.title    is None or
            self.creator  is None or
            self.modes    is None or
            self.language is None or
            self.genre    is None or
            self.tags     is None or
            self.beatmaps is None or
            any(beatmap.is_incomplete() for beatmap in self.beatmaps if beatmap is not None)
        )

    def __str__(self) -> str:
        return f"{self.artist} - {self.title} (mapped by {self.creator}) {self.mode_str()}"

    def mode_str(self) -> str:
        """Returns a string representation of the modes in this beatmapset (e.g. "[osu][taiko]")."""
        return "".join(f"[{mode}]" for mode in self.modes)

    def __get_modes(self) -> List[str]:
        """Returns a list of the game modes by name (e.g. ["osu", "taiko", "mania"])."""
        modes = []
        for beatmap in self.beatmaps:
            if beatmap.mode not in modes:
                modes.append(beatmap.mode)
        return modes
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.artist,
            self.title,
            self.creator,
            tuple(self.modes),  # Cannot hash mutable types; list is mutable, tuple is immutable.
            self.language,
            self.genre,
            tuple(self.tags),
            tuple(self.beatmaps)
        )
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Beatmapset):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

class BeatmapsetStatus():
    """Contains information about the ranked status of a beatmapset at some point in time
    (e.g. pending/qualified/ranked and nominators)."""
    def __init__(self, _id: int, beatmapset: Beatmapset, status: str, time: datetime, nominators: List[User]=[]):
        self.id         = _id
        self.beatmapset = beatmapset
        self.status     = status
        self.time       = time
        self.nominators = nominators
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.beatmapset,
            self.status,
            self.time,
            tuple(self.nominators)
        )
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, BeatmapsetStatus):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

class Discussion:
    """Contains the discussion data either supplied or further scraped (latter in case of e.g. disqualify or nomination_reset events)."""
    def __init__(
            self, _id: int, beatmapset: Beatmapset, user: User=None, content: str=None,
            tab: str=None, difficulty: str=None
        ):
        self.id = int(_id)
        self.beatmapset = beatmapset
        self.user = user if user is not None else None
        self.content = str(content) if content is not None else None
        self.tab = str(tab) if tab is not None else None
        self.difficulty = str(difficulty) if difficulty is not None else None
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.beatmapset,
            self.user,
            self.content,
            self.tab,
            self.difficulty
        )
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Discussion):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())

class Usergroup:
    """Contains the usergroup data (i.e id, name). Name is implied from id if not supplied."""
    GROUP_NAMES = {
        4: "Global Moderation Team",
        7: "Nomination Assessment Team",
        11: "Development Team",
        16: "Alumni",
        22: "Support Team",
        28: "Beatmap Nominators",
        31: "Project Loved",
        32: "Beatmap Nominators (Probationary)"
    }

    def __init__(self, _id: int, name: str=None, mode: str=None):
        self.id = int(_id)
        self.name = str(name) if name is not None else self.__get_name(int(_id))
        self.mode = mode

    def __get_name(self, _id: int) -> str:
        """Returns the name of the given group id, or None if unrecognized."""
        return self.GROUP_NAMES[_id] if _id in self.GROUP_NAMES else None
    
    def __key(self) -> tuple:
        return (
            self.id,
            self.name,
            self.mode
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Usergroup):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())
    
    def __str__(self) -> str:
        if self.name:
            return self.name
        return "group " + self.id

class NewsPost:
    """Contains news post data (e.g. title, preview, author, and image url)."""
    def __init__(self, _id: int, title: str, preview: str, author: User, slug: str, image_url: str):
        self.id = int(_id)
        self.title = str(title)
        self.preview = str(preview)
        self.author = author
        self.slug = str(slug)
        self.image_url = str(image_url)

    def __key(self) -> tuple:
        return (
            self.id,
            self.title,
            self.preview,
            self.author,
            self.slug,
            self.image_url
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, NewsPost):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())
    
    def __str__(self) -> str:
        return self.title

class Event:
    """Contains the event data (i.e. type, time, mapset, discussion, user, group, content).
    Some of these properties will be None depending on type."""
    def __init__(
            self, _type: str, time: datetime, beatmapset: Beatmapset=None, discussion: Discussion=None,
            user: User=None, group: Usergroup=None, newspost: NewsPost=None, content: str=None):
        self.type = _type
        self.time = time.replace(microsecond=0)  # Simplify precision to database-level
        self.beatmapset = beatmapset
        self.discussion = discussion
        self.user = user
        self.group = group
        self.newspost = newspost
        self.content = str(content) if content is not None else None

        # Occurs in cases where the event should not be logged.
        # e.g. discussion deleted but we don't have the discussion cached (no relevant information).
        self.marked_for_deletion = False
    
    def __str__(self) -> str:
        string = f"{self.time} | {self.type}"
        string += f" ({self.user})" if self.user else ""
        string += f" on {self.beatmapset}" if self.beatmapset else ""
        string += f" to/from {self.group}" if self.group else ""
        string += f" posted {self.newspost}" if self.newspost else ""
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
        if not isinstance(other, Event):
            return False
        return self.__key() == other.__key()
    
    def __hash__(self) -> str:
        return hash(self.__key())