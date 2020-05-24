import sys
sys.path.append('..')

import pytest

from aiess import timestamp

from scraper.requester import soupify

from scraper.tests.mocks.events import nominate as mock_nominate
from scraper.tests.mocks.events.faulty import beatmapset_events as mock_beatmapset_events
from scraper.tests.mocks import events_json as mock_events_json

from scraper.parsers.beatmapset_event_parser import beatmapset_event_parser

def test_parse():
    generated_events = []
    for event in beatmapset_event_parser.parse(mock_beatmapset_events.soup):
        generated_events.append(event)
    
    assert len(generated_events) == 1  # 1 of 2 events is of a beatmapset that no longer exists.
    assert generated_events[0].type == "nominate"

def test_parse_no_json_or_tags():
    generated_events = []
    with pytest.raises(ValueError) as err:
        for event in beatmapset_event_parser.parse(soupify("")):
            generated_events.append(event)
    
    assert len(generated_events) == 0
    assert "json" in str(err) and "HTML" in str(err)

def test_parse_prefer_json():
    combined_soup = soupify(f"""
        {mock_nominate.HTML}
        {mock_events_json.HTML}
    """)

    generated_events = []
    for event in beatmapset_event_parser.parse(combined_soup):
        generated_events.append(event)
    
    # For this test, the json has 5 events and the HTML has 1.
    assert len(generated_events) == 5

def test_parse_json():
    generated_events = []
    for event in beatmapset_event_parser.parse(mock_events_json.soup):
        generated_events.append(event)
    
    assert len(generated_events) == 5
    assert generated_events[0].type == "kudosu-gain"
    assert generated_events[0].beatmapset.id == "534054"
    assert generated_events[0].beatmapset.creator.name == "SkyFlame"
    assert generated_events[4].type == "issue-resolve"

@pytest.fixture(scope="module")
def beatmapset_event():
    return beatmapset_event_parser.parse_event(mock_nominate.tag)

def test_event_attr(beatmapset_event):
    assert beatmapset_event.time == timestamp.from_string("2019-12-05T12:39:39+00:00")
    assert beatmapset_event.type == "nominate"
    assert beatmapset_event.content is None

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
    assert beatmapset_event.discussion is None