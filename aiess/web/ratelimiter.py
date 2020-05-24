import requests
from requests import Response
from socket import gaierror
from typing import Generator, Dict
from time import sleep
from datetime import datetime, timedelta

from aiess.logger import log_err

next_request_time: Dict[str, datetime] = {}
failed_attempts: Dict[str, datetime] = {}

def request_with_rate_limit(request_url: str, rate_limit: float, rate_limit_id: str=None) -> Response:
    """Requests a response object at most once every rate_limit seconds for the same rate_limit_id (default None)."""
    global next_request_time
    
    request_time = next_request_time.get(rate_limit_id)
    if request_time and request_time > datetime.now():
        sleep((request_time - datetime.now()).total_seconds())

    response = request_with_retry(request_url)
    next_request_time[rate_limit_id] = datetime.now() + timedelta(seconds=rate_limit)

    return response

def request_with_retry(request_url: str, rate_limit_id: str=None) -> Response:
    """Requests a response object and retries if a ConnectionError is raised, backing off in between retries.
    If the given max attempts is reached (set to None to never reach), we raise the ConnectionError instead of ignoring it."""
    global failed_attempts
    while True:
        response = None

        try:
            response = requests.get(request_url)
        except ConnectionError:
            log_err(f"WARNING | ConnectionError was raised on GET \"{request_url}\", retrying...")
            back_off(rate_limit_id)
            continue
        except TimeoutError:
            raise ValueError(f"The request to url \"{request_url}\" timed out.")
        except gaierror:
            # `gaierror` is raised if getaddrinfo() fails (e.g. request_url is something like "/beatmapsets/...").
            raise ValueError(f"The request to url \"{request_url}\" is invalid.")
        
        if "<title>Just a moment...</title>" in response.text:
            log_err("WARNING | CloudFlare IUAM is active")
            back_off(rate_limit_id)
            continue

        if rate_limit_id in failed_attempts:
            failed_attempts[rate_limit_id] = 0
        return response

def back_off(rate_limit_id: str=None) -> None:
    """Postpones the next request for 30 -> 60 -> 120 -> 240 seconds for 1, 2, 3, and 4+ tries respectively.
    This way we give the website some room to breathe if there are already many incoming connections causing this."""
    global failed_attempts
    if rate_limit_id not in failed_attempts:
        failed_attempts[rate_limit_id] = 0
    if failed_attempts[rate_limit_id] < 4:
        failed_attempts[rate_limit_id] += 1
    
    next_request_time[rate_limit_id] += timedelta(seconds = 30 * 2**(failed_attempts[rate_limit_id] - 1))