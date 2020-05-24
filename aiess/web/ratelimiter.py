import requests
from requests import Response
from socket import gaierror
from typing import Generator, Dict
from time import sleep
from datetime import datetime, timedelta

from aiess.logger import log_err

next_request_time: Dict[str, datetime] = {}

def request_with_rate_limit(request_url: str, rate_limit: float, rate_limit_id: str=None) -> Response:
    """Requests a response object at most once every rate_limit seconds for the same rate_limit_id (default None)."""
    global next_request_time
    
    request_time = next_request_time.get(rate_limit_id)
    if request_time and request_time > datetime.now():
        sleep((request_time - datetime.now()).total_seconds())

    response = request_with_retry(request_url)
    next_request_time[rate_limit_id] = datetime.now() + timedelta(seconds=rate_limit)

    return response

def request_with_retry(request_url, max_attempts=None) -> Response:
    """Requests a response object and retries if a ConnectionError is raised, sleeping in between retries.
    If the given max attempts is reached (set to None to never reach), we raise the ConnectionError instead of ignoring it.
    
    Backs off exponentially, capping at 120 seconds sleep time between retries; 15 -> 30 -> 60 -> 120."""
    attempts = 0
    while True:
        try:
            return requests.get(request_url)
        
        except ConnectionError:
            log_err(f"WARNING | ConnectionError was raised on GET \"{request_url}\", retrying...")
            attempts += 1
            if max_attempts and attempts >= max_attempts:
                raise
            # Back-off to give the website some room to breathe if there are already many incoming connections causing this.
            sleep(max(15 * 2**(attempts - 1), 120))
        
        except TimeoutError:
            raise ValueError(f"The request to url \"{request_url}\" timed out.")
        
        except gaierror:
            # `gaierror` is raised if getaddrinfo() fails (e.g. request_url is something like "/beatmapsets/...").
            raise ValueError(f"The request to url \"{request_url}\" is invalid.")