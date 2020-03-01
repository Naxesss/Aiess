import requests
from requests import Response
from typing import Generator, Dict
from time import sleep
from datetime import datetime, timedelta

last_response_time: Dict[str, datetime] = {}

def request_with_rate_limit(request_url: str, rate_limit: float, rate_limit_id: str=None) -> Response:
    """Requests a response object at most once every rate_limit seconds for the same rate_limit_id (default None)."""
    global last_response_time
    
    response_time = last_response_time.get(rate_limit_id)
    if response_time and response_time + timedelta(seconds=rate_limit) > datetime.now():
        tdelta = ((response_time + timedelta(seconds=rate_limit)) - datetime.now())
        sleep(tdelta.total_seconds())
    
    response = requests.get(request_url)
    last_response_time[rate_limit_id] = datetime.now()

    return response