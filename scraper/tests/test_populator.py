import sys
sys.path.append('..')

import pytest

from aiess.objects import Beatmapset, Discussion
from aiess.errors import ParsingError
from aiess.tests.mocks.api import beatmap as mock_beatmap
from aiess.tests.mocks.api import old_beatmap as mock_old_beatmap
from aiess.database import SCRAPER_TEST_DB_NAME

from scraper.populator import get_complete_discussion_info

def test_old_discussion():
    beatmapset = Beatmapset(41823, beatmapset_json=mock_old_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset)
    
    # Can't obtain any discussion data from a beatmapset that doesn't have a discussion interface.
    with pytest.raises(ParsingError):
        get_complete_discussion_info(discussion, beatmapset, db_name=SCRAPER_TEST_DB_NAME)

def test_discussion():
    beatmapset = Beatmapset(1001546, beatmapset_json=mock_beatmap.JSON)
    discussion = Discussion(1234956, beatmapset)

    # Some information will not be available until it is supplied by other sources
    # (e.g. discussion jsons, prior database entires, scraping)
    discussion = get_complete_discussion_info(discussion, beatmapset, db_name=SCRAPER_TEST_DB_NAME)

    assert discussion.user.id == "4967662"
    assert discussion.user.name == "greenhue"
    assert discussion.content == "since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms."