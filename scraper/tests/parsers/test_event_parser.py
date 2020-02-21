import pytest
from datetime import datetime

from tests.mocks.events import issue_resolve, nominate, problem
from tests.mocks.events.faulty import no_events, deleted_beatmap
from parsers.beatmapset_event_parser import beatmapset_event_parser
from parsers.discussion_event_parser import discussion_event_parser
from parsers.time_parser import from_ISO_8601_to_datetime
from exceptions import ParsingError, DeletedContextError

def test_parse_event_type():
    tests = [
        [beatmapset_event_parser.parse_event_type(issue_resolve.tag), "issue-resolve"],
        [beatmapset_event_parser.parse_event_type(nominate.tag), "nominate"],
        [discussion_event_parser.parse_event_type(problem.tag), "problem"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_type_faulty():
    faulty_values = [
        no_events.tag,
        None
    ]

    for value in faulty_values:
        with pytest.raises(ParsingError):
            beatmapset_event_parser.parse_event_type(value)
    
    for value in faulty_values:
        with pytest.raises(ParsingError):
            discussion_event_parser.parse_event_type(value)

def test_parse_event_time():
    tests = [
        [beatmapset_event_parser.parse_event_time(issue_resolve.tag), from_ISO_8601_to_datetime("2019-12-05T10:26:54+00:00")],
        [beatmapset_event_parser.parse_event_time(nominate.tag), from_ISO_8601_to_datetime("2019-12-05T12:39:39+00:00")],
        [discussion_event_parser.parse_event_time(problem.tag), from_ISO_8601_to_datetime("2019-12-05T16:50:10+00:00")]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_time_faulty():
    faulty_values = [
        no_events.tag,
        None
    ]

    for value in faulty_values:
        with pytest.raises(ParsingError):
            beatmapset_event_parser.parse_event_time(value)
    
    for value in faulty_values:
        with pytest.raises(ParsingError):
            discussion_event_parser.parse_event_time(value)

def test_parse_event_link():
    tests = [
        [beatmapset_event_parser.parse_event_link(issue_resolve.tag), "https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675"],
        [beatmapset_event_parser.parse_event_link(nominate.tag), "https://osu.ppy.sh/beatmapsets/1013400/discussion"],
        [discussion_event_parser.parse_event_link(problem.tag), "https://osu.ppy.sh/beatmapsets/1074596/discussion#/1295203"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_link_faulty():
    faulty_values = [
        [no_events.tag, ParsingError],
        [deleted_beatmap.tag, DeletedContextError],
        [None, ParsingError]
    ]

    for value, expected_exception in faulty_values:
        with pytest.raises(expected_exception):
            beatmapset_event_parser.parse_event_link(value)
    
    for value, expected_exception in faulty_values:
        with pytest.raises(expected_exception):
            discussion_event_parser.parse_event_link(value)

def test_parse_author_id():
    tests = [
        [beatmapset_event_parser.parse_event_author_id(issue_resolve.tag), None],
        [beatmapset_event_parser.parse_event_author_id(nominate.tag), "1653229"],
        [discussion_event_parser.parse_event_author_id(problem.tag), "197805"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_author_id_faulty():
    faulty_values = [
        [no_events.tag, ParsingError],
        [deleted_beatmap.tag, DeletedContextError],
        [None, ParsingError]
    ]

    for value, expected_exception in faulty_values:
        assert beatmapset_event_parser.parse_event_author_id(value) == None
    
    for value, expected_exception in faulty_values:
        with pytest.raises(expected_exception):
            discussion_event_parser.parse_event_author_id(value)

def test_parse_author_name():
    tests = [
        [beatmapset_event_parser.parse_event_author_name(issue_resolve.tag), None],
        [beatmapset_event_parser.parse_event_author_name(nominate.tag), "_Stan"],
        [discussion_event_parser.parse_event_author_name(problem.tag), "Niva"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_event_author_name_faulty():
    faulty_values = [
        [no_events.tag, ParsingError],
        [deleted_beatmap.tag, DeletedContextError],
        [None, ParsingError]
    ]

    for value, expected_exception in faulty_values:
        assert beatmapset_event_parser.parse_event_author_name(value) == None
    
    for value, expected_exception in faulty_values:
        with pytest.raises(expected_exception):
            discussion_event_parser.parse_event_link(value)

def test_parse_id_from_user_link():
    tests = [
        [beatmapset_event_parser.parse_id_from_user_link(None), None],
        [discussion_event_parser.parse_id_from_user_link("https://osu.ppy.sh/beatmapsets/1074596"), None],
        [beatmapset_event_parser.parse_id_from_user_link("https://osu.ppy.sh/users/1653229"), "1653229"],
        [discussion_event_parser.parse_id_from_user_link("https://osu.ppy.sh/users/197805/modding"), "197805"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_id_from_discussion_link():
    tests = [
        [beatmapset_event_parser.parse_id_from_discussion_link(None), None],
        [discussion_event_parser.parse_id_from_discussion_link("https://osu.ppy.sh/beatmapsets/1074596"), None],
        [beatmapset_event_parser.parse_id_from_discussion_link("https://osu.ppy.sh/beatmapsets/1013400/discussion"), None],
        [discussion_event_parser.parse_id_from_discussion_link("https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675"), "1294675"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_parse_id_from_beatmapset_link():
    tests = [
        [beatmapset_event_parser.parse_id_from_beatmapset_link(None), None],
        [beatmapset_event_parser.parse_id_from_beatmapset_link("https://osu.ppy.sh/users/1653229"), None],
        [discussion_event_parser.parse_id_from_beatmapset_link("https://osu.ppy.sh/beatmapsets/1074596"), "1074596"],
        [discussion_event_parser.parse_id_from_beatmapset_link("https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675"), "1011055"]
    ]

    for actual, expected in tests:
        assert actual == expected

def test_from_ISO_8601_to_datetime_raise():
    faulty_values = [
        None,
        "",
        "https://osu.ppy.sh/users/1653229"
    ]

    for value in faulty_values:
        with pytest.raises(ValueError):
            from_ISO_8601_to_datetime(value)

def test_from_ISO_8601_to_datetime():
    test_datetime = from_ISO_8601_to_datetime("2019-12-05T10:26:54+00:00")

    assert test_datetime.second == 54
    assert test_datetime.minute == 26
    assert test_datetime.hour == 10
    assert test_datetime.day == 5
    assert test_datetime.month == 12
    assert test_datetime.year == 2019