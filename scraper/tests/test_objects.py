import pytest

import objects
from tests.mocks.api import beatmap as mock_beatmap
from tests.mocks.api import old_beatmap as mock_old_beatmap
from exceptions import ParsingError, DeletedContextError
from web import populator

def test_user():
    user = objects.User(101, "Generic Name")

    assert user.id == "101"
    assert user.name == "Generic Name"
    assert user.__str__() == "Generic Name"

def test_user_no_name():
    user = objects.User(2)

    assert user.id == "2"
    assert user.name == "peppy"
    assert user.__str__() == "peppy"

def test_user_restricted():
    user = objects.User(1)

    assert user.id == "1"
    assert user.name == None
    assert user.__str__() == "1"

def test_beatmapset():
    beatmapset = objects.Beatmapset(41823, beatmapset_json=mock_old_beatmap.JSON)

    assert beatmapset.id == "41823"
    assert beatmapset.artist == "The Quick Brown Fox"
    assert beatmapset.title == "The Big Black"
    assert beatmapset.creator.id == "19048"
    assert beatmapset.creator.name == "Blue Dragon"
    assert beatmapset.modes == ["osu", "taiko"]

    assert beatmapset.mode_str() == "[osu][taiko]"
    assert beatmapset.__str__() == "The Quick Brown Fox - The Big Black (mapped by Blue Dragon) [osu][taiko]"

def test_beatmapset_non_existent():
    with pytest.raises(DeletedContextError):
        objects.Beatmapset(2, beatmapset_json="[]")

def test_old_discussion():
    beatmapset = objects.Beatmapset(41823, beatmapset_json=mock_old_beatmap.JSON)
    discussion = objects.Discussion(1234956, beatmapset)

    assert discussion.id == "1234956"
    assert discussion.beatmapset == beatmapset
    
    # Can't obtain any discussion data from a beatmapset that doesn't have a discussion interface.
    with pytest.raises(ParsingError):
        populator.get_complete_discussion_info(discussion, beatmapset)

def test_discussion():
    beatmapset = objects.Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = objects.Discussion(1234956, beatmapset)

    assert discussion.id == "1234956"
    assert discussion.beatmapset == beatmapset

    # Some information will not be available until it is supplied by other sources
    # (e.g. discussion jsons, prior database entires, scraping)
    discussion = populator.get_complete_discussion_info(discussion, beatmapset)

    assert discussion.user.id == "4967662"
    assert discussion.user.name == "greenhue"
    assert discussion.content == "since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms."

def test_usergroup():
    usergroup = objects.Usergroup("4")

    assert usergroup.id == "4"
    assert usergroup.name == "Global Moderation Team"

