import pytest
from mysql.connector.errors import IntegrityError

from aiess import Event, User, Beatmapset, Discussion
from aiess.timestamp import from_string

from database import Database
from subscriptions import Subscription

@pytest.fixture
def test_database():
    database = Database("aiess_test")
    # Reset database to state before any tests ran.
    database.clear_table_data("events")
    return database

@pytest.fixture
def test_bot_database():
    database = Database("aiess_bot_test")
    database.clear_table_data("subscriptions")
    return database

def test_correct_setup(test_bot_database):
    assert not test_bot_database.retrieve_table_data("subscriptions")

def test_insert_retrieve_channel_sub(test_bot_database):
    sub1 = Subscription(guild_id=3, channel_id=1, _filter="type:problem and state:qualified")
    sub2 = Subscription(guild_id=3, channel_id=2, _filter="type:ranked")

    test_bot_database.insert_subscription(sub1)
    test_bot_database.insert_subscription(sub2)

    retrieved_subs = test_bot_database.retrieve_subscriptions()
    assert next(retrieved_subs, None) == sub1
    assert next(retrieved_subs, None) == sub2
    assert next(retrieved_subs, None) == None

def test_insert_retrieve_channel_sub_no_filter(test_bot_database):
    sub = Subscription(guild_id=1, channel_id=1, _filter=None)

    # A subscription should always have an explicit filter to prevent
    # the creation of an unfiltered subscription unintentionally.
    with pytest.raises(IntegrityError) as err:
        test_bot_database.insert_subscription(sub)
    
    assert "cannot be null" in str(err)

def test_retrieve_beatmapset_events(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "creator"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    nom2_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset)
    suggestion_event = Event("suggestion", from_string("2020-01-01 01:00:00"), beatmapset, user=User(3, "somethree"))

    test_database.insert_event(suggestion_event)
    test_database.insert_event(nom_event)
    test_database.insert_event(nom2_event)
    test_database.insert_event(qual_event)
    
    events = test_database.retrieve_beatmapset_events(beatmapset)
    qual_event.user = nom2_event.user
    assert nom_event in events
    assert qual_event in events
    assert suggestion_event in events

def test_retrieve_beatmapset_events_cache(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "creator"), ["osu"])
    nom_event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=User(1, "someone"))
    nom2_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))
    qual_event = Event("qualify", from_string("2020-01-01 05:00:00"), beatmapset)

    test_database.insert_event(nom_event)
    test_database.insert_event(nom2_event)
    test_database.insert_event(qual_event)
    
    test_database.retrieve_beatmapset_events(beatmapset)
    qual_event.user = nom2_event.user
    assert test_database.beatmapset_event_cache["3"] == [qual_event, nom_event]

    test_database.clear_cache()
    assert not test_database.beatmapset_event_cache

def test_retrieve_last_type(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")
    discussion = Discussion(7, beatmapset, nominator, "nice")

    praise_event = Event("praise", from_string("2020-01-01 04:56:00"), beatmapset, discussion, user=User(2, "sometwo"))
    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    test_database.insert_event(praise_event)
    test_database.insert_event(nom_event)

    retrieved_event = test_database.retrieve_last_type(nominator, beatmapset, "type = \"praise\"")
    assert retrieved_event == praise_event

def test_retrieve_last_type_cache(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")
    discussion = Discussion(7, beatmapset, nominator, "nice")

    praise_event = Event("praise", from_string("2020-01-01 04:56:00"), beatmapset, discussion, user=User(2, "sometwo"))
    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    test_database.insert_event(praise_event)
    test_database.insert_event(nom_event)

    test_database.retrieve_last_type(nominator, beatmapset, "type = \"praise\"")
    assert f"{nominator.id}-{beatmapset.id}-type = \"praise\"" in test_database.last_type_cache

    test_database.clear_cache()
    assert not test_database.last_type_cache

def test_retrieve_last_type_none(test_database):
    beatmapset = Beatmapset(3, "artist", "title", User(4, "mapper"), ["osu"])
    nominator = User(2, "sometwo")

    nom_event = Event("nominate", from_string("2020-01-01 05:00:00"), beatmapset, user=User(2, "sometwo"))

    test_database.insert_event(nom_event)

    retrieved_event = test_database.retrieve_last_type(nominator, beatmapset, "type = \"praise\"")
    assert not retrieved_event