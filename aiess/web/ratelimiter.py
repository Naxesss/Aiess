import requests
from requests import Response
from typing import Dict
from time import sleep
from datetime import datetime, timedelta
from collections import defaultdict
import asyncio

from aiess.logger import log_err, log

next_request_time: Dict[str, datetime] = defaultdict(datetime.utcnow)
failed_attempts: Dict[str, datetime] = defaultdict(int)

async def async_call_with_rate_limit(awaited_result_func, is_result_invalid, rate_limit: float, rate_limit_id: str=None, sleep_if_ratelimited: bool=True) -> Response:
    """Calls `result_func` at most once every `rate_limit` seconds for the same `rate_limit_id` (default None).
    If given an invalid result, backs off exponentially; waiting longer and longer between attempts."""
    global next_request_time
    
    result = None
    while is_result_invalid(result):
        request_time = next_request_time[rate_limit_id]
        if request_time and request_time > datetime.now():
            if not sleep_if_ratelimited:
                return None
            asyncio.sleep((request_time - datetime.now()).total_seconds())

        result = await awaited_result_func()
        next_request_time[rate_limit_id] = datetime.now() + timedelta(seconds=rate_limit)

        if is_result_invalid(result):
            back_off(rate_limit_id)

    if rate_limit_id in failed_attempts:
        failed_attempts[rate_limit_id] = 0

    return result

def call_with_rate_limit(result_func, is_result_invalid, rate_limit: float, rate_limit_id: str=None, sleep_if_ratelimited: bool=True) -> Response:
    """Calls `result_func` at most once every `rate_limit` seconds for the same `rate_limit_id` (default None).
    If given an invalid result, backs off exponentially; waiting longer and longer between attempts."""
    global next_request_time
    
    result = None
    while is_result_invalid(result):
        request_time = next_request_time[rate_limit_id]
        if request_time and request_time > datetime.now():
            if not sleep_if_ratelimited:
                return None
            sleep((request_time - datetime.now()).total_seconds())

        result = result_func()
        next_request_time[rate_limit_id] = datetime.now() + timedelta(seconds=rate_limit)

        if is_result_invalid(result):
            back_off(rate_limit_id)

    if rate_limit_id in failed_attempts:
        failed_attempts[rate_limit_id] = 0

    return result

def request_with_rate_limit(request_url: str, rate_limit: float, rate_limit_id: str=None, method: str="GET", sleep_if_ratelimited: bool=True, **kwargs) -> Response:
    """Requests a response object at most once every rate_limit seconds for the same rate_limit_id (default None).
    Additional keyword arguments are given to the request function (e.g. headers, timeout, etc)."""
    return call_with_rate_limit(
        result_func          = lambda: try_request(request_url, method=method, **kwargs),
        is_result_invalid    = invalid_response,
        rate_limit           = rate_limit,
        rate_limit_id        = rate_limit_id,
        sleep_if_ratelimited = sleep_if_ratelimited
    )

def try_request(request_url: str, method: str="GET", **kwargs) -> Response:
    """Requests a response object and returns it if successful, otherwise None is returned.
    If the website is in cloudflare IUAM mode, we also return None."""
    response = None

    log(f"GET {request_url}", postfix="requests")

    try:
        response = requests.request(method, request_url, **kwargs)
    except requests.exceptions.ConnectionError:
        log_err(f"WARNING | ConnectionError was raised on GET \"{request_url}\"")
        return None
    except requests.exceptions.ReadTimeout:
        log_err(f"WARNING | ReadTimeout was raised on GET \"{request_url}\"")
        return None
    
    if "<title>Just a moment...</title>" in response.text:
        log_err("WARNING | CloudFlare IUAM is active")
        return None
    
    log(f"RECEIVED {response.status_code}: {response.reason}", postfix="requests")

    return response

def invalid_response(response: Response) -> bool:
    # `try_request` will return None in case of ConnectionErrors or IUAM.
    # In these cases we back off and wait until it's over.
    return response is None or str(response.status_code).startswith('5')

def back_off(rate_limit_id: str=None) -> None:
    """Postpones the next request for 30 -> 60 -> 120 -> 240 seconds for 1, 2, 3, and 4+ tries respectively.
    This way we give the website some room to breathe if there are already many incoming connections causing this."""
    global failed_attempts
    if failed_attempts[rate_limit_id] < 4:
        failed_attempts[rate_limit_id] += 1

    next_request_time[rate_limit_id] += timedelta(seconds = 30 * 2**(failed_attempts[rate_limit_id] - 1))