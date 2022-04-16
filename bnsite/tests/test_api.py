import sys
sys.path.append('..')

from datetime import datetime, timedelta

from aiess.timestamp import from_string
from bnsite import api

def setup_function():
    api.cache.clear()

def test_request():
    # https://osu.ppy.sh/beatmapsets/1179039/discussion#/1755074
    json = api.request(route="dqInfoByDiscussionId", query=1755074)
    assert json
    assert json["obviousness"] == 0
    assert json["severity"] == 0

def test_request_cached():
    # Not cached, needs to be retrieved with bnsite API rate limit.
    time = datetime.utcnow()
    json1 = api.request(route="dqInfoByDiscussionId", query=1755074)
    json2 = api.request(route="dqInfoByDiscussionId", query=1824796)
    delta_time = datetime.utcnow() - time

    assert delta_time.total_seconds() > 1

    # Cached, should be pretty much instant.
    time = datetime.utcnow()
    json1_cached = api.request(route="dqInfoByDiscussionId", query=1755074)
    json2_cached = api.request(route="dqInfoByDiscussionId", query=1824796)
    delta_time = datetime.utcnow() - time

    assert delta_time.total_seconds() < 0.1
    assert json1 == json1_cached
    assert json2 == json2_cached

def test_request_last_eval_kick():
    # https://osu.ppy.sh/users/5875419
    json = api.request_last_eval(user_id=5875419)
    assert json
    assert json["consensus"] == "removeFromBn"
    assert from_string(json["updatedAt"])

def test_request_last_eval_resign():
    # https://osu.ppy.sh/users/1263669
    json = api.request_last_eval(user_id=8140944)
    assert json
    assert json["kind"] == "resignation"
    assert from_string(json["updatedAt"])

def test_request_last_eval_missing():
    json = api.request_last_eval(user_id=4)
    assert not json

def test_request_user_info():
    # https://osu.ppy.sh/users/8129817
    json = api.request_user_info(user_id=8129817)
    assert json
    assert json["username"] == "Naxess"
    assert json["modes"] == ["osu"]

def test_request_user_info_missing():
    json = api.request_user_info(user_id=4)
    assert not json

def test_request_dq_info():
    # https://osu.ppy.sh/beatmapsets/1179039/discussion#/1755074
    json = api.request_dq_info(discussion_id=1755074)
    assert json
    assert json["obviousness"] == 0
    assert json["severity"] == 0

def test_request_dq_info_missing():
    json = api.request_dq_info(discussion_id=4)
    assert not json

def test_request_sev_events():
    tuples = api.request_discussion_sev(datetime.utcnow() - timedelta(days=7))
    assert tuples
    amount = 0
    for discussion_id, obv, sev, time in tuples:
        assert discussion_id is not None
        assert obv is not None or sev is not None
        assert time is not None
        amount += 1
    
    assert amount > 10