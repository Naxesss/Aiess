import pytest
from mysql.connector.errors import ProgrammingError, OperationalError
from typing import List, Tuple
from datetime import datetime

from aiess.objects import User, Beatmapset, Discussion, Event
from aiess.database import Database

@pytest.fixture
def test_database():
    database = Database("aiess_test")
    # Reset database to state before any tests ran.
    database.clear_table_data("events")
    database.clear_table_data("discussions")
    database.clear_table_data("beatmapsets")
    database.clear_table_data("beatmapset_modes")
    database.clear_table_data("users")

    return database

def test_correct_setup(test_database):
    assert not test_database.retrieve_table_data("events")
    assert not test_database.retrieve_table_data("discussions")
    assert not test_database.retrieve_table_data("beatmapsets")
    assert not test_database.retrieve_table_data("beatmapset_modes")
    assert not test_database.retrieve_table_data("users")

def test_insert_delete(test_database):
    test_database.insert_table_data("users", dict(id=1, name="test"))
    assert test_database.retrieve_table_data("users", "id=1")

    test_database.delete_table_data("users", "id=1")
    assert not test_database.retrieve_table_data("users")

def test_auto_reconnect(test_database):
    test_database.connection.close()
    
    test_database.insert_table_data("users", dict(id=1, name="test"))
    assert test_database.retrieve_user("id=1")

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

    retrieved_event = test_database.retrieve_event("type=\"test\"")
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

    retrieved_event = test_database.retrieve_event("type=\"test\"")
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.beatmapset == event.beatmapset
    assert retrieved_event.discussion == event.discussion
    assert retrieved_event.user == event.user
    assert retrieved_event.content == event.content
    assert retrieved_event == event

def test_insert_retrieve_event_digit_properties(test_database):
    user = User(1, "497")
    beatmapset = Beatmapset(3, artist="5", title="2", creator=user, modes=["osu"])
    discussion = Discussion(2, beatmapset, user, content="8")
    event = Event(_type="test", time=datetime.utcnow(), user=user, beatmapset=beatmapset, discussion=discussion, content="4")
    test_database.insert_event(event)

    retrieved_event = test_database.retrieve_event("type=\"test\"")
    # Ensures the database field retrieval retains the `str` type, rather than reinterpreting as `int`.
    assert retrieved_event.content == "4"
    assert retrieved_event.user.name == "497"
    assert retrieved_event.beatmapset.artist == "5"
    assert retrieved_event.beatmapset.title == "2"
    assert retrieved_event.discussion.content == "8"

def test_insert_retrieve_user(test_database):
    user = User(1, name="test")
    test_database.insert_user(user)

    retrieved_user = test_database.retrieve_user("id=1")
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

    retrieved_beatmapset = test_database.retrieve_beatmapset("id=1")
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

    retrieved_discussion = test_database.retrieve_discussion("id=1")
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

def test_insert_retrieve_discussion_and_replies(test_database):
    time = datetime.utcnow()

    user_author = User(1, name="one")
    user_replier = User(2, name="two")

    beatmapset = Beatmapset(1, artist="123", title="456", creator=user_replier, modes=["osu", "taiko"])
    discussion = Discussion(1, beatmapset=beatmapset, user=user_author, content="ping")

    event_problem = Event(_type="problem", time=time, beatmapset=beatmapset, discussion=discussion, user=user_author, content="ping")
    event_reply1 = Event(_type="reply", time=time, beatmapset=beatmapset, discussion=discussion, user=user_replier, content="pong")
    event_reply2 = Event(_type="reply", time=time, beatmapset=beatmapset, discussion=discussion, user=user_author, content="miss")

    test_database.insert_event(event_problem)
    test_database.insert_event(event_reply1)
    test_database.insert_event(event_reply2)

    retrieved_problem = test_database.retrieve_event("type=\"problem\"")
    retrieved_reply1 = test_database.retrieve_event(f"type=\"reply\" and user_id={user_replier.id}")
    retrieved_reply2 = test_database.retrieve_event(f"type=\"reply\" and user_id={user_author.id}")

    assert retrieved_problem
    assert retrieved_reply1
    assert retrieved_reply2

def test_insert_retrieve_multiple_users(test_database):
    user1 = User(1, name="test")
    user2 = User(2, name="test")

    test_database.insert_user(user1)
    test_database.insert_user(user2)

    retrieved_users = test_database.retrieve_users(f"name=\"{user1.name}\"")
    assert next(retrieved_users, None) == user1
    assert next(retrieved_users, None) == user2

def test_insert_retrieve_multiple_beatmapsets(test_database):
    user = User(1, name="test")
    beatmapset1 = Beatmapset(1, artist="123", title="456", creator=user, modes=["osu", "taiko"])
    beatmapset2 = Beatmapset(2, artist="456", title="789", creator=user, modes=["osu"])

    test_database.insert_beatmapset(beatmapset1)
    test_database.insert_beatmapset(beatmapset2)

    retrieved_beatmapsets = test_database.retrieve_beatmapsets(f"creator_id={user.id}")
    assert next(retrieved_beatmapsets, None) == beatmapset1
    assert next(retrieved_beatmapsets, None) == beatmapset2

def test_insert_retrieve_multiple_discussions(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, artist="123", title="456", creator=user, modes=["osu", "taiko"])
    discussion1 = Discussion(1, beatmapset=beatmapset, user=user, content="testing")
    discussion2 = Discussion(2, beatmapset=beatmapset, user=user, content="real testing")

    test_database.insert_discussion(discussion1)
    test_database.insert_discussion(discussion2)

    retrieved_discussions = test_database.retrieve_discussions(f"beatmapset_id={beatmapset.id}")
    assert next(retrieved_discussions, None) == discussion1
    assert next(retrieved_discussions, None) == discussion2

def test_insert_retrieve_multiple_events(test_database):
    time = datetime.utcnow()

    user = User(1, name="test")
    beatmapset = Beatmapset(1, artist="123", title="456", creator=user, modes=["osu", "taiko"])
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing")
    event1 = Event(_type="test", time=time, beatmapset=beatmapset, discussion=discussion, user=user)
    event2 = Event(_type="123", time=time, beatmapset=beatmapset, discussion=discussion, user=user)

    test_database.insert_event(event1)
    test_database.insert_event(event2)

    retrieved_events = test_database.retrieve_events(f"beatmapset_id={beatmapset.id}")
    assert next(retrieved_events, None) == event1
    assert next(retrieved_events, None) == event2