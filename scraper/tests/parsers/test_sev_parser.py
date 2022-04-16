import sys
sys.path.append('..')

import pytest
import mock
from datetime import datetime

from aiess import Event, User, Discussion, Beatmapset
from aiess.timestamp import from_string
from aiess.database import Database, SCRAPER_TEST_DB_NAME
from aiess.errors import DeletedContextError

from scraper.parsers import sev_parser

def test_parse():
    with mock.patch("scraper.parsers.sev_parser.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME):
        user = User(_id=1, allow_api=False)
        beatmapset = Beatmapset(_id=2, creator=user, allow_api=False)
        discussion = Discussion(_id=4, beatmapset=beatmapset, user=user, content="123")
        Database(SCRAPER_TEST_DB_NAME).insert_discussion(discussion)

        event = sev_parser.parse(discussion_id=4, obv=1, sev=0, time=from_string("2020-07-22T21:00:00+00:00"))

    expected_event = Event(
        _type = "sev",
        time  = from_string("2020-07-22T21:00:00+00:00"),
        beatmapset = beatmapset,
        discussion = discussion,
        content = "1/0"
    )

    assert event.type == expected_event.type
    assert event.time == expected_event.time
    assert event.beatmapset == expected_event.beatmapset
    assert event.discussion == expected_event.discussion
    assert event.content == expected_event.content
    assert event == expected_event

def test_parse_one_unchanged():
    with mock.patch("scraper.parsers.sev_parser.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME):
        user = User(_id=1, allow_api=False)
        beatmapset = Beatmapset(_id=2, creator=user, allow_api=False)
        discussion = Discussion(_id=5, beatmapset=beatmapset, user=user, content="123")
        Database(SCRAPER_TEST_DB_NAME).insert_discussion(discussion)

        event = sev_parser.parse(discussion_id=5, obv=0, sev=None, time=from_string("2020-07-22T21:00:00+00:00"))

    expected_event = Event(
        _type = "sev",
        time  = from_string("2020-07-22T21:00:00+00:00"),
        beatmapset = beatmapset,
        discussion = discussion,
        content = "0/?"
    )

    assert event.type == expected_event.type
    assert event.time == expected_event.time
    assert event.beatmapset == expected_event.beatmapset
    assert event.discussion == expected_event.discussion
    assert event.content == expected_event.content
    assert event == expected_event

def test_parse_fetch_unchanged():
    with mock.patch("scraper.parsers.sev_parser.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME):
        user = User(_id=1, allow_api=False)
        beatmapset = Beatmapset(_id=2, creator=user, allow_api=False)
        discussion = Discussion(_id=4, beatmapset=beatmapset, user=user, content="123")
        Database(SCRAPER_TEST_DB_NAME).insert_discussion(discussion)
        Database(SCRAPER_TEST_DB_NAME).insert_obv_sev(discussion, obv=1, sev=2)

        # This event basically does: 1/2 -> 0/2
        event = sev_parser.parse(discussion_id=4, obv=0, sev=None, time=from_string("2020-07-22T21:00:00+00:00"))

    expected_event = Event(
        _type = "sev",
        time  = from_string("2020-07-22T21:00:00+00:00"),
        beatmapset = beatmapset,
        discussion = discussion,
        content = "0/2"
    )

    assert event.type == expected_event.type
    assert event.time == expected_event.time
    assert event.beatmapset == expected_event.beatmapset
    assert event.discussion == expected_event.discussion
    assert event.content == expected_event.content
    assert event == expected_event

def test_parse_both_unchanged():
    with mock.patch("scraper.parsers.sev_parser.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME):
        user = User(_id=1, allow_api=False)
        beatmapset = Beatmapset(_id=2, creator=user, allow_api=False)
        discussion = Discussion(_id=4, beatmapset=beatmapset, user=user, content="123")
        Database(SCRAPER_TEST_DB_NAME).insert_discussion(discussion)
        Database(SCRAPER_TEST_DB_NAME).insert_obv_sev(discussion, obv=1, sev=2)

        #with pytest.raises(DeletedContextError) as err1:
        #    sev_parser.parse(discussion_id=4, obv=1, sev=2, time=from_string("2020-07-22T21:00:00+00:00"))
        #assert "changed back" in str(err1).lower()

        with pytest.raises(DeletedContextError) as err2:
            sev_parser.parse(discussion_id=4, obv=None, sev=None, time=from_string("2020-07-22T21:00:00+00:00"))
        assert "neither severity nor obviousness have been set" in str(err2).lower()