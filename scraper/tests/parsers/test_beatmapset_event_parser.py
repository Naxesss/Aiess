import sys
sys.path.append('..')

import pytest

from aiess import timestamp

from scraper.requester import soupify

from scraper.tests.mocks.events.faulty import beatmapset_events as mock_beatmapset_events
from scraper.tests.mocks import events_json as mock_events_json
from scraper.tests.mocks import events_json_nominate as mock_events_nominate_json
from scraper.tests.mocks import events_json_deleted_mapset as mock_events_json_deleted_mapset
from scraper.tests.mocks import events_json_lang_genre as mock_events_lang_genre_json

from scraper.parsers.beatmapset_event_parser import beatmapset_event_parser

def test_parse_no_json():
    generated_events = []
    with pytest.raises(ValueError) as err:
        for event in beatmapset_event_parser.parse(soupify("")):
            generated_events.append(event)
    
    assert len(generated_events) == 0
    assert "Missing either json-events or json-users" in str(err)

def test_parse_json():
    generated_events = []
    for event in beatmapset_event_parser.parse(mock_events_json.soup):
        generated_events.append(event)
    
    assert len(generated_events) == 5
    assert generated_events[0].type == "kudosu_gain"
    assert generated_events[0].beatmapset.id == 534054
    assert generated_events[0].beatmapset.creator.name == "SkyFlame"
    assert generated_events[4].type == "issue_resolve"

def test_parse_json_deleted_beatmapset():
    generated_events = []
    for event in beatmapset_event_parser.parse(mock_events_json_deleted_mapset.soup):
        generated_events.append(event)
    
    assert not generated_events

def test_parse_nominate_json():
    generated_events = []
    for event in beatmapset_event_parser.parse(mock_events_nominate_json.soup):
        generated_events.append(event)
    
    assert len(generated_events) == 1
    assert generated_events[0].type == "nominate"
    assert generated_events[0].user.id == 33599
    assert generated_events[0].beatmapset.id == 1164305
    assert generated_events[0].beatmapset.creator.name == "kunka"

def test_parse_lang_genre_json():
    generated_events = []
    for event in beatmapset_event_parser.parse(mock_events_lang_genre_json.soup):
        generated_events.append(event)
    
    assert len(generated_events) == 2
    assert generated_events[0].type == "language_edit"
    assert generated_events[0].user.id == 10660777
    assert generated_events[0].content == "Unspecified -> Instrumental"
    assert generated_events[1].type == "genre_edit"
    assert generated_events[1].content == "Unspecified -> Electronic"