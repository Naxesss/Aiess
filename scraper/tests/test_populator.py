import sys
sys.path.append('..')

import pytest
import json

from aiess import Beatmapset, Discussion, User, Event
from aiess.errors import ParsingError
from aiess.tests.mocks.api import beatmap as mock_beatmap
from aiess.tests.mocks.api import old_beatmap as mock_old_beatmap
from aiess.database import Database, SCRAPER_TEST_DB_NAME
from aiess.timestamp import from_string
from aiess import event_types as types

from scraper.populator import get_complete_discussion_info
from scraper.populator import __complete_discussion_context
from scraper.populator import __populate_additional_details

from scraper.tests.mocks.discussion_format_json import JSON as mock_discussion_json

def setup_function():
    database = Database(SCRAPER_TEST_DB_NAME)
    # Reset database to state before any tests ran.
    database.clear_table_data("events")
    database.clear_table_data("discussions")

def test_correct_setup():
    database = Database(SCRAPER_TEST_DB_NAME)
    assert not database.retrieve_table_data("events")
    assert not database.retrieve_table_data("discussions")

def test_old_discussion():
    beatmapset = Beatmapset(41823, beatmapset_json=mock_old_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset)
    
    # Can't obtain any discussion data from a beatmapset that doesn't have a discussion interface.
    with pytest.raises(ParsingError):
        get_complete_discussion_info(discussion, beatmapset, db_name=SCRAPER_TEST_DB_NAME)

def test_discussion():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset)

    # Some information will not be available until it is supplied by other sources
    # (e.g. discussion jsons, prior database entires, scraping)
    discussion = get_complete_discussion_info(discussion, beatmapset, db_name=SCRAPER_TEST_DB_NAME)

    assert discussion.user.id == "4967662"
    assert discussion.user.name == "greenhue"
    assert discussion.content == "since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms."

def test_incomplete_context():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(99, beatmapset)  # Missing user and content.
    
    assert not __complete_discussion_context(discussion, db_name=SCRAPER_TEST_DB_NAME)

def test_complete_context():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(99, beatmapset, user=User(1, "someone"), content="hello there")
    incomplete_discussion = Discussion(99, beatmapset)
    
    Database(SCRAPER_TEST_DB_NAME).insert_discussion(discussion)

    assert __complete_discussion_context(incomplete_discussion, db_name=SCRAPER_TEST_DB_NAME)
    assert incomplete_discussion.user
    assert incomplete_discussion.content

def test_delete_incomplete_context():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(99, beatmapset)  # Missing user and content.
    event = Event("test", from_string("2020-01-01 00:00:00"), discussion=discussion)
    
    __populate_additional_details(event, "", db_name=SCRAPER_TEST_DB_NAME)
    assert event.marked_for_deletion

def test_additional_details_dq():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(
        1234956, beatmapset, user=User(4967662, "greenhue"),
        content="since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms."
    )

    dq_event = Event(types.DISQUALIFY, from_string("2019-10-27T04:23:20+00:00"), beatmapset, discussion)
    
    discussion_json = json.loads(mock_discussion_json)
    __populate_additional_details(dq_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert dq_event.content == dq_event.discussion.content

def test_additional_details_resolve():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(
        1234956, beatmapset, user=User(4967662, "greenhue"),
        content="since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms."
    )

    resolve_event = Event(types.RESOLVE, from_string("2019-10-27T09:00:00+00:00"), beatmapset, discussion)
    
    discussion_json = json.loads(mock_discussion_json)
    __populate_additional_details(resolve_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert resolve_event.user == User(7342798, "_Epreus")

def test_additional_details_kudosu():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(
        1182017, beatmapset, user=User(9590557, "Firika"),
        content="00:08:232 (5) - need fix too ;-;"
    )

    kudosu_event = Event(types.KUDOSU_GAIN, from_string("2019-10-04T11:50:40+00:00"), beatmapset, discussion)
    
    discussion_json = json.loads(mock_discussion_json)
    __populate_additional_details(kudosu_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert kudosu_event.user == User(7342798, "_Epreus")