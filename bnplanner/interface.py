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
        self.userId       = event.user.id if event.user else None
        self.status       = to_status_id(event.type)

class GroupChangeDocument():
    def __init__(self, event):
        self.time    = (event.time - datetime(1970,1,1)).total_seconds()
        self.type    = event.type  # "add" / "remove"
        self.userId  = event.user.id if event.user else None
        self.groupId = event.group_id

status_id_type_map = {
    types.QUALIFY:    1,
    types.NOMINATE:   2,
    types.DISQUALIFY: 3,
    types.RESET:      4,
    types.RANK:       6
}

def to_status_id(type: str) -> int:
    """Returns the status ID assoicated with the given event type (e.g. qualified = 1)."""
    return status_id_type_map[type]

def insert_event(event: Event) -> None:
    """Sends a POST request with this event as a json, outlined in `Document`."""
    url = "https://bnplannerbackend.greaper.net/v1/beatmap/add/event/aiess"
    document = GroupChangeDocument(event) if event.type in ["add", "remove"] else StatusDocument(event)
    response = requests.post(url, json=vars(document), headers=BNPLANNER_HEADERS)
    # Response codes are the usual ones.
    code = str(response.status_code)
    if not code.startswith("2"):
        # 2XX indicates success. If we don't succeed, we should raise an error.
        raise ValueError(f"Received {response.text}")