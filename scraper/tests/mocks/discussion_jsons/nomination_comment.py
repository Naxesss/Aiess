import sys
sys.path.append('..')

from bs4 import BeautifulSoup

from scraper.requester import soupify

JSON1 = r"""
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

JSON2 = r"""
{
  "beatmapset": {
    "artist": "Jashin-chan (CV: Suzuki Aina)",
    "covers": {
      "cover": "https://assets.ppy.sh/beatmaps/1147354/covers/cover.jpg?1593773437",
      "cover@2x": "https://assets.ppy.sh/beatmaps/1147354/covers/cover@2x.jpg?1593773437",
      "card": "https://assets.ppy.sh/beatmaps/1147354/covers/card.jpg?1593773437",
      "card@2x": "https://assets.ppy.sh/beatmaps/1147354/covers/card@2x.jpg?1593773437",
      "list": "https://assets.ppy.sh/beatmaps/1147354/covers/list.jpg?1593773437",
      "list@2x": "https://assets.ppy.sh/beatmaps/1147354/covers/list@2x.jpg?1593773437",
      "slimcover": "https://assets.ppy.sh/beatmaps/1147354/covers/slimcover.jpg?1593773437",
      "slimcover@2x": "https://assets.ppy.sh/beatmaps/1147354/covers/slimcover@2x.jpg?1593773437"
    },
    "creator": "Firika",
    "favourite_count": 4,
    "id": 1147354,
    "play_count": 9,
    "preview_url": "//b.ppy.sh/preview/1147354.mp3",
    "source": "邪神ちゃんドロップキック",
    "status": "qualified",
    "title": "Jinbouchou Aika",
    "user_id": 9590557,
    "video": false,
    "availability": {
      "download_disabled": false,
      "more_information": null
    },
    "bpm": 80,
    "can_be_hyped": true,
    "discussion_enabled": true,
    "discussion_locked": false,
    "hype": {
      "current": 5,
      "required": 5
    },
    "is_scoreable": true,
    "last_updated": "2020-07-03T10:49:51+00:00",
    "legacy_thread_url": "https://osu.ppy.sh/community/forums/topics/1051554",
    "nominations": {
      "required_hype": 5,
      "required": 2,
      "current": 2,
      "ranking_eta": "2020-07-10T15:10:24+00:00"
    },
    "ranked": 3,
    "ranked_date": "2020-07-03T14:30:26+00:00",
    "storyboard": true,
    "submitted_date": "2020-04-13T16:56:04+00:00",
    "tags": "jashinchan jinbocho elegy dropkick on my devil! dash japanese anime pop full 花園ゆりね hanazono yurine -claris- yorita yoshino yorita_yoshino",
    "has_favourited": false,
    "beatmaps": [
      {
        "difficulty_rating": 4.59,
        "id": 2395794,
        "mode": "osu",
        "version": "Love",
        "accuracy": 7,
        "ar": 8.7,
        "beatmapset_id": 1147354,
        "bpm": 80,
        "convert": false,
        "count_circles": 747,
        "count_sliders": 675,
        "count_spinners": 3,
        "count_total": 2106,
        "cs": 4.4,
        "deleted_at": null,
        "drain": 4,
        "hit_length": 592,
        "is_scoreable": true,
        "last_updated": "2020-07-03T10:49:52+00:00",
        "mode_int": 0,
        "passcount": 9,
        "playcount": 9,
        "ranked": 3,
        "status": "qualified",
        "total_length": 592,
        "url": "https://osu.ppy.sh/beatmaps/2395794"
      },
      {
        "difficulty_rating": 4.45,
        "id": 2397397,
        "mode": "osu",
        "version": "??",
        "accuracy": 7,
        "ar": 8.2,
        "beatmapset_id": 1147354,
        "bpm": 80,
        "convert": false,
        "count_circles": 240,
        "count_sliders": 221,
        "count_spinners": 2,
        "count_total": 688,
        "cs": 4.8,
        "deleted_at": "2020-04-17T05:06:30.000000Z",
        "drain": 4.8,
        "hit_length": 195,
        "is_scoreable": false,
        "last_updated": "2020-04-15T02:34:32+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": -2,
        "status": "graveyard",
        "total_length": 592,
        "url": "https://osu.ppy.sh/beatmaps/2397397"
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
        "id": 1571116,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 4298072,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-09T11:05:39+00:00",
        "updated_at": "2020-05-09T11:05:39+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-09T11:05:39+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4425476,
            "beatmap_discussion_id": 1571116,
            "user_id": 4298072,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "e",
            "created_at": "2020-05-09T11:05:39+00:00",
            "updated_at": "2020-05-09T11:05:39+00:00",
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
        "id": 1571137,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 4298072,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-09T11:20:47+00:00",
        "updated_at": "2020-05-09T12:57:20+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-09T12:57:20+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4425523,
            "beatmap_discussion_id": 1571137,
            "user_id": 4298072,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "softwhistle2，5是不是有点响了，听到01:29:201 (1,2,1,2,3) - 这里的时候感觉格外突兀",
            "created_at": "2020-05-09T11:20:47+00:00",
            "updated_at": "2020-05-09T11:20:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4425934,
            "beatmap_discussion_id": 1571137,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "删光光",
            "created_at": "2020-05-09T12:57:20+00:00",
            "updated_at": "2020-05-09T12:57:20+00:00",
            "deleted_at": null
          },
          {
            "id": 4425935,
            "beatmap_discussion_id": 1571137,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-09T12:57:20+00:00",
            "updated_at": "2020-05-09T12:57:20+00:00",
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
        "id": 1571145,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 4298072,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 153326,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-09T11:23:04+00:00",
        "updated_at": "2020-05-09T12:57:32+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-09T12:57:31+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4425534,
            "beatmap_discussion_id": 1571145,
            "user_id": 4298072,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:33:326 (1,2,3,1) - 需要音效反馈，默认whistle比较合适",
            "created_at": "2020-05-09T11:23:04+00:00",
            "updated_at": "2020-05-09T11:23:04+00:00",
            "deleted_at": null
          },
          {
            "id": 4425936,
            "beatmap_discussion_id": 1571145,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "加",
            "created_at": "2020-05-09T12:57:30+00:00",
            "updated_at": "2020-05-09T12:57:30+00:00",
            "deleted_at": null
          },
          {
            "id": 4425937,
            "beatmap_discussion_id": 1571145,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-09T12:57:31+00:00",
            "updated_at": "2020-05-09T12:57:31+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1571154,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 4298072,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-09T11:31:48+00:00",
        "updated_at": "2020-05-09T12:57:05+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-09T12:57:04+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4425568,
            "beatmap_discussion_id": 1571154,
            "user_id": 4298072,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "这几个soft的custom音效音色太特殊了 我觉得用默认的还合适些",
            "created_at": "2020-05-09T11:31:48+00:00",
            "updated_at": "2020-05-09T11:31:48+00:00",
            "deleted_at": null
          },
          {
            "id": 4425604,
            "beatmap_discussion_id": 1571154,
            "user_id": 4298072,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "特别很多人声地方 一般只有默认whistle合适",
            "created_at": "2020-05-09T11:34:51+00:00",
            "updated_at": "2020-05-09T11:34:51+00:00",
            "deleted_at": null
          },
          {
            "id": 4425932,
            "beatmap_discussion_id": 1571154,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "好  whistle删了",
            "created_at": "2020-05-09T12:57:04+00:00",
            "updated_at": "2020-05-09T12:57:04+00:00",
            "deleted_at": null
          },
          {
            "id": 4425933,
            "beatmap_discussion_id": 1571154,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-09T12:57:04+00:00",
            "updated_at": "2020-05-09T12:57:04+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1571168,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 4298072,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 470201,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-09T11:38:05+00:00",
        "updated_at": "2020-05-22T02:56:40+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T02:56:40+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4425614,
            "beatmap_discussion_id": 1571168,
            "user_id": 4298072,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:50:201 (1,2,3) - 根据你图风 这东西摆正点比较好(",
            "created_at": "2020-05-09T11:38:05+00:00",
            "updated_at": "2020-05-09T11:38:05+00:00",
            "deleted_at": null
          },
          {
            "id": 4510821,
            "beatmap_discussion_id": 1571168,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ee 姑且改了一下",
            "created_at": "2020-05-22T02:19:18+00:00",
            "updated_at": "2020-05-22T02:19:18+00:00",
            "deleted_at": null
          },
          {
            "id": 4510955,
            "beatmap_discussion_id": 1571168,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T02:56:40+00:00",
            "updated_at": "2020-05-22T02:56:40+00:00",
            "deleted_at": null
          },
          {
            "id": 4510956,
            "beatmap_discussion_id": 1571168,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T02:56:40+00:00",
            "updated_at": "2020-05-22T02:56:40+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1580962,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-13T15:48:12+00:00",
        "updated_at": "2020-05-14T11:21:47+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-13T15:48:12+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4453044,
            "beatmap_discussion_id": 1580962,
            "user_id": 11403815,
            "last_editor_id": 11403815,
            "deleted_by_id": null,
            "system": false,
            "message": "Cute map!! >.<, the storyboard background pictures really fits!! :D",
            "created_at": "2020-05-13T15:48:12+00:00",
            "updated_at": "2020-05-14T11:21:47+00:00",
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
        "id": 1581142,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 10132936,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 50576,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-13T17:30:35+00:00",
        "updated_at": "2020-05-14T01:21:53+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T01:21:52+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4453542,
            "beatmap_discussion_id": 1581142,
            "user_id": 10132936,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:50:576 (2,3) - this gap could be emphasized more. You could swap the positions of 00:50:951 (3,4) - and 00:51:326 (5) -",
            "created_at": "2020-05-13T17:30:35+00:00",
            "updated_at": "2020-05-13T17:30:35+00:00",
            "deleted_at": null
          },
          {
            "id": 4456086,
            "beatmap_discussion_id": 1581142,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea nice idea.  change the shape now",
            "created_at": "2020-05-14T01:21:52+00:00",
            "updated_at": "2020-05-14T01:21:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4456087,
            "beatmap_discussion_id": 1581142,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T01:21:52+00:00",
            "updated_at": "2020-05-14T01:21:52+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1581157,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 10132936,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 524951,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-13T17:36:25+00:00",
        "updated_at": "2020-05-14T08:06:56+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T01:39:12+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4453570,
            "beatmap_discussion_id": 1581157,
            "user_id": 10132936,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "08:44:951 (3,4) - 3 and 4 should be semi-stacked because of 1/8 spacing, and stack 1 and 3 for consistency with 00:26:201 (1,2,3,4) - pattern. Maybe do something like this https://osu.ppy.sh/ss/14909946/585b",
            "created_at": "2020-05-13T17:36:25+00:00",
            "updated_at": "2020-05-13T17:36:25+00:00",
            "deleted_at": null
          },
          {
            "id": 4456183,
            "beatmap_discussion_id": 1581157,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "compared with 00:26:951 (3,4) -, I buff the spacing.\nThe lyric is same between the first section and the last section. so I make the almost same pattern in the two parts. (except the spacing)    your 123 pattern would broken the consistency imo.\nMoreover, the vocal here is much stronger, more emotional and longer. so I think it needs more emphasis to show the vocal variation.  your 34 spacing is smaller than 00:26:951 (3,4) -, it can't bring enough feedback to show the difference. (In fact, it's just a 1/4 jump when i test, your spacing is easier a lot than the fisrt section)\nI want to keep it, but maybe would change it if other modders agree this.",
            "created_at": "2020-05-14T01:39:12+00:00",
            "updated_at": "2020-05-14T01:39:12+00:00",
            "deleted_at": null
          },
          {
            "id": 4456184,
            "beatmap_discussion_id": 1581157,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T01:39:12+00:00",
            "updated_at": "2020-05-14T01:39:12+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582400,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 22451,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T05:38:36+00:00",
        "updated_at": "2020-05-14T10:05:13+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T10:03:42+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4457103,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": 11403815,
            "deleted_by_id": null,
            "system": false,
            "message": "00:22:451 (2) -  00:24:326 (4,5) - 00:17:576 (2,4) -   00:44:951 (5) -  Is this intentional not stack?, because you have clean overlaps here 00:17:576 (2,4) ; 00:19:826 (4,1) - ; 00:29:201 (1,4) -  I think you could fix the stacking there, to make them consistent with the other objects in this first section",
            "created_at": "2020-05-14T05:38:36+00:00",
            "updated_at": "2020-05-14T05:42:10+00:00",
            "deleted_at": null
          },
          {
            "id": 4457136,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:47:201 (1,5) -",
            "created_at": "2020-05-14T05:44:31+00:00",
            "updated_at": "2020-05-14T05:44:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4457420,
            "beatmap_discussion_id": 1582400,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "wow   nice catch :3 fixed",
            "created_at": "2020-05-14T06:44:04+00:00",
            "updated_at": "2020-05-14T06:44:04+00:00",
            "deleted_at": null
          },
          {
            "id": 4457421,
            "beatmap_discussion_id": 1582400,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T06:44:04+00:00",
            "updated_at": "2020-05-14T06:44:04+00:00",
            "deleted_at": null
          },
          {
            "id": 4457522,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:44:201 (1,5) -  dont forget this ! :D",
            "created_at": "2020-05-14T07:09:18+00:00",
            "updated_at": "2020-05-14T07:09:18+00:00",
            "deleted_at": null
          },
          {
            "id": 4457523,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": false
            },
            "created_at": "2020-05-14T07:09:18+00:00",
            "updated_at": "2020-05-14T07:09:18+00:00",
            "deleted_at": null
          },
          {
            "id": 4457531,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nvm... im stupid",
            "created_at": "2020-05-14T07:10:38+00:00",
            "updated_at": "2020-05-14T07:10:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4457532,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T07:10:39+00:00",
            "updated_at": "2020-05-14T07:10:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4457984,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "I might accidentally skip a few that have been unnoticed but i'll try finding most: \n01:28:451 (3,2) -",
            "created_at": "2020-05-14T08:32:26+00:00",
            "updated_at": "2020-05-14T08:32:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4458035,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "03:04:638 (3,4) -",
            "created_at": "2020-05-14T08:40:55+00:00",
            "updated_at": "2020-05-14T08:40:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4458128,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:32:951 (3,3) -",
            "created_at": "2020-05-14T08:57:25+00:00",
            "updated_at": "2020-05-14T08:57:25+00:00",
            "deleted_at": null
          },
          {
            "id": 4458167,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "06:08:013 (1,4) -",
            "created_at": "2020-05-14T09:05:44+00:00",
            "updated_at": "2020-05-14T09:05:44+00:00",
            "deleted_at": null
          },
          {
            "id": 4458168,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "06:13:451 (3,1) -",
            "created_at": "2020-05-14T09:06:07+00:00",
            "updated_at": "2020-05-14T09:06:07+00:00",
            "deleted_at": null
          },
          {
            "id": 4458169,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "06:14:201 (1,3) -",
            "created_at": "2020-05-14T09:06:21+00:00",
            "updated_at": "2020-05-14T09:06:21+00:00",
            "deleted_at": null
          },
          {
            "id": 4458171,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "06:23:013 (4,3) -",
            "created_at": "2020-05-14T09:07:57+00:00",
            "updated_at": "2020-05-14T09:07:57+00:00",
            "deleted_at": null
          },
          {
            "id": 4458205,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": 11403815,
            "system": false,
            "message": "06:49:451 (3,2) -",
            "created_at": "2020-05-14T09:18:35+00:00",
            "updated_at": "2020-05-14T09:19:06+00:00",
            "deleted_at": "2020-05-14T09:19:06+00:00"
          },
          {
            "id": 4458208,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:02:201 (1,3) -",
            "created_at": "2020-05-14T09:19:50+00:00",
            "updated_at": "2020-05-14T09:19:50+00:00",
            "deleted_at": null
          },
          {
            "id": 4458217,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:16:826 (1,1) -",
            "created_at": "2020-05-14T09:22:36+00:00",
            "updated_at": "2020-05-14T09:22:36+00:00",
            "deleted_at": null
          },
          {
            "id": 4458281,
            "beatmap_discussion_id": 1582400,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "09:37:826 (2,4) -",
            "created_at": "2020-05-14T09:32:38+00:00",
            "updated_at": "2020-05-14T09:32:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4458455,
            "beatmap_discussion_id": 1582400,
            "user_id": 9590557,
            "last_editor_id": 9590557,
            "deleted_by_id": null,
            "system": false,
            "message": "wow  thank u :D  i will check all stack things after we fix mods",
            "created_at": "2020-05-14T10:03:42+00:00",
            "updated_at": "2020-05-14T10:05:13+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582418,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 51701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T05:46:27+00:00",
        "updated_at": "2020-05-14T06:36:50+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T06:36:50+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4457142,
            "beatmap_discussion_id": 1582418,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:51:701 (1) - Nice square.. though  I think this could be emphasized a bit more,  perhaps move it a bit further? Or  what i'd do is make a sharp angle, if you want to keep a similiar spacing.",
            "created_at": "2020-05-14T05:46:27+00:00",
            "updated_at": "2020-05-14T05:46:27+00:00",
            "deleted_at": null
          },
          {
            "id": 4457392,
            "beatmap_discussion_id": 1582418,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:51:701 (1,2) - the spacing is large enough in this section imo, it's even larger than 01:02:951 (3,4) -.\nbtw it's not a quare xD, maybe it's ok for me, keep",
            "created_at": "2020-05-14T06:36:50+00:00",
            "updated_at": "2020-05-14T06:36:50+00:00",
            "deleted_at": null
          },
          {
            "id": 4457393,
            "beatmap_discussion_id": 1582418,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T06:36:50+00:00",
            "updated_at": "2020-05-14T06:36:50+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582425,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 62576,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T05:48:36+00:00",
        "updated_at": "2020-05-14T06:38:17+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T06:38:15+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4457155,
            "beatmap_discussion_id": 1582425,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:02:576 (2,3,4) -  Might be me, but having same spacing from  01:02:576 (2,3) -  (1/2) and  01:02:951 (3,4) -  1/4 could be a bit hard to read.. perhaps  but the 3 a little bit closer to the 4, or move the 2 a little bit further",
            "created_at": "2020-05-14T05:48:36+00:00",
            "updated_at": "2020-05-14T05:48:36+00:00",
            "deleted_at": null
          },
          {
            "id": 4457398,
            "beatmap_discussion_id": 1582425,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "reduce the spacing on 01:02:576 (2,3) - now, and make a same spacing with 00:51:701 (1,2) -",
            "created_at": "2020-05-14T06:38:15+00:00",
            "updated_at": "2020-05-14T06:38:15+00:00",
            "deleted_at": null
          },
          {
            "id": 4457399,
            "beatmap_discussion_id": 1582425,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T06:38:15+00:00",
            "updated_at": "2020-05-14T06:38:15+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582432,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 74013,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T05:51:24+00:00",
        "updated_at": "2020-05-14T06:41:41+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T06:41:40+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4457182,
            "beatmap_discussion_id": 1582432,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:14:013 (4,1) -  I feel this could be emphasized a little bit  aswell,  https://i.imgur.com/JldJ6vU.jpg I tried working a bit and did something like this :v",
            "created_at": "2020-05-14T05:51:24+00:00",
            "updated_at": "2020-05-14T05:51:24+00:00",
            "deleted_at": null
          },
          {
            "id": 4457412,
            "beatmap_discussion_id": 1582432,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nice idea, make same spacing 01:14:013 (4,1) - with 00:51:701 (1,2) -",
            "created_at": "2020-05-14T06:41:40+00:00",
            "updated_at": "2020-05-14T06:41:40+00:00",
            "deleted_at": null
          },
          {
            "id": 4457413,
            "beatmap_discussion_id": 1582432,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T06:41:40+00:00",
            "updated_at": "2020-05-14T06:41:40+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582474,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 10132936,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-14T06:22:43+00:00",
        "updated_at": "2020-05-14T06:22:43+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T06:22:43+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4457349,
            "beatmap_discussion_id": 1582474,
            "user_id": 10132936,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Great hitsounds, and really solid map!",
            "created_at": "2020-05-14T06:22:43+00:00",
            "updated_at": "2020-05-14T06:22:43+00:00",
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
        "id": 1582681,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 112451,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T08:28:38+00:00",
        "updated_at": "2020-05-22T03:16:36+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:16:34+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4457967,
            "beatmap_discussion_id": 1582681,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:52:451 (3,4) -  Maybe instead of a 1/2 reverse how about using 1 slider and a circle like https://i.imgur.com/j9rN8OT.jpg Because you don't really use 1/2 reverses in that section, while also 01:57:701 (1,2,1,2) -  having stuff like this connected aswell, if you do like this idea 02:05:951 (6) -  you would need to change this too into a 1/2 slider + a circle!",
            "created_at": "2020-05-14T08:28:38+00:00",
            "updated_at": "2020-05-14T08:28:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4463956,
            "beatmap_discussion_id": 1582681,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "reverse look better to me XD",
            "created_at": "2020-05-15T03:04:55+00:00",
            "updated_at": "2020-05-15T03:04:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4511038,
            "beatmap_discussion_id": 1582681,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T03:16:34+00:00",
            "updated_at": "2020-05-22T03:16:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4511039,
            "beatmap_discussion_id": 1582681,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:16:34+00:00",
            "updated_at": "2020-05-22T03:16:34+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582685,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 108888,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T08:30:58+00:00",
        "updated_at": "2020-05-22T03:16:41+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:16:41+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4457977,
            "beatmap_discussion_id": 1582685,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:48:888 (2,3) -  Could make these parallel,  by copying the 2nd slider and reducing the scaling of it to make the same slider but 1/2 (Same angle)",
            "created_at": "2020-05-14T08:30:58+00:00",
            "updated_at": "2020-05-14T08:30:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4457999,
            "beatmap_discussion_id": 1582685,
            "user_id": 11403815,
            "last_editor_id": 11403815,
            "deleted_by_id": null,
            "system": false,
            "message": "if you do agree with this take a look at 02:21:326 (4,1) -  this too 02:24:326 (1,2) -  02:44:951 (4,1) -  03:09:326 (1,3) -",
            "created_at": "2020-05-14T08:34:59+00:00",
            "updated_at": "2020-05-14T08:47:35+00:00",
            "deleted_at": null
          },
          {
            "id": 4510679,
            "beatmap_discussion_id": 1582685,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "kencho is revive， fixed",
            "created_at": "2020-05-22T01:43:07+00:00",
            "updated_at": "2020-05-22T01:43:07+00:00",
            "deleted_at": null
          },
          {
            "id": 4511040,
            "beatmap_discussion_id": 1582685,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T03:16:41+00:00",
            "updated_at": "2020-05-22T03:16:41+00:00",
            "deleted_at": null
          },
          {
            "id": 4511041,
            "beatmap_discussion_id": 1582685,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:16:41+00:00",
            "updated_at": "2020-05-22T03:16:41+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582690,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 120701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T08:33:56+00:00",
        "updated_at": "2020-05-22T03:16:08+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:16:04+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4457993,
            "beatmap_discussion_id": 1582690,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:00:701 (1) -  Maybe add a 0,1x(1,10) SV to the slider, to add even more emphasis owo? :P",
            "created_at": "2020-05-14T08:33:56+00:00",
            "updated_at": "2020-05-14T08:33:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4458266,
            "beatmap_discussion_id": 1582690,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:54:701 (1) -  similiar suggestion? :o",
            "created_at": "2020-05-14T09:29:26+00:00",
            "updated_at": "2020-05-14T09:29:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4510836,
            "beatmap_discussion_id": 1582690,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "keep consistency",
            "created_at": "2020-05-22T02:22:21+00:00",
            "updated_at": "2020-05-22T02:22:21+00:00",
            "deleted_at": null
          },
          {
            "id": 4511033,
            "beatmap_discussion_id": 1582690,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T03:16:04+00:00",
            "updated_at": "2020-05-22T03:16:04+00:00",
            "deleted_at": null
          },
          {
            "id": 4511034,
            "beatmap_discussion_id": 1582690,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:16:04+00:00",
            "updated_at": "2020-05-22T03:16:04+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582695,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 132701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T08:37:10+00:00",
        "updated_at": "2020-05-22T03:15:58+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:15:58+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4458009,
            "beatmap_discussion_id": 1582695,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:12:701 (5) -  Maybe think about adding an NC  For a strong guitar sound to be consistent with 02:06:701 (1) -  02:09:701 (1) -  since you did it there <---",
            "created_at": "2020-05-14T08:37:10+00:00",
            "updated_at": "2020-05-14T08:37:10+00:00",
            "deleted_at": null
          },
          {
            "id": 4510694,
            "beatmap_discussion_id": 1582695,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "changed NC",
            "created_at": "2020-05-22T01:48:14+00:00",
            "updated_at": "2020-05-22T01:48:14+00:00",
            "deleted_at": null
          },
          {
            "id": 4511031,
            "beatmap_discussion_id": 1582695,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T03:15:58+00:00",
            "updated_at": "2020-05-22T03:15:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4511032,
            "beatmap_discussion_id": 1582695,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:15:58+00:00",
            "updated_at": "2020-05-22T03:15:58+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582704,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 192701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T08:43:02+00:00",
        "updated_at": "2020-05-14T10:02:01+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T10:02:01+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4458046,
            "beatmap_discussion_id": 1582704,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "03:12:701 (1,1,1,1) -  Maybe try adding +10% volume for each object to emphasize the strong sound that keeps going stronger and stronger, and with adding volume hitsound i think that could do pretty nice, so instead of 30% like 03:14:951 (1) -  70%/80%  03:14:201 (1) -  60% 03:13:451 (1) - 50% 03:12:701 (1) -  30/40%",
            "created_at": "2020-05-14T08:43:02+00:00",
            "updated_at": "2020-05-14T08:43:02+00:00",
            "deleted_at": null
          },
          {
            "id": 4458049,
            "beatmap_discussion_id": 1582704,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "03:15:701 (1) -  Maybe you could do a 90% here, but that's up to you",
            "created_at": "2020-05-14T08:43:27+00:00",
            "updated_at": "2020-05-14T08:43:27+00:00",
            "deleted_at": null
          },
          {
            "id": 4458050,
            "beatmap_discussion_id": 1582704,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "if you'll think about this suggestion you could do the opposite here 03:19:451 (1,2,3,4,5) - , like going from high volume to lower",
            "created_at": "2020-05-14T08:43:54+00:00",
            "updated_at": "2020-05-14T08:43:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4458113,
            "beatmap_discussion_id": 1582704,
            "user_id": 11403815,
            "last_editor_id": 11403815,
            "deleted_by_id": null,
            "system": false,
            "message": "05:23:201 (1,2,1,2,1) -  same idea",
            "created_at": "2020-05-14T08:56:30+00:00",
            "updated_at": "2020-05-14T08:56:50+00:00",
            "deleted_at": null
          },
          {
            "id": 4458445,
            "beatmap_discussion_id": 1582704,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "03:15:701 - 50% is enough imo. the fifth section is only 60% and kiai is 80% lul\nfix other with 5% variation.",
            "created_at": "2020-05-14T10:02:01+00:00",
            "updated_at": "2020-05-14T10:02:01+00:00",
            "deleted_at": null
          },
          {
            "id": 4458446,
            "beatmap_discussion_id": 1582704,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T10:02:01+00:00",
            "updated_at": "2020-05-14T10:02:01+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582728,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 346076,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T08:58:55+00:00",
        "updated_at": "2020-05-14T09:52:46+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T09:52:44+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4458137,
            "beatmap_discussion_id": 1582728,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:46:076 (2) -  mute slider end?",
            "created_at": "2020-05-14T08:58:55+00:00",
            "updated_at": "2020-05-14T08:58:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4458402,
            "beatmap_discussion_id": 1582728,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea",
            "created_at": "2020-05-14T09:52:44+00:00",
            "updated_at": "2020-05-14T09:52:44+00:00",
            "deleted_at": null
          },
          {
            "id": 4458403,
            "beatmap_discussion_id": 1582728,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T09:52:44+00:00",
            "updated_at": "2020-05-14T09:52:44+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582737,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 357701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T09:04:03+00:00",
        "updated_at": "2020-05-14T09:53:09+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T09:53:09+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4458157,
            "beatmap_discussion_id": 1582737,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:57:701 (1,2,3) -  I don't think 3 gets as enough emphasis as it has at the moment.. What about doing something like:  https://i.imgur.com/TW2Q1tO.jpg this way 3 is a sharp angle, which emphasizes that strong sound. Just an idea though XD",
            "created_at": "2020-05-14T09:04:03+00:00",
            "updated_at": "2020-05-14T09:04:03+00:00",
            "deleted_at": null
          },
          {
            "id": 4458404,
            "beatmap_discussion_id": 1582737,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "my bad,  change the pattern now.",
            "created_at": "2020-05-14T09:53:09+00:00",
            "updated_at": "2020-05-14T09:53:09+00:00",
            "deleted_at": null
          },
          {
            "id": 4458405,
            "beatmap_discussion_id": 1582737,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T09:53:09+00:00",
            "updated_at": "2020-05-14T09:53:09+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582742,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 389201,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T09:13:09+00:00",
        "updated_at": "2020-05-14T09:34:25+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T09:34:20+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4458185,
            "beatmap_discussion_id": 1582742,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "06:29:201 (1) -  what about moving x to x:74 y:18, creating more spacing for the strong sound,  and plus  since you've done 06:07:451 (2,3) -  ; 06:12:513 (5,1) -  stuff like that, where spacing is noticably more larger than the other sounds",
            "created_at": "2020-05-14T09:13:09+00:00",
            "updated_at": "2020-05-14T09:13:09+00:00",
            "deleted_at": null
          },
          {
            "id": 4458294,
            "beatmap_discussion_id": 1582742,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "1. 06:28:826 (5,6,1) -  the spacing variation is 1.3 → 2.0.   the spacing change is enough to show the strong drum, and there is no vocal here, smaller jump is reasonable.\n2. 06:28:826 (5,6,1) - it's a isosceles triangle, and 06:29:201 (1,2,3,1,2) - this is a symmetrical pattern, so i don't want to change this to break it. moreover, 06:07:451 (2,3,4,1) - also a symmetrical pattern \n3. the larger spacing in the corner is not very easy to play, so i tend to keep it.",
            "created_at": "2020-05-14T09:34:20+00:00",
            "updated_at": "2020-05-14T09:34:20+00:00",
            "deleted_at": null
          },
          {
            "id": 4458295,
            "beatmap_discussion_id": 1582742,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T09:34:20+00:00",
            "updated_at": "2020-05-14T09:34:20+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582750,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 434701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T09:22:24+00:00",
        "updated_at": "2020-05-14T09:47:11+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T09:46:32+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4458216,
            "beatmap_discussion_id": 1582750,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:14:701 (1,1,1) -  How about smalling the spacing a little bit on the 1/12's,  we can compare the spacing between of those triples and -> 07:12:701 (1,1,1) -  Or you can make a higher spacing on the  07:13:201 (1,1,1) - . Works either way!",
            "created_at": "2020-05-14T09:22:25+00:00",
            "updated_at": "2020-05-14T09:22:25+00:00",
            "deleted_at": null
          },
          {
            "id": 4458375,
            "beatmap_discussion_id": 1582750,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "1. making increasing spacing is a transition from 07:12:701 (1,1,1,1) - to 07:15:701 (1,1,1,2) -, and it can show the variation of drums well imo.\n2. NC is a sign of the 1/12 rhythm.\n3. flow is more smooth than 07:12:701 (1,1,1,1) -, so difficulty is almost same.\n keep.",
            "created_at": "2020-05-14T09:46:15+00:00",
            "updated_at": "2020-05-14T09:46:15+00:00",
            "deleted_at": null
          },
          {
            "id": 4458376,
            "beatmap_discussion_id": 1582750,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-14T09:46:15+00:00",
            "updated_at": "2020-05-14T09:46:15+00:00",
            "deleted_at": null
          },
          {
            "id": 4458377,
            "beatmap_discussion_id": 1582750,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": 9590557,
            "system": false,
            "message": "1. making increasing spacing is a transition from 07:12:701 (1,1,1,1) - to 07:15:701 (1,1,1,2) -, and it can show the variation of drums well imo.\n2. NC is a sign of the 1/12 rhythm.\n3. flow is more smooth than 07:12:701 (1,1,1,1) -, so difficulty is almost same.\n keep.",
            "created_at": "2020-05-14T09:46:32+00:00",
            "updated_at": "2020-05-14T09:47:11+00:00",
            "deleted_at": "2020-05-14T09:47:11+00:00"
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582752,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 456701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T09:26:33+00:00",
        "updated_at": "2020-05-22T02:56:50+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T02:56:50+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4458251,
            "beatmap_discussion_id": 1582752,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:36:701 (1) -  I feel 1 doesn't have that much emphasis as the other strong sounds on this part same with 07:24:701 (1) -  because if we take a look at 07:30:701 (1) - , this has way noticable spacing if we compare the two with the small spacing objects. So i'd recommend putting those 2 objects a bit further to make the player notice the strong sound he clicked!",
            "created_at": "2020-05-14T09:26:33+00:00",
            "updated_at": "2020-05-14T09:26:33+00:00",
            "deleted_at": null
          },
          {
            "id": 4458254,
            "beatmap_discussion_id": 1582752,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:45:701 (1) -  similiar situation",
            "created_at": "2020-05-14T09:27:22+00:00",
            "updated_at": "2020-05-14T09:27:22+00:00",
            "deleted_at": null
          },
          {
            "id": 4458256,
            "beatmap_discussion_id": 1582752,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:47:201 (5) -",
            "created_at": "2020-05-14T09:27:37+00:00",
            "updated_at": "2020-05-14T09:27:37+00:00",
            "deleted_at": null
          },
          {
            "id": 4458259,
            "beatmap_discussion_id": 1582752,
            "user_id": 11403815,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:48:513 (2,1) -  Really nice example how u handled the strong sound, it has a way noticable spacing between the two!",
            "created_at": "2020-05-14T09:28:34+00:00",
            "updated_at": "2020-05-14T09:28:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4510833,
            "beatmap_discussion_id": 1582752,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "a little hard to change, change in my way",
            "created_at": "2020-05-22T02:21:32+00:00",
            "updated_at": "2020-05-22T02:21:32+00:00",
            "deleted_at": null
          },
          {
            "id": 4510957,
            "beatmap_discussion_id": 1582752,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T02:56:50+00:00",
            "updated_at": "2020-05-22T02:56:50+00:00",
            "deleted_at": null
          },
          {
            "id": 4510958,
            "beatmap_discussion_id": 1582752,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T02:56:50+00:00",
            "updated_at": "2020-05-22T02:56:50+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1582909,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 11403815,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 399513,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-14T11:17:47+00:00",
        "updated_at": "2020-05-22T03:05:49+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:05:47+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4458765,
            "beatmap_discussion_id": 1582909,
            "user_id": 11403815,
            "last_editor_id": 11403815,
            "deleted_by_id": null,
            "system": false,
            "message": "06:39:513 (6,1,2,3,4) -  This pattern has a pretty bad flow, so it plays a little bit awkwardly in my opinion .. Maybe  consider changing the pattern a bit differently? \n https://i.imgur.com/yNUWz4p.jpg maybe do something like this instead? You'll have to re-arrange the other objects though.",
            "created_at": "2020-05-14T11:17:47+00:00",
            "updated_at": "2020-05-16T20:36:06+00:00",
            "deleted_at": null
          },
          {
            "id": 4510981,
            "beatmap_discussion_id": 1582909,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i think it's ok cause there are some similar flow on 01:48:513 (2,1,2) - 07:57:513 (2,1,2) - and i don't think it's very hard to play. \nwhat's more, 06:39:701 (1,2,3) - the vocal here isn't more intense than 06:40:451 (4,5,6,7) -, your pattern is harder than 06:40:451 (4,5,6,7) -, so yours can show the vocal very well.\nI will keep it.",
            "created_at": "2020-05-22T03:05:47+00:00",
            "updated_at": "2020-05-22T03:05:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4510982,
            "beatmap_discussion_id": 1582909,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:05:47+00:00",
            "updated_at": "2020-05-22T03:05:47+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1583721,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 4470854,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-14T16:48:52+00:00",
        "updated_at": "2020-05-14T16:48:53+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-14T16:48:52+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4460932,
            "beatmap_discussion_id": 1583721,
            "user_id": 4470854,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "好喜歡卡拉OK的風格 ouo b",
            "created_at": "2020-05-14T16:48:53+00:00",
            "updated_at": "2020-05-14T16:48:53+00:00",
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
        "id": 1584781,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "mapper_note",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-15T02:11:10+00:00",
        "updated_at": "2020-05-15T02:47:12+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-15T02:11:10+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4463660,
            "beatmap_discussion_id": 1584781,
            "user_id": 9590557,
            "last_editor_id": 9590557,
            "deleted_by_id": null,
            "system": false,
            "message": "Offical source: \nhttp://jashinchan.com/news/1413\nhttps://motion-gallery.net/projects/jashinchan02\nhttps://www.youtube.com/watch?time_continue=4&v=VQi6mSNUxUM\nCD pic: http://puu.sh/FKAB6/f379c76ad2.png\n(so the romanised title should be \"Jinbouchou Aika\")",
            "created_at": "2020-05-15T02:11:10+00:00",
            "updated_at": "2020-05-15T02:47:12+00:00",
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
        "id": 1600212,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 3996979,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 117701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-21T13:51:33+00:00",
        "updated_at": "2020-05-22T03:16:26+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:16:14+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4507745,
            "beatmap_discussion_id": 1600212,
            "user_id": 3996979,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:57:701 (1,2,1,2) - these 2 patterns are mapping equal voice lines, but they are in a different order, it should be circle -> slider -> circle -> slider, and you have circle -> slider -> slider -> circle",
            "created_at": "2020-05-21T13:51:33+00:00",
            "updated_at": "2020-05-21T13:51:33+00:00",
            "deleted_at": null
          },
          {
            "id": 4510683,
            "beatmap_discussion_id": 1600212,
            "user_id": 4279523,
            "last_editor_id": 4279523,
            "deleted_by_id": null,
            "system": false,
            "message": "want change rhythm to add diversity",
            "created_at": "2020-05-22T01:45:29+00:00",
            "updated_at": "2020-05-22T01:52:24+00:00",
            "deleted_at": null
          },
          {
            "id": 4511036,
            "beatmap_discussion_id": 1600212,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T03:16:14+00:00",
            "updated_at": "2020-05-22T03:16:14+00:00",
            "deleted_at": null
          },
          {
            "id": 4511037,
            "beatmap_discussion_id": 1600212,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:16:14+00:00",
            "updated_at": "2020-05-22T03:16:14+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1600229,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 3996979,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 174326,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-21T13:58:25+00:00",
        "updated_at": "2020-05-22T03:15:51+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:15:51+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4507794,
            "beatmap_discussion_id": 1600229,
            "user_id": 3996979,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:54:326 (1) - slider end outside of the grid, it's probably rankable but you can put it inside without compromising anything. Coordinates x:426 y:325",
            "created_at": "2020-05-21T13:58:26+00:00",
            "updated_at": "2020-05-21T13:58:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4510804,
            "beatmap_discussion_id": 1600229,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fixed",
            "created_at": "2020-05-22T02:16:02+00:00",
            "updated_at": "2020-05-22T02:16:02+00:00",
            "deleted_at": null
          },
          {
            "id": 4511027,
            "beatmap_discussion_id": 1600229,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T03:15:51+00:00",
            "updated_at": "2020-05-22T03:15:51+00:00",
            "deleted_at": null
          },
          {
            "id": 4511028,
            "beatmap_discussion_id": 1600229,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:15:51+00:00",
            "updated_at": "2020-05-22T03:15:51+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1600232,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 3996979,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 188201,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-21T13:59:38+00:00",
        "updated_at": "2020-05-22T03:15:42+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:15:42+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4507798,
            "beatmap_discussion_id": 1600232,
            "user_id": 3996979,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "03:08:201 (2) - you could a reverse slider here, to map the instrument",
            "created_at": "2020-05-21T13:59:38+00:00",
            "updated_at": "2020-05-21T13:59:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4510807,
            "beatmap_discussion_id": 1600232,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "imo circle can express piano(imo that is piano)'s tone",
            "created_at": "2020-05-22T02:17:22+00:00",
            "updated_at": "2020-05-22T02:17:22+00:00",
            "deleted_at": null
          },
          {
            "id": 4511025,
            "beatmap_discussion_id": 1600232,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T03:15:42+00:00",
            "updated_at": "2020-05-22T03:15:42+00:00",
            "deleted_at": null
          },
          {
            "id": 4511026,
            "beatmap_discussion_id": 1600232,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:15:42+00:00",
            "updated_at": "2020-05-22T03:15:42+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1600241,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 3996979,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 327701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-21T14:03:02+00:00",
        "updated_at": "2020-05-22T03:07:11+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:07:06+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4507815,
            "beatmap_discussion_id": 1600241,
            "user_id": 3996979,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:27:701 - this part is really strong, I don't know how you feel about adding a kiai section, but this would be the best part for it",
            "created_at": "2020-05-21T14:03:02+00:00",
            "updated_at": "2020-05-21T14:03:02+00:00",
            "deleted_at": null
          },
          {
            "id": 4510987,
            "beatmap_discussion_id": 1600241,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "of course,  thank u",
            "created_at": "2020-05-22T03:07:06+00:00",
            "updated_at": "2020-05-22T03:07:06+00:00",
            "deleted_at": null
          },
          {
            "id": 4510988,
            "beatmap_discussion_id": 1600241,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:07:06+00:00",
            "updated_at": "2020-05-22T03:07:06+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1600246,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 3996979,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 357701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-21T14:05:01+00:00",
        "updated_at": "2020-05-22T03:06:35+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T03:06:34+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4507822,
            "beatmap_discussion_id": 1600246,
            "user_id": 3996979,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:57:701 (1,2,3) - each slider should be a new combo, really hard to guess the timing by the slider sizes",
            "created_at": "2020-05-21T14:05:01+00:00",
            "updated_at": "2020-05-21T14:05:01+00:00",
            "deleted_at": null
          },
          {
            "id": 4510985,
            "beatmap_discussion_id": 1600246,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea sure. nice catch",
            "created_at": "2020-05-22T03:06:34+00:00",
            "updated_at": "2020-05-22T03:06:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4510986,
            "beatmap_discussion_id": 1600246,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T03:06:34+00:00",
            "updated_at": "2020-05-22T03:06:34+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1600252,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 3996979,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-21T14:08:13+00:00",
        "updated_at": "2020-05-21T14:08:13+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-21T14:08:13+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4507833,
            "beatmap_discussion_id": 1600252,
            "user_id": 3996979,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "It's a well polished map, and a lot of work was put into it, gl :D",
            "created_at": "2020-05-21T14:08:13+00:00",
            "updated_at": "2020-05-21T14:08:13+00:00",
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
        "id": 1602279,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 108888,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-22T13:35:21+00:00",
        "updated_at": "2020-05-22T14:57:26+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T14:57:26+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513294,
            "beatmap_discussion_id": 1602279,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:48:888 (2) - should end on blue tick, not 1/16",
            "created_at": "2020-05-22T13:35:22+00:00",
            "updated_at": "2020-05-22T13:35:22+00:00",
            "deleted_at": null
          },
          {
            "id": 4513511,
            "beatmap_discussion_id": 1602279,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sry my mistake",
            "created_at": "2020-05-22T14:09:42+00:00",
            "updated_at": "2020-05-22T14:09:42+00:00",
            "deleted_at": null
          },
          {
            "id": 4513826,
            "beatmap_discussion_id": 1602279,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T14:57:26+00:00",
            "updated_at": "2020-05-22T14:57:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4513827,
            "beatmap_discussion_id": 1602279,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T14:57:26+00:00",
            "updated_at": "2020-05-22T14:57:26+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1602283,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 63138,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-22T13:37:39+00:00",
        "updated_at": "2020-05-22T14:03:59+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T14:03:59+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513303,
            "beatmap_discussion_id": 1602283,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:03:138 (4) - even with your vocal focused rhythm this feels a bit too undermapped considering how much the 1/4 drums stand out here",
            "created_at": "2020-05-22T13:37:39+00:00",
            "updated_at": "2020-05-22T13:37:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4513457,
            "beatmap_discussion_id": 1602283,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure, add two circles now",
            "created_at": "2020-05-22T14:03:59+00:00",
            "updated_at": "2020-05-22T14:03:59+00:00",
            "deleted_at": null
          },
          {
            "id": 4513458,
            "beatmap_discussion_id": 1602283,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T14:03:59+00:00",
            "updated_at": "2020-05-22T14:03:59+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1602290,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 107201,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-22T13:39:52+00:00",
        "updated_at": "2020-06-21T14:54:55+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T14:54:55+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513320,
            "beatmap_discussion_id": 1602290,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:47:201 (4,1,2) - looks really off cause of stacking https://i.vgy.me/KRouWh.jpg\n\ntake 1-2 and manually move it to get https://i.vgy.me/fqoqzY.jpg or https://i.vgy.me/Wtf4mp.jpg",
            "created_at": "2020-05-22T13:39:52+00:00",
            "updated_at": "2020-05-22T13:39:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4513534,
            "beatmap_discussion_id": 1602290,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "okay",
            "created_at": "2020-05-22T14:14:52+00:00",
            "updated_at": "2020-05-22T14:14:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4513831,
            "beatmap_discussion_id": 1602290,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T14:57:31+00:00",
            "updated_at": "2020-05-22T14:57:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4513832,
            "beatmap_discussion_id": 1602290,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T14:57:32+00:00",
            "updated_at": "2020-05-22T14:57:32+00:00",
            "deleted_at": null
          },
          {
            "id": 4680508,
            "beatmap_discussion_id": 1602290,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa I don't think this was applied :C",
            "created_at": "2020-06-20T21:17:38+00:00",
            "updated_at": "2020-06-20T21:17:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4680509,
            "beatmap_discussion_id": 1602290,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": false
            },
            "created_at": "2020-06-20T21:17:38+00:00",
            "updated_at": "2020-06-20T21:17:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4682200,
            "beatmap_discussion_id": 1602290,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok this time changed slider's position- -",
            "created_at": "2020-06-21T03:27:05+00:00",
            "updated_at": "2020-06-21T03:27:05+00:00",
            "deleted_at": null
          },
          {
            "id": 4685167,
            "beatmap_discussion_id": 1602290,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-06-21T14:54:55+00:00",
            "updated_at": "2020-06-21T14:54:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4685168,
            "beatmap_discussion_id": 1602290,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T14:54:55+00:00",
            "updated_at": "2020-06-21T14:54:55+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1602300,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-22T13:43:30+00:00",
        "updated_at": "2020-05-22T15:01:59+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T15:01:51+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513349,
            "beatmap_discussion_id": 1602300,
            "user_id": 896613,
            "last_editor_id": 896613,
            "deleted_by_id": null,
            "system": false,
            "message": "04:09:701 -until 05:27:607 - \n custom soft hitnormal used in this part sounds really unfitting for a piano+vocal section, would just not use any custom soft hitnormal here or a more fitting hitnormal at least",
            "created_at": "2020-05-22T13:43:30+00:00",
            "updated_at": "2020-05-22T13:47:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4513364,
            "beatmap_discussion_id": 1602300,
            "user_id": 896613,
            "last_editor_id": 896613,
            "deleted_by_id": null,
            "system": false,
            "message": "(they don't sound very fitting in the next part either tbh)\n(or in any part that uses it at all)",
            "created_at": "2020-05-22T13:45:09+00:00",
            "updated_at": "2020-05-22T13:47:35+00:00",
            "deleted_at": null
          },
          {
            "id": 4513863,
            "beatmap_discussion_id": 1602300,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "I'm kinda bad at hitsound. xD   \nI will change it to soft-hitnormal2 instead, thank u for the advice w",
            "created_at": "2020-05-22T15:01:51+00:00",
            "updated_at": "2020-05-22T15:01:51+00:00",
            "deleted_at": null
          },
          {
            "id": 4513864,
            "beatmap_discussion_id": 1602300,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T15:01:51+00:00",
            "updated_at": "2020-05-22T15:01:51+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1602309,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 349169,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-22T13:46:07+00:00",
        "updated_at": "2020-05-22T14:04:41+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T14:04:40+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513373,
            "beatmap_discussion_id": 1602309,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:49:169 - map 1/8 here to kinda go with guitar?",
            "created_at": "2020-05-22T13:46:07+00:00",
            "updated_at": "2020-05-22T13:46:07+00:00",
            "deleted_at": null
          },
          {
            "id": 4513464,
            "beatmap_discussion_id": 1602309,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nice idea. fixed",
            "created_at": "2020-05-22T14:04:39+00:00",
            "updated_at": "2020-05-22T14:04:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4513465,
            "beatmap_discussion_id": 1602309,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T14:04:40+00:00",
            "updated_at": "2020-05-22T14:04:40+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1602319,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 437201,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-22T13:49:14+00:00",
        "updated_at": "2020-05-22T14:57:18+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T14:57:17+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513391,
            "beatmap_discussion_id": 1602319,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:17:201 (1,1,1) - seems overly simplified after you just had some active 1/6 rhythms\nwould at least do something like https://i.vgy.me/sIzIgg.jpg",
            "created_at": "2020-05-22T13:49:14+00:00",
            "updated_at": "2020-05-22T13:49:14+00:00",
            "deleted_at": null
          },
          {
            "id": 4513394,
            "beatmap_discussion_id": 1602319,
            "user_id": 896613,
            "last_editor_id": 896613,
            "deleted_by_id": null,
            "system": false,
            "message": "07:56:201 (1,1) - here too",
            "created_at": "2020-05-22T13:50:15+00:00",
            "updated_at": "2020-05-22T13:50:21+00:00",
            "deleted_at": null
          },
          {
            "id": 4513823,
            "beatmap_discussion_id": 1602319,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok, fixed",
            "created_at": "2020-05-22T14:57:17+00:00",
            "updated_at": "2020-05-22T14:57:17+00:00",
            "deleted_at": null
          },
          {
            "id": 4513824,
            "beatmap_discussion_id": 1602319,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T14:57:17+00:00",
            "updated_at": "2020-05-22T14:57:17+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1602323,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 484076,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-22T13:51:54+00:00",
        "updated_at": "2020-05-22T14:56:58+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T14:56:58+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513402,
            "beatmap_discussion_id": 1602323,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "08:04:076 (1,1,2) - rhythm here does opposite of what is going on in the song\n\nsomething like https://i.vgy.me/udx1kr.jpg or https://i.vgy.me/TUcNu4.jpg would make more sense coming from the vocal based rhythm right before it",
            "created_at": "2020-05-22T13:51:54+00:00",
            "updated_at": "2020-05-22T13:51:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4513634,
            "beatmap_discussion_id": 1602323,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "change to circle",
            "created_at": "2020-05-22T14:30:43+00:00",
            "updated_at": "2020-05-22T14:30:43+00:00",
            "deleted_at": null
          },
          {
            "id": 4513821,
            "beatmap_discussion_id": 1602323,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T14:56:58+00:00",
            "updated_at": "2020-05-22T14:56:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4513822,
            "beatmap_discussion_id": 1602323,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T14:56:58+00:00",
            "updated_at": "2020-05-22T14:56:58+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1602324,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 488201,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-05-22T13:52:35+00:00",
        "updated_at": "2020-05-22T14:56:47+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T14:56:47+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513403,
            "beatmap_discussion_id": 1602324,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "08:08:201 (3,4,1) - really don't get why everything is suddenly so close here, makes movement feel unfitting here",
            "created_at": "2020-05-22T13:52:35+00:00",
            "updated_at": "2020-05-22T13:52:35+00:00",
            "deleted_at": null
          },
          {
            "id": 4513404,
            "beatmap_discussion_id": 1602324,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "08:09:138 (2,3) -",
            "created_at": "2020-05-22T13:52:46+00:00",
            "updated_at": "2020-05-22T13:52:46+00:00",
            "deleted_at": null
          },
          {
            "id": 4513557,
            "beatmap_discussion_id": 1602324,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "08:08:201 (3,4) -  for make harmony's slider head stack with08:06:701 (1,2) -  , enlarged 1",
            "created_at": "2020-05-22T14:18:25+00:00",
            "updated_at": "2020-05-22T14:18:25+00:00",
            "deleted_at": null
          },
          {
            "id": 4513818,
            "beatmap_discussion_id": 1602324,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-05-22T14:56:47+00:00",
            "updated_at": "2020-05-22T14:56:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4513819,
            "beatmap_discussion_id": 1602324,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-05-22T14:56:47+00:00",
            "updated_at": "2020-05-22T14:56:47+00:00",
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
              4279523
            ],
            "down": []
          }
        }
      },
      {
        "id": 1602327,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "praise",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-22T13:54:26+00:00",
        "updated_at": "2020-05-22T13:56:26+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T13:56:26+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4513414,
            "beatmap_discussion_id": 1602327,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "feel free to poke me for a recheck after you got a second bn mod and fixed things!",
            "created_at": "2020-05-22T13:54:26+00:00",
            "updated_at": "2020-05-22T13:54:26+00:00",
            "deleted_at": null
          },
          {
            "id": 4513420,
            "beatmap_discussion_id": 1602327,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "thank you! ^ ^",
            "created_at": "2020-05-22T13:56:26+00:00",
            "updated_at": "2020-05-22T13:56:26+00:00",
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
        "id": 1602715,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 3388410,
        "deleted_by_id": null,
        "message_type": "praise",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-05-22T16:33:55+00:00",
        "updated_at": "2020-05-22T16:43:49+00:00",
        "deleted_at": null,
        "last_post_at": "2020-05-22T16:43:49+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4514421,
            "beatmap_discussion_id": 1602715,
            "user_id": 3388410,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "firika !",
            "created_at": "2020-05-22T16:33:55+00:00",
            "updated_at": "2020-05-22T16:33:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4514464,
            "beatmap_discussion_id": 1602715,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "<3",
            "created_at": "2020-05-22T16:43:49+00:00",
            "updated_at": "2020-05-22T16:43:49+00:00",
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
        "id": 1664982,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-20T16:43:05+00:00",
        "updated_at": "2020-06-21T12:44:51+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T02:28:28+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4679316,
            "beatmap_discussion_id": 1664982,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "04:21:701 -  aaaaaaaa, player feedback in this whole section is really low, because this whole part hardly uses any whistles and the hitsound volume is only 20, the hitsounds are hardly audible over the vocals happening here, i would say to either add more whistles or to increase hitsound volume a little to ~ 25-30 ( or even do both if you want)",
            "created_at": "2020-06-20T16:43:05+00:00",
            "updated_at": "2020-06-20T16:43:05+00:00",
            "deleted_at": null
          },
          {
            "id": 4681845,
            "beatmap_discussion_id": 1664982,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "oki  volume up to 30",
            "created_at": "2020-06-21T02:28:28+00:00",
            "updated_at": "2020-06-21T02:28:28+00:00",
            "deleted_at": null
          },
          {
            "id": 4681846,
            "beatmap_discussion_id": 1664982,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T02:28:28+00:00",
            "updated_at": "2020-06-21T02:28:28+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1665185,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-20T19:08:06+00:00",
        "updated_at": "2020-06-21T12:45:11+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T02:46:54+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4679995,
            "beatmap_discussion_id": 1665185,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:27:701 -  the soft hitclap that you use in this section is really piercing for the ears, its a bit painful, i think its more because of the volume of the sample itself tho because the volume of everything else in this section seems relatively fine, i would suggest lowering the volume of the sample a little or replacing it with a sample that is a bit less piercing",
            "created_at": "2020-06-20T19:08:06+00:00",
            "updated_at": "2020-06-20T19:08:06+00:00",
            "deleted_at": null
          },
          {
            "id": 4681932,
            "beatmap_discussion_id": 1665185,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😆 rip ear lul. replace it now",
            "created_at": "2020-06-21T02:46:54+00:00",
            "updated_at": "2020-06-21T02:46:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4681933,
            "beatmap_discussion_id": 1665185,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T02:46:54+00:00",
            "updated_at": "2020-06-21T02:46:54+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1665276,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 345451,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-20T20:11:54+00:00",
        "updated_at": "2020-06-21T12:44:43+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T01:53:15+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4680235,
            "beatmap_discussion_id": 1665276,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:45:451 (1,1) - hm, these sound really off, I don't blame you for thinking they are 1/3 because the guitar here is weird..\n05:45:451 (1) - the sound happening here is actually 1/8 on 05:45:419 - , but then 05:45:576 (1) -   is just unsnapped bc its ~ 05:45:549 -",
            "created_at": "2020-06-20T20:11:54+00:00",
            "updated_at": "2020-06-20T20:11:54+00:00",
            "deleted_at": null
          },
          {
            "id": 4680241,
            "beatmap_discussion_id": 1665276,
            "user_id": 5312547,
            "last_editor_id": 5312547,
            "deleted_by_id": null,
            "system": false,
            "message": "the only thing i can suggest is mapping them passively, normally id say its fine to simplify but i think they are just too off for that to be an option, maybe try something like https://fayfay2.s-ul.eu/AhiF7oOt ? or maybe something else",
            "created_at": "2020-06-20T20:15:38+00:00",
            "updated_at": "2020-06-20T20:15:57+00:00",
            "deleted_at": null
          },
          {
            "id": 4681647,
            "beatmap_discussion_id": 1665276,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "if you want u could also apply the same thing to 05:52:951 (1,1,1) - , i think it would be a good idea for consistency but this one isn't as bad as the one above",
            "created_at": "2020-06-21T01:13:08+00:00",
            "updated_at": "2020-06-21T01:13:08+00:00",
            "deleted_at": null
          },
          {
            "id": 4681751,
            "beatmap_discussion_id": 1665276,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "oh nice catch, it's my bad.\nmake the passive 1/3 reverse slider u show me now and also keep consistency.\nthank u  :D",
            "created_at": "2020-06-21T01:53:15+00:00",
            "updated_at": "2020-06-21T01:53:15+00:00",
            "deleted_at": null
          },
          {
            "id": 4681752,
            "beatmap_discussion_id": 1665276,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T01:53:15+00:00",
            "updated_at": "2020-06-21T01:53:15+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1665311,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-20T20:40:34+00:00",
        "updated_at": "2020-06-21T12:44:13+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T12:44:13+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4680331,
            "beatmap_discussion_id": 1665311,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "https://fayfay2.s-ul.eu/jbLaH9h1 is it intentional how the ring part of your sb has different size gaps? the more i look at it the more confused i get, i have no idea whats happening here but it looks off?",
            "created_at": "2020-06-20T20:40:34+00:00",
            "updated_at": "2020-06-20T20:40:34+00:00",
            "deleted_at": null
          },
          {
            "id": 4684338,
            "beatmap_discussion_id": 1665311,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fixed it.",
            "created_at": "2020-06-21T12:44:13+00:00",
            "updated_at": "2020-06-21T12:44:13+00:00",
            "deleted_at": null
          },
          {
            "id": 4684339,
            "beatmap_discussion_id": 1665311,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T12:44:13+00:00",
            "updated_at": "2020-06-21T12:44:13+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1665328,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 12701,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-20T20:46:59+00:00",
        "updated_at": "2020-06-21T13:21:03+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T13:21:03+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4680361,
            "beatmap_discussion_id": 1665328,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:12:701 -  I think it would be cute if in this section you added whistles for vocals considering the rhythms here are following them, if you avoided whistles to represent intensity, the different snare sample already does a good job at doing that, at least to me. it doesn't need to be everywhere where there is a vocal, just where vocals are stronger",
            "created_at": "2020-06-20T20:46:59+00:00",
            "updated_at": "2020-06-20T20:46:59+00:00",
            "deleted_at": null
          },
          {
            "id": 4680374,
            "beatmap_discussion_id": 1665328,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "like examples of places where you could have added some are 00:13:451 -  00:14:013 -  00:14:951 -  00:15:701 - 00:18:888 -  and etc ~ just to make the vocal rhythms stand out",
            "created_at": "2020-06-20T20:50:30+00:00",
            "updated_at": "2020-06-20T20:50:30+00:00",
            "deleted_at": null
          },
          {
            "id": 4680525,
            "beatmap_discussion_id": 1665328,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "wait, this applies to most sections, in general i strongly recommend, putting more whistles for vocals where rhythms are following vocals",
            "created_at": "2020-06-20T21:19:36+00:00",
            "updated_at": "2020-06-20T21:19:36+00:00",
            "deleted_at": null
          },
          {
            "id": 4684547,
            "beatmap_discussion_id": 1665328,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "add soft-whistle on every vocal now.",
            "created_at": "2020-06-21T13:21:03+00:00",
            "updated_at": "2020-06-21T13:21:03+00:00",
            "deleted_at": null
          },
          {
            "id": 4684548,
            "beatmap_discussion_id": 1665328,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T13:21:03+00:00",
            "updated_at": "2020-06-21T13:21:03+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1665358,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 35576,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-20T21:03:43+00:00",
        "updated_at": "2020-06-21T12:44:30+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T02:26:39+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4680411,
            "beatmap_discussion_id": 1665358,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:35:576 -  maybe it would be better if you mapped the finish thing here active instead? the other instances previous to this were active, it feels awkward as the only one being left for a slider end, maybe you can do something like https://fayfay2.s-ul.eu/98gAURus instead? another option would be doing something like https://fayfay2.s-ul.eu/jw6kaj7P or even https://fayfay2.s-ul.eu/tPOpVVB7",
            "created_at": "2020-06-20T21:03:43+00:00",
            "updated_at": "2020-06-20T21:03:43+00:00",
            "deleted_at": null
          },
          {
            "id": 4681831,
            "beatmap_discussion_id": 1665358,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fix it to 2 circles.",
            "created_at": "2020-06-21T02:26:39+00:00",
            "updated_at": "2020-06-21T02:26:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4681832,
            "beatmap_discussion_id": 1665358,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T02:26:39+00:00",
            "updated_at": "2020-06-21T02:26:39+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1665391,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 51888,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-20T21:12:43+00:00",
        "updated_at": "2020-06-21T12:44:32+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T02:21:47+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4680491,
            "beatmap_discussion_id": 1665391,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:51:888 -  this makes me a little sad because this section is more or less the same as everything previous to it in terms of spacing, sv and density (with the exception of the consecutive circle patterns), I think you could have did more because this is the chorus phrase that happens here :c",
            "created_at": "2020-06-20T21:12:43+00:00",
            "updated_at": "2020-06-20T21:12:43+00:00",
            "deleted_at": null
          },
          {
            "id": 4680494,
            "beatmap_discussion_id": 1665391,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "even if you did something as simple as bigger spacing here and there for prominent melody / vocals or something, that would distinguish the two parts a lot more",
            "created_at": "2020-06-20T21:13:02+00:00",
            "updated_at": "2020-06-20T21:13:02+00:00",
            "deleted_at": null
          },
          {
            "id": 4681814,
            "beatmap_discussion_id": 1665391,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea, nice idea. fixed",
            "created_at": "2020-06-21T02:21:47+00:00",
            "updated_at": "2020-06-21T02:21:47+00:00",
            "deleted_at": null
          },
          {
            "id": 4681815,
            "beatmap_discussion_id": 1665391,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T02:21:47+00:00",
            "updated_at": "2020-06-21T02:21:47+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1665415,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 110013,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-20T21:26:29+00:00",
        "updated_at": "2020-06-21T14:56:34+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T14:56:27+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4680584,
            "beatmap_discussion_id": 1665415,
            "user_id": 5312547,
            "last_editor_id": 5312547,
            "deleted_by_id": null,
            "system": false,
            "message": "01:50:013 (5,6) -  found this to be a little odd because the rhythms in this section seem to be following vocals but then this skips the prominent vocal on 01:50:388 -  ? if i were to guess why its because you wanted to avoid making rhythm too dense here, maybe something you can do is https://fayfay2.s-ul.eu/bORyGPxI ? or perhaps even https://fayfay2.s-ul.eu/OQo97UcO would work too to catch the vocal? another option is https://fayfay2.s-ul.eu/aoRx8j3Q too",
            "created_at": "2020-06-20T21:26:29+00:00",
            "updated_at": "2020-06-20T21:27:25+00:00",
            "deleted_at": null
          },
          {
            "id": 4682236,
            "beatmap_discussion_id": 1665415,
            "user_id": 4279523,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "TBH i thought that vocal is 1/3, fixed",
            "created_at": "2020-06-21T03:33:56+00:00",
            "updated_at": "2020-06-21T03:33:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4685176,
            "beatmap_discussion_id": 1665415,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "😋",
            "created_at": "2020-06-21T14:56:27+00:00",
            "updated_at": "2020-06-21T14:56:27+00:00",
            "deleted_at": null
          },
          {
            "id": 4685177,
            "beatmap_discussion_id": 1665415,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T14:56:27+00:00",
            "updated_at": "2020-06-21T14:56:27+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1665942,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 358388,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-21T01:17:20+00:00",
        "updated_at": "2020-07-02T20:48:04+00:00",
        "deleted_at": null,
        "last_post_at": "2020-07-02T20:48:04+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4681656,
            "beatmap_discussion_id": 1665942,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:58:388 - 05:58:513 -  aren't these 1/12 ? they sound weird right now as 1/8?",
            "created_at": "2020-06-21T01:17:20+00:00",
            "updated_at": "2020-06-21T01:17:20+00:00",
            "deleted_at": null
          },
          {
            "id": 4681687,
            "beatmap_discussion_id": 1665942,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "snaping 1/12 is also a nice idea, but it seems kinda hard to read imo.\n05:58:513 - 05:58:544 - the gap is too small to sightread, cuz there is the only 1/12 rhythm in the whole map.\nso i choose to cover the cymbal + snare + piano instead, hope it's ok ;-;",
            "created_at": "2020-06-21T01:30:56+00:00",
            "updated_at": "2020-06-21T01:30:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4681688,
            "beatmap_discussion_id": 1665942,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-21T01:30:56+00:00",
            "updated_at": "2020-06-21T01:30:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4751401,
            "beatmap_discussion_id": 1665942,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yeah it should be fine if thats what you want to do",
            "created_at": "2020-07-02T20:48:04+00:00",
            "updated_at": "2020-07-02T20:48:04+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1666803,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 16017012,
        "deleted_by_id": null,
        "message_type": "praise",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-06-21T12:53:18+00:00",
        "updated_at": "2020-06-21T12:53:18+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-21T12:53:18+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4684376,
            "beatmap_discussion_id": 1666803,
            "user_id": 16017012,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nice map",
            "created_at": "2020-06-21T12:53:18+00:00",
            "updated_at": "2020-06-21T12:53:18+00:00",
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
        "id": 1669374,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 896613,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 228705,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-06-22T16:37:56+00:00",
        "updated_at": "2020-06-23T02:20:02+00:00",
        "deleted_at": null,
        "last_post_at": "2020-06-23T02:19:45+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4691118,
            "beatmap_discussion_id": 1669374,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "03:48:705 (2) - missing finish?",
            "created_at": "2020-06-22T16:37:56+00:00",
            "updated_at": "2020-06-22T16:37:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4691119,
            "beatmap_discussion_id": 1669374,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "04:06:705 -",
            "created_at": "2020-06-22T16:38:08+00:00",
            "updated_at": "2020-06-22T16:38:08+00:00",
            "deleted_at": null
          },
          {
            "id": 4691133,
            "beatmap_discussion_id": 1669374,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "05:30:705 - maybe",
            "created_at": "2020-06-22T16:39:53+00:00",
            "updated_at": "2020-06-22T16:39:53+00:00",
            "deleted_at": null
          },
          {
            "id": 4691137,
            "beatmap_discussion_id": 1669374,
            "user_id": 896613,
            "last_editor_id": 896613,
            "deleted_by_id": null,
            "system": false,
            "message": "06:29:205 (1) - 06:41:205 (1) - maybe",
            "created_at": "2020-06-22T16:40:48+00:00",
            "updated_at": "2020-06-22T16:41:07+00:00",
            "deleted_at": null
          },
          {
            "id": 4691146,
            "beatmap_discussion_id": 1669374,
            "user_id": 896613,
            "last_editor_id": 896613,
            "deleted_by_id": null,
            "system": false,
            "message": "07:02:955 - ^ 07:38:205 -",
            "created_at": "2020-06-22T16:41:41+00:00",
            "updated_at": "2020-06-22T16:43:16+00:00",
            "deleted_at": null
          },
          {
            "id": 4691157,
            "beatmap_discussion_id": 1669374,
            "user_id": 896613,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "07:39:705 - this one definitely",
            "created_at": "2020-06-22T16:43:31+00:00",
            "updated_at": "2020-06-22T16:43:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4694195,
            "beatmap_discussion_id": 1669374,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fixed all, sounds better now.",
            "created_at": "2020-06-23T02:19:45+00:00",
            "updated_at": "2020-06-23T02:19:45+00:00",
            "deleted_at": null
          },
          {
            "id": 4694196,
            "beatmap_discussion_id": 1669374,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-06-23T02:19:45+00:00",
            "updated_at": "2020-06-23T02:19:45+00:00",
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
              9590557
            ],
            "down": []
          }
        }
      },
      {
        "id": 1691926,
        "beatmapset_id": 1147354,
        "beatmap_id": null,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "praise",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-07-02T20:41:57+00:00",
        "updated_at": "2020-07-03T00:06:57+00:00",
        "deleted_at": null,
        "last_post_at": "2020-07-03T00:06:57+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4751378,
            "beatmap_discussion_id": 1691926,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "poke me when you are ready",
            "created_at": "2020-07-02T20:41:57+00:00",
            "updated_at": "2020-07-02T20:41:57+00:00",
            "deleted_at": null
          },
          {
            "id": 4752101,
            "beatmap_discussion_id": 1691926,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ty :3",
            "created_at": "2020-07-03T00:06:57+00:00",
            "updated_at": "2020-07-03T00:06:57+00:00",
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
        "id": 1691944,
        "beatmapset_id": 1147354,
        "beatmap_id": 2395794,
        "user_id": 5312547,
        "deleted_by_id": null,
        "message_type": "mapper_note",
        "parent_id": null,
        "timestamp": 151783,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-07-02T20:55:11+00:00",
        "updated_at": "2020-07-02T20:55:11+00:00",
        "deleted_at": null,
        "last_post_at": "2020-07-02T20:55:11+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4751433,
            "beatmap_discussion_id": 1691944,
            "user_id": 5312547,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:31:783 - 02:34:783 - should be fine being snapped to 1/16, the piano does weird pick ups for these, same thing applies to  09:51:845 - i don't think its problematic",
            "created_at": "2020-07-02T20:55:11+00:00",
            "updated_at": "2020-07-02T20:55:11+00:00",
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
        "id": 1684770,
        "beatmapset_id": 1112303,
        "beatmap_id": 2323866,
        "user_id": 4,
        "deleted_by_id": null,
        "message_type": "praise",
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
            "user_id": 4,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nice",
            "created_at": "2020-06-29T14:52:57+00:00",
            "updated_at": "2020-06-29T14:52:57+00:00",
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
        "id": 1962006,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1571154,
          "beatmap_discussion_post_id": 4425932
        },
        "created_at": "2020-05-09T12:57:04+00:00",
        "user_id": 9590557
      },
      {
        "id": 1962007,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1571154,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-09T12:57:05+00:00",
        "user_id": 4298072
      },
      {
        "id": 1962008,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1571137,
          "beatmap_discussion_post_id": 4425934
        },
        "created_at": "2020-05-09T12:57:20+00:00",
        "user_id": 9590557
      },
      {
        "id": 1962009,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1571145,
          "beatmap_discussion_post_id": 4425936
        },
        "created_at": "2020-05-09T12:57:31+00:00",
        "user_id": 9590557
      },
      {
        "id": 1962010,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1571145,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-09T12:57:32+00:00",
        "user_id": 4298072
      },
      {
        "id": 1974404,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1581142,
          "beatmap_discussion_post_id": 4456086
        },
        "created_at": "2020-05-14T01:21:52+00:00",
        "user_id": 9590557
      },
      {
        "id": 1974405,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1581142,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T01:21:53+00:00",
        "user_id": 10132936
      },
      {
        "id": 1974445,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1581157,
          "beatmap_discussion_post_id": 4456183
        },
        "created_at": "2020-05-14T01:39:12+00:00",
        "user_id": 9590557
      },
      {
        "id": 1974937,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582418,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T06:36:40+00:00",
        "user_id": 11403815
      },
      {
        "id": 1974938,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582418,
          "beatmap_discussion_post_id": 4457392
        },
        "created_at": "2020-05-14T06:36:50+00:00",
        "user_id": 9590557
      },
      {
        "id": 1974939,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582425,
          "beatmap_discussion_post_id": 4457398
        },
        "created_at": "2020-05-14T06:38:15+00:00",
        "user_id": 9590557
      },
      {
        "id": 1974940,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582425,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T06:38:17+00:00",
        "user_id": 11403815
      },
      {
        "id": 1974943,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582432,
          "beatmap_discussion_post_id": 4457412
        },
        "created_at": "2020-05-14T06:41:40+00:00",
        "user_id": 9590557
      },
      {
        "id": 1974944,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582432,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T06:41:41+00:00",
        "user_id": 11403815
      },
      {
        "id": 1974946,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582400,
          "beatmap_discussion_post_id": 4457420
        },
        "created_at": "2020-05-14T06:44:04+00:00",
        "user_id": 9590557
      },
      {
        "id": 1974947,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582400,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T06:44:05+00:00",
        "user_id": 11403815
      },
      {
        "id": 1974980,
        "type": "issue_reopen",
        "comment": {
          "beatmap_discussion_id": 1582400,
          "beatmap_discussion_post_id": 4457522
        },
        "created_at": "2020-05-14T07:09:18+00:00",
        "user_id": 11403815
      },
      {
        "id": 1974984,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582400,
          "beatmap_discussion_post_id": 4457531
        },
        "created_at": "2020-05-14T07:10:39+00:00",
        "user_id": 11403815
      },
      {
        "id": 1975134,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1581157,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T08:06:56+00:00",
        "user_id": 10132936
      },
      {
        "id": 1975385,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582742,
          "beatmap_discussion_post_id": 4458294
        },
        "created_at": "2020-05-14T09:34:21+00:00",
        "user_id": 9590557
      },
      {
        "id": 1975386,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582742,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T09:34:25+00:00",
        "user_id": 11403815
      },
      {
        "id": 1975431,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582750,
          "beatmap_discussion_post_id": 4458375
        },
        "created_at": "2020-05-14T09:46:15+00:00",
        "user_id": 9590557
      },
      {
        "id": 1975432,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582750,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T09:46:31+00:00",
        "user_id": 11403815
      },
      {
        "id": 1975444,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582728,
          "beatmap_discussion_post_id": 4458402
        },
        "created_at": "2020-05-14T09:52:44+00:00",
        "user_id": 9590557
      },
      {
        "id": 1975445,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582728,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T09:52:46+00:00",
        "user_id": 11403815
      },
      {
        "id": 1975446,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582737,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T09:53:08+00:00",
        "user_id": 11403815
      },
      {
        "id": 1975447,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582737,
          "beatmap_discussion_post_id": 4458404
        },
        "created_at": "2020-05-14T09:53:09+00:00",
        "user_id": 9590557
      },
      {
        "id": 1975461,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582704,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-14T10:01:56+00:00",
        "user_id": 11403815
      },
      {
        "id": 1975462,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582704,
          "beatmap_discussion_post_id": 4458445
        },
        "created_at": "2020-05-14T10:02:01+00:00",
        "user_id": 9590557
      },
      {
        "id": 1998962,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582685,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T01:43:10+00:00",
        "user_id": 11403815
      },
      {
        "id": 1998971,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582695,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T01:48:17+00:00",
        "user_id": 11403815
      },
      {
        "id": 1999022,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1600229,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T02:16:04+00:00",
        "user_id": 3996979
      },
      {
        "id": 1999035,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1571168,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T02:19:22+00:00",
        "user_id": 4298072
      },
      {
        "id": 1999040,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582752,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T02:21:35+00:00",
        "user_id": 11403815
      },
      {
        "id": 1999128,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1571168,
          "beatmap_discussion_post_id": 4510955
        },
        "created_at": "2020-05-22T02:56:40+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999129,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582752,
          "beatmap_discussion_post_id": 4510957
        },
        "created_at": "2020-05-22T02:56:50+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999143,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582909,
          "beatmap_discussion_post_id": 4510981
        },
        "created_at": "2020-05-22T03:05:47+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999144,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582909,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T03:05:49+00:00",
        "user_id": 11403815
      },
      {
        "id": 1999146,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1600246,
          "beatmap_discussion_post_id": 4510985
        },
        "created_at": "2020-05-22T03:06:34+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999147,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1600246,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T03:06:35+00:00",
        "user_id": 3996979
      },
      {
        "id": 1999148,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1600241,
          "beatmap_discussion_post_id": 4510987
        },
        "created_at": "2020-05-22T03:07:06+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999149,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1600241,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T03:07:08+00:00",
        "user_id": 3996979
      },
      {
        "id": 1999150,
        "type": "kudosu_lost",
        "comment": {
          "beatmap_discussion_id": 1600241,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 0
          },
          "votes": []
        },
        "created_at": "2020-05-22T03:07:10+00:00",
        "user_id": 3996979
      },
      {
        "id": 1999151,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1600241,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T03:07:11+00:00",
        "user_id": 3996979
      },
      {
        "id": 1999200,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1600232,
          "beatmap_discussion_post_id": 4511025
        },
        "created_at": "2020-05-22T03:15:42+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999201,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1600232,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T03:15:42+00:00",
        "user_id": 3996979
      },
      {
        "id": 1999202,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1600229,
          "beatmap_discussion_post_id": 4511027
        },
        "created_at": "2020-05-22T03:15:51+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999204,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582695,
          "beatmap_discussion_post_id": 4511031
        },
        "created_at": "2020-05-22T03:15:58+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999205,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582690,
          "beatmap_discussion_post_id": 4511033
        },
        "created_at": "2020-05-22T03:16:04+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999206,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582690,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T03:16:08+00:00",
        "user_id": 11403815
      },
      {
        "id": 1999207,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1600212,
          "beatmap_discussion_post_id": 4511036
        },
        "created_at": "2020-05-22T03:16:14+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999208,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1600212,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T03:16:26+00:00",
        "user_id": 3996979
      },
      {
        "id": 1999209,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582681,
          "beatmap_discussion_post_id": 4511038
        },
        "created_at": "2020-05-22T03:16:34+00:00",
        "user_id": 9590557
      },
      {
        "id": 1999210,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1582681,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T03:16:36+00:00",
        "user_id": 11403815
      },
      {
        "id": 1999211,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1582685,
          "beatmap_discussion_post_id": 4511040
        },
        "created_at": "2020-05-22T03:16:41+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000229,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1602283,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T14:03:55+00:00",
        "user_id": 896613
      },
      {
        "id": 2000231,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602283,
          "beatmap_discussion_post_id": 4513457
        },
        "created_at": "2020-05-22T14:03:59+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000235,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602309,
          "beatmap_discussion_post_id": 4513464
        },
        "created_at": "2020-05-22T14:04:40+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000236,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1602309,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T14:04:41+00:00",
        "user_id": 896613
      },
      {
        "id": 2000252,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1602279,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T14:09:36+00:00",
        "user_id": 896613
      },
      {
        "id": 2000265,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1602290,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T14:14:50+00:00",
        "user_id": 896613
      },
      {
        "id": 2000272,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1602324,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T14:18:30+00:00",
        "user_id": 896613
      },
      {
        "id": 2000291,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1602323,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 4279523,
            "score": 1
          },
          "votes": [
            {
              "user_id": 4279523,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T14:30:47+00:00",
        "user_id": 896613
      },
      {
        "id": 2000373,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602324,
          "beatmap_discussion_post_id": 4513818
        },
        "created_at": "2020-05-22T14:56:47+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000374,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602323,
          "beatmap_discussion_post_id": 4513821
        },
        "created_at": "2020-05-22T14:56:58+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000375,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602319,
          "beatmap_discussion_post_id": 4513823
        },
        "created_at": "2020-05-22T14:57:18+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000376,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1602319,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T14:57:18+00:00",
        "user_id": 896613
      },
      {
        "id": 2000378,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602279,
          "beatmap_discussion_post_id": 4513826
        },
        "created_at": "2020-05-22T14:57:26+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000380,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602290,
          "beatmap_discussion_post_id": 4513831
        },
        "created_at": "2020-05-22T14:57:32+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000390,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602300,
          "beatmap_discussion_post_id": 4513863
        },
        "created_at": "2020-05-22T15:01:51+00:00",
        "user_id": 9590557
      },
      {
        "id": 2000391,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1602300,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-05-22T15:01:59+00:00",
        "user_id": 896613
      },
      {
        "id": 2083525,
        "type": "issue_reopen",
        "comment": {
          "beatmap_discussion_id": 1602290,
          "beatmap_discussion_post_id": 4680508
        },
        "created_at": "2020-06-20T21:17:38+00:00",
        "user_id": 5312547
      },
      {
        "id": 2084034,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1665942,
          "beatmap_discussion_post_id": 4681687
        },
        "created_at": "2020-06-21T01:30:56+00:00",
        "user_id": 9590557
      },
      {
        "id": 2084070,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1665276,
          "beatmap_discussion_post_id": 4681751
        },
        "created_at": "2020-06-21T01:53:15+00:00",
        "user_id": 9590557
      },
      {
        "id": 2084089,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1665391,
          "beatmap_discussion_post_id": 4681814
        },
        "created_at": "2020-06-21T02:21:47+00:00",
        "user_id": 9590557
      },
      {
        "id": 2084092,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1665358,
          "beatmap_discussion_post_id": 4681831
        },
        "created_at": "2020-06-21T02:26:39+00:00",
        "user_id": 9590557
      },
      {
        "id": 2084100,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1664982,
          "beatmap_discussion_post_id": 4681845
        },
        "created_at": "2020-06-21T02:28:28+00:00",
        "user_id": 9590557
      },
      {
        "id": 2084154,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1665185,
          "beatmap_discussion_post_id": 4681932
        },
        "created_at": "2020-06-21T02:46:54+00:00",
        "user_id": 9590557
      },
      {
        "id": 2085491,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1665311,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T12:44:12+00:00",
        "user_id": 5312547
      },
      {
        "id": 2085492,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1665311,
          "beatmap_discussion_post_id": 4684338
        },
        "created_at": "2020-06-21T12:44:13+00:00",
        "user_id": 9590557
      },
      {
        "id": 2085493,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1665328,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T12:44:26+00:00",
        "user_id": 5312547
      },
      {
        "id": 2085494,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1665358,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T12:44:30+00:00",
        "user_id": 5312547
      },
      {
        "id": 2085495,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1665391,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T12:44:32+00:00",
        "user_id": 5312547
      },
      {
        "id": 2085496,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1665276,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T12:44:43+00:00",
        "user_id": 5312547
      },
      {
        "id": 2085497,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1665942,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T12:44:44+00:00",
        "user_id": 5312547
      },
      {
        "id": 2085498,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1664982,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T12:44:51+00:00",
        "user_id": 5312547
      },
      {
        "id": 2085500,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1665185,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T12:45:11+00:00",
        "user_id": 5312547
      },
      {
        "id": 2085582,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1665328,
          "beatmap_discussion_post_id": 4684547
        },
        "created_at": "2020-06-21T13:21:03+00:00",
        "user_id": 9590557
      },
      {
        "id": 2085884,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1602290,
          "beatmap_discussion_post_id": 4685167
        },
        "created_at": "2020-06-21T14:54:55+00:00",
        "user_id": 9590557
      },
      {
        "id": 2085886,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1665415,
          "beatmap_discussion_post_id": 4685176
        },
        "created_at": "2020-06-21T14:56:27+00:00",
        "user_id": 9590557
      },
      {
        "id": 2085887,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1665415,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-21T14:56:34+00:00",
        "user_id": 5312547
      },
      {
        "id": 2090648,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1669374,
          "beatmap_discussion_post_id": 4694195
        },
        "created_at": "2020-06-23T02:19:45+00:00",
        "user_id": 9590557
      },
      {
        "id": 2090649,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1669374,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 9590557,
            "score": 1
          },
          "votes": [
            {
              "user_id": 9590557,
              "score": 1
            }
          ]
        },
        "created_at": "2020-06-23T02:20:02+00:00",
        "user_id": 896613
      },
      {
        "id": 2120283,
        "type": "nominate",
        "comment": null,
        "created_at": "2020-07-03T12:14:13+00:00",
        "user_id": 896613
      },
      {
        "id": 2120564,
        "type": "nominate",
        "comment": null,
        "created_at": "2020-07-03T14:30:26+00:00",
        "user_id": 5312547
      },
      {
        "id": 2120565,
        "type": "qualify",
        "comment": null,
        "created_at": "2020-07-03T14:30:26+00:00",
        "user_id": null
      }
    ],
    "related_users": [
      {
        "avatar_url": "https://a.ppy.sh/896613?1552063537.png",
        "country_code": "DE",
        "default_group": "nat",
        "id": 896613,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-07-03T15:03:00+00:00",
        "pm_friends_only": false,
        "profile_colour": "#fa3703",
        "username": "Lasse",
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
        "avatar_url": "https://a.ppy.sh/3388410?1593732652.jpeg",
        "country_code": "US",
        "default_group": "bng",
        "id": 3388410,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "eiri-",
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
        "avatar_url": "https://a.ppy.sh/3996979?1560353147.jpeg",
        "country_code": "PT",
        "default_group": "default",
        "id": 3996979,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-02T22:21:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "- Milhofo -",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/4279523?1585820535.png",
        "country_code": "CN",
        "default_group": "default",
        "id": 4279523,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": false,
        "last_visit": "2020-07-03T15:09:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Yorita Yoshino",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/4298072?1590050184.jpeg",
        "country_code": "CN",
        "default_group": "default",
        "id": 4298072,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Bellicose",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/4470854?1584371381.png",
        "country_code": "TW",
        "default_group": "default",
        "id": 4470854,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-07-03T14:51:35+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "YamYA",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/5312547?1593223925.jpeg",
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
        "username": "Lafayla",
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
        "avatar_url": "https://a.ppy.sh/9590557?1576031979.png",
        "country_code": "CN",
        "default_group": "default",
        "id": 9590557,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-07-03T15:10:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Firika",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/10132936?1536061395.jpeg",
        "country_code": "FI",
        "default_group": "default",
        "id": 10132936,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-07-03T15:04:11+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "verychill",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/11403815?1592125455.jpeg",
        "country_code": "LT",
        "default_group": "default",
        "id": 11403815,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": false,
        "last_visit": "2020-07-03T15:09:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "tomatas95",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/16017012?1580713887.jpeg",
        "country_code": "HK",
        "default_group": "default",
        "id": 16017012,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-02T13:56:21+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "china_DD",
        "groups": []
      }
    ]
  },
  "reviews_enabled": true
}
"""

JSON3 = r"""
{
  "beatmapset": {
    "artist": "Tachibana Arisu (CV: Satou Amina)",
    "covers": {
      "cover": "https://assets.ppy.sh/beatmaps/1142335/covers/cover.jpg?1593685973",
      "cover@2x": "https://assets.ppy.sh/beatmaps/1142335/covers/cover@2x.jpg?1593685973",
      "card": "https://assets.ppy.sh/beatmaps/1142335/covers/card.jpg?1593685973",
      "card@2x": "https://assets.ppy.sh/beatmaps/1142335/covers/card@2x.jpg?1593685973",
      "list": "https://assets.ppy.sh/beatmaps/1142335/covers/list.jpg?1593685973",
      "list@2x": "https://assets.ppy.sh/beatmaps/1142335/covers/list@2x.jpg?1593685973",
      "slimcover": "https://assets.ppy.sh/beatmaps/1142335/covers/slimcover.jpg?1593685973",
      "slimcover@2x": "https://assets.ppy.sh/beatmaps/1142335/covers/slimcover@2x.jpg?1593685973"
    },
    "creator": "CoLouRed GlaZeE",
    "favourite_count": 0,
    "id": 1142335,
    "play_count": 9,
    "preview_url": "//b.ppy.sh/preview/1142335.mp3",
    "source": "アイドルマスターシンデレラガールズ",
    "status": "qualified",
    "title": "Kimi ni Todoke",
    "user_id": 3189514,
    "video": false,
    "availability": {
      "download_disabled": false,
      "more_information": null
    },
    "bpm": 126,
    "can_be_hyped": true,
    "discussion_enabled": true,
    "discussion_locked": false,
    "hype": {
      "current": 6,
      "required": 5
    },
    "is_scoreable": true,
    "last_updated": "2020-07-02T10:32:39+00:00",
    "legacy_thread_url": "https://osu.ppy.sh/community/forums/topics/1048094",
    "nominations": {
      "required_hype": 5,
      "required": 2,
      "current": 2,
      "ranking_eta": "2020-07-10T16:47:50+00:00"
    },
    "ranked": 3,
    "ranked_date": "2020-07-03T16:26:31+00:00",
    "storyboard": false,
    "submitted_date": "2020-04-07T15:54:24+00:00",
    "tags": "anime 君に届け japanese video game 佐藤亜美菜 satou amina さとうあみな the idolmaster 谷澤智文 タニザワトモフミ tomofumi tanizawa idolm@ster cinderella girls cool jewelries! 003 akb48 onijam",
    "has_favourited": false,
    "beatmaps": [
      {
        "difficulty_rating": 3.7,
        "id": 2385664,
        "mode": "osu",
        "version": "Insane",
        "accuracy": 7,
        "ar": 8,
        "beatmapset_id": 1142335,
        "bpm": 126,
        "convert": false,
        "count_circles": 358,
        "count_sliders": 205,
        "count_spinners": 5,
        "count_total": 783,
        "cs": 4,
        "deleted_at": null,
        "drain": 6,
        "hit_length": 195,
        "is_scoreable": true,
        "last_updated": "2020-07-02T10:32:40+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": 3,
        "status": "qualified",
        "total_length": 196,
        "url": "https://osu.ppy.sh/beatmaps/2385664"
      },
      {
        "difficulty_rating": 2.86,
        "id": 2388631,
        "mode": "osu",
        "version": "Hard",
        "accuracy": 6,
        "ar": 7,
        "beatmapset_id": 1142335,
        "bpm": 126,
        "convert": false,
        "count_circles": 177,
        "count_sliders": 208,
        "count_spinners": 3,
        "count_total": 602,
        "cs": 4,
        "deleted_at": null,
        "drain": 5,
        "hit_length": 172,
        "is_scoreable": true,
        "last_updated": "2020-07-02T10:32:40+00:00",
        "mode_int": 0,
        "passcount": 0,
        "playcount": 0,
        "ranked": 3,
        "status": "qualified",
        "total_length": 196,
        "url": "https://osu.ppy.sh/beatmaps/2388631"
      },
      {
        "difficulty_rating": 1.79,
        "id": 2388818,
        "mode": "osu",
        "version": "Normal",
        "accuracy": 4,
        "ar": 5,
        "beatmapset_id": 1142335,
        "bpm": 126,
        "convert": false,
        "count_circles": 168,
        "count_sliders": 111,
        "count_spinners": 4,
        "count_total": 402,
        "cs": 3,
        "deleted_at": null,
        "drain": 4,
        "hit_length": 162,
        "is_scoreable": true,
        "last_updated": "2020-07-02T10:32:41+00:00",
        "mode_int": 0,
        "passcount": 9,
        "playcount": 9,
        "ranked": 3,
        "status": "qualified",
        "total_length": 196,
        "url": "https://osu.ppy.sh/beatmaps/2388818"
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
        "id": 1502195,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 5075660,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-04-08T15:07:48+00:00",
        "updated_at": "2020-04-09T03:52:13+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-08T15:07:48+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4231041,
            "beatmap_discussion_id": 1502195,
            "user_id": 5075660,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "冲！",
            "created_at": "2020-04-08T15:07:48+00:00",
            "updated_at": "2020-04-08T15:07:48+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504269,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-04-09T14:12:22+00:00",
        "updated_at": "2020-04-09T14:13:19+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T14:12:22+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236647,
            "beatmap_discussion_id": 1504269,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "这个我擅长",
            "created_at": "2020-04-09T14:12:22+00:00",
            "updated_at": "2020-04-09T14:12:22+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504270,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 10874984,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-04-09T14:12:41+00:00",
        "updated_at": "2020-04-09T14:13:18+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T14:12:41+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236648,
            "beatmap_discussion_id": 1504270,
            "user_id": 10874984,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "H",
            "created_at": "2020-04-09T14:12:41+00:00",
            "updated_at": "2020-04-09T14:12:41+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504272,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 10630389,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-04-09T14:12:59+00:00",
        "updated_at": "2020-04-09T14:13:17+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T14:12:59+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236650,
            "beatmap_discussion_id": 1504272,
            "user_id": 10630389,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "这个群友擅长",
            "created_at": "2020-04-09T14:12:59+00:00",
            "updated_at": "2020-04-09T14:12:59+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504293,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 2688581,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-04-09T14:23:56+00:00",
        "updated_at": "2020-04-09T14:30:41+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T14:23:56+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236695,
            "beatmap_discussion_id": 1504293,
            "user_id": 2688581,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "OK delis",
            "created_at": "2020-04-09T14:23:56+00:00",
            "updated_at": "2020-04-09T14:23:56+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504307,
        "beatmapset_id": 1142335,
        "beatmap_id": 2385664,
        "user_id": 2841009,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 3375,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-04-09T14:31:22+00:00",
        "updated_at": "2020-04-09T15:50:38+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T15:50:38+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236737,
            "beatmap_discussion_id": 1504307,
            "user_id": 2841009,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:03:375 - make it slower for vocals",
            "created_at": "2020-04-09T14:31:22+00:00",
            "updated_at": "2020-04-09T14:31:22+00:00",
            "deleted_at": null
          },
          {
            "id": 4237213,
            "beatmap_discussion_id": 1504307,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Ok",
            "created_at": "2020-04-09T15:50:38+00:00",
            "updated_at": "2020-04-09T15:50:38+00:00",
            "deleted_at": null
          },
          {
            "id": 4237214,
            "beatmap_discussion_id": 1504307,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-09T15:50:38+00:00",
            "updated_at": "2020-04-09T15:50:38+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504320,
        "beatmapset_id": 1142335,
        "beatmap_id": 2385664,
        "user_id": 2841009,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 162422,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-04-09T14:35:53+00:00",
        "updated_at": "2020-04-10T16:14:50+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-10T16:14:50+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236777,
            "beatmap_discussion_id": 1504320,
            "user_id": 2841009,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:42:422 (1) - make this a circle cause it should differ from 02:42:740 (1,1) - cause sounds are different^^;",
            "created_at": "2020-04-09T14:35:53+00:00",
            "updated_at": "2020-04-09T14:35:53+00:00",
            "deleted_at": null
          },
          {
            "id": 4237232,
            "beatmap_discussion_id": 1504320,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "good idea but fuk u cuz that emoji",
            "created_at": "2020-04-09T15:52:31+00:00",
            "updated_at": "2020-04-09T15:52:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4237233,
            "beatmap_discussion_id": 1504320,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-09T15:52:31+00:00",
            "updated_at": "2020-04-09T15:52:31+00:00",
            "deleted_at": null
          },
          {
            "id": 4243716,
            "beatmap_discussion_id": 1504320,
            "user_id": 2841009,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "let's have a discussion please? don't say i'm wrong please? just cause i used emoji? oh my god i'm not feeling well right now going to log off from discord for 1 second",
            "created_at": "2020-04-10T16:07:04+00:00",
            "updated_at": "2020-04-10T16:07:04+00:00",
            "deleted_at": null
          },
          {
            "id": 4243791,
            "beatmap_discussion_id": 1504320,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "I'm sorry but i'm keeping my fuk up until at least some......idk",
            "created_at": "2020-04-10T16:14:50+00:00",
            "updated_at": "2020-04-10T16:14:50+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504322,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 2841009,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-04-09T14:36:49+00:00",
        "updated_at": "2020-04-09T15:47:46+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T14:36:49+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236783,
            "beatmap_discussion_id": 1504322,
            "user_id": 2841009,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "OK delis",
            "created_at": "2020-04-09T14:36:49+00:00",
            "updated_at": "2020-04-09T14:36:49+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504326,
        "beatmapset_id": 1142335,
        "beatmap_id": 2388631,
        "user_id": 2841009,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 4200,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-04-09T14:38:20+00:00",
        "updated_at": "2020-04-09T15:55:09+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T15:55:09+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236800,
            "beatmap_discussion_id": 1504326,
            "user_id": 2841009,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:04:200 - https://osu.ppy.sh/beatmapsets/1142335/discussion/2385664/timeline#/1504307 1",
            "created_at": "2020-04-09T14:38:20+00:00",
            "updated_at": "2020-04-09T14:38:20+00:00",
            "deleted_at": null
          },
          {
            "id": 4237250,
            "beatmap_discussion_id": 1504326,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ye",
            "created_at": "2020-04-09T15:55:09+00:00",
            "updated_at": "2020-04-09T15:55:09+00:00",
            "deleted_at": null
          },
          {
            "id": 4237251,
            "beatmap_discussion_id": 1504326,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-09T15:55:09+00:00",
            "updated_at": "2020-04-09T15:55:09+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504338,
        "beatmapset_id": 1142335,
        "beatmap_id": 2388631,
        "user_id": 2841009,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-04-09T14:45:02+00:00",
        "updated_at": "2020-04-09T15:54:00+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T15:54:00+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236835,
            "beatmap_discussion_id": 1504338,
            "user_id": 2841009,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "YEA like delis said make 00:04:327 - these sections less dense they look dumb now, put more 1/1 slider or pauses 00:05:994 - \ndo long sliders at downbeats they feel natural 00:11:946 - \n\nthis will also highlight chorus better",
            "created_at": "2020-04-09T14:45:02+00:00",
            "updated_at": "2020-04-09T14:45:02+00:00",
            "deleted_at": null
          },
          {
            "id": 4237241,
            "beatmap_discussion_id": 1504338,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fixx",
            "created_at": "2020-04-09T15:54:00+00:00",
            "updated_at": "2020-04-09T15:54:00+00:00",
            "deleted_at": null
          },
          {
            "id": 4237242,
            "beatmap_discussion_id": 1504338,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-09T15:54:00+00:00",
            "updated_at": "2020-04-09T15:54:00+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504342,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 2841009,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-04-09T14:47:53+00:00",
        "updated_at": "2020-04-09T15:49:19+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T15:49:19+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236850,
            "beatmap_discussion_id": 1504342,
            "user_id": 2841009,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:01:470 - move break to here, on crash sound, where its possible\n\nwill create cool effect",
            "created_at": "2020-04-09T14:47:53+00:00",
            "updated_at": "2020-04-09T14:47:53+00:00",
            "deleted_at": null
          },
          {
            "id": 4237199,
            "beatmap_discussion_id": 1504342,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sry i feel dont move is better Owo",
            "created_at": "2020-04-09T15:49:19+00:00",
            "updated_at": "2020-04-09T15:49:19+00:00",
            "deleted_at": null
          },
          {
            "id": 4237200,
            "beatmap_discussion_id": 1504342,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-09T15:49:19+00:00",
            "updated_at": "2020-04-09T15:49:19+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1504359,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 3189514,
        "deleted_by_id": null,
        "message_type": "mapper_note",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-04-09T14:58:34+00:00",
        "updated_at": "2020-04-09T14:58:34+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-09T14:58:34+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4236918,
            "beatmap_discussion_id": 1504359,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "http://columbia.jp/idolmaster/COCX-39653.html",
            "created_at": "2020-04-09T14:58:34+00:00",
            "updated_at": "2020-04-09T14:58:34+00:00",
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
        "id": 1508155,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 7823498,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-04-11T03:21:30+00:00",
        "updated_at": "2020-04-11T03:34:52+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-11T03:34:52+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4247246,
            "beatmap_discussion_id": 1508155,
            "user_id": 7823498,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "from the meta link provided by mapper: https://siscon.s-ul.eu/dyoyuXrL\n\ninclude CV in artist field?\n\n橘ありす (CV: 佐藤亜美菜)\nTachibana Arisu (CV: Satou Amina)",
            "created_at": "2020-04-11T03:21:30+00:00",
            "updated_at": "2020-04-11T03:21:30+00:00",
            "deleted_at": null
          },
          {
            "id": 4247323,
            "beatmap_discussion_id": 1508155,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ur right",
            "created_at": "2020-04-11T03:34:52+00:00",
            "updated_at": "2020-04-11T03:34:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4247324,
            "beatmap_discussion_id": 1508155,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-11T03:34:52+00:00",
            "updated_at": "2020-04-11T03:34:52+00:00",
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
          "up": 2,
          "down": 0,
          "voters": {
            "up": [
              3189514,
              1249323
            ],
            "down": []
          }
        }
      },
      {
        "id": 1508178,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 3,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": false,
        "created_at": "2020-04-11T03:35:27+00:00",
        "updated_at": "2020-06-06T14:05:52+00:00",
        "deleted_at": null,
        "last_post_at": "2020-04-11T03:36:55+00:00",
        "kudosu_denied": true,
        "posts": [
          {
            "id": 4247328,
            "beatmap_discussion_id": 1508178,
            "user_id": 3,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "This beatmap set was updated by the mapper after a nomination. Please ensure to re-check the beatmaps for new issues. If you are the mapper, please comment in this thread on what you changed.",
            "created_at": "2020-04-11T03:35:27+00:00",
            "updated_at": "2020-04-11T03:35:27+00:00",
            "deleted_at": null
          },
          {
            "id": 4247336,
            "beatmap_discussion_id": 1508178,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fix artist",
            "created_at": "2020-04-11T03:36:55+00:00",
            "updated_at": "2020-04-11T03:36:55+00:00",
            "deleted_at": null
          },
          {
            "id": 4247337,
            "beatmap_discussion_id": 1508178,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-04-11T03:36:55+00:00",
            "updated_at": "2020-04-11T03:36:55+00:00",
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
        "id": 1690545,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 360437,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-07-02T05:40:17+00:00",
        "updated_at": "2020-07-02T13:15:45+00:00",
        "deleted_at": null,
        "last_post_at": "2020-07-02T13:15:45+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4747679,
            "beatmap_discussion_id": 1690545,
            "user_id": 360437,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "https://i.imgur.com/6s2b3Iy.jpg\n我試著稍微讓BG內的雜訊在少一點了\n試試看 雖然差異不大但是我覺得還是有差別",
            "created_at": "2020-07-02T05:40:17+00:00",
            "updated_at": "2020-07-02T05:40:17+00:00",
            "deleted_at": null
          },
          {
            "id": 4747775,
            "beatmap_discussion_id": 1690545,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "可以换个网站吗 我无法连接;w;",
            "created_at": "2020-07-02T05:56:39+00:00",
            "updated_at": "2020-07-02T05:56:39+00:00",
            "deleted_at": null
          },
          {
            "id": 4748599,
            "beatmap_discussion_id": 1690545,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "OK",
            "created_at": "2020-07-02T10:23:58+00:00",
            "updated_at": "2020-07-02T10:23:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4748600,
            "beatmap_discussion_id": 1690545,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-07-02T10:23:58+00:00",
            "updated_at": "2020-07-02T10:23:58+00:00",
            "deleted_at": null
          },
          {
            "id": 4749381,
            "beatmap_discussion_id": 1690545,
            "user_id": 360437,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "下次會注意! 不知道imgur可不可以用",
            "created_at": "2020-07-02T13:15:45+00:00",
            "updated_at": "2020-07-02T13:15:45+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1690556,
        "beatmapset_id": 1142335,
        "beatmap_id": 2385664,
        "user_id": 360437,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 151946,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-07-02T05:46:23+00:00",
        "updated_at": "2020-07-03T08:27:39+00:00",
        "deleted_at": null,
        "last_post_at": "2020-07-03T08:27:39+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4747706,
            "beatmap_discussion_id": 1690556,
            "user_id": 360437,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:31:946 (2) - 我懂你這個滑條的用法 也知道你的用意 只是我覺得突然用一個3/2滑條帶過鋼琴跟很多vocal有點過了 可以給這裏多一點手腳讓他打起來能更加地跟隨歌曲還有vocal",
            "created_at": "2020-07-02T05:46:23+00:00",
            "updated_at": "2020-07-02T05:46:23+00:00",
            "deleted_at": null
          },
          {
            "id": 4747709,
            "beatmap_discussion_id": 1690556,
            "user_id": 360437,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:32:898 - 主要是這個我覺得要跟到 因為後面的鋼琴都有跟到這一段只有這裡沒有",
            "created_at": "2020-07-02T05:47:06+00:00",
            "updated_at": "2020-07-02T05:47:06+00:00",
            "deleted_at": null
          },
          {
            "id": 4748628,
            "beatmap_discussion_id": 1690556,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "OK",
            "created_at": "2020-07-02T10:31:52+00:00",
            "updated_at": "2020-07-02T10:31:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4748629,
            "beatmap_discussion_id": 1690556,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-07-02T10:31:52+00:00",
            "updated_at": "2020-07-02T10:31:52+00:00",
            "deleted_at": null
          },
          {
            "id": 4753647,
            "beatmap_discussion_id": 1690556,
            "user_id": 360437,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "好多了!",
            "created_at": "2020-07-03T08:27:39+00:00",
            "updated_at": "2020-07-03T08:27:39+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1690582,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 360437,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-07-02T05:54:02+00:00",
        "updated_at": "2020-07-02T10:26:33+00:00",
        "deleted_at": null,
        "last_post_at": "2020-07-02T10:26:33+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4747762,
            "beatmap_discussion_id": 1690582,
            "user_id": 360437,
            "last_editor_id": 360437,
            "deleted_by_id": null,
            "system": false,
            "message": "add \"anime 君に届け\" to tags? it is the original source of the song and it is from an animation.",
            "created_at": "2020-07-02T05:54:02+00:00",
            "updated_at": "2020-07-02T05:54:14+00:00",
            "deleted_at": null
          },
          {
            "id": 4748610,
            "beatmap_discussion_id": 1690582,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok",
            "created_at": "2020-07-02T10:26:33+00:00",
            "updated_at": "2020-07-02T10:26:33+00:00",
            "deleted_at": null
          },
          {
            "id": 4748611,
            "beatmap_discussion_id": 1690582,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-07-02T10:26:33+00:00",
            "updated_at": "2020-07-02T10:26:33+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1690584,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 360437,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2020-07-02T05:55:24+00:00",
        "updated_at": "2020-07-02T10:24:56+00:00",
        "deleted_at": null,
        "last_post_at": "2020-07-02T10:24:56+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4747768,
            "beatmap_discussion_id": 1690584,
            "user_id": 360437,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "03:18:613 - 其實音樂還是有的 沒有必要用到5% 我覺得15%~20%差不多",
            "created_at": "2020-07-02T05:55:24+00:00",
            "updated_at": "2020-07-02T05:55:24+00:00",
            "deleted_at": null
          },
          {
            "id": 4748603,
            "beatmap_discussion_id": 1690584,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "OK",
            "created_at": "2020-07-02T10:24:56+00:00",
            "updated_at": "2020-07-02T10:24:56+00:00",
            "deleted_at": null
          },
          {
            "id": 4748604,
            "beatmap_discussion_id": 1690584,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2020-07-02T10:24:56+00:00",
            "updated_at": "2020-07-02T10:24:56+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      },
      {
        "id": 1690597,
        "beatmapset_id": 1142335,
        "beatmap_id": null,
        "user_id": 360437,
        "deleted_by_id": null,
        "message_type": "praise",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2020-07-02T06:05:29+00:00",
        "updated_at": "2020-07-02T10:34:11+00:00",
        "deleted_at": null,
        "last_post_at": "2020-07-02T10:34:11+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 4747818,
            "beatmap_discussion_id": 1690597,
            "user_id": 360437,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "好了叫我",
            "created_at": "2020-07-02T06:05:29+00:00",
            "updated_at": "2020-07-02T06:05:29+00:00",
            "deleted_at": null
          },
          {
            "id": 4748639,
            "beatmap_discussion_id": 1690597,
            "user_id": 3189514,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "叫",
            "created_at": "2020-07-02T10:34:11+00:00",
            "updated_at": "2020-07-02T10:34:11+00:00",
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
              3189514
            ],
            "down": []
          }
        }
      }
    ],
    "events": [
      {
        "id": 1881791,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1504342,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-09T15:48:50+00:00",
        "user_id": 2841009
      },
      {
        "id": 1881793,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1504342,
          "beatmap_discussion_post_id": 4237199
        },
        "created_at": "2020-04-09T15:49:19+00:00",
        "user_id": 3189514
      },
      {
        "id": 1881800,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1504307,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-09T15:50:29+00:00",
        "user_id": 2841009
      },
      {
        "id": 1881801,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1504307,
          "beatmap_discussion_post_id": 4237213
        },
        "created_at": "2020-04-09T15:50:38+00:00",
        "user_id": 3189514
      },
      {
        "id": 1881807,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1504320,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-09T15:52:02+00:00",
        "user_id": 2841009
      },
      {
        "id": 1881811,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1504320,
          "beatmap_discussion_post_id": 4237232
        },
        "created_at": "2020-04-09T15:52:31+00:00",
        "user_id": 3189514
      },
      {
        "id": 1881815,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1504338,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-09T15:53:54+00:00",
        "user_id": 2841009
      },
      {
        "id": 1881816,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1504338,
          "beatmap_discussion_post_id": 4237241
        },
        "created_at": "2020-04-09T15:54:00+00:00",
        "user_id": 3189514
      },
      {
        "id": 1881820,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1504326,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-09T15:55:04+00:00",
        "user_id": 2841009
      },
      {
        "id": 1881821,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1504326,
          "beatmap_discussion_post_id": 4237250
        },
        "created_at": "2020-04-09T15:55:09+00:00",
        "user_id": 3189514
      },
      {
        "id": 1884450,
        "type": "nominate",
        "comment": null,
        "created_at": "2020-04-10T16:20:42+00:00",
        "user_id": 2841009
      },
      {
        "id": 1885928,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1508155,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 1249323,
            "score": 1
          },
          "votes": [
            {
              "user_id": 1249323,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-11T03:23:09+00:00",
        "user_id": 7823498
      },
      {
        "id": 1885959,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1508155,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 1249323,
              "score": 1
            },
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-04-11T03:33:53+00:00",
        "user_id": 7823498
      },
      {
        "id": 1885960,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1508155,
          "beatmap_discussion_post_id": 4247323
        },
        "created_at": "2020-04-11T03:34:52+00:00",
        "user_id": 3189514
      },
      {
        "id": 1885962,
        "type": "nomination_reset",
        "comment": {
          "beatmap_discussion_id": 1508178,
          "beatmap_discussion_post_id": 4247328
        },
        "created_at": "2020-04-11T03:35:27+00:00",
        "user_id": 3
      },
      {
        "id": 1885970,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1508178,
          "beatmap_discussion_post_id": 4247336
        },
        "created_at": "2020-04-11T03:36:55+00:00",
        "user_id": 3189514
      },
      {
        "id": 2040692,
        "type": "kudosu_deny",
        "comment": {
          "beatmap_discussion_id": 1508178,
          "beatmap_discussion_post_id": null
        },
        "created_at": "2020-06-06T14:05:52+00:00",
        "user_id": 360437
      },
      {
        "id": 2117382,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1690545,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-07-02T10:23:55+00:00",
        "user_id": 360437
      },
      {
        "id": 2117383,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1690545,
          "beatmap_discussion_post_id": 4748599
        },
        "created_at": "2020-07-02T10:23:58+00:00",
        "user_id": 3189514
      },
      {
        "id": 2117384,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1690584,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-07-02T10:24:55+00:00",
        "user_id": 360437
      },
      {
        "id": 2117385,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1690584,
          "beatmap_discussion_post_id": 4748603
        },
        "created_at": "2020-07-02T10:24:56+00:00",
        "user_id": 3189514
      },
      {
        "id": 2117389,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1690582,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-07-02T10:26:32+00:00",
        "user_id": 360437
      },
      {
        "id": 2117390,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1690582,
          "beatmap_discussion_post_id": 4748610
        },
        "created_at": "2020-07-02T10:26:33+00:00",
        "user_id": 3189514
      },
      {
        "id": 2117400,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1690556,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 3189514,
            "score": 1
          },
          "votes": [
            {
              "user_id": 3189514,
              "score": 1
            }
          ]
        },
        "created_at": "2020-07-02T10:31:50+00:00",
        "user_id": 360437
      },
      {
        "id": 2117401,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1690556,
          "beatmap_discussion_post_id": 4748628
        },
        "created_at": "2020-07-02T10:31:52+00:00",
        "user_id": 3189514
      },
      {
        "id": 2119958,
        "type": "nominate",
        "comment": null,
        "created_at": "2020-07-03T08:29:01+00:00",
        "user_id": 360437
      },
      {
        "id": 2120743,
        "type": "nominate",
        "comment": null,
        "created_at": "2020-07-03T16:26:31+00:00",
        "user_id": 2841009
      },
      {
        "id": 2120744,
        "type": "qualify",
        "comment": null,
        "created_at": "2020-07-03T16:26:31+00:00",
        "user_id": null
      }
    ],
    "related_users": [
      {
        "avatar_url": "https://a.ppy.sh/3?1528948612.png",
        "country_code": "SH",
        "default_group": "bot",
        "id": 3,
        "is_active": true,
        "is_bot": true,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-03T11:32:44+00:00",
        "pm_friends_only": false,
        "profile_colour": "#e45678",
        "username": "BanchoBot",
        "groups": [
          {
            "id": 29,
            "identifier": "bot",
            "name": "Chat Bots",
            "short_name": "BOT",
            "description": "",
            "colour": null
          }
        ]
      },
      {
        "avatar_url": "https://a.ppy.sh/360437?1593432102.jpeg",
        "country_code": "TW",
        "default_group": "bng",
        "id": 360437,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-07-03T15:58:00+00:00",
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "bossandy",
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
      },
      {
        "avatar_url": "https://a.ppy.sh/1249323?1592123413.jpeg",
        "country_code": "ID",
        "default_group": "bng",
        "id": 1249323,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": false,
        "last_visit": "2020-07-03T16:44:00+00:00",
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "Hinsvar",
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
      },
      {
        "avatar_url": "https://a.ppy.sh/2688581?1585784492.jpeg",
        "country_code": "KR",
        "default_group": "default",
        "id": 2688581,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Luscent",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/2841009?1593325486.jpeg",
        "country_code": "RU",
        "default_group": "bng",
        "id": 2841009,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "Mirash",
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
        "avatar_url": "https://a.ppy.sh/3189514?1593328578.jpeg",
        "country_code": "CN",
        "default_group": "default",
        "id": 3189514,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "CoLouRed GlaZeE",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/5075660?1584050131.jpeg",
        "country_code": "CN",
        "default_group": "default",
        "id": 5075660,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Moecho",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/7823498?1590315530.jpeg",
        "country_code": "SG",
        "default_group": "default",
        "id": 7823498,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Ayucchi",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/9590557?1576031979.png",
        "country_code": "CN",
        "default_group": "default",
        "id": 9590557,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-07-03T16:04:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Firika",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/10630389?1579580884.gif",
        "country_code": "CN",
        "default_group": "default",
        "id": 10630389,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-03T16:06:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "HakaseShinonome",
        "groups": []
      },
      {
        "avatar_url": "https://a.ppy.sh/10874984?1589945378.jpeg",
        "country_code": "CN",
        "default_group": "default",
        "id": 10874984,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-07-03T13:29:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "StrengeMistake",
        "groups": []
      }
    ]
  },
  "reviews_enabled": true
}
"""