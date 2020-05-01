import sys
sys.path.append('..')

import pytest

from aiess import timestamp

from scraper.tests.mocks.events import nominate
from scraper.tests.mocks.events.faulty import beatmapset_events
from scraper.parsers.beatmapset_event_parser import beatmapset_event_parser

def test_parse():
    generator = beatmapset_event_parser.parse(beatmapset_events.soup)

    generated_events = []
    for event in generator:
        generated_events.append(event)
    
    assert len(generated_events) == 1  # 1 of 2 events is of a beatmapset that no longer exists.
    assert generated_events[0].type == "nominate"

@pytest.fixture(scope="module")
def beatmapset_event():
    return beatmapset_event_parser.parse_event(nominate.tag)

def test_event_attr(beatmapset_event):
    assert beatmapset_event.time == timestamp.from_string("2019-12-05T12:39:39+00:00")
    assert beatmapset_event.type == "nominate"
    assert beatmapset_event.content == None

def test_user_attr(beatmapset_event):
    assert beatmapset_event.user.id == "1653229"
    assert beatmapset_event.user.name == "_Stan"

def test_beatmapset_attr(beatmapset_event):
    assert beatmapset_event.beatmapset.id == "1013400"
    assert beatmapset_event.beatmapset.artist == "Nekomata Gekidan"
    assert beatmapset_event.beatmapset.title == "AsiaN distractive"
    assert beatmapset_event.beatmapset.creator.id == "6089608"
    assert beatmapset_event.beatmapset.creator.name == "Tofu1222"
    assert beatmapset_event.beatmapset.modes == ["mania"]

def test_discussion_attr(beatmapset_event):
    assert beatmapset_event.discussion == None