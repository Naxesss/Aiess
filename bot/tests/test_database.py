import sys
sys.path.append('..')

import pytest

from aiess import Event, User, Beatmapset
from aiess.timestamp import from_string
from aiess.database import SCRAPER_TEST_DB_NAME

from bot import database as db_module
from bot.database import Database, BOT_TEST_DB_NAME
from bot.objects import Subscription, Prefix

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
    database.clear_table_data("prefixes")
    db_module.clear_cache(BOT_TEST_DB_NAME)
    return database

def test_correct_bot_db_setup(bot_test_database):
    assert not bot_test_database.retrieve_table_data("subscriptions")
    assert not bot_test_database.retrieve_table_data("prefixes")
    assert not db_module.beatmapset_event_cache[SCRAPER_TEST_DB_NAME]

def test_correct_scraper_db_setup(scraper_test_database):
    assert not scraper_test_database.retrieve_table_data("events")
    assert not db_module.beatmapset_event_cache[BOT_TEST_DB_NAME]

def test_insert_retrieve_channel_sub(bot_test_database):
    sub1 = Subscription(guild_id=3, channel_id=1, _filter="type:problem and state:qualified")
    sub2 = Subscription(guild_id=3, channel_id=2, _filter="type:ranked")

    bot_test_database.insert_subscription(sub1)
    bot_test_database.insert_subscription(sub2)

    retrieved_sub = bot_test_database.retrieve_subscription("guild_id=%s AND channel_id=%s", (3, 1))
    assert retrieved_sub == sub1

def test_insert_retrieve_channel_subs(bot_test_database):
    sub1 = Subscription(guild_id=3, channel_id=1, _filter="type:problem and state:qualified")
    sub2 = Subscription(guild_id=3, channel_id=2, _filter="type:ranked")

    bot_test_database.insert_subscription(sub1)
    bot_test_database.insert_subscription(sub2)

    retrieved_subs = bot_test_database.retrieve_subscriptions()
    assert next(retrieved_subs, None) == sub1
    assert next(retrieved_subs, None) == sub2
    assert next(retrieved_subs, None) is None

def test_insert_retrieve_channel_sub_no_filter(bot_test_database):
    sub = Subscription(guild_id=1, channel_id=1, _filter=None)

    # A subscription should always have an explicit filter to prevent
    # the creation of an unfiltered subscription unintentionally.
    with pytest.raises(ValueError) as err:
        bot_test_database.insert_subscription(sub)
    
    assert "filter cannot be falsy" in str(err).lower()

def test_insert_retrieve_prefix(bot_test_database):
    prefix1 = Prefix(guild_id=3, prefix="&")
    prefix2 = Prefix(guild_id=4, prefix="%")

    bot_test_database.insert_prefix(prefix1)
    bot_test_database.insert_prefix(prefix2)

    retrieved_prefix = bot_test_database.retrieve_prefix("guild_id=%s", (3,))
    assert retrieved_prefix == prefix1

def test_insert_retrieve_prefixes(bot_test_database):
    prefix1 = Prefix(guild_id=3, prefix="&")
    prefix2 = Prefix(guild_id=4, prefix="%")

    bot_test_database.insert_prefix(prefix1)
    bot_test_database.insert_prefix(prefix2)

    retrieved_prefixes = bot_test_database.retrieve_prefixes()
    assert next(retrieved_prefixes, None) == prefix1
    assert next(retrieved_prefixes, None) == prefix2
    assert next(retrieved_prefixes, None) is None

@pytest.mark.asyncio
async def test_retrieve_beatmapset_events(scraper_test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "creator"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    nom2_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset)
    suggestion_event = Event("suggestion", from_string("2020-01-01 01:00:00"), beatmapset, user=User(3, "somethree"))

    scraper_test_database.insert_event(suggestion_event)
    scraper_test_database.insert_event(nom_event)
    scraper_test_database.insert_event(nom2_event)
    scraper_test_database.insert_event(qual_event)
    
    events = await scraper_test_database.retrieve_beatmapset_events(beatmapset)
    qual_event.user = nom2_event.user
    assert nom_event in events
    assert qual_event in events
    assert suggestion_event in events

@pytest.mark.asyncio
async def test_retrieve_beatmapset_events_cache(scraper_test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "creator"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    nom2_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset)

    scraper_test_database.insert_event(nom_event)
    scraper_test_database.insert_event(nom2_event)
    scraper_test_database.insert_event(qual_event)
    
    await scraper_test_database.retrieve_beatmapset_events(beatmapset)
    qual_event.user = nom2_event.user
    assert db_module.beatmapset_event_cache[SCRAPER_TEST_DB_NAME][3] == [qual_event, nom_event]

    db_module.clear_cache(SCRAPER_TEST_DB_NAME)
    assert not db_module.beatmapset_event_cache[SCRAPER_TEST_DB_NAME]