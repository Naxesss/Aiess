from bs4 import BeautifulSoup

from requester import soupify

# Includes an event of a deleted beatmapset, as well as an empty event.
JSON = """
[
  {
    "id": 1436266,
    "beatmapset_id": 596926,
    "beatmap_id": 1262085,
    "user_id": 11939459,
    "deleted_by_id": null,
    "message_type": "suggestion",
    "parent_id": null,
    "timestamp": 65140,
    "resolved": false,
    "can_be_resolved": true,
    "can_grant_kudosu": true,
    "created_at": "2020-03-07T20:42:58+00:00",
    "updated_at": "2020-03-07T20:42:58+00:00",
    "deleted_at": null,
    "last_post_at": "2020-03-07T20:42:58+00:00",
    "kudosu_denied": false,
    "beatmap": {
      "id": 1262085,
      "mode": "osu",
      "difficulty_rating": 7.72,
      "version": "Revaten"
    },
    "beatmapset": {
      "id": 596926,
      "title": "Lilieze to Enryuu Laevateinn",
      "artist": "Kuroneko Dungeon",
      "creator": "sYreNn",
      "user_id": 7762274,
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/596926/covers/cover.jpg?1583190965",
        "cover@2x": "https://assets.ppy.sh/beatmaps/596926/covers/cover@2x.jpg?1583190965",
        "card": "https://assets.ppy.sh/beatmaps/596926/covers/card.jpg?1583190965",
        "card@2x": "https://assets.ppy.sh/beatmaps/596926/covers/card@2x.jpg?1583190965",
        "list": "https://assets.ppy.sh/beatmaps/596926/covers/list.jpg?1583190965",
        "list@2x": "https://assets.ppy.sh/beatmaps/596926/covers/list@2x.jpg?1583190965",
        "slimcover": "https://assets.ppy.sh/beatmaps/596926/covers/slimcover.jpg?1583190965",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/596926/covers/slimcover@2x.jpg?1583190965"
      },
      "favourite_count": 9,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/596926.mp3",
      "video": false,
      "source": "REFLEC BEAT colette -Summer-",
      "status": "pending"
    },
    "starting_post": {
      "id": 4041540,
      "beatmap_discussion_id": 1436266,
      "user_id": 11939459,
      "last_editor_id": null,
      "deleted_by_id": null,
      "system": false,
      "message": "01:05:140 (1,2,1,2,1,2,1,2,1,2) - You use this back & forward stream pattern here but the music doesn't really allow for this kind of patterning. Usually patterns like this only really get mapped when the song goes more crazy with repeating changes in pitch i.e high note -> low note -> high note etc. Here that isn't really the case and that makes this pattern stand out a lot more. A pattern with lower spacing at the beginning and then increase in spacing after 01:05:590 (1) - to represent the higher pitch will represent the song more closely.",
      "created_at": "2020-03-07T20:42:58+00:00",
      "updated_at": "2020-03-07T20:42:58+00:00",
      "deleted_at": null
    }
  },
  {
    "id": 1436265,
    "beatmapset_id": 596926,
    "beatmap_id": 1262085,
    "user_id": 11939459,
    "deleted_by_id": null,
    "message_type": "suggestion",
    "parent_id": null,
    "timestamp": 46090,
    "resolved": false,
    "can_be_resolved": true,
    "can_grant_kudosu": true,
    "created_at": "2020-03-07T20:42:09+00:00",
    "updated_at": "2020-03-07T20:42:09+00:00",
    "deleted_at": null,
    "last_post_at": "2020-03-07T20:42:09+00:00",
    "kudosu_denied": false,
    "beatmap": {
      "id": 1262085,
      "mode": "osu",
      "difficulty_rating": 7.72,
      "version": "Revaten"
    },
    "beatmapset": {
      "id": 596926,
      "title": "Lilieze to Enryuu Laevateinn",
      "artist": "Kuroneko Dungeon",
      "creator": "sYreNn",
      "user_id": 7762274,
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/596926/covers/cover.jpg?1583190965",
        "cover@2x": "https://assets.ppy.sh/beatmaps/596926/covers/cover@2x.jpg?1583190965",
        "card": "https://assets.ppy.sh/beatmaps/596926/covers/card.jpg?1583190965",
        "card@2x": "https://assets.ppy.sh/beatmaps/596926/covers/card@2x.jpg?1583190965",
        "list": "https://assets.ppy.sh/beatmaps/596926/covers/list.jpg?1583190965",
        "list@2x": "https://assets.ppy.sh/beatmaps/596926/covers/list@2x.jpg?1583190965",
        "slimcover": "https://assets.ppy.sh/beatmaps/596926/covers/slimcover.jpg?1583190965",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/596926/covers/slimcover@2x.jpg?1583190965"
      },
      "favourite_count": 9,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/596926.mp3",
      "video": false,
      "source": "REFLEC BEAT colette -Summer-",
      "status": "pending"
    },
    "starting_post": {
      "id": 4041535,
      "beatmap_discussion_id": 1436265,
      "user_id": 11939459,
      "last_editor_id": null,
      "deleted_by_id": null,
      "system": false,
      "message": "00:46:090 (1,2,3,4) - The difference between how you mapped this section & 00:50:890 (1,2,1,2) - is quite big even though the song is exactly the same. For consistency chose one of the two ways you want to represent these sounds and stick with that instead of changing it.",
      "created_at": "2020-03-07T20:42:09+00:00",
      "updated_at": "2020-03-07T20:42:09+00:00",
      "deleted_at": null
    }
  },
  {
    "id": 1436264,
    "beatmapset_id": 294626,
    "beatmap_id": 2342214,
    "user_id": 2597417,
    "deleted_by_id": null,
    "message_type": "suggestion",
    "parent_id": null,
    "timestamp": 46640,
    "resolved": false,
    "can_be_resolved": true,
    "can_grant_kudosu": true,
    "created_at": "2020-03-07T20:41:35+00:00",
    "updated_at": "2020-03-07T20:41:35+00:00",
    "deleted_at": null,
    "last_post_at": "2020-03-07T20:41:35+00:00",
    "kudosu_denied": false,
    "beatmap": {
      "id": 2342214,
      "mode": "taiko",
      "difficulty_rating": 1.79,
      "version": "Muzukashii"
    },
    "beatmapset": {
      "id": 294626,
      "title": "Shidake Town",
      "artist": "Go Ichinose",
      "creator": "Charlotte",
      "user_id": 3686901,
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/294626/covers/cover.jpg?1583597094",
        "cover@2x": "https://assets.ppy.sh/beatmaps/294626/covers/cover@2x.jpg?1583597094",
        "card": "https://assets.ppy.sh/beatmaps/294626/covers/card.jpg?1583597094",
        "card@2x": "https://assets.ppy.sh/beatmaps/294626/covers/card@2x.jpg?1583597094",
        "list": "https://assets.ppy.sh/beatmaps/294626/covers/list.jpg?1583597094",
        "list@2x": "https://assets.ppy.sh/beatmaps/294626/covers/list@2x.jpg?1583597094",
        "slimcover": "https://assets.ppy.sh/beatmaps/294626/covers/slimcover.jpg?1583597094",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/294626/covers/slimcover@2x.jpg?1583597094"
      },
      "favourite_count": 1,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/294626.mp3",
      "video": false,
      "source": "ポケットモンスター ルビー・サファイア",
      "status": "pending"
    },
    "starting_post": {
      "id": 4041531,
      "beatmap_discussion_id": 1436264,
      "user_id": 2597417,
      "last_editor_id": null,
      "deleted_by_id": null,
      "system": false,
      "message": "00:46:640 - k",
      "created_at": "2020-03-07T20:41:35+00:00",
      "updated_at": "2020-03-07T20:41:35+00:00",
      "deleted_at": null
    }
  },
  [],
  {
    "id": 1389788,
    "beatmapset_id": 1010537,
    "beatmap_id": null,
    "user_id": 11746150,
    "deleted_by_id": null,
    "message_type": "hype",
    "parent_id": null,
    "timestamp": null,
    "resolved": false,
    "can_be_resolved": false,
    "can_grant_kudosu": false,
    "created_at": "2020-02-09T04:00:02+00:00",
    "updated_at": "2020-02-09T04:00:02+00:00",
    "deleted_at": null,
    "last_post_at": "2020-02-09T04:00:02+00:00",
    "kudosu_denied": false,
    "beatmapset": {
      "id": 1010537,
      "title": "Otome-domo yo.",
      "artist": "CHiCO with HoneyWorks",
      "creator": "AIR",
      "user_id": 2070688,
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/1010537/covers/cover.jpg?1583036954",
        "cover@2x": "https://assets.ppy.sh/beatmaps/1010537/covers/cover@2x.jpg?1583036954",
        "card": "https://assets.ppy.sh/beatmaps/1010537/covers/card.jpg?1583036954",
        "card@2x": "https://assets.ppy.sh/beatmaps/1010537/covers/card@2x.jpg?1583036954",
        "list": "https://assets.ppy.sh/beatmaps/1010537/covers/list.jpg?1583036954",
        "list@2x": "https://assets.ppy.sh/beatmaps/1010537/covers/list@2x.jpg?1583036954",
        "slimcover": "https://assets.ppy.sh/beatmaps/1010537/covers/slimcover.jpg?1583036954",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/1010537/covers/slimcover@2x.jpg?1583036954"
      },
      "favourite_count": 14,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/1010537.mp3",
      "video": false,
      "source": "荒ぶる季節の乙女どもよ。",
      "status": "graveyard"
    },
    "starting_post": {
      "id": 3909724,
      "beatmap_discussion_id": 1389788,
      "user_id": 11746150,
      "last_editor_id": null,
      "deleted_by_id": null,
      "system": false,
      "message": "12",
      "created_at": "2020-02-09T04:00:02+00:00",
      "updated_at": "2020-02-09T04:00:02+00:00",
      "deleted_at": null
    }
  },
  {
    "id": 1436263,
    "beatmapset_id": 1118343,
    "beatmap_id": 2335961,
    "user_id": 8050850,
    "deleted_by_id": null,
    "message_type": "suggestion",
    "parent_id": null,
    "timestamp": 11409,
    "resolved": false,
    "can_be_resolved": true,
    "can_grant_kudosu": true,
    "created_at": "2020-03-07T20:41:26+00:00",
    "updated_at": "2020-03-07T20:41:26+00:00",
    "deleted_at": null,
    "last_post_at": "2020-03-07T20:41:26+00:00",
    "kudosu_denied": false,
    "beatmap": {
      "id": 2335961,
      "mode": "taiko",
      "difficulty_rating": 4.9,
      "version": "Oni"
    },
    "beatmapset": {
      "id": 1118343,
      "title": "Absent Color",
      "artist": "Sound Souler",
      "creator": "Striiker",
      "user_id": 7291594,
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/1118343/covers/cover.jpg?1583199708",
        "cover@2x": "https://assets.ppy.sh/beatmaps/1118343/covers/cover@2x.jpg?1583199708",
        "card": "https://assets.ppy.sh/beatmaps/1118343/covers/card.jpg?1583199708",
        "card@2x": "https://assets.ppy.sh/beatmaps/1118343/covers/card@2x.jpg?1583199708",
        "list": "https://assets.ppy.sh/beatmaps/1118343/covers/list.jpg?1583199708",
        "list@2x": "https://assets.ppy.sh/beatmaps/1118343/covers/list@2x.jpg?1583199708",
        "slimcover": "https://assets.ppy.sh/beatmaps/1118343/covers/slimcover.jpg?1583199708",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/1118343/covers/slimcover@2x.jpg?1583199708"
      },
      "favourite_count": 0,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/1118343.mp3",
      "video": false,
      "source": "osu!",
      "status": "wip"
    },
    "starting_post": {
      "id": 4041530,
      "beatmap_discussion_id": 1436263,
      "user_id": 8050850,
      "last_editor_id": null,
      "deleted_by_id": null,
      "system": false,
      "message": "00:11:409 - Maybe raise the hitsound volume here since this is where the drums begin.",
      "created_at": "2020-03-07T20:41:26+00:00",
      "updated_at": "2020-03-07T20:41:26+00:00",
      "deleted_at": null
    }
  },
  {
    "id": 1436262,
    "beatmapset_id": 294626,
    "beatmap_id": 2342214,
    "user_id": 2597417,
    "deleted_by_id": null,
    "message_type": "suggestion",
    "parent_id": null,
    "timestamp": 40007,
    "resolved": false,
    "can_be_resolved": true,
    "can_grant_kudosu": true,
    "created_at": "2020-03-07T20:41:18+00:00",
    "updated_at": "2020-03-07T20:41:18+00:00",
    "deleted_at": null,
    "last_post_at": "2020-03-07T20:41:18+00:00",
    "kudosu_denied": false,
    "beatmap": {
      "id": 2342214,
      "mode": "taiko",
      "difficulty_rating": 1.79,
      "version": "Muzukashii"
    },
    "beatmapset": {
      "id": 294626,
      "title": "Shidake Town",
      "artist": "Go Ichinose",
      "creator": "Charlotte",
      "user_id": 3686901,
      "covers": {
        "cover": "https://assets.ppy.sh/beatmaps/294626/covers/cover.jpg?1583597094",
        "cover@2x": "https://assets.ppy.sh/beatmaps/294626/covers/cover@2x.jpg?1583597094",
        "card": "https://assets.ppy.sh/beatmaps/294626/covers/card.jpg?1583597094",
        "card@2x": "https://assets.ppy.sh/beatmaps/294626/covers/card@2x.jpg?1583597094",
        "list": "https://assets.ppy.sh/beatmaps/294626/covers/list.jpg?1583597094",
        "list@2x": "https://assets.ppy.sh/beatmaps/294626/covers/list@2x.jpg?1583597094",
        "slimcover": "https://assets.ppy.sh/beatmaps/294626/covers/slimcover.jpg?1583597094",
        "slimcover@2x": "https://assets.ppy.sh/beatmaps/294626/covers/slimcover@2x.jpg?1583597094"
      },
      "favourite_count": 1,
      "play_count": 0,
      "preview_url": "//b.ppy.sh/preview/294626.mp3",
      "video": false,
      "source": "ポケットモンスター ルビー・サファイア",
      "status": "pending"
    },
    "starting_post": {
      "id": 4041529,
      "beatmap_discussion_id": 1436262,
      "user_id": 2597417,
      "last_editor_id": null,
      "deleted_by_id": null,
      "system": false,
      "message": "00:40:007 - add dd for a ddk triplet",
      "created_at": "2020-03-07T20:41:18+00:00",
      "updated_at": "2020-03-07T20:41:18+00:00",
      "deleted_at": null
    }
  }
]
"""

USER_JSON = """
[
  {
    "id": 2597417,
    "username": "Jaltzu",
    "profile_colour": null,
    "avatar_url": "https://a.ppy.sh/2597417?1581606041.png",
    "country_code": "FI",
    "default_group": "default",
    "is_active": true,
    "is_bot": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2020-03-07T20:43:00+00:00",
    "pm_friends_only": false
  },
  {
    "id": 8050850,
    "username": "3san",
    "profile_colour": null,
    "avatar_url": "https://a.ppy.sh/8050850?1578633567.png",
    "country_code": "US",
    "default_group": "default",
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false
  },
  {
    "id": 11939459,
    "username": "Jelljel",
    "profile_colour": null,
    "avatar_url": "https://a.ppy.sh/11939459?1583583304.jpeg",
    "country_code": "NL",
    "default_group": "default",
    "is_active": true,
    "is_bot": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2020-03-07T20:42:00+00:00",
    "pm_friends_only": false
  }
]
"""

HTML = f"""
<script id="json-discussions" type="application/json">
{JSON}
</script>
<script id="json-users" type="application/json">
{USER_JSON}
</script>
"""

soup: BeautifulSoup = soupify(HTML)