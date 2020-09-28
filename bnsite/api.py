import sys
sys.path.append('..')

import json
from typing import Tuple

from aiess.web.ratelimiter import request_with_rate_limit
from aiess.settings import BNSITE_RATE_LIMIT, BNSITE_HEADERS

cache = {}
def request(route: str, query: str) -> object:
    """Requests the page from the given route and query.
    Caches any response such that requesting the same discussion id yields the same result."""
    request_url = f"https://bn.mappersguild.com/interOp/{route}/{query}"
    if request_url in cache:
        return cache[request_url]

    response = request_with_rate_limit(
        request_url   = request_url,
        rate_limit    = BNSITE_RATE_LIMIT,
        rate_limit_id = "bnsite",
        headers       = BNSITE_HEADERS
    )
    try:
        result = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        # This happens whenever the response text is empty (e.g. "[]").
        result = None
    
    cache[request_url] = result
    return result

def request_removal_reason(user_id: int) -> object:
    """Returns the reason for a bn being removed given their user id. Caches results."""
    return request("bnRemoval", query=user_id)

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

def request_qa_checks(user_id: int) -> object:
    """Returns all quality assurance checks done by the user with the given user id. Caches results."""
    return request("qaEventsByUser", query=user_id)