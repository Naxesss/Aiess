import pytest

from aiess import timestamp

from tests.mocks.events import problem, reply
from tests.mocks.events.faulty import discussion_events
from parsers.discussion_event_parser import discussion_event_parser
import populator

def test_parse_discussion_message():
    actual_content = discussion_event_parser.parse_discussion_message(problem.tag)
    expected_content = problem.CONTENT

    assert actual_content == expected_content

def test_parse_reply_message():
    actual_content = discussion_event_parser.parse_discussion_message(reply.tag)
    expected_content = reply.CONTENT

    assert actual_content == expected_content

def test_parse():
    generator = discussion_event_parser.parse(discussion_events.soup)

    generated_events = []
    for event in generator:
        generated_events.append(event)
    
    assert len(generated_events) == 1  # 1 of 2 events is of a beatmapset that no longer exists.
    assert generated_events[0].type == "suggestion"



@pytest.fixture(scope="module")
def discussion_event():
    return discussion_event_parser.parse_event(problem.tag)

def test_event_attr(discussion_event):
    assert discussion_event.time == timestamp.from_string("2019-12-05T16:50:10+00:00")
    assert discussion_event.type == "problem"
    assert discussion_event.content == problem.CONTENT

def test_user_attr(discussion_event):
    assert discussion_event.user.id == "197805"
    assert discussion_event.user.name == "Niva"

def test_beatmapset_attr(discussion_event):
    assert discussion_event.beatmapset.id == "1074596"
    assert discussion_event.beatmapset.artist == "Camellia"
    assert discussion_event.beatmapset.title == "werewolf howls. [\"Growling\" Long ver.]"
    assert discussion_event.beatmapset.creator.id == "419954"
    assert discussion_event.beatmapset.creator.name == "Regou"
    assert discussion_event.beatmapset.modes == ["osu"]

def test_discussion_attr(discussion_event):
    assert discussion_event.discussion.id == "1295203"
    assert discussion_event.discussion.beatmapset == discussion_event.beatmapset



@pytest.fixture(scope="module")
def reply_event():
    return discussion_event_parser.parse_event(reply.tag)

def test_reply_event_attr(reply_event):
    assert reply_event.time == timestamp.from_string("2020-02-14T17:35:47+00:00")
    assert reply_event.type == "reply"
    assert reply_event.content == reply.CONTENT

def test_reply_user_attr(reply_event):
    assert reply_event.user.id == "6751666"
    assert reply_event.user.name == "Tailsdk"

def test_reply_discussion_attr(reply_event):
    assert reply_event.discussion.id == "1396395"
    populator.populate_event(reply_event)
    assert reply_event.discussion.user.id == "9555243"
    assert reply_event.discussion.user.name == "Dubstek"
    assert reply_event.discussion.content == "If you want to express 00:27:528 (27528|1) - this clap sound with LN, I think 00:33:046 (33046|2) - this NM also should be changed into LN for consistency."