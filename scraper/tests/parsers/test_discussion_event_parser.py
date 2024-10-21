import sys
sys.path.append('..')

import pytest
import json

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

def test_parse_json():
    generator = discussion_event_parser.parse(json.loads(discussion_events_json.DISCUSSIONS_JSON))

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