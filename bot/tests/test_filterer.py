import sys
sys.path.append('..')

import pytest
import mock
from datetime import datetime

from aiess import Event, User, Beatmapset, Discussion, NewsPost

from bot.filterers.event_filterer import filter_context
from bot.filterers.event_filterer import filter_to_sql

from bot.filterer import escape
from bot.filterer import unescape
from bot.filterer import get_key_value_pairs
from bot.filterer import get_invalid_keys
from bot.filterer import get_invalid_filters
from bot.filterer import get_invalid_words
from bot.filterer import is_valid

def no_api_allowed(*args):
    raise ValueError("The api should not be used here!")

def test_escape():
    assert escape("withoutspace") == "withoutspace"
    assert escape("with space") == "\"with space\""

def test_escape_int():
    assert escape(42) == "42"

def test_unescape():
    assert unescape("\"normal \"quotes\"\"") == "normal \"quotes\""

def test_unescape_different_quotes():
    assert unescape("”“different \"quotes”\"“") == "different \"quotes”"

def test_unescape_no_quotes():
    assert unescape("no quotes") == "no quotes"

def test_dissect_simple():
    event = Event(_type="test", time=datetime.utcnow())
    assert filter_context.dissect(event) == ["type:test"]

def test_dissect_user():
    user = User(2, "some two")
    event = Event(_type="test", time=datetime.utcnow(), user=user)
    assert filter_context.dissect(event) == [
        "user:\"some two\"",
        "user-id:2",
        "type:test"
    ]

@mock.patch("aiess.objects.api.request_api", no_api_allowed)  # If we get this, simply add the new properties to the test!
def test_dissect_beatmapset():
    user = User(2, "some two")
    beatmapset = Beatmapset(4, artist="yes", title="no", creator=user, modes=["osu", "catch"], genre="g", language="l", tags=["tag1", "tag2"])
    event = Event(_type="test", time=datetime.utcnow(), beatmapset=beatmapset)
    assert filter_context.dissect(event) == [
        "set-id:4",
        "mapset-id:4",
        "beatmapset-id:4",
        "artist:yes",
        "title:no",
        "creator:\"some two\"",
        "creator-id:2",
        "mode:osu",
        "mode:catch",
        "genre:g",
        "language:l",
        "tag:tag1",
        "tags:tag1",
        "tag:tag2",
        "tags:tag2",
        "type:test"
    ]

def test_dissect_discussion():
    user = User(1, "some one")
    creator = User(2, "some two")
    beatmapset = Beatmapset(4, creator=creator, allow_api=False)
    discussion = Discussion(3, beatmapset=beatmapset, user=user, content="hello")
    event = Event(_type="test", time=datetime.utcnow(), beatmapset=beatmapset, discussion=discussion, user=user, content="hello")

    event_dissection = filter_context.dissect(event)
    for pair in [
        "type:test",
        "content:hello",
        "discussion-id:3",
        "author:\"some one\"",
        "author-id:1",
        "discussion-content:hello"
    ]:
        assert pair in event_dissection

def test_dissect_discussion_reply():
    user = User(1, "some one")
    creator = User(2, "some two")
    replier = User(3, "some three")
    beatmapset = Beatmapset(4, creator=creator, allow_api=False)
    discussion = Discussion(3, beatmapset=beatmapset, user=user, content="hello")
    event = Event(_type="reply", time=datetime.utcnow(), beatmapset=beatmapset, discussion=discussion, user=replier, content="there")

    event_dissection = filter_context.dissect(event)
    for pair in [
        "user:\"some three\"",
        "user-id:3",
        "author:\"some one\"",
        "author-id:1",
        "type:reply",
        "content:there"
    ]:
        assert pair in event_dissection

def test_dissect_newspost():
    user = User(2, "some two")
    newspost = NewsPost(_id=4, title="title", preview="preview", author=user, slug="slug", image_url="image_url")
    event = Event(_type="test", time=datetime.utcnow(), newspost=newspost, content="preview")
    
    assert filter_context.dissect(event) == [
        "news-title:title",
        "news-content:preview",
        "news-preview:preview",
        "news-author:\"some two\"",
        "news-author-id:2",
        "type:test",
        "content:preview"
    ]

def test_dissect_aliases():
    event = Event(_type="nominate", time=datetime.utcnow())

    assert "type:nominate" in filter_context.dissect(event)
    assert "type:nomination" in filter_context.dissect(event)
    assert "type:nominated" in filter_context.dissect(event)
    assert "type:bubbled" in filter_context.dissect(event)

def test_dissect_aliases_whitespace_substitution():
    event = Event(_type="kudosu_gain", time=datetime.utcnow())

    assert "type:kudosu_gain" in filter_context.dissect(event)
    assert "type:\"kudosu gain\"" in filter_context.dissect(event)
    assert "type:kudosu-gain" in filter_context.dissect(event)

def test_passes_filter():
    assert filter_context.test("type:reply", ["mode:osu", "type:reply"])
    assert not filter_context.test("type:qualify", ["mode:osu", "type:reply"])

def test_passes_filter_or():
    assert filter_context.test("type:reply or mode:taiko", ["mode:osu", "type:reply"])
    assert filter_context.test("type:reply or mode:taiko", ["mode:taiko", "type:qualify"])
    assert not filter_context.test("type:reply or mode:taiko", ["mode:osu", "type:qualify"])

def test_passes_filter_and():
    assert filter_context.test("type:reply and mode:taiko", ["mode:taiko", "type:reply"])
    assert not filter_context.test("type:reply and mode:taiko", ["mode:osu", "type:reply"])
    assert not filter_context.test("type:reply and mode:taiko", ["mode:taiko", "type:qualify"])

def test_passes_filter_and_not():
    assert filter_context.test("type:reply and not mode:taiko", ["mode:catch", "type:reply"])
    assert not filter_context.test("type:reply and not mode:taiko", ["mode:taiko", "type:reply"])
    assert not filter_context.test("type:reply and not mode:taiko", ["mode:osu", "type:qualify"])

def test_passes_filter_missing_field():
    assert not filter_context.test("content:hi", ["user:sometwo", "type:nominate"])
    assert filter_context.test("not content:hi", ["user:sometwo", "type:nominate"])

def test_passes_filter_case_sensitivity():
    assert filter_context.test("type:Reply AND mode:OSU", ["mode:osu", "type:reply"])
    assert not filter_context.test("TYPE:QUALIFY", ["mode:osu", "type:reply"])

def test_passes_filter_percent_wildcard():
    assert filter_context.test("content:%something%", ["content:someone or something"])
    assert filter_context.test("content:%something", ["content:someone or something"])
    assert filter_context.test("%", ["content:someone or something"])
    assert not filter_context.test("content:something%", ["content:someone or something"])
    assert not filter_context.test("content:%something else%", ["content:someone or something"])

def test_passes_filter_underscore_wildcard():
    assert filter_context.test("content:so_ething", ["content:something"])
    assert filter_context.test("content:someth___", ["content:something"])
    assert not filter_context.test("content:something_", ["content:something"])
    assert not filter_context.test("content:some_thing", ["content:something"])

def test_passes_filter_partial():
    assert not filter_context.test("type:reply", ["special-type:reply"])
    assert not filter_context.test("type:reply", ["type:reply-special"])

def test_passes_filter_event_object():
    beatmapset = Beatmapset(3, allow_api=False)
    event = Event(_type="nominate", time=datetime.utcnow(), beatmapset=beatmapset, user=User(2, "sometwo"))

    assert filter_context.test("type:nominate and user:sometwo", event)
    assert not filter_context.test("type:reply", event)

def test_passes_filter_conversion():
    assert filter_context.test("tags:\"mappers' guild\"",   ["tags:mappers'", "tags:guild"])
    assert filter_context.test("tag:\"mappers' guild\"",    ["tag:mappers'",  "tag:guild" ])
    assert filter_context.test("tags:(mappers' and guild)", ["tags:mappers'", "tags:guild"])



def test_get_tag():
    assert filter_context.get_tag("user")
    assert filter_context.get_tag("user-id")
    assert filter_context.get_tag("set-id")

def test_get_tag_undefined():
    assert not filter_context.get_tag("undefined")

def test_get_key_value_pairs():
    assert list(get_key_value_pairs("user:someone and content:test")) == [("user", "someone"), ("content", "test")]

def test_invalid_keys():
    assert list(get_invalid_keys("content:test or undefined:test and mpaset-id:12389", filter_context)) == ["undefined", "mpaset-id"]

def test_invalid_filter_freetext():
    assert list(get_invalid_filters("content:\"askjda kjsfh jgniqweunf\" or user:kjfhakjshd", filter_context)) == []

def test_invalid_filter_modes():
    assert list(get_invalid_filters("mode:test or mode:osu or mode:catch", filter_context)) == [("mode", "test")]

def test_invalid_filter_ids():
    assert (
        list(get_invalid_filters("user-id:test or mapset-id:\"test two\" or user-id:12381031", filter_context)) ==
        [("user-id", "test"), ("mapset-id", "test two")]
    )

def test_invalid_filter_types():
    assert list(get_invalid_filters("type:undefined or user:someone or type:qualify", filter_context)) == [("type", "undefined")]

def test_invalid_filter_types_alias():
    assert list(get_invalid_filters("type:nom or type:nomnom or type:qual", filter_context)) == [("type", "nomnom")]

def test_invalid_filter_types_escaped():
    assert list(get_invalid_filters("type:\"kudosu gain\" or type:\"something else\"", filter_context)) == [("type", "something else")]

def test_invalid_filter_types_multiple():
    assert (
        list(get_invalid_filters("type:undefined or type:nominate or user:someone and type:\"something else\"", filter_context)) ==
        [("type", "undefined"), ("type", "something else")]
    )

def test_invalid_words_missed_colon():
    assert list(get_invalid_words("typequalify or type:nominate")) == ["typequalify"]

def test_invalid_words_typoed_and():
    assert list(get_invalid_words("user:someone annd type:nominate")) == ["annd"]

def test_invalid_words_unexpanded():
    assert list(get_invalid_words("user:(someone or sometwo) and type:not (nominate or qualify)")) == []

def test_invalid_words_quotations():
    assert list(get_invalid_words("user:\"some one else\" or type:\"kudosu given\"")) == []

def test_valid_keys():
    assert is_valid("type:nominate", filter_context)
    assert not is_valid("undefined:nominate", filter_context)

def test_valid_values():
    assert is_valid("type:nominate", filter_context)
    assert not is_valid("type:undefined", filter_context)

def test_valid_words():
    assert is_valid("type:nominate and user:someone", filter_context)
    assert not is_valid("type:nominate annd user:someone", filter_context)



def test_filter_to_sql():
    assert filter_to_sql("type:nominate and not user:someone") == ("type=%s AND NOT user.name LIKE %s", ("nominate", "someone"))

def test_filter_to_sql_quotations():
    assert filter_to_sql("user:\"space in name\"") == ("user.name LIKE %s", ("space in name",))

def test_filter_to_sql_invalid_key():
    with pytest.raises(ValueError) as err:
        filter_to_sql("user:someone and undefined:nominate")
    assert "invalid" in str(err)

def test_filter_to_sql_invalid_value():
    with pytest.raises(ValueError) as err:
        filter_to_sql("user:someone and type:undefined")
    assert "invalid" in str(err)

def test_filter_to_sql_invalid_words():
    with pytest.raises(ValueError) as err:
        filter_to_sql("user:someone and nothing else")
    assert "invalid" in str(err)

def test_filter_to_sql_content_multiple_aliases():
    assert filter_to_sql("group:bn") == ("(group_id=%s OR group_id=%s)", ("28", "32"))

def test_filter_to_sql_content_wildcards():
    assert filter_to_sql("content:\"%hello there%\"") == ("events.content LIKE %s", ("%hello there%",))

def test_filter_to_sql_malicious():
    # Database drivers should take care of escaping anything within the second portion of the tuple, so
    # that's where we want the attacking string.
    assert filter_to_sql("user:\"%s; DROP TABLE events; \"\"=\"\"") == ("user.name LIKE %s", ("%s; DROP TABLE events; ",))

def test_filter_to_sql_none():
    assert filter_to_sql(None) == ("TRUE", ())