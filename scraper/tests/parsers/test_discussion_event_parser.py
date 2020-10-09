import sys
sys.path.append('..')

import pytest

from aiess import timestamp

from scraper.tests.mocks.events import problem, reply
from scraper.tests.mocks.events.faulty import discussion_events
from scraper.tests.mocks import discussion_diff_and_tabs
from scraper.tests.mocks import discussion_events_json
from scraper.parsers.discussion_event_parser import discussion_event_parser
from scraper import populator

def test_parse_discussion_message():
    actual_content = discussion_event_parser.parse_discussion_message(problem.tag)
    expected_content = problem.CONTENT

    assert actual_content == expected_content

def test_parse_reply_message():
    actual_content = discussion_event_parser.parse_discussion_message(reply.tag)
    expected_content = reply.CONTENT

    assert actual_content == expected_content

def test_parse_discussion_tab():
    actual_content = discussion_event_parser.parse_discussion_tab(discussion_diff_and_tabs.tag)
    expected_content = "general"

    assert actual_content == expected_content

def test_parse_discussion_diff():
    actual_content = discussion_event_parser.parse_discussion_diff(discussion_diff_and_tabs.tag)
    expected_content = "Expert"

    assert actual_content == expected_content

def test_parse():
    generator = discussion_event_parser.parse(discussion_events.soup)

    generated_events = []
    for event in generator:
        generated_events.append(event)
    
    assert len(generated_events) == 1  # 1 of 2 events is of a beatmapset that no longer exists.
    assert generated_events[0].type == "suggestion"
    assert generated_events[0].discussion.tab == "timeline"
    assert generated_events[0].discussion.difficulty == "Expert"

def test_parse_json():
    generator = discussion_event_parser.parse(discussion_events_json.soup)

    generated_events = []
    for event in generator:
        generated_events.append(event)
    
    # There are 7 events, but one is of a beatmapset that has been deleted, and another is empty.
    assert len(generated_events) == 5
    assert generated_events[0].type == "suggestion"
    assert generated_events[0].time == timestamp.from_string("2020-03-07T20:42:58+00:00")
    assert generated_events[2].user.id == 2597417
    assert generated_events[2].user.name == "Jaltzu"
    assert generated_events[2].discussion.tab == "timeline"
    assert generated_events[2].discussion.difficulty == "Muzukashii"

@pytest.fixture(scope="module")
def discussion_event():
    return discussion_event_parser.parse_event(problem.tag)

def test_event_attr(discussion_event):
    assert discussion_event.time == timestamp.from_string("2019-12-05T16:50:10+00:00")
    assert discussion_event.type == "problem"
    assert discussion_event.content == problem.CONTENT

def test_user_attr(discussion_event):
    assert discussion_event.user.id == 197805
    assert discussion_event.user.name == "Niva"

def test_beatmapset_attr(discussion_event):
    assert discussion_event.beatmapset.id == 1074596
    assert discussion_event.beatmapset.artist == "Camellia"
    assert discussion_event.beatmapset.title == "werewolf howls. [\"Growling\" Long ver.]"
    assert discussion_event.beatmapset.creator.id == 419954
    assert discussion_event.beatmapset.creator.name == "Regou"
    assert discussion_event.beatmapset.modes == ["osu"]

def test_discussion_attr(discussion_event):
    assert discussion_event.discussion.id == 1295203
    assert discussion_event.discussion.beatmapset == discussion_event.beatmapset
    assert discussion_event.discussion.tab == "general"
    assert discussion_event.discussion.difficulty == "Expert"



@pytest.fixture(scope="module")
def reply_event():
    return discussion_event_parser.parse_event(reply.tag)

def test_reply_event_attr(reply_event):
    assert reply_event.time == timestamp.from_string("2020-02-14T17:35:47+00:00")
    assert reply_event.type == "reply"
    assert reply_event.content == reply.CONTENT

def test_reply_user_attr(reply_event):
    assert reply_event.user.id == 6751666
    assert reply_event.user.name == "Tailsdk"

@pytest.mark.asyncio
async def test_reply_discussion_attr(reply_event):
    assert reply_event.discussion.id == 1396395
    await populator.populate_from_discussion(reply_event)
    assert reply_event.discussion.user.id == 9555243
    assert reply_event.discussion.user.name == "Dubstek"
    assert reply_event.discussion.content == "If you want to express 00:27:528 (27528|1) - this clap sound with LN, I think 00:33:046 (33046|2) - this NM also should be changed into LN for consistency."