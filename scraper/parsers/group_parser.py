import sys
sys.path.append('..')

from typing import Generator, List
from bs4 import BeautifulSoup
from datetime import datetime
import json
from dataclasses import dataclass

from aiess import Event, User, Usergroup
from aiess import event_types as types
from aiess.database import Database, SCRAPER_DB_NAME

@dataclass
class GroupUser:
    group_id: int
    user: User
    mode: str

def parse(group_id: int, group_page: BeautifulSoup, last_checked_at: datetime) -> Generator[Event, None, None]:
    """Returns a generator of group addition and removal events from the given BeautifulSoup group page and its id."""
    json_users = group_page.find("script", {"id": "json-users"})
    if not json_users:
        raise ValueError("No group users json could be found.")

    users_json = json.loads(json_users.string)
    return parse_users_json(group_id, users_json, last_checked_at)

def parse_users_json(group_id: int, users_json: object, last_checked_at: datetime) -> Generator[Event, None, None]:
    """Returns a generator of group addition and removal events from the given users json and group id."""
    missing_group_users = retrieve_group_users(group_id)
    new_group_users: List[GroupUser] = []
    for user_json in users_json:
        user_id = user_json["id"]
        modes = [None]

        for user_group_json in user_json["groups"]:
            has_modes = "playmodes" in user_group_json and user_group_json["playmodes"] is not None
            if user_group_json["id"] == group_id and has_modes:
                if len(user_group_json["playmodes"]):
                    modes = user_group_json["playmodes"]
                else:
                    # A user part of the group, but with no modes (e.g. non-captins in Project Loved / managers in the BSC).
                    modes = [None]
        
        for mode in modes:
            user = User(_id=user_id, name=user_json["username"])
            was_in_group_with_mode = False
            for group_user in missing_group_users:
                if group_user.user.id == user.id and group_user.mode == mode:
                    was_in_group_with_mode = True
                    missing_group_users.remove(group_user)
            
            if not was_in_group_with_mode:
                new_group_users.append(GroupUser(group_id, user, mode))
    
    content = None
    time = last_checked_at

    for group_user in missing_group_users:
        yield Event(
            _type   = types.REMOVE,
            time    = time,
            user    = retrieve_user_from_group(group_id=group_id, user_id=group_user.user.id, mode=group_user.mode),
            group   = Usergroup(_id=group_id, mode=group_user.mode),
            content = content
        )
    for group_user in new_group_users:
        yield Event(
            _type   = types.ADD,
            time    = time,
            user    = group_user.user,
            group   = Usergroup(_id=group_id, mode=group_user.mode),
            content = content
        )

def retrieve_group_users(group_id: int) -> List[GroupUser]:
    """Returns the last remembered user ids beloning to the given group id."""
    group_user_relations = Database(SCRAPER_DB_NAME).retrieve_group_users("group_id=%s", (group_id,))
    return [GroupUser(group.id, user, group.mode) for group, user in group_user_relations]

def retrieve_user_from_group(group_id: int, user_id: int, mode: str=None) -> List[int]:
    """Returns the last remembered user beloning to the given group id with the given user id."""
    if mode is not None:
        return Database(SCRAPER_DB_NAME).retrieve_group_user("group_id=%s AND user_id=%s AND mode=%s", (group_id, user_id, mode))[1]
    else:
        return Database(SCRAPER_DB_NAME).retrieve_group_user("group_id=%s AND user_id=%s", (group_id, user_id))[1]