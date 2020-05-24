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
    "beatmapset": {
      "artist": "TRUE",
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/534054/covers/cover.jpg?1589853050",
        "cover@2x": "https://assets.ppy.sh/beatmaps/534054/covers/cover@2x.jpg?1589853050",
        "card": "https://assets.ppy.sh/beatmaps/534054/covers/card.jpg?1589853050",
        "card@2x": "https://assets.ppy.sh/beatmaps/534054/covers/card@2x.jpg?1589853050",
        "list": "https://assets.ppy.sh/beatmaps/534054/covers/list.jpg?1589853050",
        "list@2x": "https://assets.ppy.sh/beatmaps/534054/covers/list@2x.jpg?1589853050",
        "slimcover": "https://assets.ppy.sh/beatmaps/534054/covers/slimcover.jpg?1589853050",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/534054/covers/slimcover@2x.jpg?1589853050"
      },
      "creator": "SkyFlame",
      "favourite_count": 95,
      "id": 534054,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/534054.mp3",
      "source": "響け！ユーフォニアム2",
      "status": "pending",
      "title": "Soundscape",
      "user_id": 3552948,
      "video": false,
      "user": {
        "avatar_url": "https://a.ppy.sh/3552948?1589477463.jpeg",
        "country_code": "US",
        "default_group": "default",
        "id": 3552948,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-05-24T00:52:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "SkyFlame"
      }
    },
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
  },
  {
    "id": 2004212,
    "type": "language_edit",
    "comment": {
      "beatmap_discussion_id": null,
      "beatmap_discussion_post_id": null,
      "old": "Other",
      "new": "Japanese"
    },
    "created_at": "2020-05-24T00:46:38+00:00",
    "user_id": 7149815,
    "beatmapset": {
      "artist": "HyperJuice",
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/663220/covers/cover.jpg?1590281188",
        "cover@2x": "https://assets.ppy.sh/beatmaps/663220/covers/cover@2x.jpg?1590281188",
        "card": "https://assets.ppy.sh/beatmaps/663220/covers/card.jpg?1590281188",
        "card@2x": "https://assets.ppy.sh/beatmaps/663220/covers/card@2x.jpg?1590281188",
        "list": "https://assets.ppy.sh/beatmaps/663220/covers/list.jpg?1590281188",
        "list@2x": "https://assets.ppy.sh/beatmaps/663220/covers/list@2x.jpg?1590281188",
        "slimcover": "https://assets.ppy.sh/beatmaps/663220/covers/slimcover.jpg?1590281188",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/663220/covers/slimcover@2x.jpg?1590281188"
      },
      "creator": "Plaudible",
      "favourite_count": 8,
      "id": 663220,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/663220.mp3",
      "source": "",
      "status": "wip",
      "title": "City Lights feat. EVO+, Jinmenusagi (Zekk Remix)",
      "user_id": 7149815,
      "video": false,
      "user": {
        "avatar_url": "https://a.ppy.sh/7149815?1590036181.jpeg",
        "country_code": "US",
        "default_group": "default",
        "id": 7149815,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": false,
        "last_visit": "2020-05-24T00:50:35+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Plaudible"
      }
    }
  },
  {
    "id": 2004211,
    "type": "genre_edit",
    "comment": {
      "beatmap_discussion_id": null,
      "beatmap_discussion_post_id": null,
      "old": "Unspecified",
      "new": "Electronic"
    },
    "created_at": "2020-05-24T00:46:38+00:00",
    "user_id": 7149815,
    "beatmapset": {
      "artist": "HyperJuice",
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/663220/covers/cover.jpg?1590281188",
        "cover@2x": "https://assets.ppy.sh/beatmaps/663220/covers/cover@2x.jpg?1590281188",
        "card": "https://assets.ppy.sh/beatmaps/663220/covers/card.jpg?1590281188",
        "card@2x": "https://assets.ppy.sh/beatmaps/663220/covers/card@2x.jpg?1590281188",
        "list": "https://assets.ppy.sh/beatmaps/663220/covers/list.jpg?1590281188",
        "list@2x": "https://assets.ppy.sh/beatmaps/663220/covers/list@2x.jpg?1590281188",
        "slimcover": "https://assets.ppy.sh/beatmaps/663220/covers/slimcover.jpg?1590281188",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/663220/covers/slimcover@2x.jpg?1590281188"
      },
      "creator": "Plaudible",
      "favourite_count": 8,
      "id": 663220,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/663220.mp3",
      "source": "",
      "status": "wip",
      "title": "City Lights feat. EVO+, Jinmenusagi (Zekk Remix)",
      "user_id": 7149815,
      "video": false,
      "user": {
        "avatar_url": "https://a.ppy.sh/7149815?1590036181.jpeg",
        "country_code": "US",
        "default_group": "default",
        "id": 7149815,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": false,
        "last_visit": "2020-05-24T00:50:35+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Plaudible"
      }
    }
  },
  {
    "id": 2004210,
    "type": "rank",
    "comment": null,
    "created_at": "2020-05-24T00:46:07+00:00",
    "user_id": null,
    "beatmapset": {
      "artist": "solfa feat. Shimotsuki Haruka",
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/1157280/covers/cover.jpg?1589575242",
        "cover@2x": "https://assets.ppy.sh/beatmaps/1157280/covers/cover@2x.jpg?1589575242",
        "card": "https://assets.ppy.sh/beatmaps/1157280/covers/card.jpg?1589575242",
        "card@2x": "https://assets.ppy.sh/beatmaps/1157280/covers/card@2x.jpg?1589575242",
        "list": "https://assets.ppy.sh/beatmaps/1157280/covers/list.jpg?1589575242",
        "list@2x": "https://assets.ppy.sh/beatmaps/1157280/covers/list@2x.jpg?1589575242",
        "slimcover": "https://assets.ppy.sh/beatmaps/1157280/covers/slimcover.jpg?1589575242",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/1157280/covers/slimcover@2x.jpg?1589575242"
      },
      "creator": "Lafayla",
      "favourite_count": 2,
      "id": 1157280,
      "play_count": 9,
      "preview_url": "//b.ppy.sh/preview/1157280.mp3",
      "source": "約束の夏、まほろばの夢",
      "status": "ranked",
      "title": "Mahoroba no Yume",
      "user_id": 5312547,
      "video": false,
      "user": {
        "avatar_url": "https://a.ppy.sh/5312547?1589000720.jpeg",
        "country_code": "CA",
        "default_group": "bng",
        "id": 5312547,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "Lafayla"
      }
    }
  },
  {
    "id": 2004209,
    "type": "issue_resolve",
    "comment": {
      "beatmap_discussion_id": 1605855,
      "beatmap_discussion_post_id": 4522337
    },
    "created_at": "2020-05-24T00:45:03+00:00",
    "user_id": 10476879,
    "beatmapset": {
      "artist": "umu.",
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/1145237/covers/cover.jpg?1590060859",
        "cover@2x": "https://assets.ppy.sh/beatmaps/1145237/covers/cover@2x.jpg?1590060859",
        "card": "https://assets.ppy.sh/beatmaps/1145237/covers/card.jpg?1590060859",
        "card@2x": "https://assets.ppy.sh/beatmaps/1145237/covers/card@2x.jpg?1590060859",
        "list": "https://assets.ppy.sh/beatmaps/1145237/covers/list.jpg?1590060859",
        "list@2x": "https://assets.ppy.sh/beatmaps/1145237/covers/list@2x.jpg?1590060859",
        "slimcover": "https://assets.ppy.sh/beatmaps/1145237/covers/slimcover.jpg?1590060859",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/1145237/covers/slimcover@2x.jpg?1590060859"
      },
      "creator": "Vebox",
      "favourite_count": 7,
      "id": 1145237,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/1145237.mp3",
      "source": "",
      "status": "pending",
      "title": "Ai no Sukima",
      "user_id": 10476879,
      "video": false,
      "user": {
        "avatar_url": "https://a.ppy.sh/10476879?1589254634.jpeg",
        "country_code": "US",
        "default_group": "default",
        "id": 10476879,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-05-24T00:52:19+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Vebox"
      }
    },
    "discussion": {
      "id": 1605855,
      "beatmapset_id": 1145237,
      "beatmap_id": 2418151,
      "user_id": 4312463,
      "deleted_by_id": null,
      "message_type": "problem",
      "parent_id": null,
      "timestamp": 41372,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2020-05-24T00:37:37+00:00",
      "updated_at": "2020-05-24T00:45:03+00:00",
      "deleted_at": null,
      "last_post_at": "2020-05-24T00:45:03+00:00",
      "kudosu_denied": false,
      "starting_post": {
        "id": 4522315,
        "beatmap_discussion_id": 1605855,
        "user_id": 4312463,
        "last_editor_id": null,
        "deleted_by_id": null,
        "system": false,
        "message": "why are yall focusing on vocals only? 00:41:372 - top diff, half the sounds aren't mapped o_o",
        "created_at": "2020-05-24T00:37:37+00:00",
        "updated_at": "2020-05-24T00:37:37+00:00",
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
  },
  {
    "avatar_url": "https://a.ppy.sh/7149815?1590036181.jpeg",
    "country_code": "US",
    "default_group": "default",
    "id": 7149815,
    "is_active": true,
    "is_bot": false,
    "is_online": true,
    "is_supporter": false,
    "last_visit": "2020-05-24T00:50:35+00:00",
    "pm_friends_only": false,
    "profile_colour": null,
    "username": "Plaudible"
  },
  {
    "avatar_url": "https://a.ppy.sh/10476879?1589254634.jpeg",
    "country_code": "US",
    "default_group": "default",
    "id": 10476879,
    "is_active": true,
    "is_bot": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2020-05-24T00:52:19+00:00",
    "pm_friends_only": false,
    "profile_colour": null,
    "username": "Vebox"
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