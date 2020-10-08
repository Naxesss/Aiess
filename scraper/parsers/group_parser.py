import sys
sys.path.append('..')

from typing import Generator, List
from bs4 import BeautifulSoup
from datetime import datetime
import json

from aiess import Event, User, Usergroup
from aiess import event_types as types
from aiess.database import Database, SCRAPER_DB_NAME

def parse(group_id: int, group_page: BeautifulSoup, last_checked_at: datetime) -> Generator[Event, None, None]:
    """Returns a generator of group addition and removal events from the given BeautifulSoup group page and its id."""
    json_users = group_page.find("script", {"id": "json-users"})
    if not json_users:
        raise ValueError("No group users json could be found.")

    users_json = json.loads(json_users.string)
    return parse_users_json(group_id, users_json, last_checked_at)

def parse_users_json(group_id: int, users_json: object, last_checked_at: datetime) -> Generator[Event, None, None]:
    """Returns a generator of group addition and removal events from the given users json and group id."""
    missing_user_ids = get_group_user_ids(group_id)
    new_users = []
    for user_json in users_json:
        user_id = user_json["id"]
        if user_id in missing_user_ids:
            missing_user_ids.remove(user_id)
        else:
            new_users.append(User(_id=user_id, name=user_json["username"]))
    
    content = None
    time = last_checked_at

    for missing_user_id in missing_user_ids:
        yield Event(
            _type   = types.REMOVE,
            time    = time,
            user    = get_group_user(group_id=group_id, user_id=missing_user_id),
            group   = Usergroup(_id=group_id),
            content = content
        )
    for new_user in new_users:
        yield Event(
            _type   = types.ADD,
            time    = time,
            user    = new_user,
            group   = Usergroup(_id=group_id),
            content = content
        )

def get_group_user_ids(group_id: int) -> List[int]:
    """Returns the last remembered user ids beloning to the given group id."""
    group_user_relations = Database(SCRAPER_DB_NAME).retrieve_group_users("group_id=%s", (group_id,))
    return [user.id for group, user in group_user_relations]

def get_group_user(group_id: int, user_id: int) -> List[int]:
    """Returns the last remembered user beloning to the given group id with the given user id."""
    return Database(SCRAPER_DB_NAME).retrieve_group_user("group_id=%s AND user_id=%s", (group_id, user_id))[1]