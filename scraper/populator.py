import sys
sys.path.append('..')

from datetime import datetime, timedelta

from aiess.objects import Discussion, Beatmapset, Event
from aiess.errors import ParsingError
from aiess.database import Database, SCRAPER_DB_NAME
from aiess.timestamp import from_string
from aiess import event_types as types
from bnsite import api as bnsite_api

from scraper.requester import request_discussions_json
from scraper.requester import get_map_page_discussions
from scraper.requester import get_map_page_event_jsons
from scraper.requester import get_map_page_discussion_jsons
from scraper.parsers.discussion_parser import discussion_parser

cached_discussions_json = {}

async def populate_from_discussion(event: Event) -> None:
    """Populates the given event using the beatmapset discussion json
    (e.g. missing discussion info and additional details like who did votes)."""
    discussions_json = get_discussions_json(event.beatmapset)
    if discussions_json is None:
        # This happens if the beatmapset was deleted in between us scraping it and populating it.
        event.marked_for_deletion = True
        return

    event.discussion = get_complete_discussion_info(event.discussion, event.beatmapset, discussions_json)
    await __populate_additional_details(event, discussions_json)

async def populate_from_bnsite(event: Event) -> None:
    """Populates the given event using the bnsite API if possible."""
    if event.type in [types.REMOVE, types.ADD]:
        # Group removal content should reflect the bnsite removal reason (e.g. Kicked/Resigned)
        event.content = get_group_bnsite_comment(event)
        event.group.mode = get_group_bnsite_mode(event)

def get_discussions_json(beatmapset: Beatmapset) -> object:
    """Returns the beatmapset discussions json, containing all of the discussion information for the mapset,
    if possible, otherwise None."""
    if beatmapset.id not in cached_discussions_json:
        discussions_json = request_discussions_json(beatmapset.id)
        if discussions_json:
            cached_discussions_json[beatmapset.id] = discussions_json
    else:
        discussions_json = cached_discussions_json[beatmapset.id]
    
    return discussions_json

def get_complete_discussion_info(
        discussion: Discussion, beatmapset: Beatmapset,
        discussions_json: object=None, db_name: str=SCRAPER_DB_NAME) -> Discussion:
    """Returns a discussion with complete information from the beatmapset discussion json
    (e.g. user and content, neither of which are guaranteed)."""
    if not discussion:
        return None

    if (
        discussion.user is not None and
        discussion.content is not None and
        discussion.tab is not None
    ):
        return discussion  # None of required attributes are missing, so is considered already complete.

    if not discussions_json:
        # Discussions json is the quickest option, which is why we check this first.
        # The next quickest option is retrieving the complete info from the database, if it exists.
        if __complete_discussion_context(discussion, db_name=db_name):
            return discussion
        
        discussions_json = get_discussions_json(beatmapset)
        if not discussions_json:
            raise ParsingError("No discussions json exists to use for discussion context.")

    for other_discussion in get_map_page_discussions(beatmapset, discussions_json):
        if other_discussion.id == discussion.id:
            return other_discussion

async def __populate_additional_details(event: Event, discussions_json: object, db_name: str=SCRAPER_DB_NAME) -> None:
    """Populates additional details in the given event from the beatmapset discussion json (e.g. who voted)."""
    if event.discussion and (not event.discussion.user or not event.discussion.content):
        if not __complete_discussion_context(event.discussion, db_name=db_name):
            # After being deleted, many properties of discussions are inaccessible without referring to cached information.
            # Without cached information, we skip the event, since this its context is no longer visible to the public anyway.
            event.marked_for_deletion = True
            return

    if event.type in [types.NOMINATE]:
        # Nominate/qualify content should reflect recent praise/hype/note content.
        event.content = get_nomination_comment(event, discussions_json)
    
    if event.type in [types.DISQUALIFY, types.RESET]:
        # Event content should reflect discussion content.
        if event.discussion:  # Discussion may have been deleted.
            event.content = event.discussion.content

    if not discussions_json:
        # Mapset has no discussion, probably associated with some legacy thread (e.g. ranked before modding v2).
        return
    
    beatmapset_json = discussions_json["beatmapset"]
    for page_event in get_map_page_event_jsons(event.beatmapset, discussions_json):
        # Likelihood that two same type of events happen in the same second is very unlikely,
        # so this'll work as identification (we have no access to actual event ids on scraping side, so can't use that).
        same_time = event.time == from_string(page_event["created_at"])
        same_type = event.type == page_event["type"]
        if same_time and same_type:
            if event.type in [types.RESOLVE, types.REOPEN]:
                # Event user should be whoever resolved or reopened, rather than the discussion author.
                post_author = discussion_parser.parse_discussion_post_author(
                    page_event["comment"]["beatmap_discussion_post_id"],
                    beatmapset_json)
                event.user = post_author
            
            if event.type in [types.KUDOSU_GAIN, types.KUDOSU_LOSS]:
                # Event user should be whoever gave or removed the kudosu, not the discssion author.
                kudosu_author = discussion_parser.parse_user(
                    page_event["comment"]["new_vote"]["user_id"],
                    beatmapset_json)
                event.user = kudosu_author

def __complete_discussion_context(discussion: Discussion, db_name: str=SCRAPER_DB_NAME) -> bool:
    """Completes the context of the discussion from prior database entries, if present. Returns true if succeeded."""
    cached_discussion = Database(db_name).retrieve_discussion("id=%s", (discussion.id,))
    if not cached_discussion:
        return False

    complete = (
        cached_discussion.user and
        cached_discussion.content and
        cached_discussion.tab and
        cached_discussion.difficulty
    )
    if not complete:
        return False

    discussion.user       = cached_discussion.user
    discussion.content    = cached_discussion.content
    discussion.tab        = cached_discussion.tab
    discussion.difficulty = cached_discussion.difficulty
    return True

def get_nomination_comment(event: Event, discussions_json: object) -> str:
    """Returns the text of the last discussion by the user if it is a praise or mapper note,
    otherwise any hype prior to the event by the user, if any, else None."""
    latest_discussion_json = None
    latest_hype_discussion_json = None
    for discussion_json in get_map_page_discussion_jsons(event.beatmapset, discussions_json):
        if discussion_json is None: continue
        latest_time = from_string(latest_discussion_json["created_at"]) if latest_discussion_json else None
        current_time = from_string(discussion_json["created_at"])

        if (
            discussion_json["user_id"] == event.user.id and
            current_time < event.time and
            (not latest_time or current_time > latest_time)
        ):
            latest_discussion_json = discussion_json
            if discussion_json["message_type"] == types.HYPE:
                latest_hype_discussion_json = discussion_json
    
    if latest_discussion_json and latest_discussion_json["message_type"] in [types.PRAISE, types.NOTE]:
        return latest_discussion_json["posts"][0]["message"]
    
    if latest_hype_discussion_json:
        return latest_hype_discussion_json["posts"][0]["message"]
    
    return None

def get_group_bnsite_comment(event: Event) -> str:
    """Returns any comment the bnsite has put on group events
    (e.g. BN removal reasons), if any, otherwise None."""
    if not event.group:
        raise ValueError("Event lacks a group.")

    # Only comments removals of BNs.
    if event.type != types.REMOVE or event.group.id not in [32, 28]:
        return None

    json = bnsite_api.request_last_eval(event.user.id)
    if not json or eval_likely_outdated(eval_json=json):
        return None

    kind = json["kind"]
    if   kind == "resignation": comment = "Resigned"
    elif kind == "currentBn":
        consensus = json["consensus"] if "consensus" in json else None
        if   consensus is None:           comment = None
        # Movement within the Beatmap Nominators is self-explanatory given both the added+removed events.
        elif consensus == "fullBn":       comment = None
        elif consensus == "probationBn":  comment = None
        elif consensus == "removeFromBn": comment = "Kicked"
        else:                             raise ValueError(f"Unrecognized evaluation consensus \"{consensus}\".")
    else: raise ValueError(f"Unrecognized evaluation kind \"{kind}\".")

    return comment

def get_group_bnsite_mode(event: Event) -> str:
    """Returns the mode of the bn according to the bnsite
    (e.g. "taiko"), if any, otherwise None."""
    if not event.group:
        raise ValueError("Event lacks a group.")

    # Can only get mode of groups the bnsite keeps track of.
    if event.group.id not in [7, 32, 28]:
        return None
    
    json = bnsite_api.request_last_eval(event.user.id)
    if not json or eval_likely_outdated(eval_json=json):
        return None
    
    return json["mode"]

def eval_likely_outdated(eval_json: object) -> bool:
    archived = not eval_json["active"]
    time     = from_string(eval_json["updatedAt"]) if "updatedAt" in eval_json and eval_json["updatedAt"] else None
    old      = not time or (datetime.utcnow() - time) > timedelta(days=3)
    # Chances are high that no evaluation exists for this, if all we can find is old archived evals.
    return archived and old