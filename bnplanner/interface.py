import sys
sys.path.append('..')

import requests
from datetime import datetime

from aiess import Event
from aiess import event_types as types
from aiess.settings import BNPLANNER_HEADERS

class StatusDocument():
    def __init__(self, event):
        self.time         = (event.time - datetime(1970,1,1)).total_seconds()
        self.beatmapSetId = event.beatmapset.id
        self.artist       = event.beatmapset.artist
        self.title        = event.beatmapset.title
        self.creatorId    = event.beatmapset.creator.id
        self.creatorName  = event.beatmapset.creator.name
        self.userId       = event.user.id if event.user else None
        self.userName     = event.user.name if event.user else None
        self.status       = status_by_event_type[event.type]
        self.modes        = list(map(to_api_mode, event.beatmapset.modes))

class GroupChangeDocument():
    def __init__(self, event):
        self.time      = (event.time - datetime(1970,1,1)).total_seconds()
        self.type      = event.type  # "add" / "remove"
        self.userId    = event.user.id if event.user else None
        self.userName  = event.user.name if event.user else None
        self.groupId   = event.group.id
        self.groupMode = to_api_mode(event.group.mode)

status_by_event_type = {
    types.QUALIFY:    "Qualified",
    types.NOMINATE:   "Nominated",
    types.DISQUALIFY: "Disqualified",
    types.RESET:      "Reset",
    types.RANK:       "Ranked"
}

# Greaper wants the mode names the api uses (`catch` -> `fruits`).
def to_api_mode(mode: str):
    return mode if mode != "catch" else "fruits"

def insert_event(event: Event) -> None:
    """Sends a POST request with this event as a json, outlined in `Document`."""
    is_group_change = event.type in ["add", "remove"]
    if is_group_change:
        url = "https://bnplannerbackend.greaper.net/v2/aiess/event/user"
        document = GroupChangeDocument(event)
    else:
        url = "https://bnplannerbackend.greaper.net/v2/aiess/event/beatmap"
        document = StatusDocument(event)
    
    response = requests.post(url, json=vars(document), headers=BNPLANNER_HEADERS)
    # Response codes are the usual ones.
    code = str(response.status_code)
    if not code.startswith("2"):
        # 2XX indicates success. If we don't succeed, we should raise an error.
        raise ValueError(f"Received {response.text}")