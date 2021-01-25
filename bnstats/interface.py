import sys
sys.path.append('..')

import requests

from aiess import Event
from aiess.settings import BNSTATS_HEADERS

class Document():
    def __init__(self, event):
        self.type         = event.type
        self.timestamp    = str(event.time)
        self.beatmapsetId = event.beatmapset.id
        self.creatorId    = event.beatmapset.creator.id
        self.creatorName  = event.beatmapset.creator.name
        self.discussionId = event.discussion.id if event.discussion else None
        self.userId       = event.user.id if event.user else None
        self.artistTitle  = f"{event.beatmapset.artist} - {event.beatmapset.title}"
        self.content      = event.content

def insert_event(event: Event) -> None:
    """Sends a POST request to https://bnstats.rorre.xyz/qat/aiess with
    this event as a json, outlined in `Document`."""
    response = requests.post(url="https://bnstats.rorre.xyz/qat/aiess", json=vars(Document(event)), headers=BNSTATS_HEADERS)
    # See https://github.com/rorre/BNStats/blob/naxess_score/bnstats/routes/qat.py#L81.
    code = str(response.status_code)
    if not code.startswith("2") and not code.startswith("5"):
        # 2XX indicates success. If we don't succeed, we should raise an error.
        # 5XX indicates failure on part of the server (e.g. osu!api being down). We can safely
        # ignore these, as bnstats runs a routine check for missing data, which is then recovered.
        raise ValueError(f"Received {response.text}")