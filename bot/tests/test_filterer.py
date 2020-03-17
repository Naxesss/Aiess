from datetime import datetime

from aiess import Event, Beatmapset, User

from filterer import expand, dissect

def test_expand():
    assert expand("type:(nominate or qualify)") == "type:nominate or type:qualify"

def test_expand_redundancy():
    assert expand("(type:(qualify))") == "type:qualify"

def test_expand_duplicate():
    assert expand("type:(nominate or qualify or nominate)") == "type:nominate or type:qualify"

def test_expand_unorganized():
    assert expand("type:(nominate or qualify) or type:hype") == "type:nominate or type:qualify or type:hype"

def test_expand_and():
    assert expand("type:(nominate or qualify) and user:123") == "type:nominate and user:123 or type:qualify and user:123"

def test_expand_and_quotes():
    assert (expand("type:(nominate or qualify) and user:\"some user with and in their name\"") ==
        "type:nominate and user:\"some user with and in their name\" or type:qualify and user:\"some user with and in their name\"")

def test_expand_multiple_and():
    assert (expand("type:(nominate or qualify) and user:(123 or 456)") ==
        "type:nominate and user:123 or type:nominate and user:456 or type:qualify and user:123 or type:qualify and user:456")

def test_dissect_simple():
    event = Event(_type="test", time=datetime.utcnow())
    assert dissect(event) == ["type:test"]

def test_dissect_beatmapset():
    user = User(2, "some two")
    beatmapset = Beatmapset(4, artist="", title="", creator=user, modes=["osu", "catch"])
    event = Event(_type="test", time=datetime.utcnow(), beatmapset=beatmapset)
    assert dissect(event) == ["type:test"]