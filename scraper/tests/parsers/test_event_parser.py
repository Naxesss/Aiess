import sys
sys.path.append('..')

import pytest

from aiess.errors import ParsingError, DeletedContextError
from aiess.timestamp import from_string

from scraper.tests.mocks.events import issue_resolve, problem
from scraper.tests.mocks.events.faulty import no_events, resolve_deleted_beatmap, kudosu_deleted_beatmap
from scraper.parsers.event_parser import EventParser

@pytest.fixture
def event_parser():
    return EventParser()

def test_parse_event_type(event_parser):
    tests = [
        [
            event_parser.parse_event_type(
                issue_resolve.tag,
                "beatmapset-event__icon",
                "beatmapset-event__icon--"
            ), "issue_resolve"
        ],
        [
            event_parser.parse_event_type(
                problem.tag,
                "beatmap-discussion-message-type",
                "beatmap-discussion-message-type--"
            ), "problem"
        ]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_type_faulty(event_parser):
    faulty_values = [
        no_events.tag,
        issue_resolve.tag,  # Wrong event type and class prefix.
        None
    ]

    for value in faulty_values:
        with pytest.raises(ParsingError):
            event_parser.parse_event_type(
                value,
                "beatmap-discussion-message-type",
                "beatmap-discussion-message-type--"
            )

def test_parse_event_time(event_parser):
    tests = [
        [event_parser.parse_event_time(issue_resolve.tag), from_string("2019-12-05T10:26:54+00:00")],
        [event_parser.parse_event_time(problem.tag), from_string("2019-12-05T16:50:10+00:00")]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_time_faulty(event_parser):
    faulty_values = [
        no_events.tag,
        None
    ]

    for value in faulty_values:
        with pytest.raises(ParsingError):
            event_parser.parse_event_time(value)

def test_parse_event_link(event_parser):
    tests = [
        [event_parser.parse_event_link(issue_resolve.tag), "https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675"],
        [event_parser.parse_event_link(problem.tag), "https://osu.ppy.sh/beatmapsets/1074596/discussion#/1295203"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_link_faulty(event_parser):
    faulty_values = [
        [no_events.tag, ParsingError],
        [resolve_deleted_beatmap.tag, DeletedContextError],
        [kudosu_deleted_beatmap.tag, DeletedContextError],
        [None, ParsingError]
    ]

    for value, expected_exception in faulty_values:
        with pytest.raises(expected_exception):
            event_parser.parse_event_link(value)

def test_parse_author_id(event_parser):
    tests = [
        [event_parser.parse_event_author_id(issue_resolve.tag, "user-name"), None],
        [event_parser.parse_event_author_id(problem.tag,       "beatmap-discussion-user-card__user-link"), "197805"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_author_id_faulty(event_parser):
    faulty_values = [
        [no_events.tag, ParsingError],
        [resolve_deleted_beatmap.tag, DeletedContextError],
        [None, ParsingError]
    ]

    for value, expected_exception in faulty_values:
        assert event_parser.parse_event_author_id(value, "beatmap-discussion-user-card__user-link") is None
    
    for value, expected_exception in faulty_values:
        with pytest.raises(expected_exception):
            event_parser.parse_event_author_id(value, "beatmap-discussion-user-card__user-link", must_find=True)

def test_parse_author_name(event_parser):
    tests = [
        [event_parser.parse_event_author_name(issue_resolve.tag, "user-name"), None],
        [event_parser.parse_event_author_name(problem.tag,       "beatmap-discussion-user-card__user-text"), "Niva"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_author_name_faulty(event_parser):
    faulty_values = [
        [no_events.tag, ParsingError],
        [resolve_deleted_beatmap.tag, DeletedContextError],
        [None, ParsingError]
    ]

    for value, expected_exception in faulty_values:
        assert event_parser.parse_event_author_name(value, "beatmap-discussion-user-card__user-text") is None
    
    for value, expected_exception in faulty_values:
        with pytest.raises(expected_exception):
            event_parser.parse_event_link(value)

def test_parse_id_from_user_link(event_parser):
    tests = [
        [event_parser.parse_id_from_user_link(None), None],
        [event_parser.parse_id_from_user_link("https://osu.ppy.sh/beatmapsets/1074596"), None],
        [event_parser.parse_id_from_user_link("https://osu.ppy.sh/users/1653229"), "1653229"],
        [event_parser.parse_id_from_user_link("https://osu.ppy.sh/users/197805/modding"), "197805"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_id_from_discussion_link(event_parser):
    tests = [
        [event_parser.parse_id_from_discussion_link(None), None],
        [event_parser.parse_id_from_discussion_link("https://osu.ppy.sh/beatmapsets/1074596"), None],
        [event_parser.parse_id_from_discussion_link("https://osu.ppy.sh/beatmapsets/1013400/discussion"), None],
        [event_parser.parse_id_from_discussion_link("https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675"), "1294675"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_id_from_beatmapset_link(event_parser):
    tests = [
        [event_parser.parse_id_from_beatmapset_link(None), None],
        [event_parser.parse_id_from_beatmapset_link("https://osu.ppy.sh/users/1653229"), None],
        [event_parser.parse_id_from_beatmapset_link("https://osu.ppy.sh/beatmapsets/1074596"), "1074596"],
        [event_parser.parse_id_from_beatmapset_link("https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675"), "1011055"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_from_ISO_8601_to_datetime_raise():
    faulty_values = [
        "",
        "https://osu.ppy.sh/users/1653229"
    ]

    with pytest.raises(TypeError):
        from_string(None)

    for value in faulty_values:
        with pytest.raises(ValueError):
            from_string(value)

def test_from_ISO_8601_to_datetime():
    test_datetime = from_string("2019-12-05T10:26:54+00:00")

    assert test_datetime.second == 54
    assert test_datetime.minute == 26
    assert test_datetime.hour == 10
    assert test_datetime.day == 5
    assert test_datetime.month == 12
    assert test_datetime.year == 2019