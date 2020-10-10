import sys
sys.path.append('..')

import pytest

from aiess import Beatmapset, User
from scraper.requester import request_discussions_json

from scraper.parsers.discussion_parser import discussion_parser

@pytest.fixture(scope="session")
def discussions_json():
    return request_discussions_json(beatmapset_id=1001546)

def test_parse(discussions_json):
    beatmapset = Beatmapset(_id=1001546, artist="Carpool Tunnel", title="Afterlight", creator=User(_id=7342798, name="_Epreus"), modes=["osu"])
    discussions = discussion_parser.parse(discussions_json=discussions_json, beatmapset=beatmapset)
    for discussion in discussions:
        assert discussion
        assert discussion.id
        assert discussion.beatmapset == beatmapset
        assert discussion.user
        assert discussion.content is not None
        assert discussion.tab is not None

def test_parse_discussion(discussions_json):
    beatmapset = Beatmapset(_id=1001546, artist="Carpool Tunnel", title="Afterlight", creator=User(_id=7342798, name="_Epreus"), modes=["osu"])
    discussion_jsons = discussions_json["beatmapset"]["discussions"]
    for discussion_json in discussion_jsons:
        if not discussion_json: continue

        discussion = discussion_parser.parse_discussion(
            discussion_json = discussion_json,
            beatmapset_json = discussions_json["beatmapset"],
            beatmapset      = beatmapset
        )
        assert discussion
        assert discussion.id
        assert discussion.beatmapset == beatmapset
        assert discussion.user
        assert discussion.content is not None
        assert discussion.tab is not None

def test_parse_user(discussions_json):
    discussion_jsons = discussions_json["beatmapset"]["discussions"]
    for discussion_json in discussion_jsons:
        if not discussion_json: continue

        user = discussion_parser.parse_user(user_id=discussion_json["user_id"], beatmapset_json=discussions_json["beatmapset"])
        assert user
        assert user.id
        assert user.name

def test_parse_discussion_post_author(discussions_json):
    discussion_jsons = discussions_json["beatmapset"]["discussions"]
    for discussion_json in discussion_jsons:
        if not discussion_json: continue

        user = discussion_parser.parse_discussion_post_author(post_id=3016640, beatmapset_json=discussions_json["beatmapset"])
        assert user
        assert user.id
        assert user.name

def test_parse_tab(discussions_json):
    discussion_jsons = discussions_json["beatmapset"]["discussions"]
    tabs = set()
    for discussion_json in discussion_jsons:
        if not discussion_json: continue

        tab = discussion_parser.parse_tab(discussion_json=discussion_json, beatmapset_json=discussions_json["beatmapset"])
        tabs.add(tab)
        assert tab
    
    assert "timeline" in tabs
    assert "general" in tabs
    assert "generalAll" in tabs

def test_parse_diff(discussions_json):
    discussion_jsons = discussions_json["beatmapset"]["discussions"]
    difficulties = set()
    for discussion_json in discussion_jsons:
        if not discussion_json: continue

        difficulty = discussion_parser.parse_diff(discussion_json=discussion_json, beatmapset_json=discussions_json["beatmapset"])
        difficulties.add(difficulty)
    
    for beatmap_json in discussions_json["beatmapset"]["beatmaps"]:
        assert beatmap_json["version"] in difficulties