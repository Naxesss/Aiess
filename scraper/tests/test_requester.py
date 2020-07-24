import sys
sys.path.append('..')

from datetime import datetime

from scraper.requester import get_news_events
from scraper.requester import get_beatmapset_events
from scraper.requester import get_discussion_events
from scraper.requester import get_reply_events

def test_get_news_events():
    events = get_news_events(_from=datetime.utcnow(), limit=20)
    
    event_n = 0
    for event in events:
        assert event.user
        assert event.newspost
        event_n += 1
    
    assert event_n == 20

def test_get_beatmapset_events():
    events = get_beatmapset_events(page=1, limit=50)

    event_n = 0
    for event in events:
        assert event.beatmapset
        event_n += 1
    
    assert event_n == 50

def test_get_discussion_events():
    events = get_discussion_events(page=1, limit=50)
    
    event_n = 0
    for event in events:
        assert event.beatmapset
        assert event.discussion
        event_n += 1
    
    assert event_n == 50

def test_get_reply_events():
    events = get_reply_events(page=1, limit=50)
    
    event_n = 0
    for event in events:
        assert event.user
        assert event.beatmapset
        assert event.discussion
        event_n += 1
    
    assert event_n == 50