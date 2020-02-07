import pytest

from tests.mocks import mock_events
from parsers.discussion_event_parser import discussion_event_parser
from parsers.time_parser import from_ISO_8601_to_datetime

def test_parse_discussion_message():
    actual_content = discussion_event_parser.parse_discussion_message(mock_events.discussion_tag)
    expected_content = mock_events.PROBLEM_CONTENT

    assert actual_content == expected_content

def test_parse():
    generator = discussion_event_parser.parse(mock_events.first_correct_second_faulty_discussions_soup)

    generated_events = []
    for event in generator:
        generated_events.append(event)
    
    assert len(generated_events) == 1  # 1 of 2 events is of a beatmapset that no longer exists.
    assert generated_events[0].type == "suggestion"

@pytest.fixture(scope="module")
def beatmapset_event():
    return discussion_event_parser.parse_event(mock_events.discussion_tag)

def test_event_attr(beatmapset_event):
    assert beatmapset_event.time == from_ISO_8601_to_datetime("2019-12-05T16:50:10+00:00")
    assert beatmapset_event.type == "problem"
    assert beatmapset_event.content == mock_events.PROBLEM_CONTENT

def test_user_attr(beatmapset_event):
    assert beatmapset_event.user.id == "197805"
    assert beatmapset_event.user.name == "Niva"

def test_beatmapset_attr(beatmapset_event):
    assert beatmapset_event.beatmapset.id == "1074596"
    assert beatmapset_event.beatmapset.artist == "Camellia"
    assert beatmapset_event.beatmapset.title == "werewolf howls. [\"Growling\" Long ver.]"
    assert beatmapset_event.beatmapset.creator.id == "419954"
    assert beatmapset_event.beatmapset.creator.name == "Regou"
    assert beatmapset_event.beatmapset.modes == ["osu"]

def test_discussion_attr(beatmapset_event):
    assert beatmapset_event.discussion.id == "1295203"
    assert beatmapset_event.discussion.beatmapset == beatmapset_event.beatmapset