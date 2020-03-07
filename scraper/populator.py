

from aiess.objects import Discussion, Beatmapset, Event
from aiess.errors import ParsingError
from aiess.database import database
from aiess import timestamp

from requester import request_discussions_json, get_map_page_discussions, get_map_page_event_jsons
from parsers.discussion_parser import discussion_parser

cached_discussions_json = {}

def populate_event(event: Event) -> None:
    """Populates the given event using the beatmapset discussion json
    (e.g. missing discussion info and additional details like who did votes)."""
    discussions_json = get_discussions_json(event.discussion, event.beatmapset)
    if discussions_json == None:
        raise ValueError("Could not get a discussion.")

    event.discussion = get_complete_discussion_info(event.discussion, event.beatmapset, discussions_json)
    __populate_additional_details(event, discussions_json)

def get_discussions_json(discussion: Discussion, beatmapset: Beatmapset) -> object:
    """Returns the beatmapset discussions json, containing all of the discussion information for the mapset,
    if possible, otherwise None."""
    if beatmapset.id not in cached_discussions_json:
        discussions_json = request_discussions_json(beatmapset)
        if discussions_json:
            cached_discussions_json[beatmapset.id] = discussions_json
    else:
        discussions_json = cached_discussions_json[beatmapset.id]
    
    return discussions_json

def get_complete_discussion_info(discussion: Discussion, beatmapset: Beatmapset, discussions_json: object=None) -> Discussion:
    """Returns a discussion with complete information from the beatmapset discussion json
    (e.g. user and content, neither of which are guaranteed)."""
    if not discussion or discussion.user != None and discussion.content != None:
        return discussion  # Either None (i.e. unused by the event type) or already completed.

    if not discussions_json:
        # Discussions json is the quickest option, which is why we check this first.
        # The next quickest option is retrieving the complete info from the database, if it exists.
        if __complete_discussion_context(discussion):
            return discussion
        
        discussions_json = get_discussions_json(discussion, beatmapset)
        if not discussions_json:
            raise ParsingError("No discussions json exists to use for discussion context.")

    for other_discussion in get_map_page_discussions(beatmapset, discussions_json):
        if other_discussion.id == discussion.id:
            return other_discussion

def __populate_additional_details(event: Event, discussions_json: object) -> None:
    """Populates additional details in the given event from the beatmapset discussion json (e.g. who voted)."""
    if event.discussion and (not event.discussion.user or not event.discussion.content):
        if not __complete_discussion_context(event.discussion):
            # After being deleted, many properties of discussions are inaccessible without referring to cached information.
            # Without cached information, we skip the event, since this its context is no longer visible to the public anyway.
            event.marked_for_deletion = True
            return

    beatmapset_json = discussions_json["beatmapset"]
    for page_event in get_map_page_event_jsons(event, discussions_json):
        # Likelihood that two same type of events happen in the same second is very unlikely,
        # so this'll work as identification (we have no access to actual event ids on scraping side, so can't use that).
        same_time = event.time == timestamp.from_string(page_event["created_at"])
        same_type = event.type == page_event["type"].replace("_", "-")
        if same_time and same_type:
            if event.type == "disqualify" or event.type == "nomination_reset":  # Content is discussion content.
                event.content = event.discussion.content

            if event.type == "issue-resolve":  # User is resolver, not discussion creator.
                post_author = discussion_parser.parse_discussion_post_author(
                    page_event["comment"]["beatmap_discussion_post_id"],
                    beatmapset_json)
                if post_author != None:
                    event.user = post_author
            
            if event.type == "kudosu-gain":  # User is giver, not discussion creator.
                kudosu_giver = discussion_parser.parse_user(
                    page_event["comment"]["new_vote"]["user_id"],
                    beatmapset_json)
                if kudosu_giver != None:
                    event.user = kudosu_giver
            
            if event.type == "kudosu-lost":  # User is remover, not discussion creator.
                kudosu_remover = discussion_parser.parse_user(
                    page_event["comment"]["new_vote"]["user_id"],
                    beatmapset_json)
                if kudosu_remover != None:
                    event.user = kudosu_remover
            
            if event.type == "issue-reopen":  # User is reopener, not discussion creator.
                issue_reopener = discussion_parser.parse_discussion_post_author(
                    page_event["comment"]["beatmap_discussion_post_id"],
                    beatmapset_json)
                if issue_reopener != None:
                    event.user = issue_reopener
            
            if event.type == "discussion-delete":  # User is discussion creator (which we would normally not have access to).
                if event.discussion:
                    event.user = event.discussion.user
            
            if event.type == "discussion_post_delete":  # User is discussion post creator, to which we would no longer have access.
                event.marked_for_deletion = True  # TODO: Not yet supported.

def __complete_discussion_context(discussion: Discussion) -> bool:
    """Completes the context of the discussion from prior database entries, if present. Returns true if succeeded."""
    cached_discussion = database.retrieve_discussion(f"id={discussion.id}")
    if not cached_discussion:
        return False
    
    if cached_discussion.user == None or cached_discussion.content == None:
        raise ValueError("""
            Retrieved an incomplete discussion instance. This should not be possible when
            preventing input of incomplete instances.""")

    discussion.user = cached_discussion.user
    discussion.content = cached_discussion.content
    return True