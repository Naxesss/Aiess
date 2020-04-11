import pytest

from aiess import Event, User, Beatmapset, Discussion
from aiess.timestamp import from_string

from formatter import format_link

def test_format_link_discussion():
    beatmapset = Beatmapset(3, "artist", "title", User(2, "sometwo"), ["osu"])
    user = User(3, "somethree")
    discussion = Discussion(5, beatmapset, user, content="hi")
    event = Event("suggestion", from_string("2020-04-11 20:00:00"), beatmapset, discussion, user, content="hi")

    assert format_link(event) == "https://osu.ppy.sh/beatmapsets/3/discussion#/5"

def test_format_link_no_discussion():
    beatmapset = Beatmapset(3, "artist", "title", User(2, "sometwo"), ["osu"])
    user = User(3, "somethree")
    event = Event("nominate", from_string("2020-04-11 20:00:00"), beatmapset, user=user)

    assert format_link(event) == "https://osu.ppy.sh/beatmapsets/3"

def test_format_link_no_beatmapset():
    event = Event("test", from_string("2020-04-11 20:00:00"))

    with pytest.raises(ValueError) as err:
        format_link(event)
    
    assert "missing a beatmapset" in str(err)