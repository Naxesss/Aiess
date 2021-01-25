import sys
sys.path.append('..')

from scraper.requester import soupify

EVENTS_JSON = """
[
  {
    "id": 2357896,
    "type": "nominate",
    "comment": null,
    "created_at": "2020-09-17T21:06:21+00:00",
    "user_id": 33599,
    "beatmapset": {
      "artist": "Mia REGINA",
      "artist_unicode": "Mia REGINA",
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/1164305/covers/cover.jpg?1600315549",
        "cover@2x": "https://assets.ppy.sh/beatmaps/1164305/covers/cover@2x.jpg?1600315549",
        "card": "https://assets.ppy.sh/beatmaps/1164305/covers/card.jpg?1600315549",
        "card@2x": "https://assets.ppy.sh/beatmaps/1164305/covers/card@2x.jpg?1600315549",
        "list": "https://assets.ppy.sh/beatmaps/1164305/covers/list.jpg?1600315549",
        "list@2x": "https://assets.ppy.sh/beatmaps/1164305/covers/list@2x.jpg?1600315549",
        "slimcover": "https://assets.ppy.sh/beatmaps/1164305/covers/slimcover.jpg?1600315549",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/1164305/covers/slimcover@2x.jpg?1600315549"
      },
      "creator": "kunka",
      "favourite_count": 7,
      "id": 1164305,
      "play_count": 884,
      "preview_url": "//b.ppy.sh/preview/1164305.mp3",
      "source": "天晴爛漫！",
      "status": "qualified",
      "title": "I got it! (TV Size)",
      "title_unicode": "I got it! (TV Size)",
      "user_id": 1741295,
      "video": true,
      "user": {
        "avatar_url": "https://a.ppy.sh/1741295?1557856409.jpg",
        "country_code": "JP",
        "default_group": "default",
        "id": 1741295,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "kunka"
      }
    }
  }
]
"""

USER_JSON = """
[
  {
    "avatar_url": "https://a.ppy.sh/33599?1599317457.jpeg",
    "country_code": "IT",
    "default_group": "bng",
    "id": 33599,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#6B3FA0",
    "username": "Andrea",
    "groups": [
      {
        "id": 28,
        "identifier": "bng",
        "name": "Beatmap Nominators",
        "short_name": "BN",
        "description": "",
        "colour": "#A347EB"
      },
      {
        "id": 16,
        "identifier": "alumni",
        "name": "osu! Alumni",
        "short_name": "ALM",
        "description": "",
        "colour": "#999999"
      }
    ]
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