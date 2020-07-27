import pytest
from datetime import datetime

from aiess.objects import User, Beatmapset, Discussion, Usergroup, NewsPost, Event
from aiess.errors import DeletedContextError

from aiess.tests.mocks.api import beatmap as mock_beatmap
from aiess.tests.mocks.api import old_beatmap as mock_old_beatmap

def test_user():
    user = User(101, "Generic Name")

    assert user.id == 101
    assert user.name == "Generic Name"
    assert str(user) == "Generic Name"

def test_user_get_name_from_api():
    user = User(2)
    
    assert user.id == 2
    assert user.name == "peppy"

def test_user_get_id_from_api():
    user = User(name="peppy")

    assert user.id == 2
    assert user.name == "peppy"

def test_user_no_args():
    with pytest.raises(ValueError) as err:
        User()
    assert "neither id nor name provided" in str(err)

def test_user_get_name_restricted():
    user = User(1)

    assert user.id == 1
    assert user.name is None
    assert str(user) == "1"

def test_user_get_id_restricted():
    user = User(name="a")
    
    assert user.id is None
    assert user.name == "a"

def test_user_int_name():
    user = User(3, 487)
    assert user.name == "487"

def test_user_str_id():
    user = User("101", "someone")
    assert user.id == 101

def test_beatmapset():
    beatmapset = Beatmapset(41823, beatmapset_json=mock_old_beatmap.JSON)

    assert beatmapset.id == 41823
    assert beatmapset.artist == "The Quick Brown Fox"
    assert beatmapset.title == "The Big Black"
    assert beatmapset.creator.id == 19048
    assert beatmapset.creator.name == "Blue Dragon"
    assert beatmapset.modes == ["osu", "taiko"]

    assert beatmapset.mode_str() == "[osu][taiko]"
    assert str(beatmapset) == "The Quick Brown Fox - The Big Black (mapped by Blue Dragon) [osu][taiko]"

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
    assert discussion.id == 1234956
    assert discussion.beatmapset == beatmapset

def test_discussion():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset)

    assert discussion.id == 1234956
    assert discussion.beatmapset == beatmapset

def test_discussion_int_content():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset, content=4)

    assert discussion.id == 1234956
    assert discussion.content == "4"
    assert discussion.beatmapset == beatmapset

def test_usergroup():
    usergroup = Usergroup(4)

    assert usergroup.id == 4
    assert usergroup.name == "Global Moderation Team"

def test_usergroup_str_id():
    usergroup = Usergroup("4")

    assert usergroup.id == 4
    assert usergroup.name == "Global Moderation Team"

def test_usergroup_eq():
    usergroup1 = Usergroup(4)
    usergroup2 = Usergroup(4)
    usergroup3 = Usergroup(7)

    assert usergroup1 == usergroup2
    assert usergroup1 != usergroup3

def test_usergroup_eq_different_types():
    assert Usergroup(4) != "string"

def test_usergroup_hash():
    assert hash(Usergroup(4))

def test_usergroup_str():
    usergroup = Usergroup(4)
    assert str(usergroup) == "Global Moderation Team"

def test_newspost():
    newspost = NewsPost(_id=1, title="title", preview="hello there", author=User(1, "someone"), slug="newspost-1", image_url="/image")

    assert newspost.id == 1
    assert newspost.title == "title"
    assert newspost.preview == "hello there"
    assert newspost.author.id == 1
    assert newspost.author.name == "someone"
    assert newspost.slug == "newspost-1"
    assert newspost.image_url == "/image"

def test_newspost_str_id():
    newspost = NewsPost(_id="1", title="title", preview="hello there", author=User(1, "someone"), slug="newspost-1", image_url="/image")
    assert newspost.id == 1

def test_newspost_eq():
    newspost1 = NewsPost(_id="1", title="title", preview="hello there", author=User(1, "someone"), slug="newspost-1", image_url="/image")
    newspost2 = NewsPost(_id="1", title="title", preview="hello there", author=User(1, "someone"), slug="newspost-1", image_url="/image")
    newspost3 = NewsPost(_id="1", title="title2", preview="hello there", author=User(1, "someone"), slug="newspost-1", image_url="/image")

    assert newspost1 == newspost2
    assert newspost1 != newspost3

def test_newspost_eq_different_types():
    newspost = NewsPost(_id="1", title="title", preview="hello there", author=User(1, "someone"), slug="newspost-1", image_url="/image")
    assert newspost != "string"

def test_newspost_hash():
    newspost = NewsPost(_id="1", title="title", preview="hello there", author=User(1, "someone"), slug="newspost-1", image_url="/image")
    assert hash(newspost)

def test_event_int_content():
    event = Event(_type="test", time=datetime.utcnow(), content=4)
    assert event.content == "4"