import pytest
from datetime import datetime

from aiess.objects import User, Beatmapset, Discussion, Usergroup, Event
from aiess.errors import ParsingError, DeletedContextError

from aiess.tests.mocks.api import beatmap as mock_beatmap
from aiess.tests.mocks.api import old_beatmap as mock_old_beatmap

def test_user():
    user = User(101, "Generic Name")

    assert user.id == "101"
    assert user.name == "Generic Name"
    assert user.__str__() == "Generic Name"

def test_user_no_name():
    user = User(2)

    assert user.id == "2"
    assert user.name == "peppy"
    assert user.__str__() == "peppy"

def test_user_restricted():
    user = User(1)

    assert user.id == "1"
    assert user.name is None
    assert user.__str__() == "1"

def test_user_int_name():
    user = User(3, 487)

    assert user.id == "3"
    assert user.name == "487"
    assert user.__str__() == "487"

def test_beatmapset():
    beatmapset = Beatmapset(41823, beatmapset_json=mock_old_beatmap.JSON)

    assert beatmapset.id == "41823"
    assert beatmapset.artist == "The Quick Brown Fox"
    assert beatmapset.title == "The Big Black"
    assert beatmapset.creator.id == "19048"
    assert beatmapset.creator.name == "Blue Dragon"
    assert beatmapset.modes == ["osu", "taiko"]

    assert beatmapset.mode_str() == "[osu][taiko]"
    assert beatmapset.__str__() == "The Quick Brown Fox - The Big Black (mapped by Blue Dragon) [osu][taiko]"

def test_beatmapset_int_artist_title():
    beatmapset = Beatmapset(41823, 5, 6, User(2, 222), ["osu"])

    assert beatmapset.artist == "5"
    assert beatmapset.title == "6"

def test_beatmapset_non_existent():
    with pytest.raises(DeletedContextError):
        Beatmapset(2, beatmapset_json="[]")

def test_old_discussion():
    beatmapset = Beatmapset(41823, beatmapset_json=mock_old_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset)

    # No such discussion exists, but this should still work.
    assert discussion.id == "1234956"
    assert discussion.beatmapset == beatmapset

def test_discussion():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset)

    assert discussion.id == "1234956"
    assert discussion.beatmapset == beatmapset

def test_discussion_int_content():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset, content=4)

    assert discussion.id == "1234956"
    assert discussion.content == "4"
    assert discussion.beatmapset == beatmapset

def test_usergroup():
    usergroup = Usergroup("4")

    assert usergroup.id == "4"
    assert usergroup.name == "Global Moderation Team"

def test_usergroup_int_id():
    usergroup = Usergroup(4)

    assert usergroup.id == "4"
    assert usergroup.name == "Global Moderation Team"

def test_event_int_content():
    event = Event(_type="test", time=datetime.utcnow(), content=4)

    assert event.content == "4"