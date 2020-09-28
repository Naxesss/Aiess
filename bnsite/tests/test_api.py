import sys
sys.path.append('..')

from datetime import datetime

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

def test_request_removal_reason():
    # https://osu.ppy.sh/users/5999631
    json = api.request_removal_reason(user_id=5999631)
    assert json
    assert json["action"] == "Kicked"
    assert from_string(json["timestamp"])

def test_request_removal_reason_missing():
    json = api.request_removal_reason(user_id=4)
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

def test_request_qa_checks():
    json = api.request_qa_checks(user_id=10974170)
    assert json
    assert json[0]
    assert int(json[0]["beatmapsetId"])
    assert from_string(json[0]["timestamp"])

def test_request_qa_checks_none():
    json = api.request_qa_checks(user_id=5128277)
    assert not json

def test_request_qa_checks_missing():
    json = api.request_qa_checks(user_id=4)
    assert not json