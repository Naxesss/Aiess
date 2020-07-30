import sys
sys.path.append('..')

from aiess import Event
from aiess.settings import BNSITE_MONGODB_URI

from pymongo import MongoClient

class Document():
    def __init__(self, event):                                                          # LEGACY NAME
        self.type          = event.type                                                 # eventType
        self.timestamp     = event.time                                                 # timestamp
        self.beatmapset_id = event.beatmapset.id                                        # beatmapsetId
        self.creator_id    = event.beatmapset.creator.id                                # hostId
        self.creator_name  = event.beatmapset.creator.name                              # hostName
        self.modes         = event.beatmapset.modes                                     # modes
        self.discussion_id = event.discussion.id if event.discussion else None          # postId
        self.user_id       = event.user.id if event.user else None                      # userId
        self.artist_title  = f"{event.beatmapset.artist} - {event.beatmapset.title}"    # metadata
        self.content       = event.content                                              # content

def insert_event(event: Event) -> None:
    """Creates a connection to the MongoDB server, inserts the event as a
    custom document, then immediately closes the connection."""
    client = MongoClient(BNSITE_MONGODB_URI)
    #client.qatstuff.aiess.insert_one(Document(event))
    client.close()