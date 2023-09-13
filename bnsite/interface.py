import sys

from pymongo.common import SERVER_SELECTION_TIMEOUT
sys.path.append('..')

from aiess import Event, Beatmap
from aiess.settings import BNSITE_MONGODB_URI
from aiess import event_types as types

from pymongo import MongoClient

class DocumentBeatmap():
    def __init__(self, beatmap: Beatmap):
        self.drain      = beatmap.draintime
        self.starRating = beatmap.sr_total
        self.userRating = beatmap.userrating

class Document():
    def __init__(self, event: Event):
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
        self.genre        = event.beatmapset.genre
        self.language     = event.beatmapset.language
        self.beatmaps     = list(map(lambda beatmap: vars(DocumentBeatmap(beatmap)), event.beatmapset.beatmaps))

def insert_event(event: Event) -> None:
    """Creates a connection to the MongoDB server, inserts the event as a
    custom document, then immediately closes the connection."""
    client = MongoClient(BNSITE_MONGODB_URI, retryWrites=False, serverSelectionTimeoutMS=120000)
    client.qat_db.aiess.insert_one(vars(Document(event)))
    client.close()