import sys
sys.path.append('..')

from scraper.requester import soupify

EVENTS_JSON = """
[
  {
    "id": 2434750,
    "type": "language_edit",
    "comment": {
      "beatmap_discussion_id": null,
      "beatmap_discussion_post_id": null,
      "old": "Unspecified",
      "new": "Instrumental"
    },
    "created_at": "2020-10-17T16:08:11+00:00",
    "user_id": 10660777,
    "beatmapset": {
      "artist": "ALEPH",
      "artist_unicode": "ALEPH",
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/1280248/covers/cover.jpg?1602950856",
        "cover@2x": "https://assets.ppy.sh/beatmaps/1280248/covers/cover@2x.jpg?1602950856",
        "card": "https://assets.ppy.sh/beatmaps/1280248/covers/card.jpg?1602950856",
        "card@2x": "https://assets.ppy.sh/beatmaps/1280248/covers/card@2x.jpg?1602950856",
        "list": "https://assets.ppy.sh/beatmaps/1280248/covers/list.jpg?1602950856",
        "list@2x": "https://assets.ppy.sh/beatmaps/1280248/covers/list@2x.jpg?1602950856",
        "slimcover": "https://assets.ppy.sh/beatmaps/1280248/covers/slimcover.jpg?1602950856",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/1280248/covers/slimcover@2x.jpg?1602950856"
      },
      "creator": "quantumvortex",
      "favourite_count": 0,
      "id": 1280248,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/1280248.mp3",
      "source": "osu!",
      "status": "pending",
      "title": "BREAKING AND ENTERING",
      "title_unicode": "BREAKING AND ENTERING",
      "user_id": 10660777,
      "video": false,
      "user": {
        "avatar_url": "https://a.ppy.sh/10660777?1589014084.jpeg",
        "country_code": "TH",
        "default_group": "default",
        "id": 10660777,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-10-17T16:08:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "quantumvortex"
      }
    }
  },
  {
    "id": 2434749,
    "type": "genre_edit",
    "comment": {
      "beatmap_discussion_id": null,
      "beatmap_discussion_post_id": null,
      "old": "Unspecified",
      "new": "Electronic"
    },
    "created_at": "2020-10-17T16:08:11+00:00",
    "user_id": 10660777,
    "beatmapset": {
      "artist": "ALEPH",
      "artist_unicode": "ALEPH",
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/1280248/covers/cover.jpg?1602950856",
        "cover@2x": "https://assets.ppy.sh/beatmaps/1280248/covers/cover@2x.jpg?1602950856",
        "card": "https://assets.ppy.sh/beatmaps/1280248/covers/card.jpg?1602950856",
        "card@2x": "https://assets.ppy.sh/beatmaps/1280248/covers/card@2x.jpg?1602950856",
        "list": "https://assets.ppy.sh/beatmaps/1280248/covers/list.jpg?1602950856",
        "list@2x": "https://assets.ppy.sh/beatmaps/1280248/covers/list@2x.jpg?1602950856",
        "slimcover": "https://assets.ppy.sh/beatmaps/1280248/covers/slimcover.jpg?1602950856",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/1280248/covers/slimcover@2x.jpg?1602950856"
      },
      "creator": "quantumvortex",
      "favourite_count": 0,
      "id": 1280248,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/1280248.mp3",
      "source": "osu!",
      "status": "pending",
      "title": "BREAKING AND ENTERING",
      "title_unicode": "BREAKING AND ENTERING",
      "user_id": 10660777,
      "video": false,
      "user": {
        "avatar_url": "https://a.ppy.sh/10660777?1589014084.jpeg",
        "country_code": "TH",
        "default_group": "default",
        "id": 10660777,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-10-17T16:08:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "quantumvortex"
      }
    }
  }
]
"""

USER_JSON = """
[
  {
    "avatar_url": "https://a.ppy.sh/10660777?1589014084.jpeg",
    "country_code": "TH",
    "default_group": "default",
    "id": 10660777,
    "is_active": true,
    "is_bot": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2020-10-17T16:08:00+00:00",
    "pm_friends_only": false,
    "profile_colour": null,
    "username": "quantumvortex",
    "groups": []
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