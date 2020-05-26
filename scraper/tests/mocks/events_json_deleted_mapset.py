import sys
sys.path.append('..')

from scraper.requester import soupify

EVENTS_JSON = r"""
[
  {
    "id": 2004213,
    "type": "kudosu_gain",
    "comment": {
      "beatmap_discussion_id": 1605631,
      "beatmap_discussion_post_id": null,
      "new_vote": {
        "user_id": 3552948,
        "score": 1
      },
      "votes": [
        {
          "user_id": 3552948,
          "score": 1
        }
      ]
    },
    "created_at": "2020-05-24T00:47:48+00:00",
    "user_id": 2688103,
    "discussion": {
      "id": 1605631,
      "beatmapset_id": 534054,
      "beatmap_id": 1708984,
      "user_id": 2688103,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 18592,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2020-05-23T22:39:36+00:00",
      "updated_at": "2020-05-24T00:47:52+00:00",
      "deleted_at": null,
      "last_post_at": "2020-05-24T00:47:52+00:00",
      "kudosu_denied": false,
      "starting_post": {
        "id": 4521936,
        "beatmap_discussion_id": 1605631,
        "user_id": 2688103,
        "last_editor_id": null,
        "deleted_by_id": null,
        "system": false,
        "message": "00:18:592 (4) - this rhythm is kind of questionable.. doesn't fit the song very obviously so i don't think it's too suitable for low diff",
        "created_at": "2020-05-23T22:39:36+00:00",
        "updated_at": "2020-05-23T22:39:36+00:00",
        "deleted_at": null
      }
    }
  }
]
"""

USER_JSON = r"""
[
  {
    "avatar_url": "https://a.ppy.sh/2688103?1588879943.png",
    "country_code": "US",
    "default_group": "default",
    "id": 2688103,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": null,
    "username": "IOException"
  }
]
"""

HTML = f"""
  <script id="json-events" type="application/json">
      {EVENTS_JSON}
  </script>
  <script id="json-users" type="application/json">
      {USER_JSON}
  </script>
"""

soup = soupify(HTML)