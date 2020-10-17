import sys
sys.path.append('..')

import pytest
import mock
import json
from datetime import datetime

from aiess import Beatmapset, Discussion, User, Event, Usergroup
from aiess.errors import ParsingError
from aiess.tests.mocks.api import beatmap as mock_beatmap
from aiess.tests.mocks.api import old_beatmap as mock_old_beatmap
from aiess.database import Database, SCRAPER_TEST_DB_NAME
from aiess.timestamp import from_string
from aiess import event_types as types

from scraper.populator import get_complete_discussion_info
from scraper.populator import __complete_discussion_context
from scraper.populator import __populate_additional_details
from scraper.populator import populate_from_bnsite
from scraper.populator import get_group_bnsite_comment

from scraper.tests.mocks.discussion_jsons.additional_details import JSON as mock_discussion_json
from scraper.tests.mocks.discussion_jsons.nomination_comment import JSON1 as mock_discussion_json_nom_comment_1
from scraper.tests.mocks.discussion_jsons.nomination_comment import JSON2 as mock_discussion_json_nom_comment_2

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

    assert discussion.user.id == 4967662
    assert discussion.user.name == "greenhue"
    assert discussion.content == "since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms."
    assert discussion.tab == "generalAll"

def test_incomplete_context():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(99, beatmapset)  # Missing user, content, tab, and difficulty.
    
    assert not __complete_discussion_context(discussion, db_name=SCRAPER_TEST_DB_NAME)

def test_incomplete_context_from_db():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(99, beatmapset, user=User(1, "someone"), content="hello there")  # Missing tab and difficulty.
    incomplete_discussion = Discussion(99, beatmapset)
    
    Database(SCRAPER_TEST_DB_NAME).insert_discussion(discussion)

    assert not __complete_discussion_context(incomplete_discussion, db_name=SCRAPER_TEST_DB_NAME)

def test_complete_context():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(99, beatmapset, user=User(1, "someone"), content="hello there", tab="tab", difficulty="diff")
    incomplete_discussion = Discussion(99, beatmapset)
    
    Database(SCRAPER_TEST_DB_NAME).insert_discussion(discussion)

    assert __complete_discussion_context(incomplete_discussion, db_name=SCRAPER_TEST_DB_NAME)
    assert incomplete_discussion.user
    assert incomplete_discussion.content
    assert incomplete_discussion.tab
    assert incomplete_discussion.difficulty

@pytest.mark.asyncio
async def test_delete_incomplete_context():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(99, beatmapset)  # Missing user and content.
    event = Event("test", from_string("2020-01-01 00:00:00"), discussion=discussion)
    
    # The discussions json should not be checked, so we simply set it as None.
    await __populate_additional_details(event, discussions_json=None, db_name=SCRAPER_TEST_DB_NAME)
    assert event.marked_for_deletion

@pytest.mark.asyncio
async def test_additional_details_dq():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(
        1234956, beatmapset, user=User(4967662, "greenhue"),
        content="since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms.",
        tab="tab", difficulty="diff"
    )

    dq_event = Event(types.DISQUALIFY, from_string("2019-10-27T04:23:20+00:00"), beatmapset, discussion)
    
    discussion_json = json.loads(mock_discussion_json)
    await __populate_additional_details(dq_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert dq_event.content == dq_event.discussion.content

@pytest.mark.asyncio
async def test_additional_details_resolve():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(
        1234956, beatmapset, user=User(4967662, "greenhue"),
        content="since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms.",
        tab="tab", difficulty="diff"
    )

    resolve_event = Event(types.RESOLVE, from_string("2019-10-27T09:00:00+00:00"), beatmapset, discussion)
    
    discussion_json = json.loads(mock_discussion_json)
    await __populate_additional_details(resolve_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert resolve_event.user == User(7342798, "_Epreus")

@pytest.mark.asyncio
async def test_additional_details_kudosu():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(
        1182017, beatmapset, user=User(9590557, "Firika"),
        content="00:08:232 (5) - need fix too ;-;",
        tab="tab", difficulty="diff"
    )

    kudosu_event = Event(types.KUDOSU_GAIN, from_string("2019-10-04T11:50:40+00:00"), beatmapset, discussion)
    
    discussion_json = json.loads(mock_discussion_json)
    await __populate_additional_details(kudosu_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert kudosu_event.user == User(7342798, "_Epreus")

@pytest.mark.asyncio
async def test_nom_comment_from_hype():
    beatmapset = Beatmapset(1112303, artist="Fox Stevenson", title="Take You Down", creator=User(5745865, "Altai"), modes=["osu"], genre="g", language="l")
    nominate_event = Event(types.NOMINATE, from_string("2020-07-01T20:48:57+00:00"), beatmapset, user=User(2204515, "Mao"))
    
    discussion_json = json.loads(mock_discussion_json_nom_comment_1)
    await __populate_additional_details(nominate_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert nominate_event.content == "<3"

@pytest.mark.asyncio
async def test_nom_comment_none():
    beatmapset = Beatmapset(1112303, artist="Fox Stevenson", title="Take You Down", creator=User(5745865, "Altai"), modes=["osu"], genre="g", language="l")
    nominate_event = Event(types.NOMINATE, from_string("2020-07-01T20:48:47+00:00"), beatmapset, user=User(8623835, "Peter"))
    
    discussion_json = json.loads(mock_discussion_json_nom_comment_1)
    await __populate_additional_details(nominate_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert nominate_event.content is None

@pytest.mark.asyncio
async def test_nom_comment_from_note():
    beatmapset = Beatmapset(1147354, artist="Jashin-chan (CV: Suzuki Aina)", title="Jinbouchou Aika", creator=User(9590557, "Firika"), modes=["osu"], genre="g", language="l")
    nominate_event = Event(types.NOMINATE, from_string("2020-07-03T12:14:13+00:00"), beatmapset, user=User(5312547, "Lafayla"))
    
    discussion_json = json.loads(mock_discussion_json_nom_comment_2)
    await __populate_additional_details(nominate_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert nominate_event.content == "02:31:783 - 02:34:783 - should be fine being snapped to 1/16, the piano does weird pick ups for these, same thing applies to  09:51:845 - i don't think its problematic"

@pytest.mark.asyncio
async def test_nom_comment_praise_then_suggestions():
    beatmapset = Beatmapset(1147354, artist="Jashin-chan (CV: Suzuki Aina)", title="Jinbouchou Aika", creator=User(9590557, "Firika"), modes=["osu"], genre="g", language="l")
    nominate_event = Event(types.NOMINATE, from_string("2020-07-03T12:14:13+00:00"), beatmapset, user=User(896613, "Lasse"))
    
    discussion_json = json.loads(mock_discussion_json_nom_comment_2)
    await __populate_additional_details(nominate_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert nominate_event.content is None

@pytest.mark.asyncio
async def test_nom_comment_from_praise():
    beatmapset = Beatmapset(1147354, artist="Jashin-chan (CV: Suzuki Aina)", title="Jinbouchou Aika", creator=User(9590557, "Firika"), modes=["osu"], genre="g", language="l")
    nominate_event = Event(types.NOMINATE, from_string("2020-07-03T12:14:13+00:00"), beatmapset, user=User(4, "mock user"))
    
    discussion_json = json.loads(mock_discussion_json_nom_comment_2)
    await __populate_additional_details(nominate_event, discussion_json, db_name=SCRAPER_TEST_DB_NAME)

    assert nominate_event.content == "nice"



@pytest.fixture
def group_event():
    return Event("remove", from_string("2020-01-01 00:00:00"), user=User(2, "sometwo"), group=Usergroup(32))

@pytest.mark.asyncio
async def test_populate_from_bnsite(group_event):
    with mock.patch("scraper.populator.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = from_string("2020-01-01 00:01:00")
        mock_datetime.side_effect = datetime

        with mock.patch("scraper.populator.bnsite_api") as mock_bnsite_api:
            mock_bnsite_api.request_removal_reason.return_value = {
                "action": "Resigned",
                "timestamp": "2020-01-01 00:00:00"
            }
            
            await populate_from_bnsite(group_event)

            assert group_event.content == "Resigned"

def test_get_group_nat_comment(group_event):
    with mock.patch("scraper.populator.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = from_string("2020-01-01 00:01:00")
        mock_datetime.side_effect = datetime

        with mock.patch("scraper.populator.bnsite_api") as mock_bnsite_api:
            mock_bnsite_api.request_removal_reason.return_value = {
                "action": "Resigned",
                "timestamp": "2020-01-01 00:00:00"
            }

            assert get_group_bnsite_comment(group_event) == "Resigned"

def test_get_group_nat_comment_wrong_group(group_event):
    group_event.group = Usergroup(4, "Global Moderation Team")
    with mock.patch("scraper.populator.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = from_string("2020-03-08 00:01:00")
        mock_datetime.side_effect = datetime

        with mock.patch("scraper.populator.bnsite_api") as mock_bnsite_api:
            mock_bnsite_api.request_removal_reason.return_value = {
                "action": "Resigned",
                "timestamp": "2020-01-01 00:00:00"
            }

            assert get_group_bnsite_comment(group_event) == None

def test_get_group_nat_comment_added(group_event):
    group_event.type = "add"
    with mock.patch("scraper.populator.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = from_string("2020-03-08 00:01:00")
        mock_datetime.side_effect = datetime

        with mock.patch("scraper.populator.bnsite_api") as mock_bnsite_api:
            mock_bnsite_api.request_removal_reason.return_value = {
                "action": "Resigned",
                "timestamp": "2020-01-01 00:00:00"
            }

            assert get_group_bnsite_comment(group_event) == None

def test_get_group_nat_comment_old(group_event):
    with mock.patch("scraper.populator.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = from_string("2020-03-08 00:01:00")
        mock_datetime.side_effect = datetime

        with mock.patch("scraper.populator.bnsite_api") as mock_bnsite_api:
            mock_bnsite_api.request_removal_reason.return_value = {
                "action": "Resigned",
                "timestamp": "2020-01-01 00:00:00"
            }

            assert get_group_bnsite_comment(group_event) == None

def test_get_group_nat_comment_missing_timestamp(group_event):
    with mock.patch("scraper.populator.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = from_string("2020-01-01 00:01:00")
        mock_datetime.side_effect = datetime

        with mock.patch("scraper.populator.bnsite_api") as mock_bnsite_api:
            mock_bnsite_api.request_removal_reason.return_value = {
                "action": "Resigned"
            }

            # Make the assumption that it's too old.
            assert get_group_bnsite_comment(group_event) == None

def test_get_group_nat_comment_empty_json(group_event):
    with mock.patch("scraper.populator.datetime") as mock_datetime:
        mock_datetime.utcnow.return_value = from_string("2020-01-01 00:01:00")
        mock_datetime.side_effect = datetime

        with mock.patch("scraper.populator.bnsite_api") as mock_bnsite_api:
            mock_bnsite_api.request_removal_reason.return_value = {}

            assert get_group_bnsite_comment(group_event) == None