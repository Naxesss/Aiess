import sys
sys.path.append('..')

from datetime import datetime

from aiess import Event, Beatmapset, User, Discussion
from aiess.timestamp import from_string

beatmapset = Beatmapset(4, "artist", "title", creator=User(1, "someone"), allow_api=False)
discussion = Discussion(20, beatmapset=beatmapset, user=User(2, "sometwo"), content="hi")
discussion_dq = Discussion(22, beatmapset=beatmapset, user=User(2, "sometwo"), content="no wait")

# Note that all events are yielded from newest to oldest.

def get_news_events(_from: datetime, limit: int=20):
    # The actual newspost doesn't matter, we're just making sure crawling the events works properly.
    if _from == from_string("2020-01-01 03:00:00"):
        yield Event("news", from_string("2020-01-01 03:00:00"), newspost=None, user=User(2, "sometwo"))
        yield Event("news", from_string("2020-01-01 02:30:00"), newspost=None, user=User(1, "someone"))
        yield Event("news", from_string("2020-01-01 02:00:00"), newspost=None, user=User(4, "somefour"))
    if _from == from_string("2020-01-01 02:00:00"):
        yield Event("news", from_string("2020-01-01 01:00:00"), newspost=None, user=User(3, "somethree"))
        yield Event("news", from_string("2020-01-01 00:00:00"), newspost=None, user=User(5, "somefive"))

def get_discussion_events(page: int=1, limit: int=50):
    if page == 1:
        yield Event("problem", from_string("2020-01-01 03:00:00"), beatmapset, discussion_dq, user=User(2, "sometwo"), content="no wait")
        yield Event("hype", from_string("2020-01-01 02:30:00"), beatmapset, user=User(2, "sometwo"), content="hype")
        yield Event("praise", from_string("2020-01-01 02:00:00"), beatmapset, user=User(2, "sometwo"), content="amazing")
    if page == 2:
        yield Event("issue_resolve", from_string("2020-01-01 01:00:00"), beatmapset, discussion, user=User(1, "someone"))
        yield Event("praise", from_string("2020-01-01 00:00:00"), beatmapset, user=User(2, "sometwo"), content="wow")

def get_reply_events(page: int=1, limit: int=50):
    if page == 1:
        yield Event("reply", from_string("2020-01-01 01:04:00"), beatmapset, user=User(2, "sometwo"), content="thanks")
        yield Event("reply", from_string("2020-01-01 01:00:00"), beatmapset, user=User(1, "someone"), content="hi")
        yield Event("reply", from_string("2020-01-01 00:31:00"), beatmapset, discussion, user=User(2, "sometwo"), content="say hi back")
    if page == 2:
        yield Event("reply", from_string("2020-01-01 00:30:00"), beatmapset, discussion, user=User(1, "someone"), content="yes?")
        yield Event("reply", from_string("2020-01-01 00:00:00"), beatmapset, discussion, user=User(2, "sometwo"), content="please reply")

def get_beatmapset_events(page: int=1, limit: int=50):
    if page == 1:
        yield Event("disqualify", from_string("2020-01-01 03:00:00"), beatmapset, discussion_dq, user=User(2, "sometwo"))
        yield Event("qualify", from_string("2020-01-01 02:31:00"), beatmapset)
        yield Event("nominate", from_string("2020-01-01 02:31:00"), beatmapset, user=User(2, "sometwo"))
    if page == 2:
        yield Event("nominate", from_string("2020-01-01 02:30:30"), beatmapset, user=User(1, "someone"))

def get_beatmapset_events_too_new(page: int=1, limit: int=50):
    if page == 1:
        # Feburary for this one
        yield Event("disqualify", from_string("2020-02-01 03:00:00"), beatmapset, discussion_dq, user=User(2, "sometwo"))
    if page == 2:
        # January for the rest
        yield Event("qualify", from_string("2020-01-01 02:31:00"), beatmapset)
        yield Event("nominate", from_string("2020-01-01 02:31:00"), beatmapset, user=User(2, "sometwo"))
    if page == 3:
        yield Event("nominate", from_string("2020-01-01 02:30:30"), beatmapset, user=User(1, "someone"))