import sys
sys.path.append('..')

from aiess import Event
from aiess.settings import BNSITE_MONGODB_URI
from aiess import event_types as types

from pymongo import MongoClient

class Document():
    def __init__(self, event):
        self.type         = event.type
        self.timestamp    = event.time
        self.beatmapsetId = event.beatmapset.id
        self.creatorId    = event.beatmapset.creator.id
        self.creatorName  = event.beatmapset.creator.name
        self.modes        = event.beatmapset.modes
        self.discussionId = event.discussion.id if event.discussion else None
        self.userId       = event.user.id if event.user else None
        self.artistTitle  = f"{event.beatmapset.artist} - {event.beatmapset.title}"
        self.content      = event.content

def insert_event(event: Event) -> None:
    """Creates a connection to the MongoDB server, inserts the event as a
    custom document, then immediately closes the connection."""
    client = MongoClient(BNSITE_MONGODB_URI, retryWrites=False)
    client.qat_db.aiess.insert_one(vars(Document(event)))
    client.close()