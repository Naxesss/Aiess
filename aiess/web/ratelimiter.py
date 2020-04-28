import requests
from requests import Response
from socket import gaierror
from typing import Generator, Dict
from time import sleep
from datetime import datetime, timedelta

from aiess.logger import log_err

last_response_time: Dict[str, datetime] = {}

def request_with_rate_limit(request_url: str, rate_limit: float, rate_limit_id: str=None) -> Response:
    """Requests a response object at most once every rate_limit seconds for the same rate_limit_id (default None)."""
    global last_response_time
    
    response_time = last_response_time.get(rate_limit_id)
    if response_time and response_time + timedelta(seconds=rate_limit) > datetime.now():
        tdelta = ((response_time + timedelta(seconds=rate_limit)) - datetime.now())
        sleep(tdelta.total_seconds())

    response = request_with_retry(request_url, max_attempts=10)
    last_response_time[rate_limit_id] = datetime.now()

    return response

def request_with_retry(request_url, max_attempts=None) -> Response:
    """Requests a response object and retries if a ConnectionError is raised, sleeping in between retries.
    If the given max attempts is reached (set to None to never reach), we raise the ConnectionError instead of ignoring it.
    
    Backs off exponentially, capping at 120 seconds sleep time between retries; 15 -> 30 -> 60 -> 120."""
    attempts = 0
    while True:
        try:
            return requests.get(request_url)
        except (ConnectionError, gaierror) as err:
            if err is gaierror:
                # `gaierror` is raised if getaddrinfo() fails (e.g. request_url is something like "/beatmapsets/...").
                raise ValueError(f"The request to url \"{request_url}\" is invalid.")
            
            log_err(f"WARNING | ConnectionError was raised on GET \"{request_url}\", retrying...")
            attempts += 1
            if max_attempts and attempts >= max_attempts:
                raise
            sleep(max(15 * 2**(attempts - 1), 120))