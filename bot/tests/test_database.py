import sys
sys.path.append('..')

import pytest
from mysql.connector.errors import IntegrityError

from aiess import Event, User, Beatmapset, Discussion
from aiess.timestamp import from_string
from aiess.database import SCRAPER_TEST_DB_NAME

from bot import database as db_module
from bot.database import Database, BOT_TEST_DB_NAME
from bot.subscriptions import Subscription

@pytest.fixture
def scraper_test_database():
    database = Database(SCRAPER_TEST_DB_NAME)
    # Reset database to state before any tests ran.
    database.clear_table_data("events")
    db_module.clear_cache(SCRAPER_TEST_DB_NAME)
    return database

@pytest.fixture
def bot_test_database():
    database = Database(BOT_TEST_DB_NAME)
    database.clear_table_data("subscriptions")
    db_module.clear_cache(BOT_TEST_DB_NAME)
    return database

def test_correct_bot_db_setup(bot_test_database):
    assert not bot_test_database.retrieve_table_data("subscriptions")
    assert not db_module.beatmapset_event_cache[SCRAPER_TEST_DB_NAME]
    assert not db_module.last_type_cache[SCRAPER_TEST_DB_NAME]

def test_correct_scraper_db_setup(scraper_test_database):
    assert not scraper_test_database.retrieve_table_data("events")
    assert not db_module.beatmapset_event_cache[BOT_TEST_DB_NAME]
    assert not db_module.last_type_cache[BOT_TEST_DB_NAME]

def test_insert_retrieve_channel_sub(bot_test_database):
    sub1 = Subscription(guild_id=3, channel_id=1, _filter="type:problem and state:qualified")
    sub2 = Subscription(guild_id=3, channel_id=2, _filter="type:ranked")

    bot_test_database.insert_subscription(sub1)
    bot_test_database.insert_subscription(sub2)

    retrieved_subs = bot_test_database.retrieve_subscriptions()
    assert next(retrieved_subs, None) == sub1
    assert next(retrieved_subs, None) == sub2
    assert next(retrieved_subs, None) == None

def test_insert_retrieve_channel_sub_no_filter(bot_test_database):
    sub = Subscription(guild_id=1, channel_id=1, _filter=None)

    # A subscription should always have an explicit filter to prevent
    # the creation of an unfiltered subscription unintentionally.
    with pytest.raises(IntegrityError) as err:
        bot_test_database.insert_subscription(sub)
    
    assert "cannot be null" in str(err)

def test_retrieve_beatmapset_events(scraper_test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "creator"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    nom2_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset)
    suggestion_event = Event("suggestion", from_string("2020-01-01 01:00:00"), beatmapset, user=User(3, "somethree"))

    scraper_test_database.insert_event(suggestion_event)
    scraper_test_database.insert_event(nom_event)
    scraper_test_database.insert_event(nom2_event)
    scraper_test_database.insert_event(qual_event)
    
    events = scraper_test_database.retrieve_beatmapset_events(beatmapset)
    qual_event.user = nom2_event.user
    assert nom_event in events
    assert qual_event in events
    assert suggestion_event in events

def test_retrieve_beatmapset_events_cache(scraper_test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "creator"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    nom2_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset)

    scraper_test_database.insert_event(nom_event)
    scraper_test_database.insert_event(nom2_event)
    scraper_test_database.insert_event(qual_event)
    
    scraper_test_database.retrieve_beatmapset_events(beatmapset)
    qual_event.user = nom2_event.user
    assert db_module.beatmapset_event_cache[SCRAPER_TEST_DB_NAME]["3"] == [qual_event, nom_event]

    db_module.clear_cache(SCRAPER_TEST_DB_NAME)
    assert not db_module.beatmapset_event_cache[SCRAPER_TEST_DB_NAME]

def test_retrieve_last_type(scraper_test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")
    discussion = Discussion(7, beatmapset, nominator, "nice")

    praise_event = Event("praise", from_string("2020-01-01 04:56:00"), beatmapset, discussion, user=User(2, "sometwo"))
    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    scraper_test_database.insert_event(praise_event)
    scraper_test_database.insert_event(nom_event)

    retrieved_event = scraper_test_database.retrieve_last_type(nominator, beatmapset, "type = \"praise\"")
    assert retrieved_event == praise_event

def test_retrieve_last_type_cache(scraper_test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")
    discussion = Discussion(7, beatmapset, nominator, "nice")

    praise_event = Event("praise", from_string("2020-01-01 04:56:00"), beatmapset, discussion, user=User(2, "sometwo"))
    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    scraper_test_database.insert_event(praise_event)
    scraper_test_database.insert_event(nom_event)

    scraper_test_database.retrieve_last_type(nominator, beatmapset, "type = \"praise\"")
    assert f"{nominator.id}-{beatmapset.id}-type = \"praise\"" in db_module.last_type_cache[SCRAPER_TEST_DB_NAME]

    db_module.clear_cache(SCRAPER_TEST_DB_NAME)
    assert not db_module.last_type_cache[SCRAPER_TEST_DB_NAME]

def test_retrieve_last_type_none(scraper_test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")

    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    scraper_test_database.insert_event(nom_event)

    retrieved_event = scraper_test_database.retrieve_last_type(nominator, beatmapset, "type = \"praise\"")
    assert not retrieved_event

def test_retrieve_last_type_or_priority(scraper_test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    other_beatmapset = Beatmapset(2, "other artist", "other title", User(5, "other mapper"), ["osu"])
    nominator = User(2, "sometwo")
    discussion = Discussion(7, beatmapset, nominator, "nice")

    praise_event = Event("praise", from_string("2020-01-01 04:50:00"), beatmapset, discussion, user=User(2, "sometwo"))
    hype_event = Event("hype", from_string("2020-01-01 04:56:00"), other_beatmapset, discussion, user=User(2, "sometwo"))
    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    scraper_test_database.insert_event(praise_event)
    scraper_test_database.insert_event(hype_event)
    scraper_test_database.insert_event(nom_event)

    retrieved_event = scraper_test_database.retrieve_last_type(nominator, beatmapset, "type = \"praise\" OR type = \"hype\"")
    assert retrieved_event == praise_event