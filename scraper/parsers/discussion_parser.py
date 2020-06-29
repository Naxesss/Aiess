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
        _id = discussion_json["id"]
        user = self.parse_user(discussion_json["user_id"], beatmapset_json)
        content = discussion_json["posts"][0]["message"] if discussion_json["posts"] else None
        return Discussion(_id, beatmapset, user, content)

    def parse_user(self, _id: str, beatmapset_json: object) -> User:
        """Returns a user with the given id and name supplied by the beatmapset json."""
        for related_user in beatmapset_json["related_users"]:
            if related_user["id"] == _id:
                return User(_id, related_user["username"])
    
    def parse_discussion_post_author(self, _id: str, beatmapset_json: object) -> User:
        """Returns the author of the given discussion post id if one exists, otherwise None."""
        for page_discussion in beatmapset_json["discussions"]:
            if not page_discussion: continue
            for page_discussion_post in page_discussion["posts"]:
                if not page_discussion_post: continue
                if page_discussion_post["id"] == _id:
                    return self.parse_user(page_discussion_post["user_id"], beatmapset_json)
        return None

discussion_parser = DiscussionParser()