import sys
sys.path.append('..')

import pytest
from unittest import mock
import json

from aiess import Event, User, Usergroup
from aiess.common import anext
from aiess.timestamp import from_string

from scraper.tests.mocks.requester import get_discussion_events
from scraper.tests.mocks.requester import get_reply_events
from scraper.tests.mocks.requester import get_beatmapset_events
from scraper.tests.mocks.requester import get_news_events
from scraper.tests.mocks.discussion_jsons.crawler_json import JSON as mock_discussion_json

from scraper.crawler import get_news_between
from scraper.crawler import get_group_events_between
from scraper.crawler import __get_discussion_events_between
from scraper.crawler import __get_reply_events_between
from scraper.crawler import __get_beatmapset_events_between

def mock_get_discussions_json(beatmapset_id: int) -> object:
    return json.loads(mock_discussion_json)

@pytest.mark.asyncio
async def test_get_news_between():
    with mock.patch("scraper.crawler.get_news_events", side_effect=get_news_events):
        generator = get_news_between(start_time=from_string("2020-01-01 03:00:00"), end_time=from_string("2020-01-01 00:00:00"))
        event5 = await anext(generator, None)
        event4 = await anext(generator, None)
        event3 = await anext(generator, None)
        event2 = await anext(generator, None)
        event1 = await anext(generator, None)  # Should skip this since it was covered last iteration.

    assert event5.user.name == "sometwo"
    assert event4.user.name == "someone"
    assert event3.user.name == "somefour"
    assert event2.user.name == "somethree"
    assert event1 is None

@pytest.mark.asyncio
async def test_get_news_between_far_back():
    with mock.patch("scraper.crawler.get_news_events", side_effect=get_news_events):
        generator = get_news_between(start_time=from_string("2020-01-01 03:00:00"), end_time=from_string("2019-12-01 00:00:00"))
        await anext(generator, None)
        await anext(generator, None)
        await anext(generator, None)
        await anext(generator, None)
        event2 = await anext(generator, None)
        event1 = await anext(generator, None)  # This is the part where no more newsposts generate.

    assert event2 is not None
    assert event1 is None

@pytest.mark.asyncio
async def test_get_group_events_between():
    group_events = [
        Event(_type="add", time=from_string("2020-01-01 00:00:00"), user=User(1, "someone"), group=Usergroup(4)),
        Event(_type="add", time=from_string("2020-01-01 00:00:00"), user=User(2, "sometwo"), group=Usergroup(7)),
        Event(_type="remove", time=from_string("2020-01-01 00:00:00"), user=User(1, "someone"), group=Usergroup(4))
    ]
    with mock.patch("scraper.crawler.get_group_events", return_value=group_events) as mock_get_group_events:
        generator = get_group_events_between(start_time=from_string("2020-01-01 03:00:00"), end_time=from_string("2020-01-01 00:00:00"))
        event4 = await anext(generator, None)
        event3 = await anext(generator, None)
        event2 = await anext(generator, None)
        event1 = await anext(generator, None)

        mock_get_group_events.assert_called_with(_from=from_string("2020-01-01 00:00:00"))

    assert event4.user.name == "someone"
    assert event4.type == "add"
    assert event3.user.name == "sometwo"
    assert event3.type == "add"
    assert event2.user.name == "someone"
    assert event2.type == "remove"
    assert event1 is None

@pytest.mark.asyncio
async def test_get_discussion_events_between():
    with mock.patch("scraper.crawler.get_discussion_events", side_effect=get_discussion_events):
        with mock.patch("scraper.populator.get_discussions_json", side_effect=mock_get_discussions_json):
            generator = __get_discussion_events_between(start_time=from_string("2020-01-01 03:00:00"), end_time=from_string("2020-01-01 00:00:00"))
            await anext(generator, None)
            event3 = await anext(generator, None)
            event2 = await anext(generator, None)
            # at 00:00:00, which is not > 00:00:00, hence skipped, the next call should start from 00:00:00 catching this.
            event1 = await anext(generator, None)

    assert event1.type == "issue_resolve"
    assert event1.user.name == "someone"
    assert event2.beatmapset.title == "title"
    assert event3.type == "hype"

@pytest.mark.asyncio
async def test_get_reply_events_between():
    with mock.patch("scraper.crawler.get_reply_events", side_effect=get_reply_events):
        with mock.patch("scraper.populator.get_discussions_json", side_effect=mock_get_discussions_json):
            generator = __get_reply_events_between(start_time=from_string("2020-01-03 00:00:00"), end_time=from_string("2019-12-28 00:00:00"))
            event5 = await anext(generator, None)
            event4 = await anext(generator, None)
            event3 = await anext(generator, None)
            event2 = await anext(generator, None)
            event1 = await anext(generator, None)

    assert event1.type == "reply"
    assert event1.beatmapset.artist == "artist"
    assert event2.content == "yes?"
    assert event3.user.name == "sometwo"
    assert event4.user.name == "someone"
    assert event5.content == "thanks"

@pytest.mark.asyncio
async def test_get_beatmapset_events_between():
    with mock.patch("scraper.crawler.get_beatmapset_events", side_effect=get_beatmapset_events):
        with mock.patch("scraper.populator.get_discussions_json", side_effect=mock_get_discussions_json):
            generator = __get_beatmapset_events_between(start_time=from_string("2020-01-03 00:00:00"), end_time=from_string("2020-01-01 00:00:00"))
            event1 = await anext(generator, None)
            event2 = await anext(generator, None)
            event3 = await anext(generator, None)
            event4 = await anext(generator, None)

    assert event1.type == "disqualify"
    assert event1.user.name == "sometwo"
    assert event1.content == "no wait"
    assert event2.type == "qualify"
    assert event2.user is None
    assert event3.type == "nominate"
    assert event3.user.name == "sometwo"
    assert event3.content == "hype"
    assert event4.type == "nominate"
    assert event4.content is None

@pytest.mark.asyncio
async def test_get_beatmapset_events_between_far_back():
    with mock.patch("scraper.crawler.get_beatmapset_events", side_effect=get_beatmapset_events):
        with mock.patch("scraper.populator.get_discussions_json", side_effect=mock_get_discussions_json):
            generator = __get_beatmapset_events_between(start_time=from_string("2020-01-03 00:00:00"), end_time=from_string("2019-12-01 00:00:00"))
            await anext(generator, None)
            await anext(generator, None)
            await anext(generator, None)
            event2 = await anext(generator, None)
            event1 = await anext(generator, None)  # This is the part where we have no more events available to us.

    assert event2 is not None
    assert event1 is None