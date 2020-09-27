import sys
sys.path.append('..')

from aiess import Event
from aiess import timestamp
from aiess.database import Database, SCRAPER_DB_NAME

def convert_to_event(json: object) -> Event:
    database = Database(SCRAPER_DB_NAME)

    beatmapset_id = float(json["beatmapsetId"]) if "beatmapsetId" in json and json["beatmapsetId"] else None
    discussion_id = float(json["discussionId"]) if "discussionId" in json and json["discussionId"] else None
    user_id       = float(json["userId"])       if "userId"       in json and json["userId"]       else None

    _type      = json["type"]
    time       = timestamp.from_string(json["timestamp"])
    beatmapset = database.retrieve_beatmapset("id=%s", (beatmapset_id,)) if beatmapset_id else None
    discussion = database.retrieve_discussion("id=%s", (discussion_id,)) if discussion_id else None
    user       = database.retrieve_user("id=%s", (user_id,))             if user_id       else None
    content    = json["content"]

    return Event(_type=_type, time=time, beatmapset=beatmapset, discussion=discussion, user=user, content=content)