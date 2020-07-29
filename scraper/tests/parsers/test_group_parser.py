import sys
sys.path.append('..')

import mock
from datetime import datetime

from aiess import Event, User, Usergroup
from aiess.timestamp import from_string
from aiess.database import Database, SCRAPER_TEST_DB_NAME

from scraper.tests.mocks import groups as mock_groups
from scraper.parsers import group_parser

def setup_function():
    Database(SCRAPER_TEST_DB_NAME).clear_table_data("group_users")

def test_parse_timing():
    # Test both additions and removals.
    Database(SCRAPER_TEST_DB_NAME).insert_group_user(group=Usergroup(7), user=User(1, "one"))
    Database(SCRAPER_TEST_DB_NAME).insert_group_user(group=Usergroup(7), user=User(2, "two"))
    Database(SCRAPER_TEST_DB_NAME).insert_group_user(group=Usergroup(7), user=User(3, "three"))
    Database(SCRAPER_TEST_DB_NAME).insert_group_user(group=Usergroup(7), user=User(4, "four"))
    Database(SCRAPER_TEST_DB_NAME).insert_group_user(group=Usergroup(7), user=User(5, "five"))

    start_time = datetime.utcnow()

    events = []
    with mock.patch("scraper.parsers.group_parser.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME):
        for event in group_parser.parse(group_id=7, group_page=mock_groups.soup, last_checked_at=from_string("2020-07-22T21:00:00+00:00")):
            events.append(event)

    end_time = datetime.utcnow()
    # We should not be using the api to fill in user names and such, as this data is available within the users json.
    assert (end_time - start_time).total_seconds() < 3

def test_parse_additions():
    events = []
    with mock.patch("scraper.parsers.group_parser.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME):
        for event in group_parser.parse(group_id=7, group_page=mock_groups.soup, last_checked_at=from_string("2020-07-22T21:00:00+00:00")):
            events.append(event)

    assert len(events) == 17
    assert events[0] == Event(
        _type = "add",
        time  = from_string("2020-07-22T21:00:00+00:00"),
        group = Usergroup(7),
        user  = User(_id=2202163)
    )
    assert events[1] == Event(
        _type = "add",
        time  = from_string("2020-07-22T21:00:00+00:00"),
        group = Usergroup(7),
        user  = User(_id=3621552)
    )

def test_parse_removals():
    Database(SCRAPER_TEST_DB_NAME).insert_group_user(group=Usergroup(7), user=User(1, "someone"))

    events = []
    with mock.patch("scraper.parsers.group_parser.SCRAPER_DB_NAME", SCRAPER_TEST_DB_NAME):
        for event in group_parser.parse(group_id=7, group_page=mock_groups.soup, last_checked_at=from_string("2020-07-22T21:00:00+00:00")):
            events.append(event)

    assert len(events) == 18
    assert events[0] == Event(
        _type = "remove",
        time  = from_string("2020-07-22T21:00:00+00:00"),
        group = Usergroup(7),
        user  = User(_id=1, name="someone")
    )