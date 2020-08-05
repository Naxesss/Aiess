import sys
sys.path.append('..')

import pytest

from aiess import Event, Beatmapset, Discussion, User
from aiess.timestamp import from_string
from aiess import event_types as types

from bnsite.interface import Document

@pytest.fixture
def dq_event():
    disqualifier = User(1, "someone")
    creator = User(2, "sometwo")
    beatmapset = Beatmapset(_id=4, artist="artist", title="title", creator=creator, modes=["osu", "catch"])
    discussion = Discussion(_id=3, beatmapset=beatmapset, user=disqualifier, content="dqed")
    return Event(
        _type      = types.DISQUALIFY,
        time       = from_string("2020-01-01 03:00:00"),
        beatmapset = beatmapset,
        discussion = discussion,
        user       = disqualifier,
        content    = "dqed"
    )

def test_document(dq_event):
    document = Document(dq_event)

    assert document.eventType    == "Disqualified"
    assert document.timestamp    == from_string("2020-01-01 03:00:00")
    assert document.beatmapsetId == 4
    assert document.hostId       == 2
    assert document.hostName     == "sometwo"
    assert document.modes        == ["osu", "catch"]
    assert document.postId       == 3
    assert document.userId       == 1
    assert document.metadata     == "artist - title"
    assert document.content      == "dqed"