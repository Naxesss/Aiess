import sys
sys.path.append('..')

from typing import Generator

from aiess import Discussion, Beatmapset, User

class DiscussionParser():

    def parse(self, discussions_json: object, beatmapset: Beatmapset) -> Generator[Discussion, None, None]:
        """Returns a generator of discussions from the given beatmapset discussion page json, or None if no discussions exist."""
        discussion_jsons = discussions_json["beatmapset"]["discussions"]
        for discussion_json in discussion_jsons:
            if not discussion_json: continue
            yield self.parse_discussion(discussion_json, discussions_json["beatmapset"], beatmapset)
    
    def parse_discussion(self, discussion_json: object, beatmapset_json: object, beatmapset: Beatmapset) -> Discussion:
        """Returns a discussion from the given discussion json. The beatmapset json is also included for efficient username querying."""
        _id        = discussion_json["id"]
        user       = self.parse_user(discussion_json["user_id"], beatmapset_json)
        content    = discussion_json["posts"][0]["message"] if discussion_json["posts"] else None
        tab        = self.parse_tab(discussion_json, beatmapset_json)
        difficulty = self.parse_diff(discussion_json, beatmapset_json)
        return Discussion(_id, beatmapset, user, content, tab, difficulty)

    def parse_user(self, user_id: str, beatmapset_json: object) -> User:
        """Returns a user with the given id and name supplied by the beatmapset json."""
        for related_user in beatmapset_json["related_users"]:
            if related_user["id"] == user_id:
                return User(user_id, related_user["username"])
    
    def parse_discussion_post_author(self, post_id: str, beatmapset_json: object) -> User:
        """Returns the author of the given discussion post id if one exists, otherwise None."""
        for page_discussion in beatmapset_json["discussions"]:
            if not page_discussion: continue
            for page_discussion_post in page_discussion["posts"]:
                if not page_discussion_post: continue
                if page_discussion_post["id"] == post_id:
                    return self.parse_user(page_discussion_post["user_id"], beatmapset_json)
        return None
    
    def parse_tab(self, discussion_json: str, beatmapset_json: object) -> User:
        """Returns the tab which the given discussion is posted on."""
        has_timestamp = "timestamp" in discussion_json and discussion_json["timestamp"] is not None
        has_difficulty = "beatmap_id" in discussion_json and discussion_json["beatmap_id"]

        if   has_timestamp:  return "timeline"
        elif has_difficulty: return "general"
        else:                return "generalAll"
    
    def parse_diff(self, discussion_json: str, beatmapset_json: object) -> User:
        """Returns the name of the difficulty which the given discussion is posted on, if any, otherwise None."""
        # Key may be missing in case the value would be N/A.
        if "beatmap_id" not in discussion_json or not discussion_json["beatmap_id"]:
            return None
        
        beatmap_id = discussion_json["beatmap_id"]
        for beatmap_json in beatmapset_json["beatmaps"]:
            if beatmap_json["id"] == beatmap_id:
                return beatmap_json["version"]

discussion_parser = DiscussionParser()