import sys
sys.path.append('..')

from bs4 import BeautifulSoup

from scraper.requester import soupify

JSON = r"""
{
  "beatmapset": {
    "artist": "Fox Stevenson",
    "covers": {
      "cover": "https://assets.ppy.sh/beatmaps/1112303/covers/cover.jpg?1593620060",
      "cover@2x": "https://assets.ppy.sh/beatmaps/1112303/covers/cover@2x.jpg?1593620060",
      "card": "https://assets.ppy.sh/beatmaps/1112303/covers/card.jpg?1593620060",
      "card@2x": "https://assets.ppy.sh/beatmaps/1112303/covers/card@2x.jpg?1593620060",
      "list": "https://assets.ppy.sh/beatmaps/1112303/covers/list.jpg?1593620060",
      "list@2x": "https://assets.ppy.sh/beatmaps/1112303/covers/list@2x.jpg?1593620060",
      "slimcover": "https://assets.ppy.sh/beatmaps/1112303/covers/slimcover.jpg?1593620060",
      "slimcover@2x": "https://assets.ppy.sh/beatmaps/1112303/covers/slimcover@2x.jpg?1593620060"
    },
    "creator": "Altai",
    "favourite_count": 11,
    "id": 1112303,
    "play_count": 135,
    "preview_url": "//b.ppy.sh/preview/1112303.mp3",
    "source": "",
    "status": "qualified",
    "title": "Take You Down",
    "user_id": 5745865,
    "video": false,
    "availability": {
      "download_disabled": false,
      "more_information": null
    },
    "bpm": 174,
    "can_be_hyped": true,
    "discussion_enabled": true,
    "discussion_locked": false,
    "hype": {
      "current": 9,
      "required": 5
    },
    "is_scoreable": true,
    "last_updated": "2020-07-01T16:13:46+00:00",
    "legacy_thread_url": "https://osu.ppy.sh/community/forums/topics/1025106",
    "nominations": {
      "required_hype": 5,
      "required": 2,
      "current": 2,
      "ranking_eta": "2020-07-08T22:29:40+00:00"
    },
    "ranked": 3,
    "ranked_date": "2020-07-01T20:48:57+00:00",
    "storyboard": false,
    "submitted_date": "2020-02-19T20:59:18+00:00",
    "tags": "stan sb stanley stevenson byrne english electronic dnb dance frakturehawkens lmt icekalt sirmirai kirylln undeadphoneguy ksardas drum and bass n &",
    "has_favourited": false,
    "beatmaps": [
      {
        "difficulty_rating": 5.35,
        "id": 2323862,
        "mode": "osu",
        "version": "Descend",
        "accuracy": 8.5,
        "ar": 9.2,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 133,
        "count_sliders": 201,
        "count_spinners": 1,
        "count_total": 538,
        "cs": 4.1,
        "deleted_at": null,
        "drain": 6,
        "hit_length": 108,
        "is_scoreable": true,
        "last_updated": "2020-07-01T16:13:47+00:00",
        "mode_int": 0,
        "passcount": 9,
        "playcount": 45,
        "ranked": 3,
        "status": "qualified",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2323862"
      },
      {
        "difficulty_rating": 4.95,
        "id": 2323863,
        "mode": "osu",
        "version": "Frakturehawkens' Extra",
        "accuracy": 8,
        "ar": 9,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 140,
        "count_sliders": 172,
        "count_spinners": 4,
        "count_total": 496,
        "cs": 3.8,
        "deleted_at": null,
        "drain": 5.2,
        "hit_length": 108,
        "is_scoreable": true,
        "last_updated": "2020-07-01T16:13:48+00:00",
        "mode_int": 0,
        "passcount": 9,
        "playcount": 18,
        "ranked": 3,
        "status": "qualified",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2323863"
      },
      {
        "difficulty_rating": 4.84,
        "id": 2323864,
        "mode": "osu",
        "version": "Icekalt's Insane",
        "accuracy": 8,
        "ar": 9,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 166,
        "count_sliders": 182,
        "count_spinners": 1,
        "count_total": 533,
        "cs": 3.4,
        "deleted_at": null,
        "drain": 5,
        "hit_length": 108,
        "is_scoreable": true,
        "last_updated": "2020-07-01T16:13:48+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": 3,
        "status": "qualified",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2323864"
      },
      {
        "difficulty_rating": 4.75,
        "id": 2323865,
        "mode": "osu",
        "version": "kiry's Insane",
        "accuracy": 7.5,
        "ar": 9,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 227,
        "count_sliders": 107,
        "count_spinners": 1,
        "count_total": 444,
        "cs": 4,
        "deleted_at": "2020-04-25T15:13:33.000000Z",
        "drain": 5,
        "hit_length": 102,
        "is_scoreable": false,
        "last_updated": "2020-04-25T15:02:31+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2323865"
      },
      {
        "difficulty_rating": 2.3,
        "id": 2323866,
        "mode": "osu",
        "version": "Normal",
        "accuracy": 4,
        "ar": 5,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 81,
        "count_sliders": 109,
        "count_spinners": 1,
        "count_total": 302,
        "cs": 3,
        "deleted_at": null,
        "drain": 3,
        "hit_length": 108,
        "is_scoreable": true,
        "last_updated": "2020-07-01T16:13:49+00:00",
        "mode_int": 0,
        "passcount": 9,
        "playcount": 45,
        "ranked": 3,
        "status": "qualified",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2323866"
      },
      {
        "difficulty_rating": 0,
        "id": 2331900,
        "mode": "osu",
        "version": "",
        "accuracy": 0,
        "ar": 0,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 0,
        "count_sliders": 0,
        "count_spinners": 0,
        "count_total": 0,
        "cs": 0,
        "deleted_at": "2020-02-27T12:19:54.000000Z",
        "drain": 0,
        "hit_length": 0,
        "is_scoreable": false,
        "last_updated": "2020-02-27T12:11:14+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 0,
        "url": "https://osu.ppy.sh/beatmaps/2331900"
      },
      {
        "difficulty_rating": 0,
        "id": 2331901,
        "mode": "osu",
        "version": "",
        "accuracy": 0,
        "ar": 0,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 0,
        "count_sliders": 0,
        "count_spinners": 0,
        "count_total": 0,
        "cs": 0,
        "deleted_at": "2020-02-27T12:19:54.000000Z",
        "drain": 0,
        "hit_length": 0,
        "is_scoreable": false,
        "last_updated": "2020-02-27T12:11:14+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 0,
        "url": "https://osu.ppy.sh/beatmaps/2331901"
      },
      {
        "difficulty_rating": 0,
        "id": 2331902,
        "mode": "osu",
        "version": "",
        "accuracy": 0,
        "ar": 0,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 0,
        "count_sliders": 0,
        "count_spinners": 0,
        "count_total": 0,
        "cs": 0,
        "deleted_at": "2020-02-27T12:19:54.000000Z",
        "drain": 0,
        "hit_length": 0,
        "is_scoreable": false,
        "last_updated": "2020-02-27T12:11:14+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 0,
        "url": "https://osu.ppy.sh/beatmaps/2331902"
      },
      {
        "difficulty_rating": 5.1,
        "id": 2331905,
        "mode": "osu",
        "version": "LMT's Expert",
        "accuracy": 8.3,
        "ar": 9.2,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 259,
        "count_sliders": 159,
        "count_spinners": 2,
        "count_total": 583,
        "cs": 4,
        "deleted_at": null,
        "drain": 5.5,
        "hit_length": 111,
        "is_scoreable": true,
        "last_updated": "2020-07-01T16:13:50+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": 3,
        "status": "qualified",
        "total_length": 122,
        "url": "https://osu.ppy.sh/beatmaps/2331905"
      },
      {
        "difficulty_rating": 3.46,
        "id": 2331906,
        "mode": "osu",
        "version": "Mirai x Altai's Hard",
        "accuracy": 7,
        "ar": 8,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 98,
        "count_sliders": 152,
        "count_spinners": 0,
        "count_total": 402,
        "cs": 3.5,
        "deleted_at": null,
        "drain": 4.5,
        "hit_length": 108,
        "is_scoreable": true,
        "last_updated": "2020-07-01T16:13:51+00:00",
        "mode_int": 0,
        "passcount": 9,
        "playcount": 18,
        "ranked": 3,
        "status": "qualified",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2331906"
      },
      {
        "difficulty_rating": 0,
        "id": 2413430,
        "mode": "osu",
        "version": "",
        "accuracy": 0,
        "ar": 0,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 0,
        "count_sliders": 0,
        "count_spinners": 0,
        "count_total": 0,
        "cs": 0,
        "deleted_at": "2020-04-25T15:25:44.000000Z",
        "drain": 0,
        "hit_length": 0,
        "is_scoreable": false,
        "last_updated": "2020-04-25T15:13:02+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 0,
        "url": "https://osu.ppy.sh/beatmaps/2413430"
      },
      {
        "difficulty_rating": 4.75,
        "id": 2413431,
        "mode": "osu",
        "version": "kiry's Insane",
        "accuracy": 7.5,
        "ar": 9,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 227,
        "count_sliders": 107,
        "count_spinners": 1,
        "count_total": 444,
        "cs": 4,
        "deleted_at": "2020-04-25T16:36:50.000000Z",
        "drain": 5,
        "hit_length": 102,
        "is_scoreable": false,
        "last_updated": "2020-04-25T15:26:57+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2413431"
      },
      {
        "difficulty_rating": 0,
        "id": 2413444,
        "mode": "osu",
        "version": "",
        "accuracy": 0,
        "ar": 0,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 0,
        "count_sliders": 0,
        "count_spinners": 0,
        "count_total": 0,
        "cs": 0,
        "deleted_at": "2020-04-25T15:26:44.000000Z",
        "drain": 0,
        "hit_length": 0,
        "is_scoreable": false,
        "last_updated": "2020-04-25T15:25:44+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 0,
        "url": "https://osu.ppy.sh/beatmaps/2413444"
      },
      {
        "difficulty_rating": 0,
        "id": 2413551,
        "mode": "osu",
        "version": "",
        "accuracy": 0,
        "ar": 0,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 0,
        "count_sliders": 0,
        "count_spinners": 0,
        "count_total": 0,
        "cs": 0,
        "deleted_at": "2020-04-25T16:38:00.000000Z",
        "drain": 0,
        "hit_length": 0,
        "is_scoreable": false,
        "last_updated": "2020-04-25T16:36:16+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 0,
        "url": "https://osu.ppy.sh/beatmaps/2413551"
      },
      {
        "difficulty_rating": 4.75,
        "id": 2413552,
        "mode": "osu",
        "version": "kiry's Insane",
        "accuracy": 7.5,
        "ar": 9,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 227,
        "count_sliders": 107,
        "count_spinners": 1,
        "count_total": 444,
        "cs": 4,
        "deleted_at": null,
        "drain": 5,
        "hit_length": 103,
        "is_scoreable": true,
        "last_updated": "2020-07-01T16:13:52+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 9,
        "ranked": 3,
        "status": "qualified",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2413552"
      },
      {
        "difficulty_rating": 5.33,
        "id": 2448363,
        "mode": "osu",
        "version": "Ksardas' Extra",
        "accuracy": 8.5,
        "ar": 9.3,
        "beatmapset_id": 1112303,
        "bpm": 174,
        "convert": false,
        "count_circles": 132,
        "count_sliders": 239,
        "count_spinners": 2,
        "count_total": 616,
        "cs": 4,
        "deleted_at": null,
        "drain": 5,
        "hit_length": 108,
        "is_scoreable": true,
        "last_updated": "2020-07-01T16:13:52+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": 3,
        "status": "qualified",
        "total_length": 119,
        "url": "https://osu.ppy.sh/beatmaps/2448363"
      }
    ],
    "current_user_attributes": {
      "can_delete": false,
      "can_edit_metadata": true,
      "can_hype": true,
      "can_hype_reason": null,
      "can_love": false,
      "is_watching": false,
      "new_hype_time": null,
      "remaining_hype": 10
    },
    "discussions": [
      {
        "id": 1406140,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-02-19T21:13:09+00:00",
        "updated_at": "2020-02-19T21:13:09+00:00",
        "deleted_at": null,
        "last_post_at": "2020-02-19T21:13:09+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3955267,
            "beatmap_discussion_id": 1406140,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "<3",
            "created_at": "2020-02-19T21:13:09+00:00",
            "updated_at": "2020-02-19T21:13:09+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1406430,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 6842421,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-02-20T01:11:30+00:00",
        "updated_at": "2020-02-20T01:11:30+00:00",
        "deleted_at": null,
        "last_post_at": "2020-02-20T01:11:30+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3955914,
            "beatmap_discussion_id": 1406430,
            "user_id": 6842421,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Hype",
            "created_at": "2020-02-20T01:11:30+00:00",
            "updated_at": "2020-02-20T01:11:30+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1406431,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 7458583,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-02-20T01:12:12+00:00",
        "updated_at": "2020-02-20T01:12:12+00:00",
        "deleted_at": null,
        "last_post_at": "2020-02-20T01:12:12+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3955915,
            "beatmap_discussion_id": 1406431,
            "user_id": 7458583,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i gucci",
            "created_at": "2020-02-20T01:12:12+00:00",
            "updated_at": "2020-02-20T01:12:12+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1407831,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 6115007,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-02-20T22:48:27+00:00",
        "updated_at": "2020-02-20T22:48:27+00:00",
        "deleted_at": null,
        "last_post_at": "2020-02-20T22:48:27+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3960191,
            "beatmap_discussion_id": 1407831,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "cool",
            "created_at": "2020-02-20T22:48:27+00:00",
            "updated_at": "2020-02-20T22:48:27+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1410732,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 11310911,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-02-22T14:17:02+00:00",
        "updated_at": "2020-02-22T14:17:02+00:00",
        "deleted_at": null,
        "last_post_at": "2020-02-22T14:17:02+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3968755,
            "beatmap_discussion_id": 1410732,
            "user_id": 11310911,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊",
            "created_at": "2020-02-22T14:17:02+00:00",
            "updated_at": "2020-02-22T14:17:02+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1421639,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331906,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 96233,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T21:49:50+00:00",
        "updated_at": "2020-04-25T14:55:33+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:55:33+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000497,
            "beatmap_discussion_id": 1421639,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:36:233 (4,1) - wouldn't say this is the best idea in a hard, especially since something like this hasn't been introduced before. try https://i.imgur.com/cQ1undP.png to make it easier to read",
            "created_at": "2020-02-28T21:49:50+00:00",
            "updated_at": "2020-02-28T21:49:50+00:00",
            "deleted_at": null
          },
          {
            "id": 4000615,
            "beatmap_discussion_id": 1421639,
            "user_id": 13646997,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "agree",
            "created_at": "2020-02-28T22:38:55+00:00",
            "updated_at": "2020-02-28T22:38:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4340491,
            "beatmap_discussion_id": 1421639,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T14:55:33+00:00",
            "updated_at": "2020-04-25T14:55:33+00:00",
            "deleted_at": null
          },
          {
            "id": 4340492,
            "beatmap_discussion_id": 1421639,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:55:33+00:00",
            "updated_at": "2020-04-25T14:55:33+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              13646997
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421645,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 22095,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T21:53:44+00:00",
        "updated_at": "2020-04-25T15:03:42+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:58:04+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000513,
            "beatmap_discussion_id": 1421645,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:22:095 (1,2,3) - this might be confusing for newbs to read cos 3/2 gap and 3 being visually closer to 1.  try something like https://i.imgur.com/JOHA3Hh.png",
            "created_at": "2020-02-28T21:53:44+00:00",
            "updated_at": "2020-02-28T21:53:44+00:00",
            "deleted_at": null
          },
          {
            "id": 4340507,
            "beatmap_discussion_id": 1421645,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure",
            "created_at": "2020-04-25T14:58:03+00:00",
            "updated_at": "2020-04-25T14:58:03+00:00",
            "deleted_at": null
          },
          {
            "id": 4340508,
            "beatmap_discussion_id": 1421645,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:58:04+00:00",
            "updated_at": "2020-04-25T14:58:04+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421647,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 80026,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T21:55:19+00:00",
        "updated_at": "2020-04-25T15:03:44+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:59:18+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000518,
            "beatmap_discussion_id": 1421647,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:20:026 (1,2) - i highly doubt that this is intentional",
            "created_at": "2020-02-28T21:55:19+00:00",
            "updated_at": "2020-02-28T21:55:19+00:00",
            "deleted_at": null
          },
          {
            "id": 4340514,
            "beatmap_discussion_id": 1421647,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea u right",
            "created_at": "2020-04-25T14:59:18+00:00",
            "updated_at": "2020-04-25T14:59:18+00:00",
            "deleted_at": null
          },
          {
            "id": 4340515,
            "beatmap_discussion_id": 1421647,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:59:18+00:00",
            "updated_at": "2020-04-25T14:59:18+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421651,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T21:59:34+00:00",
        "updated_at": "2020-04-25T15:01:25+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T15:01:25+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000527,
            "beatmap_discussion_id": 1421651,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i'd recommend you to adjust your hitsounding in the section starting at 01:06:923 - cos here u start following the backgrounding instrument with normal whistles which sounds very off considering that you still follow the main instrument. an example would be 01:08:302 (5) - where it would make much more sense to have the whistle on the head to fit ur rhythm",
            "created_at": "2020-02-28T21:59:34+00:00",
            "updated_at": "2020-02-28T21:59:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4000645,
            "beatmap_discussion_id": 1421651,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "also applies to hard",
            "created_at": "2020-02-28T22:54:52+00:00",
            "updated_at": "2020-02-28T22:54:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4340521,
            "beatmap_discussion_id": 1421651,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "the hsing is following it to compensate for the fact that I can't follow both without the rhythm being too dense, although I do understand ur point. I'll look into it if more ppl think it's an issue but I think it's not too big of a deal for now",
            "created_at": "2020-04-25T15:01:25+00:00",
            "updated_at": "2020-04-25T15:01:25+00:00",
            "deleted_at": null
          },
          {
            "id": 4340522,
            "beatmap_discussion_id": 1421651,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T15:01:25+00:00",
            "updated_at": "2020-04-25T15:01:25+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1421653,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 24681,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:01:05+00:00",
        "updated_at": "2020-04-25T15:03:43+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:58:56+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000529,
            "beatmap_discussion_id": 1421653,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:24:681 (6) - just a tiny suggestion but u could use the red anchor to bump the sound at 00:25:371 -",
            "created_at": "2020-02-28T22:01:05+00:00",
            "updated_at": "2020-02-28T22:01:05+00:00",
            "deleted_at": null
          },
          {
            "id": 4340512,
            "beatmap_discussion_id": 1421653,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure",
            "created_at": "2020-04-25T14:58:56+00:00",
            "updated_at": "2020-04-25T14:58:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4340513,
            "beatmap_discussion_id": 1421653,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:58:56+00:00",
            "updated_at": "2020-04-25T14:58:56+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421656,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323862,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 30457,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:02:57+00:00",
        "updated_at": "2020-04-25T15:03:14+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:36:34+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000532,
            "beatmap_discussion_id": 1421656,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:30:457 (1) - silence the end pls",
            "created_at": "2020-02-28T22:02:57+00:00",
            "updated_at": "2020-02-28T22:02:57+00:00",
            "deleted_at": null
          },
          {
            "id": 4035019,
            "beatmap_discussion_id": 1421656,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "actually i'd end this 1/4 later and remove the circle cos it makes 00:32:612 (1,1,1) - much easier to play and there's not really a significant thing on 00:32:440 (1) - imo",
            "created_at": "2020-03-06T22:26:17+00:00",
            "updated_at": "2020-03-06T22:26:17+00:00",
            "deleted_at": null
          },
          {
            "id": 4340368,
            "beatmap_discussion_id": 1421656,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea u right",
            "created_at": "2020-04-25T14:36:34+00:00",
            "updated_at": "2020-04-25T14:36:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4340369,
            "beatmap_discussion_id": 1421656,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:36:34+00:00",
            "updated_at": "2020-04-25T14:36:34+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421657,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323862,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 38992,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:04:02+00:00",
        "updated_at": "2020-04-25T15:03:32+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:37:03+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000533,
            "beatmap_discussion_id": 1421657,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:38:992 (3) - minor but put this into the triangle centre to make it look extra cute",
            "created_at": "2020-02-28T22:04:02+00:00",
            "updated_at": "2020-02-28T22:04:02+00:00",
            "deleted_at": null
          },
          {
            "id": 4340372,
            "beatmap_discussion_id": 1421657,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "was meant to be like that, should be better now",
            "created_at": "2020-04-25T14:37:03+00:00",
            "updated_at": "2020-04-25T14:37:03+00:00",
            "deleted_at": null
          },
          {
            "id": 4340373,
            "beatmap_discussion_id": 1421657,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:37:03+00:00",
            "updated_at": "2020-04-25T14:37:03+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421661,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323862,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 44164,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:04:53+00:00",
        "updated_at": "2020-04-25T15:03:33+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:37:53+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000539,
            "beatmap_discussion_id": 1421661,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:44:164 (1) - finish on head, this has the same cymbal sound as 00:33:129 (1) -",
            "created_at": "2020-02-28T22:04:53+00:00",
            "updated_at": "2020-02-28T22:04:53+00:00",
            "deleted_at": null
          },
          {
            "id": 4000540,
            "beatmap_discussion_id": 1421661,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "applies for copied hitsounding too btw",
            "created_at": "2020-02-28T22:05:07+00:00",
            "updated_at": "2020-02-28T22:05:07+00:00",
            "deleted_at": null
          },
          {
            "id": 4000542,
            "beatmap_discussion_id": 1421661,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:02:267 (2) - normal whistle on head",
            "created_at": "2020-02-28T22:06:18+00:00",
            "updated_at": "2020-02-28T22:06:18+00:00",
            "deleted_at": null
          },
          {
            "id": 4000551,
            "beatmap_discussion_id": 1421661,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": 2204515,
            "system": false,
            "message": "01:07:785 (1) - ^",
            "created_at": "2020-02-28T22:08:32+00:00",
            "updated_at": "2020-02-28T22:08:47+00:00",
            "deleted_at": "2020-02-28T22:08:47+00:00"
          },
          {
            "id": 4340387,
            "beatmap_discussion_id": 1421661,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "aaa ok",
            "created_at": "2020-04-25T14:37:53+00:00",
            "updated_at": "2020-04-25T14:37:53+00:00",
            "deleted_at": null
          },
          {
            "id": 4340388,
            "beatmap_discussion_id": 1421661,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:37:53+00:00",
            "updated_at": "2020-04-25T14:37:53+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421664,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323862,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 65457,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:10:45+00:00",
        "updated_at": "2020-04-25T15:03:34+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:48:55+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000554,
            "beatmap_discussion_id": 1421664,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:05:457 (2) - 01:16:492 (2) - 01:27:526 (2) - would recommend adding claps (or drum addition whistles) to these cos they are the strongest drum sound in the triple",
            "created_at": "2020-02-28T22:10:45+00:00",
            "updated_at": "2020-02-28T22:10:45+00:00",
            "deleted_at": null
          },
          {
            "id": 4340458,
            "beatmap_discussion_id": 1421664,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fixed",
            "created_at": "2020-04-25T14:48:54+00:00",
            "updated_at": "2020-04-25T14:48:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4340459,
            "beatmap_discussion_id": 1421664,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:48:55+00:00",
            "updated_at": "2020-04-25T14:48:55+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421667,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323862,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 24681,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:13:05+00:00",
        "updated_at": "2020-04-25T14:35:56+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:35:56+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000558,
            "beatmap_discussion_id": 1421667,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:24:681 (1,2,3) - if u wanna make this super fancy put 2 right in the middle between 3's head and tail aaaand in the middle between 1's head and 3's head https://i.imgur.com/dhKHbdr.png",
            "created_at": "2020-02-28T22:13:05+00:00",
            "updated_at": "2020-02-28T22:13:05+00:00",
            "deleted_at": null
          },
          {
            "id": 4340361,
            "beatmap_discussion_id": 1421667,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure ig xD",
            "created_at": "2020-04-25T14:35:56+00:00",
            "updated_at": "2020-04-25T14:35:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4340362,
            "beatmap_discussion_id": 1421667,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:35:56+00:00",
            "updated_at": "2020-04-25T14:35:56+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              13646997
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421670,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 77267,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:18:57+00:00",
        "updated_at": "2020-04-25T16:44:13+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T16:44:13+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000568,
            "beatmap_discussion_id": 1421670,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:17:267 (1) - the first slider bump is early by enough that i was able to notice it while playing",
            "created_at": "2020-02-28T22:18:57+00:00",
            "updated_at": "2020-02-28T22:18:57+00:00",
            "deleted_at": null
          },
          {
            "id": 4341095,
            "beatmap_discussion_id": 1421670,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "not really sure what you mean here",
            "created_at": "2020-04-25T16:26:38+00:00",
            "updated_at": "2020-04-25T16:26:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4341205,
            "beatmap_discussion_id": 1421670,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nah i just wanted a slider that looks slightly weird nothing to do with following the wubzy",
            "created_at": "2020-04-25T16:44:08+00:00",
            "updated_at": "2020-04-25T16:44:08+00:00",
            "deleted_at": null
          },
          {
            "id": 4341207,
            "beatmap_discussion_id": 1421670,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "spoke to LMT cos I knew what u meant but yea no change",
            "created_at": "2020-04-25T16:44:13+00:00",
            "updated_at": "2020-04-25T16:44:13+00:00",
            "deleted_at": null
          },
          {
            "id": 4341208,
            "beatmap_discussion_id": 1421670,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T16:44:13+00:00",
            "updated_at": "2020-04-25T16:44:13+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1421674,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 86061,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:20:12+00:00",
        "updated_at": "2020-04-25T16:44:18+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T16:44:18+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000572,
            "beatmap_discussion_id": 1421674,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:26:061 (2) - 01:26:578 (6) - would use normal whistles on those to give contrast to the following two sounds",
            "created_at": "2020-02-28T22:20:12+00:00",
            "updated_at": "2020-02-28T22:20:12+00:00",
            "deleted_at": null
          },
          {
            "id": 4000576,
            "beatmap_discussion_id": 1421674,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:37:095 (2) - 01:37:612 (1) - ^",
            "created_at": "2020-02-28T22:20:43+00:00",
            "updated_at": "2020-02-28T22:20:43+00:00",
            "deleted_at": null
          },
          {
            "id": 4341104,
            "beatmap_discussion_id": 1421674,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure",
            "created_at": "2020-04-25T16:27:56+00:00",
            "updated_at": "2020-04-25T16:27:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4341209,
            "beatmap_discussion_id": 1421674,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T16:44:18+00:00",
            "updated_at": "2020-04-25T16:44:18+00:00",
            "deleted_at": null
          },
          {
            "id": 4341210,
            "beatmap_discussion_id": 1421674,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T16:44:18+00:00",
            "updated_at": "2020-04-25T16:44:18+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7262798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421678,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 99336,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:22:13+00:00",
        "updated_at": "2020-04-25T16:44:21+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T16:44:21+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000581,
            "beatmap_discussion_id": 1421678,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:39:336 (1) - wouldn't make this part of the curve with the following notes cos 01:40:026 (2,3,4,5,6) - belong to their own group of 5. just move it so that it's separated and nc 01:40:026 (2) -",
            "created_at": "2020-02-28T22:22:13+00:00",
            "updated_at": "2020-02-28T22:22:13+00:00",
            "deleted_at": null
          },
          {
            "id": 4341109,
            "beatmap_discussion_id": 1421678,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "did something that would acheive that",
            "created_at": "2020-04-25T16:28:45+00:00",
            "updated_at": "2020-04-25T16:28:45+00:00",
            "deleted_at": null
          },
          {
            "id": 4341211,
            "beatmap_discussion_id": 1421678,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T16:44:21+00:00",
            "updated_at": "2020-04-25T16:44:21+00:00",
            "deleted_at": null
          },
          {
            "id": 4341212,
            "beatmap_discussion_id": 1421678,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T16:44:21+00:00",
            "updated_at": "2020-04-25T16:44:21+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7262798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421681,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 118647,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:24:33+00:00",
        "updated_at": "2020-04-25T16:44:23+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T16:44:23+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000586,
            "beatmap_discussion_id": 1421681,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:58:647 (1,2,1,2,1,2,1,2,1) - might be cool to decrease distance between these the further it goes to represent the fadeout https://i.imgur.com/uuBLopo.png (example also did some changes to the angles cos i thought it looked cool)",
            "created_at": "2020-02-28T22:24:33+00:00",
            "updated_at": "2020-02-28T22:24:33+00:00",
            "deleted_at": null
          },
          {
            "id": 4341119,
            "beatmap_discussion_id": 1421681,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ye",
            "created_at": "2020-04-25T16:29:26+00:00",
            "updated_at": "2020-04-25T16:29:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4341213,
            "beatmap_discussion_id": 1421681,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T16:44:23+00:00",
            "updated_at": "2020-04-25T16:44:23+00:00",
            "deleted_at": null
          },
          {
            "id": 4341214,
            "beatmap_discussion_id": 1421681,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T16:44:23+00:00",
            "updated_at": "2020-04-25T16:44:23+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7262798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421689,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323863,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 82267,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:32:27+00:00",
        "updated_at": "2020-04-25T14:55:18+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:55:18+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000605,
            "beatmap_discussion_id": 1421689,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:22:267 (1,2,3) - i kinda get where you are coming from but at this point the player expects these to be 1/4 so it feels pretty counter intuitive to play imo, would recommend to just do what u did for the others",
            "created_at": "2020-02-28T22:32:27+00:00",
            "updated_at": "2020-02-28T22:32:27+00:00",
            "deleted_at": null
          },
          {
            "id": 4087915,
            "beatmap_discussion_id": 1421689,
            "user_id": 7458583,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i did it because i wanted to make this pattern play different since it's new section but it won't work with 1/4 hihats part. aight, fixed to 1/4 kicksliders",
            "created_at": "2020-03-16T17:49:17+00:00",
            "updated_at": "2020-03-16T17:49:17+00:00",
            "deleted_at": null
          },
          {
            "id": 4340482,
            "beatmap_discussion_id": 1421689,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T14:55:18+00:00",
            "updated_at": "2020-04-25T14:55:18+00:00",
            "deleted_at": null
          },
          {
            "id": 4340483,
            "beatmap_discussion_id": 1421689,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:55:18+00:00",
            "updated_at": "2020-04-25T14:55:18+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7458583
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421692,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323863,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 43819,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:34:20+00:00",
        "updated_at": "2020-04-25T14:55:15+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:55:15+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000608,
            "beatmap_discussion_id": 1421692,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:43:819 (2,3,4) - i don't really see the sense in spacing 3 and 4 so far away from 2 as the drum sounds on 2's tail and 3 are basically the same. i'd rather use this as a nice introduction for spaced 1/4 and lower the spacing",
            "created_at": "2020-02-28T22:34:20+00:00",
            "updated_at": "2020-02-28T22:34:20+00:00",
            "deleted_at": null
          },
          {
            "id": 4087881,
            "beatmap_discussion_id": 1421692,
            "user_id": 7458583,
            "last_editor_id": 7458583,
            "deleted_by_id": null,
            "system": false,
            "message": "dunno, it plays very comfortable but stacked, ok",
            "created_at": "2020-03-16T17:39:57+00:00",
            "updated_at": "2020-03-16T17:42:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4340478,
            "beatmap_discussion_id": 1421692,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T14:55:14+00:00",
            "updated_at": "2020-04-25T14:55:14+00:00",
            "deleted_at": null
          },
          {
            "id": 4340479,
            "beatmap_discussion_id": 1421692,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:55:15+00:00",
            "updated_at": "2020-04-25T14:55:15+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7458583
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421695,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323863,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 87267,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:36:38+00:00",
        "updated_at": "2020-04-25T14:55:23+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:55:23+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000611,
            "beatmap_discussion_id": 1421695,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:27:267 (2,3,4,5) - would be cool if u stayed consistent here and mapped 01:27:267 (2) - as a repeat and a jump to 01:27:526 (4,5) -",
            "created_at": "2020-02-28T22:36:38+00:00",
            "updated_at": "2020-02-28T22:36:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4087920,
            "beatmap_discussion_id": 1421695,
            "user_id": 7458583,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok",
            "created_at": "2020-03-16T17:50:32+00:00",
            "updated_at": "2020-03-16T17:50:32+00:00",
            "deleted_at": null
          },
          {
            "id": 4340485,
            "beatmap_discussion_id": 1421695,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T14:55:23+00:00",
            "updated_at": "2020-04-25T14:55:23+00:00",
            "deleted_at": null
          },
          {
            "id": 4340486,
            "beatmap_discussion_id": 1421695,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:55:23+00:00",
            "updated_at": "2020-04-25T14:55:23+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7458583
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421696,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323863,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 65198,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:37:54+00:00",
        "updated_at": "2020-04-25T14:55:16+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:55:16+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000613,
            "beatmap_discussion_id": 1421696,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:05:198 (1,2,3) - this is a pretty large difficulty spike when playing imo as this is a setup that hasn't been introduced like this before, i'd suggest to lower the spacing to the double (also considering that the following two instances of this in the song are mapped easier)",
            "created_at": "2020-02-28T22:37:54+00:00",
            "updated_at": "2020-02-28T22:37:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4087893,
            "beatmap_discussion_id": 1421696,
            "user_id": 7458583,
            "last_editor_id": 7458583,
            "deleted_by_id": null,
            "system": false,
            "message": "aight\n01:16:492 (2,3) - here as well",
            "created_at": "2020-03-16T17:42:16+00:00",
            "updated_at": "2020-03-16T17:44:42+00:00",
            "deleted_at": null
          },
          {
            "id": 4340480,
            "beatmap_discussion_id": 1421696,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T14:55:16+00:00",
            "updated_at": "2020-04-25T14:55:16+00:00",
            "deleted_at": null
          },
          {
            "id": 4340481,
            "beatmap_discussion_id": 1421696,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:55:16+00:00",
            "updated_at": "2020-04-25T14:55:16+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7458583
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421701,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323864,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 31492,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:40:38+00:00",
        "updated_at": "2020-06-16T14:44:32+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:44:32+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000620,
            "beatmap_discussion_id": 1421701,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:31:492 (1) - silence",
            "created_at": "2020-02-28T22:40:38+00:00",
            "updated_at": "2020-02-28T22:40:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4648332,
            "beatmap_discussion_id": 1421701,
            "user_id": 5410645,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i guess=",
            "created_at": "2020-06-15T11:03:57+00:00",
            "updated_at": "2020-06-15T11:03:57+00:00",
            "deleted_at": null
          },
          {
            "id": 4654521,
            "beatmap_discussion_id": 1421701,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-16T14:44:32+00:00",
            "updated_at": "2020-06-16T14:44:32+00:00",
            "deleted_at": null
          },
          {
            "id": 4654522,
            "beatmap_discussion_id": 1421701,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:44:32+00:00",
            "updated_at": "2020-06-16T14:44:32+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5410645
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421707,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323864,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:42:49+00:00",
        "updated_at": "2020-06-16T14:44:42+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:44:42+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000627,
            "beatmap_discussion_id": 1421707,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:06:233 - this section does not work with copied hitsounding cos u didn't follow the layer that was hitsounded on the top diff which can clearely be heard on objects like 01:06:751 (3) - where the normal whistle on the top diff is on the white tick but here it should be on the head. just go through the section and hitsound it to the main instrument",
            "created_at": "2020-02-28T22:42:49+00:00",
            "updated_at": "2020-02-28T22:42:49+00:00",
            "deleted_at": null
          },
          {
            "id": 4648331,
            "beatmap_discussion_id": 1421707,
            "user_id": 5410645,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "did",
            "created_at": "2020-06-15T11:03:19+00:00",
            "updated_at": "2020-06-15T11:03:19+00:00",
            "deleted_at": null
          },
          {
            "id": 4654527,
            "beatmap_discussion_id": 1421707,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-16T14:44:42+00:00",
            "updated_at": "2020-06-16T14:44:42+00:00",
            "deleted_at": null
          },
          {
            "id": 4654528,
            "beatmap_discussion_id": 1421707,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:44:42+00:00",
            "updated_at": "2020-06-16T14:44:42+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5410645
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421708,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323864,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 104854,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:44:35+00:00",
        "updated_at": "2020-06-16T14:44:38+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:44:38+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000629,
            "beatmap_discussion_id": 1421708,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:44:854 (2) - nc cos new group and slow ass follow points",
            "created_at": "2020-02-28T22:44:35+00:00",
            "updated_at": "2020-02-28T22:44:35+00:00",
            "deleted_at": null
          },
          {
            "id": 4648342,
            "beatmap_discussion_id": 1421708,
            "user_id": 5410645,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "o",
            "created_at": "2020-06-15T11:05:24+00:00",
            "updated_at": "2020-06-15T11:05:24+00:00",
            "deleted_at": null
          },
          {
            "id": 4654525,
            "beatmap_discussion_id": 1421708,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-16T14:44:38+00:00",
            "updated_at": "2020-06-16T14:44:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4654526,
            "beatmap_discussion_id": 1421708,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:44:38+00:00",
            "updated_at": "2020-06-16T14:44:38+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5410645
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421710,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323864,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "praise",
        "parent_id": null,
        "timestamp": 100026,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-02-28T22:44:51+00:00",
        "updated_at": "2020-02-28T22:44:51+00:00",
        "deleted_at": null,
        "last_post_at": "2020-02-28T22:44:51+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000631,
            "beatmap_discussion_id": 1421710,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:40:026 (1) - bruh",
            "created_at": "2020-02-28T22:44:51+00:00",
            "updated_at": "2020-02-28T22:44:51+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1421711,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:46:24+00:00",
        "updated_at": "2020-06-16T14:35:30+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:35:30+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000636,
            "beatmap_discussion_id": 1421711,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "might be nice to vary hp drain on the 5 highest diffs a little, currently they all have 5",
            "created_at": "2020-02-28T22:46:24+00:00",
            "updated_at": "2020-02-28T22:46:24+00:00",
            "deleted_at": null
          },
          {
            "id": 4340525,
            "beatmap_discussion_id": 1421711,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "I've made mine 6, will let the other's decide",
            "created_at": "2020-04-25T15:01:58+00:00",
            "updated_at": "2020-04-25T15:01:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4341122,
            "beatmap_discussion_id": 1421711,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "did 5.5",
            "created_at": "2020-04-25T16:29:47+00:00",
            "updated_at": "2020-04-25T16:29:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4445553,
            "beatmap_discussion_id": 1421711,
            "user_id": 7458583,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Altai please change mine on 5.2 thanks",
            "created_at": "2020-05-12T12:54:23+00:00",
            "updated_at": "2020-05-12T12:54:23+00:00",
            "deleted_at": null
          },
          {
            "id": 4654427,
            "beatmap_discussion_id": 1421711,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yeet",
            "created_at": "2020-06-16T14:35:30+00:00",
            "updated_at": "2020-06-16T14:35:30+00:00",
            "deleted_at": null
          },
          {
            "id": 4654428,
            "beatmap_discussion_id": 1421711,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:35:30+00:00",
            "updated_at": "2020-06-16T14:35:30+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421718,
        "beatmapset_id": 1112303,
        "beatmap_id": 2413552,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 111061,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:52:59+00:00",
        "updated_at": "2020-04-25T15:12:32+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T15:12:32+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000643,
            "beatmap_discussion_id": 1421718,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:51:061 (1) - as much as i'm an edgy boi, i'd make this a little clearer. overlapping the tail with the body like this is pretty hard to read if you don't have slider end circles + the overlap with its own tail makes it even harder and shapes like this haven't been introduced in the map anywhere else before",
            "created_at": "2020-02-28T22:52:59+00:00",
            "updated_at": "2020-02-28T22:52:59+00:00",
            "deleted_at": null
          },
          {
            "id": 4340554,
            "beatmap_discussion_id": 1421718,
            "user_id": 7228554,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "pulled it out a little, hopefully shud be clearer now",
            "created_at": "2020-04-25T15:08:23+00:00",
            "updated_at": "2020-04-25T15:08:23+00:00",
            "deleted_at": null
          },
          {
            "id": 4340600,
            "beatmap_discussion_id": 1421718,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "pog",
            "created_at": "2020-04-25T15:12:32+00:00",
            "updated_at": "2020-04-25T15:12:32+00:00",
            "deleted_at": null
          },
          {
            "id": 4340601,
            "beatmap_discussion_id": 1421718,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T15:12:32+00:00",
            "updated_at": "2020-04-25T15:12:32+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7228554
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421724,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331906,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 75888,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T22:59:54+00:00",
        "updated_at": "2020-04-25T15:03:38+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:57:07+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000650,
            "beatmap_discussion_id": 1421724,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:15:888 (1,2,3,4,5,1,2,3) - not sure what to think about this cos it's definitely one of the hardest patterns of the map (harder than the buildup and rest of the chorus). could nerf it a little by making 01:16:061 (2) - a 1/2 slider to follow the synth",
            "created_at": "2020-02-28T22:59:54+00:00",
            "updated_at": "2020-02-28T22:59:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4340502,
            "beatmap_discussion_id": 1421724,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "agree",
            "created_at": "2020-04-25T14:57:07+00:00",
            "updated_at": "2020-04-25T14:57:07+00:00",
            "deleted_at": null
          },
          {
            "id": 4340503,
            "beatmap_discussion_id": 1421724,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:57:07+00:00",
            "updated_at": "2020-04-25T14:57:07+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1421728,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331906,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 38819,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-02-28T23:03:24+00:00",
        "updated_at": "2020-04-25T14:55:30+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-25T14:55:30+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4000657,
            "beatmap_discussion_id": 1421728,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:38:819 (1,2,3,4,1,2,3,4) - this feels a little dense and lacking in rhythmical contrast to the build up later on imo. you could replace 00:39:681 (4) - with a circle to break the chain up a little",
            "created_at": "2020-02-28T23:03:24+00:00",
            "updated_at": "2020-02-28T23:03:24+00:00",
            "deleted_at": null
          },
          {
            "id": 4000867,
            "beatmap_discussion_id": 1421728,
            "user_id": 13646997,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fixed the parts",
            "created_at": "2020-02-29T00:13:06+00:00",
            "updated_at": "2020-02-29T00:13:06+00:00",
            "deleted_at": null
          },
          {
            "id": 4340489,
            "beatmap_discussion_id": 1421728,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-04-25T14:55:30+00:00",
            "updated_at": "2020-04-25T14:55:30+00:00",
            "deleted_at": null
          },
          {
            "id": 4340490,
            "beatmap_discussion_id": 1421728,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-25T14:55:30+00:00",
            "updated_at": "2020-04-25T14:55:30+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              13646997
            ],
            "down": []
          }
        }
      },
      {
        "id": 1422416,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 11174970,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-02-29T09:50:38+00:00",
        "updated_at": "2020-05-18T18:01:03+00:00",
        "deleted_at": null,
        "last_post_at": "2020-02-29T09:50:38+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4002727,
            "beatmap_discussion_id": 1422416,
            "user_id": 11174970,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "хавкинз трахнул и улетел в оффлайн",
            "created_at": "2020-02-29T09:50:38+00:00",
            "updated_at": "2020-02-29T09:50:38+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6115007
            ],
            "down": []
          }
        }
      },
      {
        "id": 1427451,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 13646997,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-03-03T03:07:03+00:00",
        "updated_at": "2020-03-03T03:07:03+00:00",
        "deleted_at": null,
        "last_post_at": "2020-03-03T03:07:03+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4016272,
            "beatmap_discussion_id": 1427451,
            "user_id": 13646997,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "meep",
            "created_at": "2020-03-03T03:07:03+00:00",
            "updated_at": "2020-03-03T03:07:03+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1564263,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 66923,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-06T06:57:52+00:00",
        "updated_at": "2020-06-16T14:44:03+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:41:31+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4406759,
            "beatmap_discussion_id": 1564263,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:06:923 (3) - Shouldn't this be 1/2 shorter",
            "created_at": "2020-05-06T06:57:52+00:00",
            "updated_at": "2020-05-06T06:57:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4654478,
            "beatmap_discussion_id": 1564263,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "was meant to follow the backing sounds like top diff but yea clap is stronger so will shorten this",
            "created_at": "2020-06-16T14:41:31+00:00",
            "updated_at": "2020-06-16T14:41:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4654479,
            "beatmap_discussion_id": 1564263,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:41:31+00:00",
            "updated_at": "2020-06-16T14:41:31+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1564264,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 41405,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-06T06:59:46+00:00",
        "updated_at": "2020-06-16T14:44:02+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:43:04+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4406762,
            "beatmap_discussion_id": 1564264,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:41:405 (1) - This shape might be unclear to beginners I recommend changing it",
            "created_at": "2020-05-06T06:59:46+00:00",
            "updated_at": "2020-05-06T06:59:46+00:00",
            "deleted_at": null
          },
          {
            "id": 4406765,
            "beatmap_discussion_id": 1564264,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:58:647 (1) - also you could use spinner here or long slider without reverses here just like top difficulty don't see why you would use sliders with so many reverses here",
            "created_at": "2020-05-06T07:00:36+00:00",
            "updated_at": "2020-05-06T07:00:36+00:00",
            "deleted_at": null
          },
          {
            "id": 4654502,
            "beatmap_discussion_id": 1564264,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "As for the first one I agree, that has been changed.\nFor the second, I like the echoing effect and it's not really unrankable since the reverses are further than 1/1",
            "created_at": "2020-06-16T14:43:04+00:00",
            "updated_at": "2020-06-16T14:43:04+00:00",
            "deleted_at": null
          },
          {
            "id": 4654503,
            "beatmap_discussion_id": 1564264,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:43:04+00:00",
            "updated_at": "2020-06-16T14:43:04+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1564266,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-06T07:01:21+00:00",
        "updated_at": "2020-06-16T14:43:59+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:40:33+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4406767,
            "beatmap_discussion_id": 1564266,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "HP at least 3 please 2 is more for easy",
            "created_at": "2020-05-06T07:01:21+00:00",
            "updated_at": "2020-05-06T07:01:21+00:00",
            "deleted_at": null
          },
          {
            "id": 4654465,
            "beatmap_discussion_id": 1564266,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure thing chicken wing",
            "created_at": "2020-06-16T14:40:33+00:00",
            "updated_at": "2020-06-16T14:40:33+00:00",
            "deleted_at": null
          },
          {
            "id": 4654466,
            "beatmap_discussion_id": 1564266,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:40:33+00:00",
            "updated_at": "2020-06-16T14:40:33+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1564275,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-06T07:12:17+00:00",
        "updated_at": "2020-06-16T14:44:08+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:39:51+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4406838,
            "beatmap_discussion_id": 1564275,
            "user_id": 8623835,
            "last_editor_id": 8623835,
            "deleted_by_id": null,
            "system": false,
            "message": "Hitsounds volumes are really low to me on most parts like for example 00:32:612 - those claps are inaudible I recommend increasing overall volume",
            "created_at": "2020-05-06T07:12:17+00:00",
            "updated_at": "2020-05-06T07:12:36+00:00",
            "deleted_at": null
          },
          {
            "id": 4654460,
            "beatmap_discussion_id": 1564275,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "buffed a little but don't want it too loud cos it kicks in later",
            "created_at": "2020-06-16T14:39:51+00:00",
            "updated_at": "2020-06-16T14:39:51+00:00",
            "deleted_at": null
          },
          {
            "id": 4654461,
            "beatmap_discussion_id": 1564275,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:39:51+00:00",
            "updated_at": "2020-06-16T14:39:51+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1564293,
        "beatmapset_id": 1112303,
        "beatmap_id": 2413552,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 19336,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-06T07:23:36+00:00",
        "updated_at": "2020-06-16T19:54:54+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T19:54:54+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4406883,
            "beatmap_discussion_id": 1564293,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:19:336 (3) - Could make it longer by 1/2 for vocals",
            "created_at": "2020-05-06T07:23:36+00:00",
            "updated_at": "2020-05-06T07:23:36+00:00",
            "deleted_at": null
          },
          {
            "id": 4654632,
            "beatmap_discussion_id": 1564293,
            "user_id": 7228554,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure",
            "created_at": "2020-06-16T15:13:05+00:00",
            "updated_at": "2020-06-16T15:13:05+00:00",
            "deleted_at": null
          },
          {
            "id": 4656002,
            "beatmap_discussion_id": 1564293,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yeet",
            "created_at": "2020-06-16T19:54:54+00:00",
            "updated_at": "2020-06-16T19:54:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4656003,
            "beatmap_discussion_id": 1564293,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T19:54:54+00:00",
            "updated_at": "2020-06-16T19:54:54+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7228554
            ],
            "down": []
          }
        }
      },
      {
        "id": 1564303,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-06T07:27:50+00:00",
        "updated_at": "2020-06-16T14:44:09+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:36:31+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4406923,
            "beatmap_discussion_id": 1564303,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:06:923 - shouldn't this normal whistle be on 01:06:750 ? it's noticeable on some diffs that's it's missing",
            "created_at": "2020-05-06T07:27:50+00:00",
            "updated_at": "2020-05-06T07:27:50+00:00",
            "deleted_at": null
          },
          {
            "id": 4654432,
            "beatmap_discussion_id": 1564303,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "it's following the backing part that comes in for that section, was done for top diff, if it's a problem in other diffs lmk but for now I think it's fine",
            "created_at": "2020-06-16T14:36:31+00:00",
            "updated_at": "2020-06-16T14:36:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4654433,
            "beatmap_discussion_id": 1564303,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:36:31+00:00",
            "updated_at": "2020-06-16T14:36:31+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1564314,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323864,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 76060,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-06T07:35:39+00:00",
        "updated_at": "2020-06-16T14:44:35+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:44:34+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4406963,
            "beatmap_discussion_id": 1564314,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:16:060 (2) - Offscreen on 4:3 ratio",
            "created_at": "2020-05-06T07:35:39+00:00",
            "updated_at": "2020-05-06T07:35:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4648340,
            "beatmap_discussion_id": 1564314,
            "user_id": 5410645,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "not anymore i hope",
            "created_at": "2020-06-15T11:05:11+00:00",
            "updated_at": "2020-06-15T11:05:11+00:00",
            "deleted_at": null
          },
          {
            "id": 4654523,
            "beatmap_discussion_id": 1564314,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-16T14:44:34+00:00",
            "updated_at": "2020-06-16T14:44:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4654524,
            "beatmap_discussion_id": 1564314,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:44:35+00:00",
            "updated_at": "2020-06-16T14:44:35+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5410645
            ],
            "down": []
          }
        }
      },
      {
        "id": 1564650,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-06T12:03:49+00:00",
        "updated_at": "2020-05-19T10:15:49+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-19T10:15:48+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4407947,
            "beatmap_discussion_id": 1564650,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Ah ya do +15 or +20 to timing since audio compatibility off now",
            "created_at": "2020-05-06T12:03:49+00:00",
            "updated_at": "2020-05-06T12:03:49+00:00",
            "deleted_at": null
          },
          {
            "id": 4493501,
            "beatmap_discussion_id": 1564650,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "https://www.youtube.com/watch?v=-1qju6V1jLM (doesn't need fixing anymore cos revert yay)",
            "created_at": "2020-05-19T10:15:48+00:00",
            "updated_at": "2020-05-19T10:15:48+00:00",
            "deleted_at": null
          },
          {
            "id": 4493502,
            "beatmap_discussion_id": 1564650,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-19T10:15:48+00:00",
            "updated_at": "2020-05-19T10:15:48+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1594049,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 12123512,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-18T19:14:08+00:00",
        "updated_at": "2020-05-18T19:14:08+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-18T19:14:08+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4489895,
            "beatmap_discussion_id": 1594049,
            "user_id": 12123512,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "poooooog",
            "created_at": "2020-05-18T19:14:08+00:00",
            "updated_at": "2020-05-18T19:14:08+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1594251,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 10526814,
        "deleted_by_id": null,
        "message_type": "praise",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-18T21:20:04+00:00",
        "updated_at": "2020-05-18T21:20:04+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-18T21:20:04+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4490448,
            "beatmap_discussion_id": 1594251,
            "user_id": 10526814,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "mwah",
            "created_at": "2020-05-18T21:20:04+00:00",
            "updated_at": "2020-05-18T21:20:04+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1596429,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 2384296,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 63388,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-19T21:55:05+00:00",
        "updated_at": "2020-06-16T14:52:28+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-16T14:52:28+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4497147,
            "beatmap_discussion_id": 1596429,
            "user_id": 2384296,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:03:388 (1) - Oops I've found the overmapping.",
            "created_at": "2020-05-19T21:55:05+00:00",
            "updated_at": "2020-05-19T21:55:05+00:00",
            "deleted_at": null
          },
          {
            "id": 4497164,
            "beatmap_discussion_id": 1596429,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "monkas",
            "created_at": "2020-05-19T21:57:35+00:00",
            "updated_at": "2020-05-19T21:57:35+00:00",
            "deleted_at": null
          },
          {
            "id": 4654575,
            "beatmap_discussion_id": 1596429,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "thats fine actualy",
            "created_at": "2020-06-16T14:51:50+00:00",
            "updated_at": "2020-06-16T14:51:50+00:00",
            "deleted_at": null
          },
          {
            "id": 4654580,
            "beatmap_discussion_id": 1596429,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "YEET",
            "created_at": "2020-06-16T14:52:28+00:00",
            "updated_at": "2020-06-16T14:52:28+00:00",
            "deleted_at": null
          },
          {
            "id": 4654581,
            "beatmap_discussion_id": 1596429,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-16T14:52:28+00:00",
            "updated_at": "2020-06-16T14:52:28+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1598749,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 8346108,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-20T19:29:12+00:00",
        "updated_at": "2020-05-20T19:29:12+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-20T19:29:12+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4503348,
            "beatmap_discussion_id": 1598749,
            "user_id": 8346108,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Лисиный хайп",
            "created_at": "2020-05-20T19:29:12+00:00",
            "updated_at": "2020-05-20T19:29:12+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1677762,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 53817,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-26T10:32:24+00:00",
        "updated_at": "2020-06-27T13:26:56+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-27T13:26:55+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4713355,
            "beatmap_discussion_id": 1677762,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:53:817 - 00:53:645 - Circles unsnapped",
            "created_at": "2020-06-26T10:32:24+00:00",
            "updated_at": "2020-06-26T10:32:24+00:00",
            "deleted_at": null
          },
          {
            "id": 4720414,
            "beatmap_discussion_id": 1677762,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "mr ksardas how dare u",
            "created_at": "2020-06-27T13:26:55+00:00",
            "updated_at": "2020-06-27T13:26:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4720415,
            "beatmap_discussion_id": 1677762,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-27T13:26:55+00:00",
            "updated_at": "2020-06-27T13:26:55+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1680027,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-27T10:45:50+00:00",
        "updated_at": "2020-06-27T13:26:28+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-27T13:26:26+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4719762,
            "beatmap_discussion_id": 1680027,
            "user_id": 8623835,
            "last_editor_id": 8623835,
            "deleted_by_id": null,
            "system": false,
            "message": "01:07:958 - 01:08:474 - 01:13:992 - normal whistle shouldn't be here but on 01:07:785 - 01:08:302 - 01:13:820",
            "created_at": "2020-06-27T10:45:50+00:00",
            "updated_at": "2020-06-27T10:50:40+00:00",
            "deleted_at": null
          },
          {
            "id": 4719764,
            "beatmap_discussion_id": 1680027,
            "user_id": 8623835,
            "last_editor_id": null,
            "deleted_by_id": 8623835,
            "system": false,
            "message": "also one is missing on 01:08:302 - looking at some diffs",
            "created_at": "2020-06-27T10:46:31+00:00",
            "updated_at": "2020-06-27T10:50:03+00:00",
            "deleted_at": "2020-06-27T10:50:03+00:00"
          },
          {
            "id": 4720361,
            "beatmap_discussion_id": 1680027,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "the problem is that here a new melody was introduced in the song for a moment so I decided to follow that, tho the later half is inconsistent so I'll see what I can do",
            "created_at": "2020-06-27T13:10:50+00:00",
            "updated_at": "2020-06-27T13:10:50+00:00",
            "deleted_at": null
          },
          {
            "id": 4720369,
            "beatmap_discussion_id": 1680027,
            "user_id": 5745865,
            "last_editor_id": 5745865,
            "deleted_by_id": null,
            "system": false,
            "message": "no I think ur right, I think it's best just to be consistent with the same as before since it's continuing, will change this\n\nI am not removing the hitwhistle on 01:07:957 since it sounds wrong to me\n\nAlso adding normal hitwhistles on:\n01:14:164\n01:08:647\n\nThis is with exception of Icekalt's diff since he already did his own whistling on this part",
            "created_at": "2020-06-27T13:12:39+00:00",
            "updated_at": "2020-06-27T13:23:44+00:00",
            "deleted_at": null
          },
          {
            "id": 4720410,
            "beatmap_discussion_id": 1680027,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "done",
            "created_at": "2020-06-27T13:26:26+00:00",
            "updated_at": "2020-06-27T13:26:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4720411,
            "beatmap_discussion_id": 1680027,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-27T13:26:26+00:00",
            "updated_at": "2020-06-27T13:26:26+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1680039,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 8623835,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 65543,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-27T10:53:54+00:00",
        "updated_at": "2020-06-27T13:27:39+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-27T13:27:37+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4719788,
            "beatmap_discussion_id": 1680039,
            "user_id": 8623835,
            "last_editor_id": 8623835,
            "deleted_by_id": null,
            "system": false,
            "message": "01:05:543 - 01:06:750 - normal addition and whistle if its missing",
            "created_at": "2020-06-27T10:53:54+00:00",
            "updated_at": "2020-06-27T10:55:45+00:00",
            "deleted_at": null
          },
          {
            "id": 4720417,
            "beatmap_discussion_id": 1680039,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure",
            "created_at": "2020-06-27T13:27:37+00:00",
            "updated_at": "2020-06-27T13:27:37+00:00",
            "deleted_at": null
          },
          {
            "id": 4720418,
            "beatmap_discussion_id": 1680039,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-27T13:27:37+00:00",
            "updated_at": "2020-06-27T13:27:37+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684574,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 58992,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T13:25:57+00:00",
        "updated_at": "2020-06-29T16:19:29+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:19:28+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731536,
            "beatmap_discussion_id": 1684574,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:58:992 (3,4,5) - might wanna make this a little clearer so newbs don't go for the tail instead https://i.imgur.com/032OdZe.png",
            "created_at": "2020-06-29T13:25:57+00:00",
            "updated_at": "2020-06-29T13:25:57+00:00",
            "deleted_at": null
          },
          {
            "id": 4732660,
            "beatmap_discussion_id": 1684574,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea",
            "created_at": "2020-06-29T16:19:28+00:00",
            "updated_at": "2020-06-29T16:19:28+00:00",
            "deleted_at": null
          },
          {
            "id": 4732661,
            "beatmap_discussion_id": 1684574,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:19:28+00:00",
            "updated_at": "2020-06-29T16:19:28+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684580,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331906,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 41405,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T13:32:38+00:00",
        "updated_at": "2020-06-29T16:16:57+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:16:57+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731569,
            "beatmap_discussion_id": 1684580,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:41:405 (5,6) - this spacing seems a little random to me cos u never do 1/2 like this so you might wanna make it a little clearer",
            "created_at": "2020-06-29T13:32:38+00:00",
            "updated_at": "2020-06-29T13:32:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4732644,
            "beatmap_discussion_id": 1684580,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yes",
            "created_at": "2020-06-29T16:16:42+00:00",
            "updated_at": "2020-06-29T16:16:42+00:00",
            "deleted_at": null
          },
          {
            "id": 4732645,
            "beatmap_discussion_id": 1684580,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:16:42+00:00",
            "updated_at": "2020-06-29T16:16:42+00:00",
            "deleted_at": null
          },
          {
            "id": 4732648,
            "beatmap_discussion_id": 1684580,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "as in I didn't make it clearer I just removed it",
            "created_at": "2020-06-29T16:16:57+00:00",
            "updated_at": "2020-06-29T16:16:57+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684591,
        "beatmapset_id": 1112303,
        "beatmap_id": 2413552,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 111061,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T13:40:58+00:00",
        "updated_at": "2020-06-30T14:48:56+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-30T14:48:56+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731588,
            "beatmap_discussion_id": 1684591,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:51:061 (1) - just a suggestion but it might be cool to have the direction change with the first red anchor on 01:51:578 - to emphasise the synth. https://osu.ppy.sh/ss/15146758/bb03",
            "created_at": "2020-06-29T13:40:58+00:00",
            "updated_at": "2020-06-29T13:40:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4736566,
            "beatmap_discussion_id": 1684591,
            "user_id": 7228554,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sounds cool",
            "created_at": "2020-06-30T06:51:40+00:00",
            "updated_at": "2020-06-30T06:51:40+00:00",
            "deleted_at": null
          },
          {
            "id": 4738504,
            "beatmap_discussion_id": 1684591,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-30T14:48:56+00:00",
            "updated_at": "2020-06-30T14:48:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4738505,
            "beatmap_discussion_id": 1684591,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-30T14:48:56+00:00",
            "updated_at": "2020-06-30T14:48:56+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7228554
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684609,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323864,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 107612,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T13:52:09+00:00",
        "updated_at": "2020-06-29T22:00:19+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T22:00:19+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731634,
            "beatmap_discussion_id": 1684609,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:47:612 (1,2,1,2,1,2,1,2,1,2) - these should definitely have some hitsounding cos rn they are unhitsounded cos top diff doesn't have anything here (maybe also do some volume change stuff with them)",
            "created_at": "2020-06-29T13:52:09+00:00",
            "updated_at": "2020-06-29T13:52:09+00:00",
            "deleted_at": null
          },
          {
            "id": 4731637,
            "beatmap_discussion_id": 1684609,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i'd also add some volume changes to 01:58:647 (1) -",
            "created_at": "2020-06-29T13:53:25+00:00",
            "updated_at": "2020-06-29T13:53:25+00:00",
            "deleted_at": null
          },
          {
            "id": 4732695,
            "beatmap_discussion_id": 1684609,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure",
            "created_at": "2020-06-29T16:23:47+00:00",
            "updated_at": "2020-06-29T16:23:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4732696,
            "beatmap_discussion_id": 1684609,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:23:47+00:00",
            "updated_at": "2020-06-29T16:23:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4732697,
            "beatmap_discussion_id": 1684609,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fixed for icey",
            "created_at": "2020-06-29T16:23:54+00:00",
            "updated_at": "2020-06-29T16:23:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4734674,
            "beatmap_discussion_id": 1684609,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "actually implemented this elsewhere on diffs that mapped the fading vocals cos it is cute",
            "created_at": "2020-06-29T22:00:19+00:00",
            "updated_at": "2020-06-29T22:00:19+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684614,
        "beatmapset_id": 1112303,
        "beatmap_id": 2413552,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 118647,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T13:54:03+00:00",
        "updated_at": "2020-06-30T14:49:01+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-30T14:48:59+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731641,
            "beatmap_discussion_id": 1684614,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:58:647 (1) - maybe decrease the volume for the repeats steadily",
            "created_at": "2020-06-29T13:54:03+00:00",
            "updated_at": "2020-06-29T13:54:03+00:00",
            "deleted_at": null
          },
          {
            "id": 4738506,
            "beatmap_discussion_id": 1684614,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yes",
            "created_at": "2020-06-30T14:48:59+00:00",
            "updated_at": "2020-06-30T14:48:59+00:00",
            "deleted_at": null
          },
          {
            "id": 4738507,
            "beatmap_discussion_id": 1684614,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-30T14:48:59+00:00",
            "updated_at": "2020-06-30T14:48:59+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684638,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323863,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 102440,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:00:15+00:00",
        "updated_at": "2020-06-29T16:22:04+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:22:03+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731694,
            "beatmap_discussion_id": 1684638,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:42:440 (1,2,1,2,1,2,1) - add some whistles here and there cos these currently have no hitsounding",
            "created_at": "2020-06-29T14:00:15+00:00",
            "updated_at": "2020-06-29T14:00:15+00:00",
            "deleted_at": null
          },
          {
            "id": 4732686,
            "beatmap_discussion_id": 1684638,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "done for frakture",
            "created_at": "2020-06-29T16:22:03+00:00",
            "updated_at": "2020-06-29T16:22:03+00:00",
            "deleted_at": null
          },
          {
            "id": 4732687,
            "beatmap_discussion_id": 1684638,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:22:03+00:00",
            "updated_at": "2020-06-29T16:22:03+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684650,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 2204515,
        "deleted_by_id": 2204515,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 16492,
        "resolved": false,
        "can_be_resolved": true,
        "can_grant_kudosu": false,
        "created_at": "2020-06-29T14:03:39+00:00",
        "updated_at": "2020-06-29T14:08:08+00:00",
        "deleted_at": "2020-06-29T14:08:08+00:00",
        "last_post_at": "2020-06-29T14:04:40+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731716,
            "beatmap_discussion_id": 1684650,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:16:492 (5) - unhitsounded triple makes me big sad",
            "created_at": "2020-06-29T14:03:39+00:00",
            "updated_at": "2020-06-29T14:03:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4731717,
            "beatmap_discussion_id": 1684650,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:22:009 (5) -",
            "created_at": "2020-06-29T14:03:58+00:00",
            "updated_at": "2020-06-29T14:03:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4731719,
            "beatmap_discussion_id": 1684650,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "all of them in this section are",
            "created_at": "2020-06-29T14:04:10+00:00",
            "updated_at": "2020-06-29T14:04:10+00:00",
            "deleted_at": null
          },
          {
            "id": 4731724,
            "beatmap_discussion_id": 1684650,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "and even beyond that section so u might wanna check them all",
            "created_at": "2020-06-29T14:04:40+00:00",
            "updated_at": "2020-06-29T14:04:40+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      },
      {
        "id": 1684659,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 52440,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:05:42+00:00",
        "updated_at": "2020-06-29T21:52:47+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T21:52:47+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731735,
            "beatmap_discussion_id": 1684659,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:52:440 (1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,7) - full whistle spam sounds a bit eeeh, if you wanna keep them at least do like a volume build-up to represent the song better",
            "created_at": "2020-06-29T14:05:42+00:00",
            "updated_at": "2020-06-29T14:05:42+00:00",
            "deleted_at": null
          },
          {
            "id": 4734177,
            "beatmap_discussion_id": 1684659,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i really do not like changing volumes on streams... did some magic on the kick hitsounds so they don't feel... as boring?",
            "created_at": "2020-06-29T20:07:23+00:00",
            "updated_at": "2020-06-29T20:07:23+00:00",
            "deleted_at": null
          },
          {
            "id": 4734616,
            "beatmap_discussion_id": 1684659,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T21:52:47+00:00",
            "updated_at": "2020-06-29T21:52:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4734617,
            "beatmap_discussion_id": 1684659,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T21:52:47+00:00",
            "updated_at": "2020-06-29T21:52:47+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7262798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684665,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 68877,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:07:26+00:00",
        "updated_at": "2020-06-29T21:52:52+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T21:52:52+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731750,
            "beatmap_discussion_id": 1684665,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:08:877 (4,5) - hitsound the 1/6 please",
            "created_at": "2020-06-29T14:07:26+00:00",
            "updated_at": "2020-06-29T14:07:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4734180,
            "beatmap_discussion_id": 1684665,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea",
            "created_at": "2020-06-29T20:07:47+00:00",
            "updated_at": "2020-06-29T20:07:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4734618,
            "beatmap_discussion_id": 1684665,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T21:52:52+00:00",
            "updated_at": "2020-06-29T21:52:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4734619,
            "beatmap_discussion_id": 1684665,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T21:52:52+00:00",
            "updated_at": "2020-06-29T21:52:52+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7262798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684670,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331905,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:08:48+00:00",
        "updated_at": "2020-06-29T21:53:00+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T21:53:00+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731757,
            "beatmap_discussion_id": 1684670,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "unhitsounded triples make me big sad, there are so so many that just skip the middle note or even all of them that listing them isn't sensible. just go through the map and fix those rascals",
            "created_at": "2020-06-29T14:08:48+00:00",
            "updated_at": "2020-06-29T14:08:48+00:00",
            "deleted_at": null
          },
          {
            "id": 4734220,
            "beatmap_discussion_id": 1684670,
            "user_id": 7262798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i did them",
            "created_at": "2020-06-29T20:14:53+00:00",
            "updated_at": "2020-06-29T20:14:53+00:00",
            "deleted_at": null
          },
          {
            "id": 4734620,
            "beatmap_discussion_id": 1684670,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T21:53:00+00:00",
            "updated_at": "2020-06-29T21:53:00+00:00",
            "deleted_at": null
          },
          {
            "id": 4734621,
            "beatmap_discussion_id": 1684670,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T21:53:00+00:00",
            "updated_at": "2020-06-29T21:53:00+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7262798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684676,
        "beatmapset_id": 1112303,
        "beatmap_id": 2331906,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:10:06+00:00",
        "updated_at": "2020-06-29T16:17:35+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:17:34+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731768,
            "beatmap_discussion_id": 1684676,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "you definitely don't want OD8 on this, go for OD7",
            "created_at": "2020-06-29T14:10:06+00:00",
            "updated_at": "2020-06-29T14:10:06+00:00",
            "deleted_at": null
          },
          {
            "id": 4732651,
            "beatmap_discussion_id": 1684676,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "any truers in chat",
            "created_at": "2020-06-29T16:17:34+00:00",
            "updated_at": "2020-06-29T16:17:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4732652,
            "beatmap_discussion_id": 1684676,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:17:34+00:00",
            "updated_at": "2020-06-29T16:17:34+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684687,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:17:55+00:00",
        "updated_at": "2020-06-29T16:13:17+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:13:17+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731803,
            "beatmap_discussion_id": 1684687,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i know it's a guest diff but i feel like the rest of the set is very cohesive and the combo colours are kinda... too bright imo so i'd like to ask you to change them to match the rest of the set",
            "created_at": "2020-06-29T14:17:55+00:00",
            "updated_at": "2020-06-29T14:17:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4732307,
            "beatmap_discussion_id": 1684687,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "okk",
            "created_at": "2020-06-29T15:37:47+00:00",
            "updated_at": "2020-06-29T15:37:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4732612,
            "beatmap_discussion_id": 1684687,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T16:13:17+00:00",
            "updated_at": "2020-06-29T16:13:17+00:00",
            "deleted_at": null
          },
          {
            "id": 4732613,
            "beatmap_discussion_id": 1684687,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:13:17+00:00",
            "updated_at": "2020-06-29T16:13:17+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6115007
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684690,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 26405,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:19:41+00:00",
        "updated_at": "2020-06-29T16:12:34+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:12:34+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731809,
            "beatmap_discussion_id": 1684690,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:26:405 (1,1) - either put a soft whistle onto the second slider or silence the first one's tail (and possibly also the tick)",
            "created_at": "2020-06-29T14:19:41+00:00",
            "updated_at": "2020-06-29T14:19:41+00:00",
            "deleted_at": null
          },
          {
            "id": 4732356,
            "beatmap_discussion_id": 1684690,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "silence",
            "created_at": "2020-06-29T15:44:17+00:00",
            "updated_at": "2020-06-29T15:44:17+00:00",
            "deleted_at": null
          },
          {
            "id": 4732601,
            "beatmap_discussion_id": 1684690,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T16:12:34+00:00",
            "updated_at": "2020-06-29T16:12:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4732602,
            "beatmap_discussion_id": 1684690,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:12:34+00:00",
            "updated_at": "2020-06-29T16:12:34+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6115007
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684695,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 57871,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:22:26+00:00",
        "updated_at": "2020-06-29T18:17:24+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T18:17:24+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731822,
            "beatmap_discussion_id": 1684695,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:57:871 (1) - 01:03:388 (1) - 01:08:905 (1) - 01:14:423 (1) - (and others if i missed any) are 1/6 so mapping a 1/8 slider over them doesn't really make sense",
            "created_at": "2020-06-29T14:22:26+00:00",
            "updated_at": "2020-06-29T14:22:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4732386,
            "beatmap_discussion_id": 1684695,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "are replacing that 1/8 sliders with 1/4 circles would be okk idk just askin",
            "created_at": "2020-06-29T15:49:58+00:00",
            "updated_at": "2020-06-29T15:49:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4733625,
            "beatmap_discussion_id": 1684695,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "after talking cos it's 1/6, Ksardas decided to just remove these like in the top diff",
            "created_at": "2020-06-29T18:17:24+00:00",
            "updated_at": "2020-06-29T18:17:24+00:00",
            "deleted_at": null
          },
          {
            "id": 4733626,
            "beatmap_discussion_id": 1684695,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T18:17:24+00:00",
            "updated_at": "2020-06-29T18:17:24+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6115007
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684716,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:28:12+00:00",
        "updated_at": "2020-06-29T16:13:14+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:13:14+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731863,
            "beatmap_discussion_id": 1684716,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "I don't really get your comboing - I mean yeah it is mostly pattern based but still I think you can do with much less NC spamming in general. Especially in the beginning there are soooo many objects that are just single object combos which makes everything looks messy imo. Please go over the whole map and remove combos where they are not necessary for to separate or highlight specific patterns. (stuff like 00:32:612 (1,1,1) - is fine)",
            "created_at": "2020-06-29T14:28:12+00:00",
            "updated_at": "2020-06-29T14:28:12+00:00",
            "deleted_at": null
          },
          {
            "id": 4732392,
            "beatmap_discussion_id": 1684716,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "changed some",
            "created_at": "2020-06-29T15:50:39+00:00",
            "updated_at": "2020-06-29T15:50:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4732610,
            "beatmap_discussion_id": 1684716,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T16:13:14+00:00",
            "updated_at": "2020-06-29T16:13:14+00:00",
            "deleted_at": null
          },
          {
            "id": 4732611,
            "beatmap_discussion_id": 1684716,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:13:14+00:00",
            "updated_at": "2020-06-29T16:13:14+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6115007
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684717,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 26061,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:29:27+00:00",
        "updated_at": "2020-06-29T16:12:30+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:12:30+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731866,
            "beatmap_discussion_id": 1684717,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:26:061 (1,1) - would be cool if you could nerf this 1/4 as it feels kinda unnatural in the context of the calm section",
            "created_at": "2020-06-29T14:29:27+00:00",
            "updated_at": "2020-06-29T14:29:27+00:00",
            "deleted_at": null
          },
          {
            "id": 4732287,
            "beatmap_discussion_id": 1684717,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nerfed",
            "created_at": "2020-06-29T15:35:47+00:00",
            "updated_at": "2020-06-29T15:35:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4732599,
            "beatmap_discussion_id": 1684717,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T16:12:30+00:00",
            "updated_at": "2020-06-29T16:12:30+00:00",
            "deleted_at": null
          },
          {
            "id": 4732600,
            "beatmap_discussion_id": 1684717,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:12:30+00:00",
            "updated_at": "2020-06-29T16:12:30+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6115007
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684729,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:33:55+00:00",
        "updated_at": "2020-06-29T16:13:22+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:13:22+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731886,
            "beatmap_discussion_id": 1684729,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "as with some of the other lower experts the section starting at 01:40:026 - could take some more hitsounding as nothing got copied over cos the top diff is much less dense here",
            "created_at": "2020-06-29T14:33:56+00:00",
            "updated_at": "2020-06-29T14:33:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4732271,
            "beatmap_discussion_id": 1684729,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "whistles",
            "created_at": "2020-06-29T15:32:31+00:00",
            "updated_at": "2020-06-29T15:32:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4732615,
            "beatmap_discussion_id": 1684729,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T16:13:21+00:00",
            "updated_at": "2020-06-29T16:13:21+00:00",
            "deleted_at": null
          },
          {
            "id": 4732616,
            "beatmap_discussion_id": 1684729,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:13:22+00:00",
            "updated_at": "2020-06-29T16:13:22+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6115007
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684732,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323862,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 76406,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:37:19+00:00",
        "updated_at": "2020-06-29T16:15:22+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:15:22+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731896,
            "beatmap_discussion_id": 1684732,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:16:406 (1,2,3) - i kno this i VERY minor but the ds difference here triggers my ocd",
            "created_at": "2020-06-29T14:37:19+00:00",
            "updated_at": "2020-06-29T14:37:19+00:00",
            "deleted_at": null
          },
          {
            "id": 4732637,
            "beatmap_discussion_id": 1684732,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure",
            "created_at": "2020-06-29T16:15:22+00:00",
            "updated_at": "2020-06-29T16:15:22+00:00",
            "deleted_at": null
          },
          {
            "id": 4732638,
            "beatmap_discussion_id": 1684732,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:15:22+00:00",
            "updated_at": "2020-06-29T16:15:22+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684740,
        "beatmapset_id": 1112303,
        "beatmap_id": 2448363,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:43:09+00:00",
        "updated_at": "2020-06-29T16:13:27+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:13:27+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731944,
            "beatmap_discussion_id": 1684740,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "not an issue because it's a gd but would be cool to have the second kiai time as well for cohesion within the set",
            "created_at": "2020-06-29T14:43:09+00:00",
            "updated_at": "2020-06-29T14:43:09+00:00",
            "deleted_at": null
          },
          {
            "id": 4732253,
            "beatmap_discussion_id": 1684740,
            "user_id": 6115007,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "123",
            "created_at": "2020-06-29T15:30:40+00:00",
            "updated_at": "2020-06-29T15:30:40+00:00",
            "deleted_at": null
          },
          {
            "id": 4732617,
            "beatmap_discussion_id": 1684740,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "h",
            "created_at": "2020-06-29T16:13:27+00:00",
            "updated_at": "2020-06-29T16:13:27+00:00",
            "deleted_at": null
          },
          {
            "id": 4732618,
            "beatmap_discussion_id": 1684740,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:13:27+00:00",
            "updated_at": "2020-06-29T16:13:27+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6115007
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684744,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:44:22+00:00",
        "updated_at": "2020-06-30T14:53:25+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-30T14:53:22+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731959,
            "beatmap_discussion_id": 1684744,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "obligatory hitsound general hitsound mod:\n\n00:22:095 - put something like a soft whislte or finish here because a new section starts in the music and it's quite emphasised\n00:48:647 - clap\n01:02:267 - is this clap intentional?\n01:05:198 - clap\n01:12:612 - normal sampleset\n01:17:785 - drum sampleset or something similar",
            "created_at": "2020-06-29T14:44:22+00:00",
            "updated_at": "2020-06-29T14:44:22+00:00",
            "deleted_at": null
          },
          {
            "id": 4738530,
            "beatmap_discussion_id": 1684744,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:22:095 - added soft finish\n00:48:647 - palc\n01:02:267 - no\n01:05:198 - palc\n01:12:612 - normal sampleset\n01:17:785 - I like the idea of a drum sampleset since it's softer than normal yes",
            "created_at": "2020-06-30T14:53:22+00:00",
            "updated_at": "2020-06-30T14:53:22+00:00",
            "deleted_at": null
          },
          {
            "id": 4738531,
            "beatmap_discussion_id": 1684744,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-30T14:53:22+00:00",
            "updated_at": "2020-06-30T14:53:22+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684761,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:50:31+00:00",
        "updated_at": "2020-06-30T14:50:54+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-30T14:50:52+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4731994,
            "beatmap_discussion_id": 1684761,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "add drum and bass to tags, you currently only have dnb",
            "created_at": "2020-06-29T14:50:31+00:00",
            "updated_at": "2020-06-29T14:50:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4738518,
            "beatmap_discussion_id": 1684761,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yes",
            "created_at": "2020-06-30T14:50:52+00:00",
            "updated_at": "2020-06-30T14:50:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4738519,
            "beatmap_discussion_id": 1684761,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-30T14:50:52+00:00",
            "updated_at": "2020-06-30T14:50:52+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684770,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 91405,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-29T14:52:57+00:00",
        "updated_at": "2020-06-29T16:20:19+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T16:20:18+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4732017,
            "beatmap_discussion_id": 1684770,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:31:405 (2,3) - ds here is a little large",
            "created_at": "2020-06-29T14:52:57+00:00",
            "updated_at": "2020-06-29T14:52:57+00:00",
            "deleted_at": null
          },
          {
            "id": 4732674,
            "beatmap_discussion_id": 1684770,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "also a truers in chat moment",
            "created_at": "2020-06-29T16:20:18+00:00",
            "updated_at": "2020-06-29T16:20:18+00:00",
            "deleted_at": null
          },
          {
            "id": 4732675,
            "beatmap_discussion_id": 1684770,
            "user_id": 5745865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-29T16:20:18+00:00",
            "updated_at": "2020-06-29T16:20:18+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              5745865
            ],
            "down": []
          }
        }
      },
      {
        "id": 1684787,
        "beatmapset_id": 1112303,
        "beatmap_id": null,
        "user_id": 2204515,
        "deleted_by_id": null,
        "message_type": "mapper_note",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-06-29T14:58:51+00:00",
        "updated_at": "2020-06-29T14:58:51+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-29T14:58:51+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4732071,
            "beatmap_discussion_id": 1684787,
            "user_id": 2204515,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Metadata\nArtist: Fox Stevenson\nTitle: Take You Down\nSource: https://www.youtube.com/watch?v=uJp2LV4FHXc (official channel)",
            "created_at": "2020-06-29T14:58:51+00:00",
            "updated_at": "2020-06-29T14:58:51+00:00",
            "deleted_at": null
          }
        ],
        "current_user_attributes": {
          "vote_score": 0,
          "can_moderate_kudosu": true,
          "can_resolve": true,
          "can_reopen": true,
          "can_destroy": true
        },
        "votes": {
          "up": 0,
          "down": 0,
          "voters": {
            "up": [],
            "down": []
          }
        }
      }
    ],
    "events": [
      {
        "id": 1779935,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421639,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 13646997,
            "score": 1
          },
          "votes": [
            {
              "user_id": 13646997,
              "score": 1
            }
          ]
        },
        "created_at": "2020-02-28T22:38:56+00:00",
        "user_id": 2204515
      },
      {
        "id": 1780044,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421728,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 13646997,
            "score": 1
          },
          "votes": [
            {
              "user_id": 13646997,
              "score": 1
            }
          ]
        },
        "created_at": "2020-02-29T00:13:06+00:00",
        "user_id": 2204515
      },
      {
        "id": 1796392,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421667,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 13646997,
            "score": 1
          },
          "votes": [
            {
              "user_id": 13646997,
              "score": 1
            }
          ]
        },
        "created_at": "2020-03-07T14:05:25+00:00",
        "user_id": 2204515
      },
      {
        "id": 1817588,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421692,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7458583,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7458583,
              "score": 1
            }
          ]
        },
        "created_at": "2020-03-16T17:39:57+00:00",
        "user_id": 2204515
      },
      {
        "id": 1817593,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421696,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7458583,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7458583,
              "score": 1
            }
          ]
        },
        "created_at": "2020-03-16T17:42:18+00:00",
        "user_id": 2204515
      },
      {
        "id": 1817596,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421689,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7458583,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7458583,
              "score": 1
            }
          ]
        },
        "created_at": "2020-03-16T17:49:18+00:00",
        "user_id": 2204515
      },
      {
        "id": 1817598,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421695,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7458583,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7458583,
              "score": 1
            }
          ]
        },
        "created_at": "2020-03-16T17:50:32+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925217,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421667,
          "beatmap_discussion_post_id": 4340361
        },
        "created_at": "2020-04-25T14:35:56+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925223,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421656,
          "beatmap_discussion_post_id": 4340368
        },
        "created_at": "2020-04-25T14:36:34+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925225,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421657,
          "beatmap_discussion_post_id": 4340372
        },
        "created_at": "2020-04-25T14:37:03+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925233,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421661,
          "beatmap_discussion_post_id": 4340387
        },
        "created_at": "2020-04-25T14:37:53+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925271,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421664,
          "beatmap_discussion_post_id": 4340458
        },
        "created_at": "2020-04-25T14:48:55+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925275,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421692,
          "beatmap_discussion_post_id": 4340478
        },
        "created_at": "2020-04-25T14:55:15+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925276,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421696,
          "beatmap_discussion_post_id": 4340480
        },
        "created_at": "2020-04-25T14:55:16+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925277,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421689,
          "beatmap_discussion_post_id": 4340482
        },
        "created_at": "2020-04-25T14:55:18+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925278,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421695,
          "beatmap_discussion_post_id": 4340485
        },
        "created_at": "2020-04-25T14:55:23+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925280,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421728,
          "beatmap_discussion_post_id": 4340489
        },
        "created_at": "2020-04-25T14:55:30+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925281,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421639,
          "beatmap_discussion_post_id": 4340491
        },
        "created_at": "2020-04-25T14:55:33+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925286,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421724,
          "beatmap_discussion_post_id": 4340502
        },
        "created_at": "2020-04-25T14:57:07+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925287,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421645,
          "beatmap_discussion_post_id": 4340507
        },
        "created_at": "2020-04-25T14:58:04+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925288,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421653,
          "beatmap_discussion_post_id": 4340512
        },
        "created_at": "2020-04-25T14:58:56+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925289,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421647,
          "beatmap_discussion_post_id": 4340514
        },
        "created_at": "2020-04-25T14:59:18+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925292,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421651,
          "beatmap_discussion_post_id": 4340521
        },
        "created_at": "2020-04-25T15:01:25+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925296,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421656,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:14+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925297,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421657,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:32+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925298,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421661,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:33+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925299,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421664,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:34+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925300,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421724,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:38+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925301,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421645,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:42+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925302,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421653,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:43+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925303,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421647,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:44+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925306,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421711,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:03:53+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925313,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421718,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7228554,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7228554,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T15:08:21+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925338,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421718,
          "beatmap_discussion_post_id": 4340600
        },
        "created_at": "2020-04-25T15:12:32+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925588,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421674,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7262798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7262798,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T16:27:54+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925589,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421678,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7262798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7262798,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T16:28:42+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925594,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421681,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7262798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7262798,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-25T16:29:24+00:00",
        "user_id": 2204515
      },
      {
        "id": 1925632,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421670,
          "beatmap_discussion_post_id": 4341207
        },
        "created_at": "2020-04-25T16:44:13+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925633,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421674,
          "beatmap_discussion_post_id": 4341209
        },
        "created_at": "2020-04-25T16:44:18+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925634,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421678,
          "beatmap_discussion_post_id": 4341211
        },
        "created_at": "2020-04-25T16:44:21+00:00",
        "user_id": 5745865
      },
      {
        "id": 1925635,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421681,
          "beatmap_discussion_post_id": 4341213
        },
        "created_at": "2020-04-25T16:44:23+00:00",
        "user_id": 5745865
      },
      {
        "id": 1990706,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1564650,
          "beatmap_discussion_post_id": 4493501
        },
        "created_at": "2020-05-19T10:15:48+00:00",
        "user_id": 5745865
      },
      {
        "id": 1990707,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1564650,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-19T10:15:49+00:00",
        "user_id": 8623835
      },
      {
        "id": 2065114,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421707,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5410645,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5410645,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-15T11:03:18+00:00",
        "user_id": 2204515
      },
      {
        "id": 2065115,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421701,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5410645,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5410645,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-15T11:03:56+00:00",
        "user_id": 2204515
      },
      {
        "id": 2065121,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1564314,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5410645,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5410645,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-15T11:05:10+00:00",
        "user_id": 8623835
      },
      {
        "id": 2065122,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1421708,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5410645,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5410645,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-15T11:05:23+00:00",
        "user_id": 2204515
      },
      {
        "id": 2069983,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421711,
          "beatmap_discussion_post_id": 4654427
        },
        "created_at": "2020-06-16T14:35:30+00:00",
        "user_id": 5745865
      },
      {
        "id": 2069988,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1564303,
          "beatmap_discussion_post_id": 4654432
        },
        "created_at": "2020-06-16T14:36:31+00:00",
        "user_id": 5745865
      },
      {
        "id": 2069997,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1564275,
          "beatmap_discussion_post_id": 4654460
        },
        "created_at": "2020-06-16T14:39:51+00:00",
        "user_id": 5745865
      },
      {
        "id": 2069999,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1564266,
          "beatmap_discussion_post_id": 4654465
        },
        "created_at": "2020-06-16T14:40:33+00:00",
        "user_id": 5745865
      },
      {
        "id": 2070004,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1564263,
          "beatmap_discussion_post_id": 4654478
        },
        "created_at": "2020-06-16T14:41:31+00:00",
        "user_id": 5745865
      },
      {
        "id": 2070020,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1564264,
          "beatmap_discussion_post_id": 4654502
        },
        "created_at": "2020-06-16T14:43:04+00:00",
        "user_id": 5745865
      },
      {
        "id": 2070028,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1564266,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-16T14:43:59+00:00",
        "user_id": 8623835
      },
      {
        "id": 2070029,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1564264,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-16T14:44:02+00:00",
        "user_id": 8623835
      },
      {
        "id": 2070030,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1564263,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-16T14:44:03+00:00",
        "user_id": 8623835
      },
      {
        "id": 2070031,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1564275,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-16T14:44:08+00:00",
        "user_id": 8623835
      },
      {
        "id": 2070033,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1564303,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-16T14:44:09+00:00",
        "user_id": 8623835
      },
      {
        "id": 2070037,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421701,
          "beatmap_discussion_post_id": 4654521
        },
        "created_at": "2020-06-16T14:44:32+00:00",
        "user_id": 5745865
      },
      {
        "id": 2070038,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1564314,
          "beatmap_discussion_post_id": 4654523
        },
        "created_at": "2020-06-16T14:44:35+00:00",
        "user_id": 5745865
      },
      {
        "id": 2070039,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421708,
          "beatmap_discussion_post_id": 4654525
        },
        "created_at": "2020-06-16T14:44:38+00:00",
        "user_id": 5745865
      },
      {
        "id": 2070040,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1421707,
          "beatmap_discussion_post_id": 4654527
        },
        "created_at": "2020-06-16T14:44:42+00:00",
        "user_id": 5745865
      },
      {
        "id": 2070065,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1596429,
          "beatmap_discussion_post_id": 4654580
        },
        "created_at": "2020-06-16T14:52:28+00:00",
        "user_id": 5745865
      },
      {
        "id": 2070093,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1564293,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7228554,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7228554,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-16T15:13:04+00:00",
        "user_id": 8623835
      },
      {
        "id": 2070811,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1564293,
          "beatmap_discussion_post_id": 4656002
        },
        "created_at": "2020-06-16T19:54:54+00:00",
        "user_id": 5745865
      },
      {
        "id": 2086975,
        "type": "genre_edit",
        "comment": {
          "beatmap_discussion_id": null,
          "beatmap_discussion_post_id": null,
          "old": "Unspecified",
          "new": "Electronic"
        },
        "created_at": "2020-06-21T22:11:26+00:00",
        "user_id": 4966334
      },
      {
        "id": 2086976,
        "type": "language_edit",
        "comment": {
          "beatmap_discussion_id": null,
          "beatmap_discussion_post_id": null,
          "old": "Unspecified",
          "new": "English"
        },
        "created_at": "2020-06-21T22:11:26+00:00",
        "user_id": 4966334
      },
      {
        "id": 2103384,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1680027,
          "beatmap_discussion_post_id": 4720410
        },
        "created_at": "2020-06-27T13:26:26+00:00",
        "user_id": 5745865
      },
      {
        "id": 2103385,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1680027,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-27T13:26:28+00:00",
        "user_id": 8623835
      },
      {
        "id": 2103386,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1677762,
          "beatmap_discussion_post_id": 4720414
        },
        "created_at": "2020-06-27T13:26:55+00:00",
        "user_id": 5745865
      },
      {
        "id": 2103387,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1677762,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-27T13:26:56+00:00",
        "user_id": 8623835
      },
      {
        "id": 2103388,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1680039,
          "beatmap_discussion_post_id": 4720417
        },
        "created_at": "2020-06-27T13:27:37+00:00",
        "user_id": 5745865
      },
      {
        "id": 2103389,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1680039,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-27T13:27:39+00:00",
        "user_id": 8623835
      },
      {
        "id": 2109134,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684690,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6115007,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6115007,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T15:44:18+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109135,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684717,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6115007,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6115007,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T15:44:21+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109143,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684695,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6115007,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6115007,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T15:49:59+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109145,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684716,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6115007,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6115007,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T15:50:48+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109146,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684687,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6115007,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6115007,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T15:50:50+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109147,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684729,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6115007,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6115007,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T15:50:51+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109148,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684740,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6115007,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6115007,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T15:50:55+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109201,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684717,
          "beatmap_discussion_post_id": 4732599
        },
        "created_at": "2020-06-29T16:12:30+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109202,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684690,
          "beatmap_discussion_post_id": 4732601
        },
        "created_at": "2020-06-29T16:12:34+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109204,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684716,
          "beatmap_discussion_post_id": 4732610
        },
        "created_at": "2020-06-29T16:13:14+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109205,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684687,
          "beatmap_discussion_post_id": 4732612
        },
        "created_at": "2020-06-29T16:13:17+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109206,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684729,
          "beatmap_discussion_post_id": 4732615
        },
        "created_at": "2020-06-29T16:13:22+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109207,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684740,
          "beatmap_discussion_post_id": 4732617
        },
        "created_at": "2020-06-29T16:13:27+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109212,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684732,
          "beatmap_discussion_post_id": 4732637
        },
        "created_at": "2020-06-29T16:15:22+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109213,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684732,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T16:15:23+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109214,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684580,
          "beatmap_discussion_post_id": 4732644
        },
        "created_at": "2020-06-29T16:16:42+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109215,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684580,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T16:16:43+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109217,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684676,
          "beatmap_discussion_post_id": 4732651
        },
        "created_at": "2020-06-29T16:17:34+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109218,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684676,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T16:17:35+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109223,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684574,
          "beatmap_discussion_post_id": 4732660
        },
        "created_at": "2020-06-29T16:19:29+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109224,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684574,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T16:19:29+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109229,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684770,
          "beatmap_discussion_post_id": 4732674
        },
        "created_at": "2020-06-29T16:20:18+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109230,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684770,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T16:20:19+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109236,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684638,
          "beatmap_discussion_post_id": 4732686
        },
        "created_at": "2020-06-29T16:22:03+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109237,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684638,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T16:22:04+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109239,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684609,
          "beatmap_discussion_post_id": 4732695
        },
        "created_at": "2020-06-29T16:23:47+00:00",
        "user_id": 5745865
      },
      {
        "id": 2109240,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684609,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 5745865,
            "score": 1
          },
          "votes": [
            {
              "user_id": 5745865,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T16:23:48+00:00",
        "user_id": 2204515
      },
      {
        "id": 2109684,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684695,
          "beatmap_discussion_post_id": 4733625
        },
        "created_at": "2020-06-29T18:17:24+00:00",
        "user_id": 5745865
      },
      {
        "id": 2110087,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684659,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7262798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7262798,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T20:07:22+00:00",
        "user_id": 2204515
      },
      {
        "id": 2110090,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684665,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7262798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7262798,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T20:07:44+00:00",
        "user_id": 2204515
      },
      {
        "id": 2110108,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1684670,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7262798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7262798,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-29T20:14:49+00:00",
        "user_id": 2204515
      },
      {
        "id": 2110316,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684659,
          "beatmap_discussion_post_id": 4734616
        },
        "created_at": "2020-06-29T21:52:47+00:00",
        "user_id": 5745865
      },
      {
        "id": 2110317,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684665,
          "beatmap_discussion_post_id": 4734618
        },
        "created_at": "2020-06-29T21:52:52+00:00",
        "user_id": 5745865
      },
      {
        "id": 2110318,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684670,
          "beatmap_discussion_post_id": 4734620
        },
        "created_at": "2020-06-29T21:53:00+00:00",
        "user_id": 5745865
      },
      {
        "id": 2112351,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684591,
          "beatmap_discussion_post_id": 4738504
        },
        "created_at": "2020-06-30T14:48:56+00:00",
        "user_id": 5745865
      },
      {
        "id": 2112352,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684614,
          "beatmap_discussion_post_id": 4738506
        },
        "created_at": "2020-06-30T14:48:59+00:00",
        "user_id": 5745865
      },
      {
        "id": 2112356,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684761,
          "beatmap_discussion_post_id": 4738518
        },
        "created_at": "2020-06-30T14:50:52+00:00",
        "user_id": 5745865
      },
      {
        "id": 2112361,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1684744,
          "beatmap_discussion_post_id": 4738530
        },
        "created_at": "2020-06-30T14:53:22+00:00",
        "user_id": 5745865
      },
      {
        "id": 2115896,
        "type": "nominate",
        "comment": null,
        "created_at": "2020-07-01T20:48:47+00:00",
        "user_id": 8623835
      },
      {
        "id": 2115897,
        "type": "nominate",
        "comment": null,
        "created_at": "2020-07-01T20:48:57+00:00",
        "user_id": 2204515
      },
      {
        "id": 2115898,
        "type": "qualify",
        "comment": null,
        "created_at": "2020-07-01T20:48:57+00:00",
        "user_id": null
      }
    ],
    "related_users": [
      {
        "avatar_url": "https://a.ppy.sh/2204515?1570382644.jpeg",
        "country_code": "DE",
        "default_group": "nat",
        "id": 2204515,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": "#fa3703",
        "username": "Mao",
        "groups": [
          {
            "id": 7,
            "identifier": "nat",
            "name": "Nomination Assessment Team",
            "short_name": "NAT",
            "description": "",
            "colour": "#EB8C47"
          }
        ]
      },
      {
        "avatar_url": "https://a.ppy.sh/2384296?1569870043.jpeg",
        "country_code": "JP",
        "default_group": "default",
        "id": 2384296,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-06-30T18:44:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "A s h e m u",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/4966334?1592202370.png",
        "country_code": "GB",
        "default_group": "bng",
        "id": 4966334,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-07-01T22:29:00+00:00",
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "DeviousPanda",
        "groups": [
          {
            "id": 28,
            "identifier": "bng",
            "name": "Beatmap Nominators",
            "short_name": "BN",
            "description": "",
            "colour": "#A347EB"
          }
        ]
      },
      {
        "avatar_url": "https://a.ppy.sh/5410645?1550370761.jpg",
        "country_code": "DE",
        "default_group": "bng",
        "id": 5410645,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-07-01T20:00:00+00:00",
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "Icekalt",
        "groups": [
          {
            "id": 28,
            "identifier": "bng",
            "name": "Beatmap Nominators",
            "short_name": "BN",
            "description": "",
            "colour": "#A347EB"
          }
        ]
      },
      {
        "avatar_url": "https://a.ppy.sh/5745865?1576536955.jpeg",
        "country_code": "GB",
        "default_group": "default",
        "id": 5745865,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-01T21:51:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Altai",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/6115007?1591567477.gif",
        "country_code": "RU",
        "default_group": "default",
        "id": 6115007,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Ksardas",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/6842421?1590798561.jpeg",
        "country_code": "RU",
        "default_group": "default",
        "id": 6842421,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "xbopost",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/7228554?1592639833.jpeg",
        "country_code": "VN",
        "default_group": "default",
        "id": 7228554,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Kirylln",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/7262798?1566731131.jpeg",
        "country_code": "VN",
        "default_group": "default",
        "id": 7262798,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-07-01T22:28:34+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "LMT",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/7458583?1590786711.jpeg",
        "country_code": "RU",
        "default_group": "default",
        "id": 7458583,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-01T14:14:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Frakturehawkens",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/8346108?1578322019.jpeg",
        "country_code": "RU",
        "default_group": "default",
        "id": 8346108,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-06-20T16:44:24+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Dudlik42",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/8623835?1593514305.jpeg",
        "country_code": "PL",
        "default_group": "bng",
        "id": 8623835,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "Peter",
        "groups": [
          {
            "id": 28,
            "identifier": "bng",
            "name": "Beatmap Nominators",
            "short_name": "BN",
            "description": "",
            "colour": "#A347EB"
          }
        ]
      },
      {
        "avatar_url": "https://a.ppy.sh/10526814?1592815664.jpeg",
        "country_code": "GB",
        "default_group": "default",
        "id": 10526814,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-07-01T22:27:02+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Luminiscental",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/11174970?1592401785.jpeg",
        "country_code": "RU",
        "default_group": "default",
        "id": 11174970,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": false,
        "last_visit": "2020-07-01T22:27:11+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "atix174",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/11310911?1587491709.jpeg",
        "country_code": "US",
        "default_group": "default",
        "id": 11310911,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-01T22:16:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Neosk",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/12123512?1584366391.gif",
        "country_code": "LB",
        "default_group": "default",
        "id": 12123512,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-07-01T17:15:09+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Tactix",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/13646997?1581007055.jpeg",
        "country_code": "DE",
        "default_group": "default",
        "id": 13646997,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-01T18:20:04+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "SirMirai",
        "groups": []
      }
    ]
  },
  "reviews_enabled": true
}
"""