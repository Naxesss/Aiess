import sys
sys.path.append('..')

import pytest
from datetime import datetime

from aiess import Event, User, Beatmapset, Discussion, NewsPost

from bot.filterer import escape
from bot.filterer import dissect
from bot.filterer import passes_filter
from bot.filterer import get_tag
from bot.filterer import get_tag_keys
from bot.filterer import get_key_value_pairs
from bot.filterer import get_invalid_keys
from bot.filterer import get_invalid_filters
from bot.filterer import get_invalid_words
from bot.filterer import is_valid
from bot.filterer import filter_to_sql

def test_escape():
    assert escape("withoutspace") == "withoutspace"
    assert escape("with space") == "\"with space\""

def test_escape_int():
    assert escape(42) == "42"

def test_dissect_simple():
    event = Event(_type="test", time=datetime.utcnow())
    assert dissect(event) == ["type:test"]

def test_dissect_user():
    user = User(2, "some two")
    event = Event(_type="test", time=datetime.utcnow(), user=user)
    assert dissect(user) == [
        "user:\"some two\"",
        "user-id:2"
    ]
    assert dissect(event) == ["type:test"] + dissect(user)

def test_dissect_beatmapset():
    user = User(2, "some two")
    beatmapset = Beatmapset(4, artist="yes", title="no", creator=user, modes=["osu", "catch"])
    event = Event(_type="test", time=datetime.utcnow(), beatmapset=beatmapset)
    assert dissect(beatmapset) == [
        "set-id:4",
        "mapset-id:4",
        "beatmapset-id:4",
        "artist:yes",
        "title:no",
        "creator:\"some two\"",
        "creator-id:2",
        "mode:osu",
        "mode:catch"
    ]
    assert dissect(event) == ["type:test"] + dissect(beatmapset)

def test_dissect_discussion():
    user = User(1, "some one")
    creator = User(2, "some two")
    beatmapset = Beatmapset(4, artist="yes", title="no", creator=creator, modes=["osu", "catch"])
    discussion = Discussion(3, beatmapset=beatmapset, user=user, content="hello")
    event = Event(_type="test", time=datetime.utcnow(), beatmapset=beatmapset, discussion=discussion, user=user, content="hello")

    dissection = dissect(discussion)
    for pair in [
        "discussion-id:3",
        "author:\"some one\"",
        "author-id:1",
        "discussion-content:hello"
    ]:
        assert pair in dissection

    event_dissection = dissect(event)
    for pair in (["type:test"] + dissect(discussion) + dissect(user) + ["content:hello"]):
        assert pair in event_dissection

def test_dissect_discussion_reply():
    user = User(1, "some one")
    creator = User(2, "some two")
    replier = User(3, "some three")
    beatmapset = Beatmapset(4, artist="yes", title="no", creator=creator, modes=["osu", "catch"])
    discussion = Discussion(3, beatmapset=beatmapset, user=user, content="hello")
    event = Event(_type="reply", time=datetime.utcnow(), beatmapset=beatmapset, discussion=discussion, user=replier, content="there")

    event_dissection = dissect(event)
    for pair in (["type:reply"] + dissect(discussion) + dissect(replier) + ["content:there"]):
        assert pair in event_dissection

def test_dissect_newspost():
    user = User(2, "some two")
    newspost = NewsPost(_id=4, title="title", preview="preview", author=user, slug="slug", image_url="image_url")
    event = Event(_type="test", time=datetime.utcnow(), newspost=newspost, content="preview")

    dissection = dissect(newspost)
    for pair in [
        "news-title:title",
        "news-content:preview",
        "news-preview:preview",
        "news-author:\"some two\"",
        "news-author-id:2"
    ]:
        assert pair in dissection
    
    assert dissect(event) == ["type:test", "content:preview"] + dissect(newspost)

def test_dissect_aliases():
    event = Event(_type="nominate", time=datetime.utcnow())

    assert "type:nominate" in dissect(event)
    assert "type:nomination" in dissect(event)
    assert "type:nominated" in dissect(event)
    assert "type:bubbled" in dissect(event)

def test_dissect_aliases_whitespace_substitution():
    event = Event(_type="kudosu_gain", time=datetime.utcnow())

    assert "type:kudosu_gain" in dissect(event)
    assert "type:\"kudosu gain\"" in dissect(event)
    assert "type:kudosu-gain" in dissect(event)

def test_passes_filter():
    assert passes_filter("type:reply", ["mode:osu", "type:reply"])
    assert not passes_filter("type:qualify", ["mode:osu", "type:reply"])

def test_passes_filter_or():
    assert passes_filter("type:reply or mode:taiko", ["mode:osu", "type:reply"])
    assert passes_filter("type:reply or mode:taiko", ["mode:taiko", "type:qualify"])
    assert not passes_filter("type:reply or mode:taiko", ["mode:osu", "type:qualify"])

def test_passes_filter_and():
    assert passes_filter("type:reply and mode:taiko", ["mode:taiko", "type:reply"])
    assert not passes_filter("type:reply and mode:taiko", ["mode:osu", "type:reply"])
    assert not passes_filter("type:reply and mode:taiko", ["mode:taiko", "type:qualify"])

def test_passes_filter_and_not():
    assert passes_filter("type:reply and not mode:taiko", ["mode:catch", "type:reply"])
    assert passes_filter("type:reply and !mode:taiko", ["mode:catch", "type:reply"])
    assert not passes_filter("type:reply and not mode:taiko", ["mode:taiko", "type:reply"])
    assert not passes_filter("type:reply and not mode:taiko", ["mode:osu", "type:qualify"])

def test_passes_filter_missing_field():
    assert not passes_filter("content:hi", ["user:sometwo", "type:nominate"])
    assert passes_filter("not content:hi", ["user:sometwo", "type:nominate"])

def test_passes_filter_case_sensitivity():
    assert passes_filter("type:Reply AND mode:OSU", ["mode:osu", "type:reply"])
    assert not passes_filter("TYPE:QUALIFY", ["mode:osu", "type:reply"])

def test_passes_filter_event_object():
    beatmapset = Beatmapset(3, "artist", "title", creator=User(1, "someone"), modes=["osu"])
    event = Event(_type="nominate", time=datetime.utcnow(), beatmapset=beatmapset, user=User(2, "sometwo"))

    assert passes_filter("type:nominate and user:sometwo", event)
    assert not passes_filter("type:reply", event)



def test_get_tag():
    assert get_tag("user")
    assert get_tag("user-id")
    assert get_tag("set-id")

def test_get_tag_keys():
    assert get_tag_keys("user") == ("user",)
    assert get_tag_keys("set-id") == ("set-id", "mapset-id", "beatmapset-id")

def test_get_tag_undefined():
    assert not get_tag("undefined")

def test_get_key_value_pairs():
    assert list(get_key_value_pairs("user:someone and content:test")) == [("user", "someone"), ("content", "test")]

def test_invalid_keys():
    assert list(get_invalid_keys("content:test or undefined:test and mpaset-id:12389")) == ["undefined", "mpaset-id"]

def test_invalid_filter_freetext():
    assert list(get_invalid_filters("content:\"askjda kjsfh jgniqweunf\" or user:kjfhakjshd")) == []

def test_invalid_filter_modes():
    assert list(get_invalid_filters("mode:test or mode:osu or mode:catch")) == [("mode", "test")]

def test_invalid_filter_ids():
    assert (
        list(get_invalid_filters("user-id:test or mapset-id:\"test two\" or user-id:12381031")) ==
        [("user-id", "test"), ("mapset-id", "test two")]
    )

def test_invalid_filter_types():
    assert list(get_invalid_filters("type:undefined or user:someone or type:qualify")) == [("type", "undefined")]

def test_invalid_filter_types_alias():
    assert list(get_invalid_filters("type:nom or type:nomnom or type:qual")) == [("type", "nomnom")]

def test_invalid_filter_types_escaped():
    assert list(get_invalid_filters("type:\"kudosu gain\" or type:\"something else\"")) == [("type", "something else")]

def test_invalid_filter_types_multiple():
    assert (
        list(get_invalid_filters("type:undefined or type:nominate or user:someone and type:\"something else\"")) ==
        [("type", "undefined"), ("type", "something else")]
    )

def test_invalid_words_missed_colon():
    assert list(get_invalid_words("typequalify or type:nominate")) == ["typequalify"]

def test_invalid_words_typoed_and():
    assert list(get_invalid_words("user:someone annd type:nominate")) == ["annd"]

def test_invalid_words_unexpanded():
    assert list(get_invalid_words("user:(someone or sometwo) and type: not (nominate or qualify)")) == []

def test_invalid_words_quotations():
    assert list(get_invalid_words("user:\"some one else\" or type:\"kudosu given\"")) == []

def test_valid_keys():
    assert is_valid("type:nominate")
    assert not is_valid("undefined:nominate")

def test_valid_values():
    assert is_valid("type:nominate")
    assert not is_valid("type:undefined")

def test_valid_words():
    assert is_valid("type:nominate and user:someone")
    assert not is_valid("type:nominate annd user:someone")



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

def test_filter_to_sql_content_wildcards():
    assert filter_to_sql("content:\"%hello there%\"") == ("events.content LIKE %s", ("%hello there%",))

def test_filter_to_sql_malicious():
    # Database drivers should take care of escaping anything within the second portion of the tuple, so
    # that's where we want the attacking string.
    assert filter_to_sql("user:\"%s; DROP TABLE events; \"\"=\"\"") == ("user.name LIKE %s", ("%s; DROP TABLE events; ",))

def test_filter_to_sql_none():
    assert filter_to_sql(None) == ("TRUE", ())