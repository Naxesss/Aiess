import sys
sys.path.append('..')

import json
from typing import Tuple, Generator
from datetime import datetime

from aiess.web.ratelimiter import request_with_rate_limit
from aiess.settings import BNSITE_RATE_LIMIT, BNSITE_HEADERS
from aiess import timestamp

cache = {}
def request(route: str, query: str, allow_cache: bool=True) -> object:
    """Requests the page from the given route and query.
    Caches any response such that requesting the same discussion id yields the same result."""
    request_url = f"https://bn.mappersguild.com/interOp/{route}/{query}"
    if request_url in cache and cache[request_url] and allow_cache:
        return cache[request_url]

    response = request_with_rate_limit(
        request_url   = request_url,
        rate_limit    = BNSITE_RATE_LIMIT,
        rate_limit_id = "bnsite",
        headers       = BNSITE_HEADERS,
        timeout       = 10
    )
    try:
        result = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        # This happens whenever the response text is empty (e.g. "[]").
        result = None
    
    cache[request_url] = result
    return result

def request_last_eval(user_id: int) -> object:
    """Returns the last updated evaluation associated with a user given their user id. Caches results."""
    return request("latestEvaluation", query=user_id)

def request_user_info(user_id: int) -> str:
    """Returns the data associated with a user given their user id. Caches results."""
    return request("users", query=user_id)

def request_dq_info(discussion_id: int) -> object:
    """Returns the disqualification info (SEV, QAH checkers, etc) associated with the given
    discussion id. Caches results."""
    return request("dqInfoByDiscussionId", query=discussion_id)

def request_obv_sev(discussion_id: int) -> Tuple[int, int]:
    """Returns a tuple of the obviousness (0-2) and severity (0-3) ratings from the disqualification
    associated with the given discussion id, if any, otherwise a (None, None) tuple. Caches results."""
    dq_info_json = request_dq_info(discussion_id)
    if not dq_info_json:
        return (None, None)
    
    return (dq_info_json["obviousness"], dq_info_json["severity"])

def request_discussion_sev(since: datetime) -> Generator[Tuple[int, int, int, datetime], None, None]:
    """Returns a list of tuples representing the SEV for a reset `(discussion_id, obv, sev, time)`, since
    the given time. If either the severity or obviousness was unchanged, they will be returned as None.
    If the severity or obviousness were unset, they will be returned as -1."""
    sev_logs = request("eventsByDate", query=timestamp.to_string(since), allow_cache=False)
    discussion_ids = []
    discussion_obv = {}
    discussion_sev = {}
    discussion_time = {}
    for sev_log in sev_logs:
        if "Updated DQ reason" in sev_log["action"] or "Toggled review status" in sev_log["action"]:
            # May find, e.g. "DQ reason updated to \"xyz\"" or "Toggled review status of s/1457453 to false", which isn't what we're looking for.
            continue

        discussion_id = sev_log["relatedId"]["discussionId"]
        if discussion_id not in discussion_ids:
            discussion_ids.append(discussion_id)

        # E.g. "Updated severity of s/1207984 to "0""
        amount_str = sev_log["action"].split(" ")[-1].strip("\"")
        if amount_str == "null":
            amount = -1
        else:
            try:
                amount = int(amount_str)
            except ValueError:
                raise ValueError(f"Could not parse \"{amount_str}\" as int. The entire action is \"{sev_log['action']}\".")

        if "obviousness" in sev_log["action"]: discussion_obv[discussion_id] = amount
        else:                                  discussion_sev[discussion_id] = amount

        time = timestamp.from_string(sev_log["updatedAt"])
        if discussion_id not in discussion_time or time < discussion_time[discussion_id]:
            discussion_time[discussion_id] = time

    # Much more intuitive to receive these in bulk rather than obv/sev separately.
    for discussion_id in discussion_ids:
        obv = discussion_obv[discussion_id] if discussion_id in discussion_obv else None
        sev = discussion_sev[discussion_id] if discussion_id in discussion_sev else None
        time = discussion_time[discussion_id]
        yield (discussion_id, obv, sev, time)