import sys
sys.path.append('..')

import mock
from datetime import datetime, timedelta

from aiess.database import Database, SCRAPER_TEST_DB_NAME
from aiess import event_types as types

from scraper.requester import get_news_events
from scraper.requester import get_group_events
from scraper.requester import get_beatmapset_events
from scraper.requester import get_discussion_events
from scraper.requester import get_reply_events

def test_get_group_events():
    Database(SCRAPER_TEST_DB_NAME).clear_table_data("group_users")

    with mock.patch("scraper.parsers.group_parser.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME):
        events = get_group_events(_from=datetime.utcnow())

        event_n = 0
        for event in events:
            assert event.type == types.ADD
            assert event.user
            assert event.group
            event_n += 1
    
    assert event_n > 100

def test_get_news_events():
    events = get_news_events(_from=datetime.utcnow(), limit=20)
    
    event_n = 0
    for event in events:
        assert event.type == types.NEWS
        assert event.newspost
        assert event.newspost.title
        assert event.newspost.preview
        assert event.newspost.image_url
        assert event.newspost.author
        assert event.newspost.slug
        event_n += 1
    
    assert event_n == 20

def test_get_beatmapset_events():
    events = get_beatmapset_events(page=1, limit=50)

    event_n = 0
    for event in events:
        assert event.beatmapset
        event_n += 1
    
    assert event_n >= 45  # Leniency in case a beatmapset was deleted.

def test_get_discussion_events():
    events = get_discussion_events(page=1, limit=50)
    
    event_n = 0
    for event in events:
        assert event.beatmapset
        assert event.discussion
        event_n += 1
    
    assert event_n >= 45  # Leniency in case a discussion was deleted.

def test_get_reply_events():
    events = get_reply_events(page=1, limit=50)
    
    event_n = 0
    for event in events:
        assert event.type == types.REPLY
        assert event.user
        assert event.beatmapset
        assert event.discussion
        event_n += 1
    
    assert event_n >= 45  # Leniency in case a reply was deleted.