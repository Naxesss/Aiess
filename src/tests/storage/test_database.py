import pytest
from mysql.connector.errors import ProgrammingError, OperationalError
from typing import List, Tuple
from datetime import datetime

from storage.database import Database
from objects import User, Beatmapset, Discussion, Event

@pytest.fixture
def test_database():
    database = Database("aiess_test")
    # Reset database to state before any tests ran.
    database.delete_table_data("events", dict(type="test"))
    database.delete_table_data("discussions", dict(id=1))
    database.delete_table_data("beatmapsets", dict(id=1))
    database.delete_table_data("beatmapset_modes", dict(beatmapset_id=1))
    database.delete_table_data("users", dict(id=1))

    return database

def test_correct_setup(test_database):
    assert not test_database.retrieve_table_data("events", dict(type="test"))
    assert not test_database.retrieve_table_data("discussions", dict(id=1))
    assert not test_database.retrieve_table_data("beatmapsets", dict(id=1))
    assert not test_database.retrieve_table_data("beatmapset_modes", dict(beatmapset_id=1))
    assert not test_database.retrieve_table_data("users", dict(id=1))

def test_insert_delete(test_database):
    test_database.insert_table_data("users", dict(id=1, name="test"))
    assert test_database.retrieve_table_data("users", dict(id=1))

    test_database.delete_table_data("users", dict(id=1))
    assert not test_database.retrieve_table_data("users", dict(id=1))

def test_auto_reconnect(test_database):
    test_database.connection.close()
    
    test_database.insert_table_data("users", dict(id=1, name="test"))
    assert test_database.retrieve_user(dict(id=1))

def test_missing_table(test_database):
    with pytest.raises(ProgrammingError) as error:
        test_database.insert_table_data("missing_table", dict(id=1, name="test"))
    assert "Table 'aiess_test.missing_table' doesn't exist" in str(error.value)

def test_insert_retrieve_event(test_database):
    time = datetime.utcnow()

    user = User(1, name="test")
    beatmapset = Beatmapset(1, artist="123", title="456", creator=user, modes=["osu", "taiko"])
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing")
    event = Event(_type="test", time=time, beatmapset=beatmapset, discussion=discussion, user=user)

    test_database.insert_event(event)

    retrieved_event = test_database.retrieve_event(dict(type="test"))
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.beatmapset == event.beatmapset
    assert retrieved_event.discussion == event.discussion
    assert retrieved_event.user == event.user
    assert retrieved_event.content == event.content
    assert retrieved_event == event

def test_insert_retrieve_small_event(test_database):
    event = Event(_type="test", time=datetime.utcnow())
    test_database.insert_event(event)

    retrieved_event = test_database.retrieve_event(dict(type="test"))
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.beatmapset == event.beatmapset
    assert retrieved_event.discussion == event.discussion
    assert retrieved_event.user == event.user
    assert retrieved_event.content == event.content
    assert retrieved_event == event

def test_insert_retrieve_user(test_database):
    user = User(1, name="test")
    test_database.insert_user(user)

    retrieved_user = test_database.retrieve_user(dict(id=1))
    assert retrieved_user.id == user.id
    assert retrieved_user.name == user.name
    assert retrieved_user == user

def test_insert_retrieve_beatmapset_modes(test_database):
    modes = ["osu", "taiko"]
    user = User(1, name="test")
    beatmapset = Beatmapset(1, artist="123", title="456", creator=user, modes=modes)
    test_database.insert_beatmapset_modes(beatmapset)

    retrieved_modes = test_database.retrieve_beatmapset_modes(1)
    assert retrieved_modes == modes

def test_insert_retrieve_beatmapset(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, artist="123", title="456", creator=user, modes=["osu", "taiko"])
    test_database.insert_beatmapset(beatmapset)

    retrieved_beatmapset = test_database.retrieve_beatmapset(dict(id=1))
    assert retrieved_beatmapset.id == beatmapset.id
    assert retrieved_beatmapset.artist == beatmapset.artist
    assert retrieved_beatmapset.title == beatmapset.title
    assert retrieved_beatmapset.creator == beatmapset.creator
    assert retrieved_beatmapset.modes == beatmapset.modes
    assert retrieved_beatmapset == beatmapset

def test_insert_retrieve_discussion(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, artist="123", title="456", creator=user, modes=["osu", "taiko"])
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing")
    test_database.insert_discussion(discussion)

    retrieved_discussion = test_database.retrieve_discussion(dict(id=1))
    assert retrieved_discussion.id == discussion.id
    assert retrieved_discussion.beatmapset == discussion.beatmapset
    assert retrieved_discussion.user == discussion.user
    assert retrieved_discussion.content == discussion.content
    assert retrieved_discussion == discussion

def test_insert_incomplete_discussion(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, artist="123", title="456", creator=user, modes=["osu", "taiko"])
    discussion = Discussion(1, beatmapset=beatmapset)

    with pytest.raises(ValueError) as error:
        test_database.insert_discussion(discussion)
    assert "missing from discussion" in str(error.value)