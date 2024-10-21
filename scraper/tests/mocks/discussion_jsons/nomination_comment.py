import sys
sys.path.append('..')

JSON1 = r"""
{
  "artist": "Fox Stevenson",
  "artist_unicode": "Fox Stevenson",
  "covers": {
    "cover": "https://assets.ppy.sh/beatmaps/1112303/covers/cover.jpg?1650694664",
    "cover@2x": "https://assets.ppy.sh/beatmaps/1112303/covers/cover@2x.jpg?1650694664",
    "card": "https://assets.ppy.sh/beatmaps/1112303/covers/card.jpg?1650694664",
    "card@2x": "https://assets.ppy.sh/beatmaps/1112303/covers/card@2x.jpg?1650694664",
    "list": "https://assets.ppy.sh/beatmaps/1112303/covers/list.jpg?1650694664",
    "list@2x": "https://assets.ppy.sh/beatmaps/1112303/covers/list@2x.jpg?1650694664",
    "slimcover": "https://assets.ppy.sh/beatmaps/1112303/covers/slimcover.jpg?1650694664",
    "slimcover@2x": "https://assets.ppy.sh/beatmaps/1112303/covers/slimcover@2x.jpg?1650694664"
  },
  "creator": "Altai",
  "favourite_count": 148,
  "hype": null,
  "id": 1112303,
  "nsfw": false,
  "offset": 0,
  "play_count": 443745,
  "preview_url": "//b.ppy.sh/preview/1112303.mp3",
  "source": "",
  "spotlight": false,
  "status": "ranked",
  "title": "Take You Down",
  "title_unicode": "Take You Down",
  "track_id": null,
  "user_id": 5745865,
  "video": false,
  "bpm": 174,
  "can_be_hyped": false,
  "deleted_at": null,
  "discussion_enabled": true,
  "discussion_locked": false,
  "is_scoreable": true,
  "last_updated": "2020-07-01T16:13:46Z",
  "legacy_thread_url": "https://osu.ppy.sh/community/forums/topics/1025106",
  "nominations_summary": {
    "current": 2,
    "eligible_main_rulesets": [
      "osu"
    ],
    "required_meta": {
      "main_ruleset": 2,
      "non_main_ruleset": 1
    }
  },
  "ranked": 1,
  "ranked_date": "2020-07-09T00:25:38Z",
  "storyboard": false,
  "submitted_date": "2020-02-19T20:59:18Z",
  "tags": "stan sb stanley stevenson byrne english electronic dnb dance frakturehawkens lmt icekalt sirmirai kirylln undeadphoneguy ksardas drum and bass n &",
  "availability": {
    "download_disabled": false,
    "more_information": null
  },
  "beatmaps": [
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 5.37,
      "id": 2323862,
      "mode": "osu",
      "status": "ranked",
      "total_length": 119,
      "user_id": 5745865,
      "version": "Descend",
      "accuracy": 8.5,
      "ar": 9.2,
      "bpm": 174,
      "convert": false,
      "count_circles": 133,
      "count_sliders": 201,
      "count_spinners": 1,
      "cs": 4.1,
      "deleted_at": null,
      "drain": 6,
      "hit_length": 108,
      "is_scoreable": true,
      "last_updated": "2020-07-01T16:13:47Z",
      "mode_int": 0,
      "passcount": 12159,
      "playcount": 65565,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/2323862",
      "checksum": "e315999334abc495e0a17336e245653a"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 4.83,
      "id": 2323863,
      "mode": "osu",
      "status": "ranked",
      "total_length": 119,
      "user_id": 7458583,
      "version": "Frakturehawkens' Extra",
      "accuracy": 8,
      "ar": 9,
      "bpm": 174,
      "convert": false,
      "count_circles": 140,
      "count_sliders": 172,
      "count_spinners": 4,
      "cs": 3.8,
      "deleted_at": null,
      "drain": 5.2,
      "hit_length": 108,
      "is_scoreable": true,
      "last_updated": "2020-07-01T16:13:48Z",
      "mode_int": 0,
      "passcount": 2169,
      "playcount": 32049,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/2323863",
      "checksum": "b8d326ccf28f4916745f9e329de45ae6"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 4.73,
      "id": 2323864,
      "mode": "osu",
      "status": "ranked",
      "total_length": 119,
      "user_id": 5410645,
      "version": "Icekalt's Insane",
      "accuracy": 8,
      "ar": 9,
      "bpm": 174,
      "convert": false,
      "count_circles": 166,
      "count_sliders": 182,
      "count_spinners": 1,
      "cs": 3.4,
      "deleted_at": null,
      "drain": 5,
      "hit_length": 108,
      "is_scoreable": true,
      "last_updated": "2020-07-01T16:13:48Z",
      "mode_int": 0,
      "passcount": 9207,
      "playcount": 51642,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/2323864",
      "checksum": "0fa01f675c0c68abcadb5194588bbac3"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 4.75,
      "id": 2323865,
      "mode": "osu",
      "status": "graveyard",
      "total_length": 119,
      "user_id": 5745865,
      "version": "kiry's Insane",
      "accuracy": 7.5,
      "ar": 9,
      "bpm": 174,
      "convert": false,
      "count_circles": 227,
      "count_sliders": 107,
      "count_spinners": 1,
      "cs": 4,
      "deleted_at": "2020-04-25T15:13:33Z",
      "drain": 5,
      "hit_length": 102,
      "is_scoreable": false,
      "last_updated": "2020-04-25T15:02:31Z",
      "mode_int": 0,
      "passcount": 0,
      "playcount": 0,
      "ranked": -2,
      "url": "https://osu.ppy.sh/beatmaps/2323865",
      "checksum": "469a1feb1627fee28d600ce9de7d471a"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 2.27,
      "id": 2323866,
      "mode": "osu",
      "status": "ranked",
      "total_length": 119,
      "user_id": 5745865,
      "version": "Normal",
      "accuracy": 4,
      "ar": 5,
      "bpm": 174,
      "convert": false,
      "count_circles": 81,
      "count_sliders": 109,
      "count_spinners": 1,
      "cs": 3,
      "deleted_at": null,
      "drain": 3,
      "hit_length": 108,
      "is_scoreable": true,
      "last_updated": "2020-07-01T16:13:49Z",
      "mode_int": 0,
      "passcount": 15003,
      "playcount": 41526,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/2323866",
      "checksum": "ba63a386b3a0fe7f9285cd8e39322f73"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 0,
      "id": 2331900,
      "mode": "osu",
      "status": "graveyard",
      "total_length": 0,
      "user_id": 5745865,
      "version": "",
      "accuracy": 0,
      "ar": 0,
      "bpm": 174,
      "convert": false,
      "count_circles": 0,
      "count_sliders": 0,
      "count_spinners": 0,
      "cs": 0,
      "deleted_at": "2020-02-27T12:19:54Z",
      "drain": 0,
      "hit_length": 0,
      "is_scoreable": false,
      "last_updated": "2020-02-27T12:11:14Z",
      "mode_int": 0,
      "passcount": 0,
      "playcount": 0,
      "ranked": -2,
      "url": "https://osu.ppy.sh/beatmaps/2331900",
      "checksum": null
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 0,
      "id": 2331901,
      "mode": "osu",
      "status": "graveyard",
      "total_length": 0,
      "user_id": 5745865,
      "version": "",
      "accuracy": 0,
      "ar": 0,
      "bpm": 174,
      "convert": false,
      "count_circles": 0,
      "count_sliders": 0,
      "count_spinners": 0,
      "cs": 0,
      "deleted_at": "2020-02-27T12:19:54Z",
      "drain": 0,
      "hit_length": 0,
      "is_scoreable": false,
      "last_updated": "2020-02-27T12:11:14Z",
      "mode_int": 0,
      "passcount": 0,
      "playcount": 0,
      "ranked": -2,
      "url": "https://osu.ppy.sh/beatmaps/2331901",
      "checksum": null
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 0,
      "id": 2331902,
      "mode": "osu",
      "status": "graveyard",
      "total_length": 0,
      "user_id": 5745865,
      "version": "",
      "accuracy": 0,
      "ar": 0,
      "bpm": 174,
      "convert": false,
      "count_circles": 0,
      "count_sliders": 0,
      "count_spinners": 0,
      "cs": 0,
      "deleted_at": "2020-02-27T12:19:54Z",
      "drain": 0,
      "hit_length": 0,
      "is_scoreable": false,
      "last_updated": "2020-02-27T12:11:14Z",
      "mode_int": 0,
      "passcount": 0,
      "playcount": 0,
      "ranked": -2,
      "url": "https://osu.ppy.sh/beatmaps/2331902",
      "checksum": null
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 5.36,
      "id": 2331905,
      "mode": "osu",
      "status": "ranked",
      "total_length": 122,
      "user_id": 7262798,
      "version": "LMT's Expert",
      "accuracy": 8.3,
      "ar": 9.2,
      "bpm": 174,
      "convert": false,
      "count_circles": 259,
      "count_sliders": 159,
      "count_spinners": 2,
      "cs": 4,
      "deleted_at": null,
      "drain": 5.5,
      "hit_length": 111,
      "is_scoreable": true,
      "last_updated": "2020-07-01T16:13:50Z",
      "mode_int": 0,
      "passcount": 4788,
      "playcount": 57087,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/2331905",
      "checksum": "77e84120080b46e1c50f0dc315d08a61"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 3.44,
      "id": 2331906,
      "mode": "osu",
      "status": "ranked",
      "total_length": 119,
      "user_id": 13646997,
      "version": "Mirai x Altai's Hard",
      "accuracy": 7,
      "ar": 8,
      "bpm": 174,
      "convert": false,
      "count_circles": 98,
      "count_sliders": 152,
      "count_spinners": 0,
      "cs": 3.5,
      "deleted_at": null,
      "drain": 4.5,
      "hit_length": 108,
      "is_scoreable": true,
      "last_updated": "2020-07-01T16:13:51Z",
      "mode_int": 0,
      "passcount": 32832,
      "playcount": 82494,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/2331906",
      "checksum": "2251df6c56f307cd7a61cda3cb9fb613"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 0,
      "id": 2413430,
      "mode": "osu",
      "status": "graveyard",
      "total_length": 0,
      "user_id": 5745865,
      "version": "",
      "accuracy": 0,
      "ar": 0,
      "bpm": 174,
      "convert": false,
      "count_circles": 0,
      "count_sliders": 0,
      "count_spinners": 0,
      "cs": 0,
      "deleted_at": "2020-04-25T15:25:44Z",
      "drain": 0,
      "hit_length": 0,
      "is_scoreable": false,
      "last_updated": "2020-04-25T15:13:02Z",
      "mode_int": 0,
      "passcount": 0,
      "playcount": 0,
      "ranked": -2,
      "url": "https://osu.ppy.sh/beatmaps/2413430",
      "checksum": null
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 4.75,
      "id": 2413431,
      "mode": "osu",
      "status": "graveyard",
      "total_length": 119,
      "user_id": 5745865,
      "version": "kiry's Insane",
      "accuracy": 7.5,
      "ar": 9,
      "bpm": 174,
      "convert": false,
      "count_circles": 227,
      "count_sliders": 107,
      "count_spinners": 1,
      "cs": 4,
      "deleted_at": "2020-04-25T16:36:50Z",
      "drain": 5,
      "hit_length": 102,
      "is_scoreable": false,
      "last_updated": "2020-04-25T15:26:57Z",
      "mode_int": 0,
      "passcount": 0,
      "playcount": 0,
      "ranked": -2,
      "url": "https://osu.ppy.sh/beatmaps/2413431",
      "checksum": "d09cf35a7f2d3676fd3a7e73b78f4a48"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 0,
      "id": 2413444,
      "mode": "osu",
      "status": "graveyard",
      "total_length": 0,
      "user_id": 5745865,
      "version": "",
      "accuracy": 0,
      "ar": 0,
      "bpm": 174,
      "convert": false,
      "count_circles": 0,
      "count_sliders": 0,
      "count_spinners": 0,
      "cs": 0,
      "deleted_at": "2020-04-25T15:26:44Z",
      "drain": 0,
      "hit_length": 0,
      "is_scoreable": false,
      "last_updated": "2020-04-25T15:25:44Z",
      "mode_int": 0,
      "passcount": 0,
      "playcount": 0,
      "ranked": -2,
      "url": "https://osu.ppy.sh/beatmaps/2413444",
      "checksum": null
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 0,
      "id": 2413551,
      "mode": "osu",
      "status": "graveyard",
      "total_length": 0,
      "user_id": 5745865,
      "version": "",
      "accuracy": 0,
      "ar": 0,
      "bpm": 174,
      "convert": false,
      "count_circles": 0,
      "count_sliders": 0,
      "count_spinners": 0,
      "cs": 0,
      "deleted_at": "2020-04-25T16:38:00Z",
      "drain": 0,
      "hit_length": 0,
      "is_scoreable": false,
      "last_updated": "2020-04-25T16:36:16Z",
      "mode_int": 0,
      "passcount": 0,
      "playcount": 0,
      "ranked": -2,
      "url": "https://osu.ppy.sh/beatmaps/2413551",
      "checksum": null
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 4.94,
      "id": 2413552,
      "mode": "osu",
      "status": "ranked",
      "total_length": 119,
      "user_id": 7228554,
      "version": "kiry's Insane",
      "accuracy": 7.5,
      "ar": 9,
      "bpm": 174,
      "convert": false,
      "count_circles": 227,
      "count_sliders": 107,
      "count_spinners": 1,
      "cs": 4,
      "deleted_at": null,
      "drain": 5,
      "hit_length": 103,
      "is_scoreable": true,
      "last_updated": "2020-07-01T16:13:52Z",
      "mode_int": 0,
      "passcount": 14616,
      "playcount": 84951,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/2413552",
      "checksum": "8cc12c76cab0de0c047dcebe56c326a1"
    },
    {
      "beatmapset_id": 1112303,
      "difficulty_rating": 5.33,
      "id": 2448363,
      "mode": "osu",
      "status": "ranked",
      "total_length": 119,
      "user_id": 6115007,
      "version": "Ksardas' Extra",
      "accuracy": 8.5,
      "ar": 9.3,
      "bpm": 174,
      "convert": false,
      "count_circles": 132,
      "count_sliders": 239,
      "count_spinners": 2,
      "cs": 4,
      "deleted_at": null,
      "drain": 5,
      "hit_length": 108,
      "is_scoreable": true,
      "last_updated": "2020-07-01T16:13:52Z",
      "mode_int": 0,
      "passcount": 4059,
      "playcount": 28431,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/2448363",
      "checksum": "f01a877b0f4f1bb198093a2b7dfa40ed"
    }
  ],
  "current_user_attributes": {
    "can_beatmap_update_owner": false,
    "can_delete": false,
    "can_edit_metadata": false,
    "can_edit_offset": false,
    "can_edit_tags": false,
    "can_hype": false,
    "can_hype_reason": "Must be signed in to hype.",
    "can_love": false,
    "can_remove_from_loved": false,
    "is_watching": false,
    "new_hype_time": null,
    "nomination_modes": null,
    "remaining_hype": 0
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
          "beatmapset_discussion_id": 1406140,
          "created_at": "2020-02-19T21:13:09+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 3955267,
          "last_editor_id": null,
          "message": "<3",
          "system": false,
          "updated_at": "2020-02-19T21:13:09+00:00",
          "user_id": 2204515
        }
      ],
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
          "beatmapset_discussion_id": 1406430,
          "created_at": "2020-02-20T01:11:30+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 3955914,
          "last_editor_id": null,
          "message": "Hype",
          "system": false,
          "updated_at": "2020-02-20T01:11:30+00:00",
          "user_id": 6842421
        }
      ],
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
          "beatmapset_discussion_id": 1406431,
          "created_at": "2020-02-20T01:12:12+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 3955915,
          "last_editor_id": null,
          "message": "i gucci",
          "system": false,
          "updated_at": "2020-02-20T01:12:12+00:00",
          "user_id": 7458583
        }
      ],
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
          "beatmapset_discussion_id": 1407831,
          "created_at": "2020-02-20T22:48:27+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 3960191,
          "last_editor_id": null,
          "message": "cool",
          "system": false,
          "updated_at": "2020-02-20T22:48:27+00:00",
          "user_id": 6115007
        }
      ],
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
          "beatmapset_discussion_id": 1410732,
          "created_at": "2020-02-22T14:17:02+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 3968755,
          "last_editor_id": null,
          "message": "🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊🦊",
          "system": false,
          "updated_at": "2020-02-22T14:17:02+00:00",
          "user_id": 11310911
        }
      ],
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
          "beatmapset_discussion_id": 1421639,
          "created_at": "2020-02-28T21:49:50+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000497,
          "last_editor_id": null,
          "message": "01:36:233 (4,1) - wouldn't say this is the best idea in a hard, especially since something like this hasn't been introduced before. try https://i.imgur.com/cQ1undP.png to make it easier to read",
          "system": false,
          "updated_at": "2020-02-28T21:49:50+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421639,
          "created_at": "2020-02-28T22:38:55+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000615,
          "last_editor_id": null,
          "message": "agree",
          "system": false,
          "updated_at": "2020-02-28T22:38:55+00:00",
          "user_id": 13646997
        },
        {
          "beatmapset_discussion_id": 1421639,
          "created_at": "2020-04-25T14:55:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340491,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T14:55:33+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421639,
          "created_at": "2020-04-25T14:55:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340492,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:55:33+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421645,
          "created_at": "2020-02-28T21:53:44+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000513,
          "last_editor_id": null,
          "message": "00:22:095 (1,2,3) - this might be confusing for newbs to read cos 3/2 gap and 3 being visually closer to 1.  try something like https://i.imgur.com/JOHA3Hh.png",
          "system": false,
          "updated_at": "2020-02-28T21:53:44+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421645,
          "created_at": "2020-04-25T14:58:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340507,
          "last_editor_id": null,
          "message": "sure",
          "system": false,
          "updated_at": "2020-04-25T14:58:03+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421645,
          "created_at": "2020-04-25T14:58:04+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340508,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:58:04+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421647,
          "created_at": "2020-02-28T21:55:19+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000518,
          "last_editor_id": null,
          "message": "01:20:026 (1,2) - i highly doubt that this is intentional",
          "system": false,
          "updated_at": "2020-02-28T21:55:19+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421647,
          "created_at": "2020-04-25T14:59:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340514,
          "last_editor_id": null,
          "message": "yea u right",
          "system": false,
          "updated_at": "2020-04-25T14:59:18+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421647,
          "created_at": "2020-04-25T14:59:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340515,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:59:18+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421651,
          "created_at": "2020-02-28T21:59:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000527,
          "last_editor_id": null,
          "message": "i'd recommend you to adjust your hitsounding in the section starting at 01:06:923 - cos here u start following the backgrounding instrument with normal whistles which sounds very off considering that you still follow the main instrument. an example would be 01:08:302 (5) - where it would make much more sense to have the whistle on the head to fit ur rhythm",
          "system": false,
          "updated_at": "2020-02-28T21:59:34+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421651,
          "created_at": "2020-02-28T22:54:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000645,
          "last_editor_id": null,
          "message": "also applies to hard",
          "system": false,
          "updated_at": "2020-02-28T22:54:52+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421651,
          "created_at": "2020-04-25T15:01:25+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340521,
          "last_editor_id": null,
          "message": "the hsing is following it to compensate for the fact that I can't follow both without the rhythm being too dense, although I do understand ur point. I'll look into it if more ppl think it's an issue but I think it's not too big of a deal for now",
          "system": false,
          "updated_at": "2020-04-25T15:01:25+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421651,
          "created_at": "2020-04-25T15:01:25+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340522,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T15:01:25+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421653,
          "created_at": "2020-02-28T22:01:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000529,
          "last_editor_id": null,
          "message": "00:24:681 (6) - just a tiny suggestion but u could use the red anchor to bump the sound at 00:25:371 -",
          "system": false,
          "updated_at": "2020-02-28T22:01:05+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421653,
          "created_at": "2020-04-25T14:58:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340512,
          "last_editor_id": null,
          "message": "sure",
          "system": false,
          "updated_at": "2020-04-25T14:58:56+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421653,
          "created_at": "2020-04-25T14:58:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340513,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:58:56+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421656,
          "created_at": "2020-02-28T22:02:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000532,
          "last_editor_id": null,
          "message": "00:30:457 (1) - silence the end pls",
          "system": false,
          "updated_at": "2020-02-28T22:02:57+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421656,
          "created_at": "2020-03-06T22:26:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4035019,
          "last_editor_id": null,
          "message": "actually i'd end this 1/4 later and remove the circle cos it makes 00:32:612 (1,1,1) - much easier to play and there's not really a significant thing on 00:32:440 (1) - imo",
          "system": false,
          "updated_at": "2020-03-06T22:26:17+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421656,
          "created_at": "2020-04-25T14:36:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340368,
          "last_editor_id": null,
          "message": "yea u right",
          "system": false,
          "updated_at": "2020-04-25T14:36:34+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421656,
          "created_at": "2020-04-25T14:36:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340369,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:36:34+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421657,
          "created_at": "2020-02-28T22:04:02+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000533,
          "last_editor_id": null,
          "message": "00:38:992 (3) - minor but put this into the triangle centre to make it look extra cute",
          "system": false,
          "updated_at": "2020-02-28T22:04:02+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421657,
          "created_at": "2020-04-25T14:37:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340372,
          "last_editor_id": null,
          "message": "was meant to be like that, should be better now",
          "system": false,
          "updated_at": "2020-04-25T14:37:03+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421657,
          "created_at": "2020-04-25T14:37:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340373,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:37:03+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421661,
          "created_at": "2020-02-28T22:04:53+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000539,
          "last_editor_id": null,
          "message": "00:44:164 (1) - finish on head, this has the same cymbal sound as 00:33:129 (1) -",
          "system": false,
          "updated_at": "2020-02-28T22:04:53+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421661,
          "created_at": "2020-02-28T22:05:07+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000540,
          "last_editor_id": null,
          "message": "applies for copied hitsounding too btw",
          "system": false,
          "updated_at": "2020-02-28T22:05:07+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421661,
          "created_at": "2020-02-28T22:06:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000542,
          "last_editor_id": null,
          "message": "01:02:267 (2) - normal whistle on head",
          "system": false,
          "updated_at": "2020-02-28T22:06:18+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421661,
          "created_at": "2020-04-25T14:37:53+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340387,
          "last_editor_id": null,
          "message": "aaa ok",
          "system": false,
          "updated_at": "2020-04-25T14:37:53+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421661,
          "created_at": "2020-04-25T14:37:53+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340388,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:37:53+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421664,
          "created_at": "2020-02-28T22:10:45+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000554,
          "last_editor_id": null,
          "message": "01:05:457 (2) - 01:16:492 (2) - 01:27:526 (2) - would recommend adding claps (or drum addition whistles) to these cos they are the strongest drum sound in the triple",
          "system": false,
          "updated_at": "2020-02-28T22:10:45+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421664,
          "created_at": "2020-04-25T14:48:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340458,
          "last_editor_id": null,
          "message": "fixed",
          "system": false,
          "updated_at": "2020-04-25T14:48:54+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421664,
          "created_at": "2020-04-25T14:48:55+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340459,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:48:55+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421667,
          "created_at": "2020-02-28T22:13:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000558,
          "last_editor_id": null,
          "message": "00:24:681 (1,2,3) - if u wanna make this super fancy put 2 right in the middle between 3's head and tail aaaand in the middle between 1's head and 3's head https://i.imgur.com/dhKHbdr.png",
          "system": false,
          "updated_at": "2020-02-28T22:13:05+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421667,
          "created_at": "2020-04-25T14:35:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340361,
          "last_editor_id": null,
          "message": "sure ig xD",
          "system": false,
          "updated_at": "2020-04-25T14:35:56+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421667,
          "created_at": "2020-04-25T14:35:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340362,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:35:56+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421670,
          "created_at": "2020-02-28T22:18:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000568,
          "last_editor_id": null,
          "message": "01:17:267 (1) - the first slider bump is early by enough that i was able to notice it while playing",
          "system": false,
          "updated_at": "2020-02-28T22:18:57+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421670,
          "created_at": "2020-04-25T16:26:38+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341095,
          "last_editor_id": null,
          "message": "not really sure what you mean here",
          "system": false,
          "updated_at": "2020-04-25T16:26:38+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1421670,
          "created_at": "2020-04-25T16:44:08+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341205,
          "last_editor_id": null,
          "message": "nah i just wanted a slider that looks slightly weird nothing to do with following the wubzy",
          "system": false,
          "updated_at": "2020-04-25T16:44:08+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1421670,
          "created_at": "2020-04-25T16:44:13+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341207,
          "last_editor_id": null,
          "message": "spoke to LMT cos I knew what u meant but yea no change",
          "system": false,
          "updated_at": "2020-04-25T16:44:13+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421670,
          "created_at": "2020-04-25T16:44:13+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341208,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T16:44:13+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421674,
          "created_at": "2020-02-28T22:20:12+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000572,
          "last_editor_id": null,
          "message": "01:26:061 (2) - 01:26:578 (6) - would use normal whistles on those to give contrast to the following two sounds",
          "system": false,
          "updated_at": "2020-02-28T22:20:12+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421674,
          "created_at": "2020-02-28T22:20:43+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000576,
          "last_editor_id": null,
          "message": "01:37:095 (2) - 01:37:612 (1) - ^",
          "system": false,
          "updated_at": "2020-02-28T22:20:43+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421674,
          "created_at": "2020-04-25T16:27:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341104,
          "last_editor_id": null,
          "message": "sure",
          "system": false,
          "updated_at": "2020-04-25T16:27:56+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1421674,
          "created_at": "2020-04-25T16:44:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341209,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T16:44:18+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421674,
          "created_at": "2020-04-25T16:44:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341210,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T16:44:18+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421678,
          "created_at": "2020-02-28T22:22:13+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000581,
          "last_editor_id": null,
          "message": "01:39:336 (1) - wouldn't make this part of the curve with the following notes cos 01:40:026 (2,3,4,5,6) - belong to their own group of 5. just move it so that it's separated and nc 01:40:026 (2) -",
          "system": false,
          "updated_at": "2020-02-28T22:22:13+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421678,
          "created_at": "2020-04-25T16:28:45+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341109,
          "last_editor_id": null,
          "message": "did something that would acheive that",
          "system": false,
          "updated_at": "2020-04-25T16:28:45+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1421678,
          "created_at": "2020-04-25T16:44:21+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341211,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T16:44:21+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421678,
          "created_at": "2020-04-25T16:44:21+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341212,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T16:44:21+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421681,
          "created_at": "2020-02-28T22:24:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000586,
          "last_editor_id": null,
          "message": "01:58:647 (1,2,1,2,1,2,1,2,1) - might be cool to decrease distance between these the further it goes to represent the fadeout https://i.imgur.com/uuBLopo.png (example also did some changes to the angles cos i thought it looked cool)",
          "system": false,
          "updated_at": "2020-02-28T22:24:33+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421681,
          "created_at": "2020-04-25T16:29:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341119,
          "last_editor_id": null,
          "message": "ye",
          "system": false,
          "updated_at": "2020-04-25T16:29:26+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1421681,
          "created_at": "2020-04-25T16:44:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341213,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T16:44:23+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421681,
          "created_at": "2020-04-25T16:44:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341214,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T16:44:23+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421689,
          "created_at": "2020-02-28T22:32:27+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000605,
          "last_editor_id": null,
          "message": "01:22:267 (1,2,3) - i kinda get where you are coming from but at this point the player expects these to be 1/4 so it feels pretty counter intuitive to play imo, would recommend to just do what u did for the others",
          "system": false,
          "updated_at": "2020-02-28T22:32:27+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421689,
          "created_at": "2020-03-16T17:49:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4087915,
          "last_editor_id": null,
          "message": "i did it because i wanted to make this pattern play different since it's new section but it won't work with 1/4 hihats part. aight, fixed to 1/4 kicksliders",
          "system": false,
          "updated_at": "2020-03-16T17:49:17+00:00",
          "user_id": 7458583
        },
        {
          "beatmapset_discussion_id": 1421689,
          "created_at": "2020-04-25T14:55:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340482,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T14:55:18+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421689,
          "created_at": "2020-04-25T14:55:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340483,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:55:18+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421692,
          "created_at": "2020-02-28T22:34:20+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000608,
          "last_editor_id": null,
          "message": "00:43:819 (2,3,4) - i don't really see the sense in spacing 3 and 4 so far away from 2 as the drum sounds on 2's tail and 3 are basically the same. i'd rather use this as a nice introduction for spaced 1/4 and lower the spacing",
          "system": false,
          "updated_at": "2020-02-28T22:34:20+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421692,
          "created_at": "2020-03-16T17:39:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4087881,
          "last_editor_id": 7458583,
          "message": "dunno, it plays very comfortable but stacked, ok",
          "system": false,
          "updated_at": "2020-03-16T17:42:39+00:00",
          "user_id": 7458583
        },
        {
          "beatmapset_discussion_id": 1421692,
          "created_at": "2020-04-25T14:55:14+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340478,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T14:55:14+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421692,
          "created_at": "2020-04-25T14:55:15+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340479,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:55:15+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421695,
          "created_at": "2020-02-28T22:36:38+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000611,
          "last_editor_id": null,
          "message": "01:27:267 (2,3,4,5) - would be cool if u stayed consistent here and mapped 01:27:267 (2) - as a repeat and a jump to 01:27:526 (4,5) -",
          "system": false,
          "updated_at": "2020-02-28T22:36:38+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421695,
          "created_at": "2020-03-16T17:50:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4087920,
          "last_editor_id": null,
          "message": "ok",
          "system": false,
          "updated_at": "2020-03-16T17:50:32+00:00",
          "user_id": 7458583
        },
        {
          "beatmapset_discussion_id": 1421695,
          "created_at": "2020-04-25T14:55:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340485,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T14:55:23+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421695,
          "created_at": "2020-04-25T14:55:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340486,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:55:23+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421696,
          "created_at": "2020-02-28T22:37:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000613,
          "last_editor_id": null,
          "message": "01:05:198 (1,2,3) - this is a pretty large difficulty spike when playing imo as this is a setup that hasn't been introduced like this before, i'd suggest to lower the spacing to the double (also considering that the following two instances of this in the song are mapped easier)",
          "system": false,
          "updated_at": "2020-02-28T22:37:54+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421696,
          "created_at": "2020-03-16T17:42:16+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4087893,
          "last_editor_id": 7458583,
          "message": "aight\n01:16:492 (2,3) - here as well",
          "system": false,
          "updated_at": "2020-03-16T17:44:42+00:00",
          "user_id": 7458583
        },
        {
          "beatmapset_discussion_id": 1421696,
          "created_at": "2020-04-25T14:55:16+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340480,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T14:55:16+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421696,
          "created_at": "2020-04-25T14:55:16+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340481,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:55:16+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421701,
          "created_at": "2020-02-28T22:40:38+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000620,
          "last_editor_id": null,
          "message": "00:31:492 (1) - silence",
          "system": false,
          "updated_at": "2020-02-28T22:40:38+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421701,
          "created_at": "2020-06-15T11:03:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4648332,
          "last_editor_id": null,
          "message": "i guess=",
          "system": false,
          "updated_at": "2020-06-15T11:03:57+00:00",
          "user_id": 5410645
        },
        {
          "beatmapset_discussion_id": 1421701,
          "created_at": "2020-06-16T14:44:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654521,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-16T14:44:32+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421701,
          "created_at": "2020-06-16T14:44:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654522,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:44:32+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421707,
          "created_at": "2020-02-28T22:42:49+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000627,
          "last_editor_id": null,
          "message": "01:06:233 - this section does not work with copied hitsounding cos u didn't follow the layer that was hitsounded on the top diff which can clearely be heard on objects like 01:06:751 (3) - where the normal whistle on the top diff is on the white tick but here it should be on the head. just go through the section and hitsound it to the main instrument",
          "system": false,
          "updated_at": "2020-02-28T22:42:49+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421707,
          "created_at": "2020-06-15T11:03:19+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4648331,
          "last_editor_id": null,
          "message": "did",
          "system": false,
          "updated_at": "2020-06-15T11:03:19+00:00",
          "user_id": 5410645
        },
        {
          "beatmapset_discussion_id": 1421707,
          "created_at": "2020-06-16T14:44:42+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654527,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-16T14:44:42+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421707,
          "created_at": "2020-06-16T14:44:42+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654528,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:44:42+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421708,
          "created_at": "2020-02-28T22:44:35+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000629,
          "last_editor_id": null,
          "message": "01:44:854 (2) - nc cos new group and slow ass follow points",
          "system": false,
          "updated_at": "2020-02-28T22:44:35+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421708,
          "created_at": "2020-06-15T11:05:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4648342,
          "last_editor_id": null,
          "message": "o",
          "system": false,
          "updated_at": "2020-06-15T11:05:24+00:00",
          "user_id": 5410645
        },
        {
          "beatmapset_discussion_id": 1421708,
          "created_at": "2020-06-16T14:44:38+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654525,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-16T14:44:38+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421708,
          "created_at": "2020-06-16T14:44:38+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654526,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:44:38+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421710,
          "created_at": "2020-02-28T22:44:51+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000631,
          "last_editor_id": null,
          "message": "01:40:026 (1) - bruh",
          "system": false,
          "updated_at": "2020-02-28T22:44:51+00:00",
          "user_id": 2204515
        }
      ],
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
          "beatmapset_discussion_id": 1421711,
          "created_at": "2020-02-28T22:46:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000636,
          "last_editor_id": null,
          "message": "might be nice to vary hp drain on the 5 highest diffs a little, currently they all have 5",
          "system": false,
          "updated_at": "2020-02-28T22:46:24+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421711,
          "created_at": "2020-04-25T15:01:58+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340525,
          "last_editor_id": null,
          "message": "I've made mine 6, will let the other's decide",
          "system": false,
          "updated_at": "2020-04-25T15:01:58+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421711,
          "created_at": "2020-04-25T16:29:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4341122,
          "last_editor_id": null,
          "message": "did 5.5",
          "system": false,
          "updated_at": "2020-04-25T16:29:47+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1421711,
          "created_at": "2020-05-12T12:54:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4445553,
          "last_editor_id": null,
          "message": "Altai please change mine on 5.2 thanks",
          "system": false,
          "updated_at": "2020-05-12T12:54:23+00:00",
          "user_id": 7458583
        },
        {
          "beatmapset_discussion_id": 1421711,
          "created_at": "2020-06-16T14:35:30+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654427,
          "last_editor_id": null,
          "message": "yeet",
          "system": false,
          "updated_at": "2020-06-16T14:35:30+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421711,
          "created_at": "2020-06-16T14:35:30+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654428,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:35:30+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421718,
          "created_at": "2020-02-28T22:52:59+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000643,
          "last_editor_id": null,
          "message": "01:51:061 (1) - as much as i'm an edgy boi, i'd make this a little clearer. overlapping the tail with the body like this is pretty hard to read if you don't have slider end circles + the overlap with its own tail makes it even harder and shapes like this haven't been introduced in the map anywhere else before",
          "system": false,
          "updated_at": "2020-02-28T22:52:59+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421718,
          "created_at": "2020-04-25T15:08:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340554,
          "last_editor_id": null,
          "message": "pulled it out a little, hopefully shud be clearer now",
          "system": false,
          "updated_at": "2020-04-25T15:08:23+00:00",
          "user_id": 7228554
        },
        {
          "beatmapset_discussion_id": 1421718,
          "created_at": "2020-04-25T15:12:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340600,
          "last_editor_id": null,
          "message": "pog",
          "system": false,
          "updated_at": "2020-04-25T15:12:32+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421718,
          "created_at": "2020-04-25T15:12:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340601,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T15:12:32+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421724,
          "created_at": "2020-02-28T22:59:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000650,
          "last_editor_id": null,
          "message": "01:15:888 (1,2,3,4,5,1,2,3) - not sure what to think about this cos it's definitely one of the hardest patterns of the map (harder than the buildup and rest of the chorus). could nerf it a little by making 01:16:061 (2) - a 1/2 slider to follow the synth",
          "system": false,
          "updated_at": "2020-02-28T22:59:54+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421724,
          "created_at": "2020-04-25T14:57:07+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340502,
          "last_editor_id": null,
          "message": "agree",
          "system": false,
          "updated_at": "2020-04-25T14:57:07+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421724,
          "created_at": "2020-04-25T14:57:07+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340503,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:57:07+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1421728,
          "created_at": "2020-02-28T23:03:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000657,
          "last_editor_id": null,
          "message": "00:38:819 (1,2,3,4,1,2,3,4) - this feels a little dense and lacking in rhythmical contrast to the build up later on imo. you could replace 00:39:681 (4) - with a circle to break the chain up a little",
          "system": false,
          "updated_at": "2020-02-28T23:03:24+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1421728,
          "created_at": "2020-02-29T00:13:06+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4000867,
          "last_editor_id": null,
          "message": "fixed the parts",
          "system": false,
          "updated_at": "2020-02-29T00:13:06+00:00",
          "user_id": 13646997
        },
        {
          "beatmapset_discussion_id": 1421728,
          "created_at": "2020-04-25T14:55:30+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340489,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-04-25T14:55:30+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1421728,
          "created_at": "2020-04-25T14:55:30+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4340490,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-04-25T14:55:30+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1422416,
          "created_at": "2020-02-29T09:50:38+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4002727,
          "last_editor_id": null,
          "message": "хавкинз трахнул и улетел в оффлайн",
          "system": false,
          "updated_at": "2020-02-29T09:50:38+00:00",
          "user_id": 11174970
        }
      ],
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
          "beatmapset_discussion_id": 1427451,
          "created_at": "2020-03-03T03:07:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4016272,
          "last_editor_id": null,
          "message": "meep",
          "system": false,
          "updated_at": "2020-03-03T03:07:03+00:00",
          "user_id": 13646997
        }
      ],
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
          "beatmapset_discussion_id": 1564263,
          "created_at": "2020-05-06T06:57:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4406759,
          "last_editor_id": null,
          "message": "01:06:923 (3) - Shouldn't this be 1/2 shorter",
          "system": false,
          "updated_at": "2020-05-06T06:57:52+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564263,
          "created_at": "2020-06-16T14:41:31+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654478,
          "last_editor_id": null,
          "message": "was meant to follow the backing sounds like top diff but yea clap is stronger so will shorten this",
          "system": false,
          "updated_at": "2020-06-16T14:41:31+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1564263,
          "created_at": "2020-06-16T14:41:31+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654479,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:41:31+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1564264,
          "created_at": "2020-05-06T06:59:46+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4406762,
          "last_editor_id": null,
          "message": "00:41:405 (1) - This shape might be unclear to beginners I recommend changing it",
          "system": false,
          "updated_at": "2020-05-06T06:59:46+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564264,
          "created_at": "2020-05-06T07:00:36+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4406765,
          "last_editor_id": null,
          "message": "01:58:647 (1) - also you could use spinner here or long slider without reverses here just like top difficulty don't see why you would use sliders with so many reverses here",
          "system": false,
          "updated_at": "2020-05-06T07:00:36+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564264,
          "created_at": "2020-06-16T14:43:04+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654502,
          "last_editor_id": null,
          "message": "As for the first one I agree, that has been changed.\nFor the second, I like the echoing effect and it's not really unrankable since the reverses are further than 1/1",
          "system": false,
          "updated_at": "2020-06-16T14:43:04+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1564264,
          "created_at": "2020-06-16T14:43:04+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654503,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:43:04+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1564266,
          "created_at": "2020-05-06T07:01:21+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4406767,
          "last_editor_id": null,
          "message": "HP at least 3 please 2 is more for easy",
          "system": false,
          "updated_at": "2020-05-06T07:01:21+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564266,
          "created_at": "2020-06-16T14:40:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654465,
          "last_editor_id": null,
          "message": "sure thing chicken wing",
          "system": false,
          "updated_at": "2020-06-16T14:40:33+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1564266,
          "created_at": "2020-06-16T14:40:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654466,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:40:33+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1564275,
          "created_at": "2020-05-06T07:12:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4406838,
          "last_editor_id": 8623835,
          "message": "Hitsounds volumes are really low to me on most parts like for example 00:32:612 - those claps are inaudible I recommend increasing overall volume",
          "system": false,
          "updated_at": "2020-05-06T07:12:36+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564275,
          "created_at": "2020-06-16T14:39:51+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654460,
          "last_editor_id": null,
          "message": "buffed a little but don't want it too loud cos it kicks in later",
          "system": false,
          "updated_at": "2020-06-16T14:39:51+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1564275,
          "created_at": "2020-06-16T14:39:51+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654461,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:39:51+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1564293,
          "created_at": "2020-05-06T07:23:36+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4406883,
          "last_editor_id": null,
          "message": "00:19:336 (3) - Could make it longer by 1/2 for vocals",
          "system": false,
          "updated_at": "2020-05-06T07:23:36+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564293,
          "created_at": "2020-06-16T15:13:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654632,
          "last_editor_id": null,
          "message": "sure",
          "system": false,
          "updated_at": "2020-06-16T15:13:05+00:00",
          "user_id": 7228554
        },
        {
          "beatmapset_discussion_id": 1564293,
          "created_at": "2020-06-16T19:54:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4656002,
          "last_editor_id": null,
          "message": "yeet",
          "system": false,
          "updated_at": "2020-06-16T19:54:54+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1564293,
          "created_at": "2020-06-16T19:54:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4656003,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T19:54:54+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1564303,
          "created_at": "2020-05-06T07:27:50+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4406923,
          "last_editor_id": null,
          "message": "01:06:923 - shouldn't this normal whistle be on 01:06:750 ? it's noticeable on some diffs that's it's missing",
          "system": false,
          "updated_at": "2020-05-06T07:27:50+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564303,
          "created_at": "2020-06-16T14:36:31+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654432,
          "last_editor_id": null,
          "message": "it's following the backing part that comes in for that section, was done for top diff, if it's a problem in other diffs lmk but for now I think it's fine",
          "system": false,
          "updated_at": "2020-06-16T14:36:31+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1564303,
          "created_at": "2020-06-16T14:36:31+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654433,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:36:31+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1564314,
          "created_at": "2020-05-06T07:35:39+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4406963,
          "last_editor_id": null,
          "message": "01:16:060 (2) - Offscreen on 4:3 ratio",
          "system": false,
          "updated_at": "2020-05-06T07:35:39+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564314,
          "created_at": "2020-06-15T11:05:11+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4648340,
          "last_editor_id": null,
          "message": "not anymore i hope",
          "system": false,
          "updated_at": "2020-06-15T11:05:11+00:00",
          "user_id": 5410645
        },
        {
          "beatmapset_discussion_id": 1564314,
          "created_at": "2020-06-16T14:44:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654523,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-16T14:44:34+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1564314,
          "created_at": "2020-06-16T14:44:35+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654524,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:44:35+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1564650,
          "created_at": "2020-05-06T12:03:49+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4407947,
          "last_editor_id": null,
          "message": "Ah ya do +15 or +20 to timing since audio compatibility off now",
          "system": false,
          "updated_at": "2020-05-06T12:03:49+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1564650,
          "created_at": "2020-05-19T10:15:48+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4493501,
          "last_editor_id": null,
          "message": "https://www.youtube.com/watch?v=-1qju6V1jLM (doesn't need fixing anymore cos revert yay)",
          "system": false,
          "updated_at": "2020-05-19T10:15:48+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1564650,
          "created_at": "2020-05-19T10:15:48+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4493502,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-05-19T10:15:48+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1594049,
          "created_at": "2020-05-18T19:14:08+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4489895,
          "last_editor_id": null,
          "message": "poooooog",
          "system": false,
          "updated_at": "2020-05-18T19:14:08+00:00",
          "user_id": 12123512
        }
      ],
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
          "beatmapset_discussion_id": 1594251,
          "created_at": "2020-05-18T21:20:04+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4490448,
          "last_editor_id": null,
          "message": "mwah",
          "system": false,
          "updated_at": "2020-05-18T21:20:04+00:00",
          "user_id": 10526814
        }
      ],
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
          "beatmapset_discussion_id": 1596429,
          "created_at": "2020-05-19T21:55:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4497147,
          "last_editor_id": null,
          "message": "01:03:388 (1) - Oops I've found the overmapping.",
          "system": false,
          "updated_at": "2020-05-19T21:55:05+00:00",
          "user_id": 2384296
        },
        {
          "beatmapset_discussion_id": 1596429,
          "created_at": "2020-05-19T21:57:35+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4497164,
          "last_editor_id": null,
          "message": "monkas",
          "system": false,
          "updated_at": "2020-05-19T21:57:35+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1596429,
          "created_at": "2020-06-16T14:51:50+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654575,
          "last_editor_id": null,
          "message": "thats fine actualy",
          "system": false,
          "updated_at": "2020-06-16T14:51:50+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1596429,
          "created_at": "2020-06-16T14:52:28+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654580,
          "last_editor_id": null,
          "message": "YEET",
          "system": false,
          "updated_at": "2020-06-16T14:52:28+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1596429,
          "created_at": "2020-06-16T14:52:28+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4654581,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-16T14:52:28+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1598749,
          "created_at": "2020-05-20T19:29:12+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4503348,
          "last_editor_id": null,
          "message": "Лисиный хайп",
          "system": false,
          "updated_at": "2020-05-20T19:29:12+00:00",
          "user_id": 8346108
        }
      ],
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
          "beatmapset_discussion_id": 1677762,
          "created_at": "2020-06-26T10:32:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4713355,
          "last_editor_id": null,
          "message": "00:53:817 - 00:53:645 - Circles unsnapped",
          "system": false,
          "updated_at": "2020-06-26T10:32:24+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1677762,
          "created_at": "2020-06-27T13:26:55+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4720414,
          "last_editor_id": null,
          "message": "mr ksardas how dare u",
          "system": false,
          "updated_at": "2020-06-27T13:26:55+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1677762,
          "created_at": "2020-06-27T13:26:55+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4720415,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-27T13:26:55+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1680027,
          "created_at": "2020-06-27T10:45:50+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4719762,
          "last_editor_id": 8623835,
          "message": "01:07:958 - 01:08:474 - 01:13:992 - normal whistle shouldn't be here but on 01:07:785 - 01:08:302 - 01:13:820",
          "system": false,
          "updated_at": "2020-06-27T10:50:40+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1680027,
          "created_at": "2020-06-27T13:10:50+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4720361,
          "last_editor_id": null,
          "message": "the problem is that here a new melody was introduced in the song for a moment so I decided to follow that, tho the later half is inconsistent so I'll see what I can do",
          "system": false,
          "updated_at": "2020-06-27T13:10:50+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1680027,
          "created_at": "2020-06-27T13:12:39+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4720369,
          "last_editor_id": 5745865,
          "message": "no I think ur right, I think it's best just to be consistent with the same as before since it's continuing, will change this\n\nI am not removing the hitwhistle on 01:07:957 since it sounds wrong to me\n\nAlso adding normal hitwhistles on:\n01:14:164\n01:08:647\n\nThis is with exception of Icekalt's diff since he already did his own whistling on this part",
          "system": false,
          "updated_at": "2020-06-27T13:23:44+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1680027,
          "created_at": "2020-06-27T13:26:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4720410,
          "last_editor_id": null,
          "message": "done",
          "system": false,
          "updated_at": "2020-06-27T13:26:26+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1680027,
          "created_at": "2020-06-27T13:26:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4720411,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-27T13:26:26+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1680039,
          "created_at": "2020-06-27T10:53:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4719788,
          "last_editor_id": 8623835,
          "message": "01:05:543 - 01:06:750 - normal addition and whistle if its missing",
          "system": false,
          "updated_at": "2020-06-27T10:55:45+00:00",
          "user_id": 8623835
        },
        {
          "beatmapset_discussion_id": 1680039,
          "created_at": "2020-06-27T13:27:37+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4720417,
          "last_editor_id": null,
          "message": "sure",
          "system": false,
          "updated_at": "2020-06-27T13:27:37+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1680039,
          "created_at": "2020-06-27T13:27:37+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4720418,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-27T13:27:37+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684574,
          "created_at": "2020-06-29T13:25:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731536,
          "last_editor_id": null,
          "message": "00:58:992 (3,4,5) - might wanna make this a little clearer so newbs don't go for the tail instead https://i.imgur.com/032OdZe.png",
          "system": false,
          "updated_at": "2020-06-29T13:25:57+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684574,
          "created_at": "2020-06-29T16:19:28+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732660,
          "last_editor_id": null,
          "message": "yea",
          "system": false,
          "updated_at": "2020-06-29T16:19:28+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684574,
          "created_at": "2020-06-29T16:19:28+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732661,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:19:28+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684580,
          "created_at": "2020-06-29T13:32:38+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731569,
          "last_editor_id": null,
          "message": "00:41:405 (5,6) - this spacing seems a little random to me cos u never do 1/2 like this so you might wanna make it a little clearer",
          "system": false,
          "updated_at": "2020-06-29T13:32:38+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684580,
          "created_at": "2020-06-29T16:16:42+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732644,
          "last_editor_id": null,
          "message": "yes",
          "system": false,
          "updated_at": "2020-06-29T16:16:42+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684580,
          "created_at": "2020-06-29T16:16:42+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732645,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:16:42+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684580,
          "created_at": "2020-06-29T16:16:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732648,
          "last_editor_id": null,
          "message": "as in I didn't make it clearer I just removed it",
          "system": false,
          "updated_at": "2020-06-29T16:16:57+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684591,
          "created_at": "2020-06-29T13:40:58+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731588,
          "last_editor_id": null,
          "message": "01:51:061 (1) - just a suggestion but it might be cool to have the direction change with the first red anchor on 01:51:578 - to emphasise the synth. https://osu.ppy.sh/ss/15146758/bb03",
          "system": false,
          "updated_at": "2020-06-29T13:40:58+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684591,
          "created_at": "2020-06-30T06:51:40+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4736566,
          "last_editor_id": null,
          "message": "sounds cool",
          "system": false,
          "updated_at": "2020-06-30T06:51:40+00:00",
          "user_id": 7228554
        },
        {
          "beatmapset_discussion_id": 1684591,
          "created_at": "2020-06-30T14:48:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4738504,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-30T14:48:56+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684591,
          "created_at": "2020-06-30T14:48:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4738505,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-30T14:48:56+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684609,
          "created_at": "2020-06-29T13:52:09+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731634,
          "last_editor_id": null,
          "message": "01:47:612 (1,2,1,2,1,2,1,2,1,2) - these should definitely have some hitsounding cos rn they are unhitsounded cos top diff doesn't have anything here (maybe also do some volume change stuff with them)",
          "system": false,
          "updated_at": "2020-06-29T13:52:09+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684609,
          "created_at": "2020-06-29T13:53:25+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731637,
          "last_editor_id": null,
          "message": "i'd also add some volume changes to 01:58:647 (1) -",
          "system": false,
          "updated_at": "2020-06-29T13:53:25+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684609,
          "created_at": "2020-06-29T16:23:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732695,
          "last_editor_id": null,
          "message": "sure",
          "system": false,
          "updated_at": "2020-06-29T16:23:47+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684609,
          "created_at": "2020-06-29T16:23:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732696,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:23:47+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684609,
          "created_at": "2020-06-29T16:23:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732697,
          "last_editor_id": null,
          "message": "fixed for icey",
          "system": false,
          "updated_at": "2020-06-29T16:23:54+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684609,
          "created_at": "2020-06-29T22:00:19+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734674,
          "last_editor_id": null,
          "message": "actually implemented this elsewhere on diffs that mapped the fading vocals cos it is cute",
          "system": false,
          "updated_at": "2020-06-29T22:00:19+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684614,
          "created_at": "2020-06-29T13:54:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731641,
          "last_editor_id": null,
          "message": "01:58:647 (1) - maybe decrease the volume for the repeats steadily",
          "system": false,
          "updated_at": "2020-06-29T13:54:03+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684614,
          "created_at": "2020-06-30T14:48:59+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4738506,
          "last_editor_id": null,
          "message": "yes",
          "system": false,
          "updated_at": "2020-06-30T14:48:59+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684614,
          "created_at": "2020-06-30T14:48:59+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4738507,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-30T14:48:59+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684638,
          "created_at": "2020-06-29T14:00:15+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731694,
          "last_editor_id": null,
          "message": "01:42:440 (1,2,1,2,1,2,1) - add some whistles here and there cos these currently have no hitsounding",
          "system": false,
          "updated_at": "2020-06-29T14:00:15+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684638,
          "created_at": "2020-06-29T16:22:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732686,
          "last_editor_id": null,
          "message": "done for frakture",
          "system": false,
          "updated_at": "2020-06-29T16:22:03+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684638,
          "created_at": "2020-06-29T16:22:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732687,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:22:03+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684659,
          "created_at": "2020-06-29T14:05:42+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731735,
          "last_editor_id": null,
          "message": "00:52:440 (1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,7) - full whistle spam sounds a bit eeeh, if you wanna keep them at least do like a volume build-up to represent the song better",
          "system": false,
          "updated_at": "2020-06-29T14:05:42+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684659,
          "created_at": "2020-06-29T20:07:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734177,
          "last_editor_id": null,
          "message": "i really do not like changing volumes on streams... did some magic on the kick hitsounds so they don't feel... as boring?",
          "system": false,
          "updated_at": "2020-06-29T20:07:23+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1684659,
          "created_at": "2020-06-29T21:52:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734616,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T21:52:47+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684659,
          "created_at": "2020-06-29T21:52:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734617,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T21:52:47+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684665,
          "created_at": "2020-06-29T14:07:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731750,
          "last_editor_id": null,
          "message": "01:08:877 (4,5) - hitsound the 1/6 please",
          "system": false,
          "updated_at": "2020-06-29T14:07:26+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684665,
          "created_at": "2020-06-29T20:07:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734180,
          "last_editor_id": null,
          "message": "yea",
          "system": false,
          "updated_at": "2020-06-29T20:07:47+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1684665,
          "created_at": "2020-06-29T21:52:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734618,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T21:52:52+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684665,
          "created_at": "2020-06-29T21:52:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734619,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T21:52:52+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684670,
          "created_at": "2020-06-29T14:08:48+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731757,
          "last_editor_id": null,
          "message": "unhitsounded triples make me big sad, there are so so many that just skip the middle note or even all of them that listing them isn't sensible. just go through the map and fix those rascals",
          "system": false,
          "updated_at": "2020-06-29T14:08:48+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684670,
          "created_at": "2020-06-29T20:14:53+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734220,
          "last_editor_id": null,
          "message": "i did them",
          "system": false,
          "updated_at": "2020-06-29T20:14:53+00:00",
          "user_id": 7262798
        },
        {
          "beatmapset_discussion_id": 1684670,
          "created_at": "2020-06-29T21:53:00+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734620,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T21:53:00+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684670,
          "created_at": "2020-06-29T21:53:00+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4734621,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T21:53:00+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684676,
          "created_at": "2020-06-29T14:10:06+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731768,
          "last_editor_id": null,
          "message": "you definitely don't want OD8 on this, go for OD7",
          "system": false,
          "updated_at": "2020-06-29T14:10:06+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684676,
          "created_at": "2020-06-29T16:17:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732651,
          "last_editor_id": null,
          "message": "any truers in chat",
          "system": false,
          "updated_at": "2020-06-29T16:17:34+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684676,
          "created_at": "2020-06-29T16:17:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732652,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:17:34+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684687,
          "created_at": "2020-06-29T14:17:55+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731803,
          "last_editor_id": null,
          "message": "i know it's a guest diff but i feel like the rest of the set is very cohesive and the combo colours are kinda... too bright imo so i'd like to ask you to change them to match the rest of the set",
          "system": false,
          "updated_at": "2020-06-29T14:17:55+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684687,
          "created_at": "2020-06-29T15:37:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732307,
          "last_editor_id": null,
          "message": "okk",
          "system": false,
          "updated_at": "2020-06-29T15:37:47+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1684687,
          "created_at": "2020-06-29T16:13:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732612,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T16:13:17+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684687,
          "created_at": "2020-06-29T16:13:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732613,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:13:17+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684690,
          "created_at": "2020-06-29T14:19:41+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731809,
          "last_editor_id": null,
          "message": "00:26:405 (1,1) - either put a soft whistle onto the second slider or silence the first one's tail (and possibly also the tick)",
          "system": false,
          "updated_at": "2020-06-29T14:19:41+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684690,
          "created_at": "2020-06-29T15:44:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732356,
          "last_editor_id": null,
          "message": "silence",
          "system": false,
          "updated_at": "2020-06-29T15:44:17+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1684690,
          "created_at": "2020-06-29T16:12:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732601,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T16:12:34+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684690,
          "created_at": "2020-06-29T16:12:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732602,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:12:34+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684695,
          "created_at": "2020-06-29T14:22:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731822,
          "last_editor_id": null,
          "message": "00:57:871 (1) - 01:03:388 (1) - 01:08:905 (1) - 01:14:423 (1) - (and others if i missed any) are 1/6 so mapping a 1/8 slider over them doesn't really make sense",
          "system": false,
          "updated_at": "2020-06-29T14:22:26+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684695,
          "created_at": "2020-06-29T15:49:58+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732386,
          "last_editor_id": null,
          "message": "are replacing that 1/8 sliders with 1/4 circles would be okk idk just askin",
          "system": false,
          "updated_at": "2020-06-29T15:49:58+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1684695,
          "created_at": "2020-06-29T18:17:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4733625,
          "last_editor_id": null,
          "message": "after talking cos it's 1/6, Ksardas decided to just remove these like in the top diff",
          "system": false,
          "updated_at": "2020-06-29T18:17:24+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684695,
          "created_at": "2020-06-29T18:17:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4733626,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T18:17:24+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684716,
          "created_at": "2020-06-29T14:28:12+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731863,
          "last_editor_id": null,
          "message": "I don't really get your comboing - I mean yeah it is mostly pattern based but still I think you can do with much less NC spamming in general. Especially in the beginning there are soooo many objects that are just single object combos which makes everything looks messy imo. Please go over the whole map and remove combos where they are not necessary for to separate or highlight specific patterns. (stuff like 00:32:612 (1,1,1) - is fine)",
          "system": false,
          "updated_at": "2020-06-29T14:28:12+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684716,
          "created_at": "2020-06-29T15:50:39+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732392,
          "last_editor_id": null,
          "message": "changed some",
          "system": false,
          "updated_at": "2020-06-29T15:50:39+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1684716,
          "created_at": "2020-06-29T16:13:14+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732610,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T16:13:14+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684716,
          "created_at": "2020-06-29T16:13:14+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732611,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:13:14+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684717,
          "created_at": "2020-06-29T14:29:27+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731866,
          "last_editor_id": null,
          "message": "00:26:061 (1,1) - would be cool if you could nerf this 1/4 as it feels kinda unnatural in the context of the calm section",
          "system": false,
          "updated_at": "2020-06-29T14:29:27+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684717,
          "created_at": "2020-06-29T15:35:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732287,
          "last_editor_id": null,
          "message": "nerfed",
          "system": false,
          "updated_at": "2020-06-29T15:35:47+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1684717,
          "created_at": "2020-06-29T16:12:30+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732599,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T16:12:30+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684717,
          "created_at": "2020-06-29T16:12:30+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732600,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:12:30+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684729,
          "created_at": "2020-06-29T14:33:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731886,
          "last_editor_id": null,
          "message": "as with some of the other lower experts the section starting at 01:40:026 - could take some more hitsounding as nothing got copied over cos the top diff is much less dense here",
          "system": false,
          "updated_at": "2020-06-29T14:33:56+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684729,
          "created_at": "2020-06-29T15:32:31+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732271,
          "last_editor_id": null,
          "message": "whistles",
          "system": false,
          "updated_at": "2020-06-29T15:32:31+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1684729,
          "created_at": "2020-06-29T16:13:21+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732615,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T16:13:21+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684729,
          "created_at": "2020-06-29T16:13:22+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732616,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:13:22+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684732,
          "created_at": "2020-06-29T14:37:19+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731896,
          "last_editor_id": null,
          "message": "01:16:406 (1,2,3) - i kno this i VERY minor but the ds difference here triggers my ocd",
          "system": false,
          "updated_at": "2020-06-29T14:37:19+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684732,
          "created_at": "2020-06-29T16:15:22+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732637,
          "last_editor_id": null,
          "message": "sure",
          "system": false,
          "updated_at": "2020-06-29T16:15:22+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684732,
          "created_at": "2020-06-29T16:15:22+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732638,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:15:22+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684740,
          "created_at": "2020-06-29T14:43:09+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731944,
          "last_editor_id": null,
          "message": "not an issue because it's a gd but would be cool to have the second kiai time as well for cohesion within the set",
          "system": false,
          "updated_at": "2020-06-29T14:43:09+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684740,
          "created_at": "2020-06-29T15:30:40+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732253,
          "last_editor_id": null,
          "message": "123",
          "system": false,
          "updated_at": "2020-06-29T15:30:40+00:00",
          "user_id": 6115007
        },
        {
          "beatmapset_discussion_id": 1684740,
          "created_at": "2020-06-29T16:13:27+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732617,
          "last_editor_id": null,
          "message": "h",
          "system": false,
          "updated_at": "2020-06-29T16:13:27+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684740,
          "created_at": "2020-06-29T16:13:27+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732618,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:13:27+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684744,
          "created_at": "2020-06-29T14:44:22+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731959,
          "last_editor_id": null,
          "message": "obligatory hitsound general hitsound mod:\n\n00:22:095 - put something like a soft whislte or finish here because a new section starts in the music and it's quite emphasised\n00:48:647 - clap\n01:02:267 - is this clap intentional?\n01:05:198 - clap\n01:12:612 - normal sampleset\n01:17:785 - drum sampleset or something similar",
          "system": false,
          "updated_at": "2020-06-29T14:44:22+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684744,
          "created_at": "2020-06-30T14:53:22+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4738530,
          "last_editor_id": null,
          "message": "00:22:095 - added soft finish\n00:48:647 - palc\n01:02:267 - no\n01:05:198 - palc\n01:12:612 - normal sampleset\n01:17:785 - I like the idea of a drum sampleset since it's softer than normal yes",
          "system": false,
          "updated_at": "2020-06-30T14:53:22+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684744,
          "created_at": "2020-06-30T14:53:22+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4738531,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-30T14:53:22+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684761,
          "created_at": "2020-06-29T14:50:31+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4731994,
          "last_editor_id": null,
          "message": "add drum and bass to tags, you currently only have dnb",
          "system": false,
          "updated_at": "2020-06-29T14:50:31+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684761,
          "created_at": "2020-06-30T14:50:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4738518,
          "last_editor_id": null,
          "message": "yes",
          "system": false,
          "updated_at": "2020-06-30T14:50:52+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684761,
          "created_at": "2020-06-30T14:50:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4738519,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-30T14:50:52+00:00",
          "user_id": 5745865
        }
      ],
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
          "beatmapset_discussion_id": 1684770,
          "created_at": "2020-06-29T14:52:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732017,
          "last_editor_id": null,
          "message": "01:31:405 (2,3) - ds here is a little large",
          "system": false,
          "updated_at": "2020-06-29T14:52:57+00:00",
          "user_id": 2204515
        },
        {
          "beatmapset_discussion_id": 1684770,
          "created_at": "2020-06-29T16:20:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732674,
          "last_editor_id": null,
          "message": "also a truers in chat moment",
          "system": false,
          "updated_at": "2020-06-29T16:20:18+00:00",
          "user_id": 5745865
        },
        {
          "beatmapset_discussion_id": 1684770,
          "created_at": "2020-06-29T16:20:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4732675,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2020-06-29T16:20:18+00:00",
          "user_id": 5745865
        }
      ],
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
      "id": 1691044,
      "beatmapset_id": 1112303,
      "beatmap_id": null,
      "user_id": 9126943,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2020-07-02T12:20:43+00:00",
      "updated_at": "2020-07-02T12:20:43+00:00",
      "deleted_at": null,
      "last_post_at": "2020-07-02T12:20:43+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 1691044,
          "created_at": "2020-07-02T12:20:43+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4749155,
          "last_editor_id": null,
          "message": "gbpf ппиздатая картонка хайпируем",
          "system": false,
          "updated_at": "2020-07-02T12:20:43+00:00",
          "user_id": 9126943
        }
      ],
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
      "id": 1691045,
      "beatmapset_id": 1112303,
      "beatmap_id": null,
      "user_id": 8360581,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2020-07-02T12:21:14+00:00",
      "updated_at": "2020-07-02T12:21:14+00:00",
      "deleted_at": null,
      "last_post_at": "2020-07-02T12:21:14+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 1691045,
          "created_at": "2020-07-02T12:21:14+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 4749156,
          "last_editor_id": null,
          "message": "WATAFA kSARDSA EXTRA \nand Frakturehawkens!",
          "system": false,
          "updated_at": "2020-07-02T12:21:14+00:00",
          "user_id": 8360581
        }
      ],
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
  "eligible_main_rulesets": [
    "osu"
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
    },
    {
      "id": 2135438,
      "type": "rank",
      "comment": null,
      "created_at": "2020-07-09T00:25:38+00:00",
      "user_id": null
    },
    {
      "id": 4175744,
      "type": "beatmap_owner_change",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "beatmap_id": 2413552,
        "beatmap_version": "kiry's Insane",
        "new_user_id": 7228554,
        "new_user_username": "Kirylln"
      },
      "created_at": "2022-07-10T03:46:25+00:00",
      "user_id": 2849992
    },
    {
      "id": 4474082,
      "type": "beatmap_owner_change",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "beatmap_id": 2331906,
        "beatmap_version": "Mirai x Altai's Hard",
        "new_user_id": 13646997,
        "new_user_username": "Le Mirai"
      },
      "created_at": "2022-11-13T06:25:44+00:00",
      "user_id": 2849992
    }
  ],
  "nominations": {
    "legacy_mode": true,
    "current": 2,
    "required_meta": {
      "main_ruleset": 2,
      "non_main_ruleset": 1
    }
  },
  "related_users": [
    {
      "avatar_url": "https://a.ppy.sh/2204515?1716210356.jpeg",
      "country_code": "DE",
      "default_group": "alumni",
      "id": 2204515,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": "#999999",
      "username": "Mao",
      "groups": [
        {
          "colour": "#999999",
          "has_listing": true,
          "has_playmodes": false,
          "id": 16,
          "identifier": "alumni",
          "is_probationary": false,
          "name": "osu! Alumni",
          "short_name": "ALM",
          "playmodes": null
        }
      ]
    },
    {
      "avatar_url": "https://a.ppy.sh/2384296?1609740826.jpeg",
      "country_code": "JP",
      "default_group": "default",
      "id": 2384296,
      "is_active": false,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-08-20T15:45:23+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "A s h e m u",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/2849992?1711987493.jpeg",
      "country_code": "CN",
      "default_group": "alumni",
      "id": 2849992,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": "#999999",
      "username": "Garden",
      "groups": [
        {
          "colour": "#999999",
          "has_listing": true,
          "has_playmodes": false,
          "id": 16,
          "identifier": "alumni",
          "is_probationary": false,
          "name": "osu! Alumni",
          "short_name": "ALM",
          "playmodes": null
        }
      ]
    },
    {
      "avatar_url": "https://a.ppy.sh/4966334?1651087793.jpeg",
      "country_code": "GB",
      "default_group": "default",
      "id": 4966334,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": "2024-10-21T11:31:06+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "DeviousPanda",
      "groups": [
        {
          "colour": "#76AEBC",
          "has_listing": true,
          "has_playmodes": true,
          "id": 48,
          "identifier": "bsc",
          "is_probationary": false,
          "name": "Beatmap Spotlight Curators",
          "short_name": "BSC",
          "playmodes": [
            "osu"
          ]
        }
      ]
    },
    {
      "avatar_url": "https://a.ppy.sh/5410645?1605999918.jpeg",
      "country_code": "DE",
      "default_group": "default",
      "id": 5410645,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-21T11:01:41+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Icekalt",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/5745865?1694117464.jpeg",
      "country_code": "GB",
      "default_group": "default",
      "id": 5745865,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-20T19:13:41+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Altai",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/6115007?1711829239.jpeg",
      "country_code": "RU",
      "default_group": "default",
      "id": 6115007,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-11T18:15:45+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Ksardas",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/6842421?1658912607.jpeg",
      "country_code": "RU",
      "default_group": "default",
      "id": 6842421,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "xbopost",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/7228554?1594625660.jpeg",
      "country_code": "VN",
      "default_group": "default",
      "id": 7228554,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
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
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": "2024-10-20T12:21:53+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "LMT",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/7458583?1719853319.jpeg",
      "country_code": "RU",
      "default_group": "default",
      "id": 7458583,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-21T09:55:01+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Frakturehawkens",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/8346108?1722591186.jpeg",
      "country_code": "RU",
      "default_group": "default",
      "id": 8346108,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-20T20:51:53+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Dudlik42",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/8360581?1679919055.jpeg",
      "country_code": "RU",
      "default_group": "default",
      "id": 8360581,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-17T16:37:29+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "nexx-",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/8623835?1714677360.jpeg",
      "country_code": "PL",
      "default_group": "default",
      "id": 8623835,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Peter",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/9126943?1725499305.jpeg",
      "country_code": "RU",
      "default_group": "default",
      "id": 9126943,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": "2024-10-21T02:41:28+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Twiggykun",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/10526814?1609346076.png",
      "country_code": "GB",
      "default_group": "default",
      "id": 10526814,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": "2024-10-21T10:47:31+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Luminiscental",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/11174970?1663146375.jpeg",
      "country_code": "RU",
      "default_group": "default",
      "id": 11174970,
      "is_active": false,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2022-12-31T14:26:22+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Miraui",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/11310911?1725158600.jpeg",
      "country_code": "US",
      "default_group": "default",
      "id": 11310911,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": "2024-10-21T02:03:43+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Your mom",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/12123512?1721728631.jpeg",
      "country_code": "US",
      "default_group": "default",
      "id": 12123512,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-21T00:40:52+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Tactix",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/13646997?1715810123.jpeg",
      "country_code": "DE",
      "default_group": "default",
      "id": 13646997,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Le Mirai",
      "groups": []
    }
  ]
}
"""

JSON2 = r"""
{
  "artist": "Hashimoto Miyuki",
  "artist_unicode": "橋本みゆき",
  "covers": {
    "cover": "https://assets.ppy.sh/beatmaps/2237577/covers/cover.jpg?1728484483",
    "cover@2x": "https://assets.ppy.sh/beatmaps/2237577/covers/cover@2x.jpg?1728484483",
    "card": "https://assets.ppy.sh/beatmaps/2237577/covers/card.jpg?1728484483",
    "card@2x": "https://assets.ppy.sh/beatmaps/2237577/covers/card@2x.jpg?1728484483",
    "list": "https://assets.ppy.sh/beatmaps/2237577/covers/list.jpg?1728484483",
    "list@2x": "https://assets.ppy.sh/beatmaps/2237577/covers/list@2x.jpg?1728484483",
    "slimcover": "https://assets.ppy.sh/beatmaps/2237577/covers/slimcover.jpg?1728484483",
    "slimcover@2x": "https://assets.ppy.sh/beatmaps/2237577/covers/slimcover@2x.jpg?1728484483"
  },
  "creator": "AJT",
  "favourite_count": 34,
  "hype": null,
  "id": 2237577,
  "nsfw": false,
  "offset": 0,
  "play_count": 12011,
  "preview_url": "//b.ppy.sh/preview/2237577.mp3",
  "source": "ましろ色シンフォニー -Love is pure white-",
  "spotlight": false,
  "status": "ranked",
  "title": "Symphonic Love (Game Ver.)",
  "title_unicode": "シンフォニック・ラブ (Game Ver.)",
  "track_id": null,
  "user_id": 3181083,
  "video": false,
  "bpm": 144,
  "can_be_hyped": false,
  "deleted_at": null,
  "discussion_enabled": true,
  "discussion_locked": false,
  "is_scoreable": true,
  "last_updated": "2024-10-09T14:34:26Z",
  "legacy_thread_url": "https://osu.ppy.sh/community/forums/topics/1967750",
  "nominations_summary": {
    "current": 2,
    "eligible_main_rulesets": [
      "osu"
    ],
    "required_meta": {
      "main_ruleset": 2,
      "non_main_ruleset": 1
    }
  },
  "ranked": 1,
  "ranked_date": "2024-10-17T00:05:31Z",
  "storyboard": false,
  "submitted_date": "2024-08-23T22:59:37Z",
  "tags": "mashiroiro symphony japanese pop jpop j-pop visual novel vn opening op video game version gorou wanpachi deppyforce chanmann sonnyc pata-mon shiritani",
  "availability": {
    "download_disabled": false,
    "more_information": null
  },
  "beatmaps": [
    {
      "beatmapset_id": 2237577,
      "difficulty_rating": 5.82,
      "id": 4754261,
      "mode": "osu",
      "status": "ranked",
      "total_length": 93,
      "user_id": 3181083,
      "version": "Extra",
      "accuracy": 9,
      "ar": 8,
      "bpm": 144,
      "convert": false,
      "count_circles": 405,
      "count_sliders": 76,
      "count_spinners": 2,
      "cs": 4,
      "deleted_at": null,
      "drain": 6,
      "hit_length": 92,
      "is_scoreable": true,
      "last_updated": "2024-10-09T14:34:27Z",
      "mode_int": 0,
      "passcount": 155,
      "playcount": 2341,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/4754261",
      "checksum": "ffc2d0df78030fed8f372a3d0cf44e6f"
    },
    {
      "beatmapset_id": 2237577,
      "difficulty_rating": 4.79,
      "id": 4756508,
      "mode": "osu",
      "status": "ranked",
      "total_length": 93,
      "user_id": 5286213,
      "version": "Deppy's Insane",
      "accuracy": 6,
      "ar": 6,
      "bpm": 144,
      "convert": false,
      "count_circles": 227,
      "count_sliders": 46,
      "count_spinners": 2,
      "cs": 6,
      "deleted_at": null,
      "drain": 6,
      "hit_length": 84,
      "is_scoreable": true,
      "last_updated": "2024-10-09T14:34:27Z",
      "mode_int": 0,
      "passcount": 140,
      "playcount": 976,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/4756508",
      "checksum": "e6f9c0d50a62ada8990e613eed0d9432"
    },
    {
      "beatmapset_id": 2237577,
      "difficulty_rating": 5.55,
      "id": 4758261,
      "mode": "osu",
      "status": "ranked",
      "total_length": 92,
      "user_id": 12157130,
      "version": "Gorou's Expert",
      "accuracy": 8.5,
      "ar": 8,
      "bpm": 144,
      "convert": false,
      "count_circles": 179,
      "count_sliders": 163,
      "count_spinners": 2,
      "cs": 5,
      "deleted_at": null,
      "drain": 7,
      "hit_length": 86,
      "is_scoreable": true,
      "last_updated": "2024-10-09T14:34:27Z",
      "mode_int": 0,
      "passcount": 83,
      "playcount": 760,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/4758261",
      "checksum": "58f174f42a44b45c5292c49719872713"
    },
    {
      "beatmapset_id": 2237577,
      "difficulty_rating": 2.29,
      "id": 4786678,
      "mode": "osu",
      "status": "ranked",
      "total_length": 92,
      "user_id": 3181083,
      "version": "Normal",
      "accuracy": 4.5,
      "ar": 5.5,
      "bpm": 144,
      "convert": false,
      "count_circles": 102,
      "count_sliders": 71,
      "count_spinners": 3,
      "cs": 3,
      "deleted_at": null,
      "drain": 3,
      "hit_length": 80,
      "is_scoreable": true,
      "last_updated": "2024-10-09T14:34:28Z",
      "mode_int": 0,
      "passcount": 499,
      "playcount": 1576,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/4786678",
      "checksum": "7bbf336f2f2832dd34e8ec77bb131cb6"
    },
    {
      "beatmapset_id": 2237577,
      "difficulty_rating": 3.63,
      "id": 4787106,
      "mode": "osu",
      "status": "ranked",
      "total_length": 92,
      "user_id": 3181083,
      "version": "Hard",
      "accuracy": 6,
      "ar": 7.5,
      "bpm": 144,
      "convert": false,
      "count_circles": 193,
      "count_sliders": 127,
      "count_spinners": 2,
      "cs": 3.5,
      "deleted_at": null,
      "drain": 4,
      "hit_length": 91,
      "is_scoreable": true,
      "last_updated": "2024-10-09T14:34:28Z",
      "mode_int": 0,
      "passcount": 380,
      "playcount": 1495,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/4787106",
      "checksum": "8ddf5819315b3de5e615b279b6aaec60"
    },
    {
      "beatmapset_id": 2237577,
      "difficulty_rating": 5.59,
      "id": 4790302,
      "mode": "osu",
      "status": "ranked",
      "total_length": 93,
      "user_id": 11771,
      "version": "Sonnyc's Extra",
      "accuracy": 9,
      "ar": 8.5,
      "bpm": 144,
      "convert": false,
      "count_circles": 369,
      "count_sliders": 40,
      "count_spinners": 1,
      "cs": 3,
      "deleted_at": null,
      "drain": 6,
      "hit_length": 92,
      "is_scoreable": true,
      "last_updated": "2024-10-09T14:34:29Z",
      "mode_int": 0,
      "passcount": 222,
      "playcount": 1396,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/4790302",
      "checksum": "96545218250d5c0cae46b3d78c670e52"
    },
    {
      "beatmapset_id": 2237577,
      "difficulty_rating": 4.7,
      "id": 4791473,
      "mode": "osu",
      "status": "ranked",
      "total_length": 93,
      "user_id": 7270089,
      "version": "Chanmann's Insane",
      "accuracy": 7,
      "ar": 8,
      "bpm": 144,
      "convert": false,
      "count_circles": 334,
      "count_sliders": 66,
      "count_spinners": 1,
      "cs": 4,
      "deleted_at": null,
      "drain": 5,
      "hit_length": 92,
      "is_scoreable": true,
      "last_updated": "2024-10-09T14:34:29Z",
      "mode_int": 0,
      "passcount": 161,
      "playcount": 2107,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/4791473",
      "checksum": "c25d208a5810a64fed981594102e034a"
    },
    {
      "beatmapset_id": 2237577,
      "difficulty_rating": 5.24,
      "id": 4796933,
      "mode": "osu",
      "status": "ranked",
      "total_length": 93,
      "user_id": 6149313,
      "version": "Pata-Mon's Another",
      "accuracy": 8,
      "ar": 9,
      "bpm": 144,
      "convert": false,
      "count_circles": 220,
      "count_sliders": 236,
      "count_spinners": 0,
      "cs": 4,
      "deleted_at": null,
      "drain": 6,
      "hit_length": 92,
      "is_scoreable": true,
      "last_updated": "2024-10-09T14:34:30Z",
      "mode_int": 0,
      "passcount": 108,
      "playcount": 1360,
      "ranked": 1,
      "url": "https://osu.ppy.sh/beatmaps/4796933",
      "checksum": "d65eff6a201add2f43267c17ac5186d4"
    }
  ],
  "current_user_attributes": {
    "can_beatmap_update_owner": false,
    "can_delete": false,
    "can_edit_metadata": false,
    "can_edit_offset": false,
    "can_edit_tags": false,
    "can_hype": false,
    "can_hype_reason": "Must be signed in to hype.",
    "can_love": false,
    "can_remove_from_loved": false,
    "is_watching": false,
    "new_hype_time": null,
    "nomination_modes": null,
    "remaining_hype": 0
  },
  "discussions": [
    {
      "id": 4546392,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 3648459,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-08-23T23:03:57+00:00",
      "updated_at": "2024-08-23T23:03:57+00:00",
      "deleted_at": null,
      "last_post_at": "2024-08-23T23:03:57+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4546392,
          "created_at": "2024-08-23T23:03:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12081955,
          "last_editor_id": null,
          "message": "nice",
          "system": false,
          "updated_at": "2024-08-23T23:03:57+00:00",
          "user_id": 3648459
        }
      ],
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
      "id": 4546402,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 6260705,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-08-23T23:12:23+00:00",
      "updated_at": "2024-08-23T23:12:23+00:00",
      "deleted_at": null,
      "last_post_at": "2024-08-23T23:12:23+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4546402,
          "created_at": "2024-08-23T23:12:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12081999,
          "last_editor_id": null,
          "message": "ajt kawaii",
          "system": false,
          "updated_at": "2024-08-23T23:12:23+00:00",
          "user_id": 6260705
        }
      ],
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
      "id": 4546409,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 7270089,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-08-23T23:17:54+00:00",
      "updated_at": "2024-08-23T23:17:54+00:00",
      "deleted_at": null,
      "last_post_at": "2024-08-23T23:17:54+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4546409,
          "created_at": "2024-08-23T23:17:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12082013,
          "last_editor_id": null,
          "message": "oh no",
          "system": false,
          "updated_at": "2024-08-23T23:17:54+00:00",
          "user_id": 7270089
        }
      ],
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
      "id": 4546427,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 9648246,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-08-23T23:32:32+00:00",
      "updated_at": "2024-08-23T23:32:32+00:00",
      "deleted_at": null,
      "last_post_at": "2024-08-23T23:32:32+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4546427,
          "created_at": "2024-08-23T23:32:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12082054,
          "last_editor_id": null,
          "message": "pure cocaine uh oh",
          "system": false,
          "updated_at": "2024-08-23T23:32:32+00:00",
          "user_id": 9648246
        }
      ],
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
      "id": 4546652,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 17916791,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-08-24T03:08:11+00:00",
      "updated_at": "2024-08-24T03:08:11+00:00",
      "deleted_at": null,
      "last_post_at": "2024-08-24T03:08:11+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4546652,
          "created_at": "2024-08-24T03:08:11+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12082708,
          "last_editor_id": null,
          "message": "I'm here to glaze",
          "system": false,
          "updated_at": "2024-08-24T03:08:11+00:00",
          "user_id": 17916791
        }
      ],
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
      "id": 4547507,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 16680343,
      "deleted_by_id": null,
      "message_type": "praise",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-08-24T13:34:38+00:00",
      "updated_at": "2024-08-24T13:34:38+00:00",
      "deleted_at": null,
      "last_post_at": "2024-08-24T13:34:38+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4547507,
          "created_at": "2024-08-24T13:34:38+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12084789,
          "last_editor_id": null,
          "message": "!!  AJT",
          "system": false,
          "updated_at": "2024-08-24T13:34:38+00:00",
          "user_id": 16680343
        }
      ],
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
      "id": 4581921,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 12751518,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-09-13T05:01:05+00:00",
      "updated_at": "2024-09-13T05:01:05+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-13T05:01:05+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4581921,
          "created_at": "2024-09-13T05:01:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12171924,
          "last_editor_id": null,
          "message": "ah hell naw my set gonna get gapped",
          "system": false,
          "updated_at": "2024-09-13T05:01:05+00:00",
          "user_id": 12751518
        }
      ],
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
      "id": 4585132,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 2490770,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-09-15T02:01:45+00:00",
      "updated_at": "2024-09-15T02:01:45+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-15T02:01:45+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4585132,
          "created_at": "2024-09-15T02:01:45+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12180665,
          "last_editor_id": null,
          "message": "we are living in 2010",
          "system": false,
          "updated_at": "2024-09-15T02:01:45+00:00",
          "user_id": 2490770
        }
      ],
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
      "id": 4591249,
      "beatmapset_id": 2237577,
      "beatmap_id": 4754261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 93121,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-18T19:50:26+00:00",
      "updated_at": "2024-09-29T17:56:29+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-29T17:56:29+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591249,
          "created_at": "2024-09-18T19:50:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196132,
          "last_editor_id": null,
          "message": "01:33:121 (1) - remove finish? felt too loud for the calm ending imo",
          "system": false,
          "updated_at": "2024-09-18T19:50:26+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4591249,
          "created_at": "2024-09-19T01:00:08+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196912,
          "last_editor_id": null,
          "message": "I'll think about it",
          "system": false,
          "updated_at": "2024-09-19T01:00:08+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591249,
          "created_at": "2024-09-19T01:00:08+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196913,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-19T01:00:08+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591249,
          "created_at": "2024-09-19T01:00:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196914,
          "last_editor_id": null,
          "message": "Resolved by accident",
          "system": false,
          "updated_at": "2024-09-19T01:00:17+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591249,
          "created_at": "2024-09-19T01:00:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196915,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": false
          },
          "system": true,
          "updated_at": "2024-09-19T01:00:17+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591249,
          "created_at": "2024-09-29T17:56:29+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12236082,
          "last_editor_id": null,
          "message": "Keeping",
          "system": false,
          "updated_at": "2024-09-29T17:56:29+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591249,
          "created_at": "2024-09-29T17:56:29+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12236083,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-29T17:56:29+00:00",
          "user_id": 3181083
        }
      ],
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
      "id": 4591251,
      "beatmapset_id": 2237577,
      "beatmap_id": 4754261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 2913,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-18T19:51:17+00:00",
      "updated_at": "2024-09-19T00:47:33+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-19T00:47:33+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591251,
          "created_at": "2024-09-18T19:51:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196134,
          "last_editor_id": 11771,
          "message": "00:02:913 (1,2) - 00:06:246 (1,2) - what do you think doing ctrl+G? the pitch is different from the pattern right before, so giving a small variation would be great",
          "system": false,
          "updated_at": "2024-09-18T20:12:31+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4591251,
          "created_at": "2024-09-19T00:47:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196884,
          "last_editor_id": null,
          "message": "did smth",
          "system": false,
          "updated_at": "2024-09-19T00:47:33+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591251,
          "created_at": "2024-09-19T00:47:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196885,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-19T00:47:33+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4591252,
      "beatmapset_id": 2237577,
      "beatmap_id": 4754261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 7287,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-18T19:51:37+00:00",
      "updated_at": "2024-09-19T00:47:45+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-19T00:47:45+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591252,
          "created_at": "2024-09-18T19:51:37+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196135,
          "last_editor_id": null,
          "message": "00:07:287 (1,3) - overlaps visually hurt, would you mind avoiding them? xdxd",
          "system": false,
          "updated_at": "2024-09-18T19:51:37+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4591252,
          "created_at": "2024-09-19T00:47:45+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196886,
          "last_editor_id": null,
          "message": "I like the way they look but I moved it anyway",
          "system": false,
          "updated_at": "2024-09-19T00:47:45+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591252,
          "created_at": "2024-09-19T00:47:45+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196887,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-19T00:47:45+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4591253,
      "beatmapset_id": 2237577,
      "beatmap_id": 4754261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 44370,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-18T19:52:52+00:00",
      "updated_at": "2024-09-19T00:50:50+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-19T00:50:50+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591253,
          "created_at": "2024-09-18T19:52:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196136,
          "last_editor_id": null,
          "message": "00:44:370 (3) - mistakenly missing sampleset-normal? this was the only soft-clap for the section.",
          "system": false,
          "updated_at": "2024-09-18T19:52:52+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4591253,
          "created_at": "2024-09-19T00:50:50+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196895,
          "last_editor_id": null,
          "message": "Yep, thanks, fixed set-wide",
          "system": false,
          "updated_at": "2024-09-19T00:50:50+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591253,
          "created_at": "2024-09-19T00:50:50+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196896,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-19T00:50:50+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4591256,
      "beatmapset_id": 2237577,
      "beatmap_id": 4754261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 13954,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-18T19:55:05+00:00",
      "updated_at": "2024-09-19T00:59:46+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-19T00:59:46+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591256,
          "created_at": "2024-09-18T19:55:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196139,
          "last_editor_id": 11771,
          "message": "00:13:954 (1) - 00:15:621 (1) - kinda minor touch but what do you think about making these 1/4 sliders 1.2x in SV so it gets visually symmetrical with 00:14:579 (1,2) - ? will also clean out the follow point",
          "system": false,
          "updated_at": "2024-09-18T20:08:07+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4591256,
          "created_at": "2024-09-19T00:59:46+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196910,
          "last_editor_id": null,
          "message": "Sure",
          "system": false,
          "updated_at": "2024-09-19T00:59:46+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591256,
          "created_at": "2024-09-19T00:59:46+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196911,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-19T00:59:46+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4591257,
      "beatmapset_id": 2237577,
      "beatmap_id": 4754261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 35412,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-18T19:58:25+00:00",
      "updated_at": "2024-09-19T00:49:56+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-19T00:49:56+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591257,
          "created_at": "2024-09-18T19:58:25+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196144,
          "last_editor_id": 11771,
          "message": "00:35:412 (6) - Add NC? Felt this was a separate pattern from 00:34:579 (1,2,3,4,5) - . Also adding NC will make the combo color of 00:19:162 (1,2,3,4,5,6,7) - vs. 00:45:621 (3,4,5,6,7,8,9) - consistent. Felt like a really iconic pattern, but having different combo color seems inconsistent.",
          "system": false,
          "updated_at": "2024-09-18T20:07:20+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4591257,
          "created_at": "2024-09-19T00:49:55+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196892,
          "last_editor_id": null,
          "message": "Done",
          "system": false,
          "updated_at": "2024-09-19T00:49:55+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591257,
          "created_at": "2024-09-19T00:49:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196893,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-19T00:49:56+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4591263,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-09-18T20:03:20+00:00",
      "updated_at": "2024-09-18T20:03:20+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-18T20:03:20+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591263,
          "created_at": "2024-09-18T20:03:20+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196157,
          "last_editor_id": null,
          "message": "hype",
          "system": false,
          "updated_at": "2024-09-18T20:03:20+00:00",
          "user_id": 11771
        }
      ],
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
      "id": 4591265,
      "beatmapset_id": 2237577,
      "beatmap_id": 4754261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 54371,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-18T20:04:12+00:00",
      "updated_at": "2024-09-19T00:56:52+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-19T00:56:52+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591265,
          "created_at": "2024-09-18T20:04:12+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196159,
          "last_editor_id": null,
          "message": "00:54:371 (1,1,2,3) - the stacks kinda hurt visually, what about flipping the formation? ![](http://puu.sh/Kfcn0/09df6a6fbc.jpg)",
          "system": false,
          "updated_at": "2024-09-18T20:04:12+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4591265,
          "created_at": "2024-09-19T00:56:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196903,
          "last_editor_id": null,
          "message": "Did something again (seems like I have a different preference with stacks and overlaps than most people xd)",
          "system": false,
          "updated_at": "2024-09-19T00:56:52+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591265,
          "created_at": "2024-09-19T00:56:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196904,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-19T00:56:52+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4591267,
      "beatmapset_id": 2237577,
      "beatmap_id": 4754261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 64683,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-18T20:05:26+00:00",
      "updated_at": "2024-09-19T00:57:46+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-19T00:57:46+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4591267,
          "created_at": "2024-09-18T20:05:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196163,
          "last_editor_id": null,
          "message": "01:04:683 (1) - remove NC? Seems the patterning for the stream was intended as an NC spam, but having the stacked one new combo'd made both 01:04:579 (1) - 01:04:787 (1) - the same color which didn't turned out as intended.",
          "system": false,
          "updated_at": "2024-09-18T20:05:26+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4591267,
          "created_at": "2024-09-19T00:57:46+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196905,
          "last_editor_id": null,
          "message": "👍🏿",
          "system": false,
          "updated_at": "2024-09-19T00:57:46+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4591267,
          "created_at": "2024-09-19T00:57:46+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12196906,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-19T00:57:46+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4592773,
      "beatmapset_id": 2237577,
      "beatmap_id": 4787106,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 22912,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T17:53:32+00:00",
      "updated_at": "2024-10-06T14:17:03+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-06T14:17:03+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592773,
          "created_at": "2024-09-19T17:53:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12199926,
          "last_editor_id": null,
          "message": "00:22:912 (3,1) - 1/2 spacing feels fishy here, mind spacing them more?",
          "system": false,
          "updated_at": "2024-09-19T17:53:32+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592773,
          "created_at": "2024-09-20T02:59:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201023,
          "last_editor_id": null,
          "message": "It's fine IMO",
          "system": false,
          "updated_at": "2024-09-20T02:59:24+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4592773,
          "created_at": "2024-09-20T02:59:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201024,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T02:59:24+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4592773,
          "created_at": "2024-10-06T14:17:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12262284,
          "last_editor_id": null,
          "message": "well LOL",
          "system": false,
          "updated_at": "2024-10-06T14:17:03+00:00",
          "user_id": 9590557
        }
      ],
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
      "id": 4592783,
      "beatmapset_id": 2237577,
      "beatmap_id": 4787106,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": null,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T17:59:52+00:00",
      "updated_at": "2024-09-20T03:02:11+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T03:02:11+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592783,
          "created_at": "2024-09-19T17:59:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12199946,
          "last_editor_id": 11771,
          "message": "The following new combo/patterns felt a bit awkward with the lyrics. Very optional, but would be awesome if the NC setting matched with the lyrics.\n\n- 01:13:954 - Uketomete 01:15:412 - Kuremasuka | Starting NC from 01:15:204 - will work better as 01:14:996 - belongs to the previous lyric\n- 01:20:621 - Symphonic Love 01:22:496 - Kimieto | Starting NC from 01:22:496 - will work better since that's the new line\n- 01:28:329 - Hajimeta 01:29:787 - Sora | Could start NC from 01:29:787 - for the same reason.",
          "system": false,
          "updated_at": "2024-09-19T20:14:03+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592783,
          "created_at": "2024-09-20T03:02:11+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201026,
          "last_editor_id": null,
          "message": "I applied these but I decided it felt more natural to have the NC accomodating the patterns + the pitch mainly so I reverted (maybe I'd have a different opinion if I spoke Japanese but IMO it's fine)",
          "system": false,
          "updated_at": "2024-09-20T03:02:11+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4592783,
          "created_at": "2024-09-20T03:02:11+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201027,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T03:02:11+00:00",
          "user_id": 3181083
        }
      ],
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
      "id": 4592791,
      "beatmapset_id": 2237577,
      "beatmap_id": 4786678,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 25621,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T18:03:01+00:00",
      "updated_at": "2024-09-20T02:58:41+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T02:58:41+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592791,
          "created_at": "2024-09-19T18:03:01+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12199960,
          "last_editor_id": null,
          "message": "00:25:621 (6) - 00:52:287 - Kiai fountains for non-clickable rhythms felt a bit odd, what do you think about reducing a bit so it can actually work with the Normal rhythms?",
          "system": false,
          "updated_at": "2024-09-19T18:03:01+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592791,
          "created_at": "2024-09-20T02:58:41+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201021,
          "last_editor_id": null,
          "message": "[]()",
          "system": false,
          "updated_at": "2024-09-20T02:58:41+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4592791,
          "created_at": "2024-09-20T02:58:41+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201022,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T02:58:41+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4592795,
      "beatmapset_id": 2237577,
      "beatmap_id": 4786678,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 35204,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T18:04:14+00:00",
      "updated_at": "2024-09-20T02:56:32+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T02:56:32+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592795,
          "created_at": "2024-09-19T18:04:14+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12199965,
          "last_editor_id": null,
          "message": "00:35:204 (4) - imo would be better if this was a circle, feels something what you'd normally simplify the rhythm. The chain went a bit long here unlike other parts",
          "system": false,
          "updated_at": "2024-09-19T18:04:14+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592795,
          "created_at": "2024-09-20T02:56:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201014,
          "last_editor_id": null,
          "message": "[]()",
          "system": false,
          "updated_at": "2024-09-20T02:56:32+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4592795,
          "created_at": "2024-09-20T02:56:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201015,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T02:56:32+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4592801,
      "beatmapset_id": 2237577,
      "beatmap_id": 4786678,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 92287,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T18:06:06+00:00",
      "updated_at": "2024-09-20T02:57:12+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T02:57:12+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592801,
          "created_at": "2024-09-19T18:06:06+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12199971,
          "last_editor_id": null,
          "message": "01:32:287 (6) - what do you think about removing this note and starting the spinner 1/2 earlier? Having 3 1/2 beats stacked felt something for a powerful sound like 01:10:621 (1,2,3,4,5,6) - 01:13:121 (9,10,11) - etc, but (6) being a weak sound didn't fit well with other context.",
          "system": false,
          "updated_at": "2024-09-19T18:06:06+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592801,
          "created_at": "2024-09-20T02:57:12+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201017,
          "last_editor_id": null,
          "message": "Agree",
          "system": false,
          "updated_at": "2024-09-20T02:57:12+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4592801,
          "created_at": "2024-09-20T02:57:12+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201018,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T02:57:12+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4592899,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 47287,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T19:41:45+00:00",
      "updated_at": "2024-09-26T00:39:23+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T03:23:14+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592899,
          "created_at": "2024-09-19T19:41:45+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12200217,
          "last_editor_id": null,
          "message": "00:47:287 (1,2,3) - Actually the lyrics behind here was \"freeze\" which was different from 00:40:621 (1,2,3) - \"please\". Do you prefer keeping the sliders as PLS?",
          "system": false,
          "updated_at": "2024-09-19T19:41:45+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592899,
          "created_at": "2024-09-20T03:23:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201055,
          "last_editor_id": null,
          "message": "OOPS!\n\nwasnt intentional but now that you point it out ngl i think having misheard lyrics representation is kinda funny so i want to keep",
          "system": false,
          "updated_at": "2024-09-20T03:23:05+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4592899,
          "created_at": "2024-09-20T03:23:14+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201056,
          "last_editor_id": null,
          "message": "r",
          "system": false,
          "updated_at": "2024-09-20T03:23:14+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4592899,
          "created_at": "2024-09-20T03:23:14+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201057,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T03:23:14+00:00",
          "user_id": 5286213
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            5286213
          ],
          "down": []
        }
      }
    },
    {
      "id": 4592902,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 59579,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T19:44:06+00:00",
      "updated_at": "2024-09-20T03:31:03+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T03:31:03+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592902,
          "created_at": "2024-09-19T19:44:06+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12200223,
          "last_editor_id": null,
          "message": "00:59:579 (9,10,11,12,13,14) - what about moving either a grid up or down? 00:59:371 (8,9) - this flow didn't felt polished enough and ironing out by either making it straight or giving a slight curve would work better imo",
          "system": false,
          "updated_at": "2024-09-19T19:44:06+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592902,
          "created_at": "2024-09-20T03:31:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201068,
          "last_editor_id": null,
          "message": "i think its cool, i dont think all curves have  to be comfortable and follow the same arc",
          "system": false,
          "updated_at": "2024-09-20T03:31:03+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4592902,
          "created_at": "2024-09-20T03:31:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201069,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T03:31:03+00:00",
          "user_id": 5286213
        }
      ],
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
      "id": 4592903,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 90516,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T19:47:23+00:00",
      "updated_at": "2024-09-20T03:28:56+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T03:28:56+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592903,
          "created_at": "2024-09-19T19:47:23+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12200227,
          "last_editor_id": null,
          "message": "01:30:516 (2) - 01:31:350 (6) - umm I understand it's a grid map, but what do you think about making the distance snapping equal here? having an uneven spacing because of the grid snapping feels like a random 2009 map which doesn't feel nice tbh",
          "system": false,
          "updated_at": "2024-09-19T19:47:23+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592903,
          "created_at": "2024-09-20T03:28:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201063,
          "last_editor_id": null,
          "message": "2009 was a better time",
          "system": false,
          "updated_at": "2024-09-20T03:28:56+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4592903,
          "created_at": "2024-09-20T03:28:56+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201064,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T03:28:56+00:00",
          "user_id": 5286213
        }
      ],
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
      "id": 4592904,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 57287,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T19:49:57+00:00",
      "updated_at": "2024-09-20T03:20:27+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T03:20:27+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592904,
          "created_at": "2024-09-19T19:49:57+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12200230,
          "last_editor_id": null,
          "message": "00:57:287 (1,2,3,4) - 01:06:662 (1,1,2,3,4,5) - 01:08:329 (4,5,6) - 01:31:350 (6,7,8,9) - 01:32:079 (10,1,2,3) - spacing / visual went off because of the stacks. would be nice if we can utilize some future techniques such as manual stacks or off grid to iron things out.",
          "system": false,
          "updated_at": "2024-09-19T19:49:57+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592904,
          "created_at": "2024-09-20T03:20:27+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201053,
          "last_editor_id": null,
          "message": "nah this is good. future techniques make the map look too modern",
          "system": false,
          "updated_at": "2024-09-20T03:20:27+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4592904,
          "created_at": "2024-09-20T03:20:27+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201054,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T03:20:27+00:00",
          "user_id": 5286213
        }
      ],
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
      "id": 4592907,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 87912,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T19:52:42+00:00",
      "updated_at": "2024-09-20T05:37:00+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T05:37:00+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592907,
          "created_at": "2024-09-19T19:52:42+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12200238,
          "last_editor_id": 11771,
          "message": "01:27:912 (2,3,4,5,6) - Can you try making the shapes clearer so it can feel something more similar to 01:14:579 (1,2,3,4,5) - ? While DS was assured, the placement felt a bit random as the formation was unclear. I think it's important to form a clear shape especially for 1/1 rhythms, because grid maps give a feeling of highly polished under fixed position while placing ambiguously gives the off grid vibes.",
          "system": false,
          "updated_at": "2024-09-19T19:58:43+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592907,
          "created_at": "2024-09-20T03:27:41+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201061,
          "last_editor_id": null,
          "message": "nah, \"clean/ polished/ perfect symmetry\" was not the objective of this map. nothing against them but i have always disliked how modern attempt at \"old maps\" always make everything perfectly symmetric w/ copy pasted symmetry and just because its on a grid, its old according to them (sory bloxi). i prefer stuff like shotgun symphony+ or evolution (time is now) so not actually making shapes accurately gives off the vibe that i wanted to go for more here",
          "system": false,
          "updated_at": "2024-09-20T03:27:41+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4592907,
          "created_at": "2024-09-20T03:27:41+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201062,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T03:27:41+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4592907,
          "created_at": "2024-09-20T03:29:42+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201067,
          "last_editor_id": 5286213,
          "message": "i meant evolution (time is pop). oops fake fan\n\nas a player i find unclean patterns a LOT more satisfying to hit in general, hitting a perfect curve or shape does not give me any real sense of achievement or \"wow, how did i hit that\" anymore. tho this one is not really that hard because its 1/1 but same philosophy applies",
          "system": false,
          "updated_at": "2024-09-20T03:38:52+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4592907,
          "created_at": "2024-09-20T05:37:00+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201205,
          "last_editor_id": null,
          "message": "Fair take, i get what you’re trying to do",
          "system": false,
          "updated_at": "2024-09-20T05:37:00+00:00",
          "user_id": 11771
        }
      ],
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
      "id": 4592910,
      "beatmapset_id": 2237577,
      "beatmap_id": 4758261,
      "user_id": 11771,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 58954,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-09-19T19:56:32+00:00",
      "updated_at": "2024-09-20T05:20:19+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T05:20:19+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4592910,
          "created_at": "2024-09-19T19:56:32+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12200245,
          "last_editor_id": null,
          "message": "00:58:954 (3) - 01:00:204 - What about using a 1/4 rhythm for the drums? Rhythms felt to following the instruments as some vocal beats were being skipped, so expressing the 1/4 could work nice with the intention imo.",
          "system": false,
          "updated_at": "2024-09-19T19:56:32+00:00",
          "user_id": 11771
        },
        {
          "beatmapset_discussion_id": 4592910,
          "created_at": "2024-09-20T05:20:19+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201167,
          "last_editor_id": null,
          "message": "i took what you said and made some adjustments to rhythm in this section. I tried to focus on vocals primarily, but my ideas were rather skewed when i was making this lol\nmade rhythm follow vocals more clearly now",
          "system": false,
          "updated_at": "2024-09-20T05:20:19+00:00",
          "user_id": 12157130
        },
        {
          "beatmapset_discussion_id": 4592910,
          "created_at": "2024-09-20T05:20:19+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12201168,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-09-20T05:20:19+00:00",
          "user_id": 12157130
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            12157130
          ],
          "down": []
        }
      }
    },
    {
      "id": 4594176,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 7270089,
      "deleted_by_id": null,
      "message_type": "praise",
      "parent_id": null,
      "timestamp": 80621,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-09-20T19:29:09+00:00",
      "updated_at": "2024-09-20T19:29:12+00:00",
      "deleted_at": null,
      "last_post_at": "2024-09-20T19:29:12+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4594176,
          "created_at": "2024-09-20T19:29:09+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12203370,
          "last_editor_id": null,
          "message": "01:20:621 (1,2) -",
          "system": false,
          "updated_at": "2024-09-20T19:29:09+00:00",
          "user_id": 7270089
        },
        {
          "beatmapset_discussion_id": 4594176,
          "created_at": "2024-09-20T19:29:12+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12203371,
          "last_editor_id": null,
          "message": "based",
          "system": false,
          "updated_at": "2024-09-20T19:29:12+00:00",
          "user_id": 7270089
        }
      ],
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
      "id": 4610801,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 10701418,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-10-01T20:48:31+00:00",
      "updated_at": "2024-10-01T20:48:47+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-01T20:48:47+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4610801,
          "created_at": "2024-10-01T20:48:31+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12243380,
          "last_editor_id": null,
          "message": ",",
          "system": false,
          "updated_at": "2024-10-01T20:48:31+00:00",
          "user_id": 10701418
        },
        {
          "beatmapset_discussion_id": 4610801,
          "created_at": "2024-10-01T20:48:47+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12243381,
          "last_editor_id": null,
          "message": "hi big fan",
          "system": false,
          "updated_at": "2024-10-01T20:48:47+00:00",
          "user_id": 3181083
        }
      ],
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
      "id": 4618338,
      "beatmapset_id": 2237577,
      "beatmap_id": 4786678,
      "user_id": 9590557,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 73121,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-06T14:12:42+00:00",
      "updated_at": "2024-10-07T20:11:06+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T20:11:06+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4618338,
          "created_at": "2024-10-06T14:12:42+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12262252,
          "last_editor_id": null,
          "message": "01:13:121 (9,10,11) - feels lack of enough contrast with 01:10:621 (1,2,3) - 01:11:454 (4,5,6) - etc.\n\nTry https://osu.ppy.sh/ss/19349396/a62c",
          "system": false,
          "updated_at": "2024-10-06T14:12:42+00:00",
          "user_id": 9590557
        },
        {
          "beatmapset_discussion_id": 4618338,
          "created_at": "2024-10-07T20:11:06+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268094,
          "last_editor_id": null,
          "message": "yep",
          "system": false,
          "updated_at": "2024-10-07T20:11:06+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4618338,
          "created_at": "2024-10-07T20:11:06+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268095,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T20:11:06+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4618365,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 9590557,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 48537,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-06T14:25:50+00:00",
      "updated_at": "2024-10-07T10:01:39+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T10:01:39+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-06T14:25:50+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12262306,
          "last_editor_id": null,
          "message": "00:48:537 (2) - just wanna sure if the slider shape is slider \"L\" 👀\n\nThe current slider looks more like “∟” which feels kinda weird...\nmaybe 0.75* + the shape https://osu.ppy.sh/ss/19349415/f982",
          "system": false,
          "updated_at": "2024-10-06T14:25:50+00:00",
          "user_id": 9590557
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T08:17:07+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265621,
          "last_editor_id": null,
          "message": "i made it a bit more vertical but im not doing sv, old maps wouldnt switch sv in this situation on the single slider",
          "system": false,
          "updated_at": "2024-10-07T08:17:07+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T08:17:07+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265622,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T08:17:07+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T08:22:27+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265636,
          "last_editor_id": null,
          "message": "actually maybe its just me but im too adjusted to the current L shape... i think it looks better so i reverted back. unfixed",
          "system": false,
          "updated_at": "2024-10-07T08:22:27+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T09:00:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265709,
          "last_editor_id": null,
          "message": "can u give me some old maps that contain some sliders like this, I'm curious that which old maps contain the \"L\" slider like this...",
          "system": false,
          "updated_at": "2024-10-07T09:00:17+00:00",
          "user_id": 9590557
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T09:00:17+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265710,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": false
          },
          "system": true,
          "updated_at": "2024-10-07T09:00:17+00:00",
          "user_id": 9590557
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T09:03:01+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265715,
          "last_editor_id": 9590557,
          "message": "Actually I can see 00:40:621 (1) - is \"P\", 00:43:954 (3) - is \"Z\".\nI just hope u can make a real \"L\" instead of “∟”... XD \n\nresolved this if u just wanna use a random slider art tho. 👀",
          "system": false,
          "updated_at": "2024-10-07T09:09:07+00:00",
          "user_id": 9590557
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T09:53:11+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265887,
          "last_editor_id": null,
          "message": "it is an L!!!!!!! Not random sliderart!!\n\nnot everyone writes L <-- exactly like this by hand. Human handwriting can vary!! As long as it's a right angle on the bottom left its intelligible especially when its sandwiched btween 2 other letters. PLZ trust\n\ni ddint mean it like old maps would do the letter L like this on purpose, i meant they would not think to make this single slider slower just to make a better L shape so the entire section would have to be 1.0x sv. I played around with this limitation and the vertical part looked way too tall (taller than the P) to compensate which looks worse!!",
          "system": false,
          "updated_at": "2024-10-07T09:53:11+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T09:55:35+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265894,
          "last_editor_id": null,
          "message": "I see 👀 but why u think taller than P is bad but fatter than P is ok LOL",
          "system": false,
          "updated_at": "2024-10-07T09:55:35+00:00",
          "user_id": 9590557
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T09:55:35+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265895,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T09:55:35+00:00",
          "user_id": 9590557
        },
        {
          "beatmapset_discussion_id": 4618365,
          "created_at": "2024-10-07T10:01:39+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265915,
          "last_editor_id": null,
          "message": "e... its not that fat...\nL > P > Z sorted by height look so strange imo",
          "system": false,
          "updated_at": "2024-10-07T10:01:39+00:00",
          "user_id": 5286213
        }
      ],
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
      "id": 4619512,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "mapper_note",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-10-07T05:01:22+00:00",
      "updated_at": "2024-10-07T05:01:22+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T05:01:22+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619512,
          "created_at": "2024-10-07T05:01:22+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265103,
          "last_editor_id": null,
          "message": "https://www.youtube.com/watch?v=pMbEHivhFvM",
          "system": false,
          "updated_at": "2024-10-07T05:01:22+00:00",
          "user_id": 10447058
        }
      ],
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
      "id": 4619515,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": null,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:02:33+00:00",
      "updated_at": "2024-10-07T20:12:52+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T20:12:52+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619515,
          "created_at": "2024-10-07T05:02:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265107,
          "last_editor_id": 10447058,
          "message": "not too sure about this but shouldn't title use (Short Ver.) marker cus of new metadata changes?\n\ni say this cus theres actually a full 3 min version of this same song so this one its technically its short ver",
          "system": false,
          "updated_at": "2024-10-07T05:08:10+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619515,
          "created_at": "2024-10-07T05:04:03+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265111,
          "last_editor_id": null,
          "message": "tho not sure if marker has to be short ver exactly or something else since by seing this https://osu.ppy.sh/beatmapsets/2237577/discussion/-/generalAll#/4619512 i think its an OP or something like that ?",
          "system": false,
          "updated_at": "2024-10-07T05:04:03+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619515,
          "created_at": "2024-10-07T20:12:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268101,
          "last_editor_id": null,
          "message": "discussed in dm + asked in #help, goign with game ver for now",
          "system": false,
          "updated_at": "2024-10-07T20:12:52+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4619515,
          "created_at": "2024-10-07T20:12:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268102,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T20:12:52+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4619523,
      "beatmapset_id": 2237577,
      "beatmap_id": 4758261,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": null,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:14:01+00:00",
      "updated_at": "2024-10-09T01:32:54+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-09T01:32:54+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619523,
          "created_at": "2024-10-07T05:14:01+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265128,
          "last_editor_id": 10447058,
          "message": "do u think u can bump your ds or smth on verses cus right now the spacing jump into choruses feels like a jumpscare\n\nlike, 1/2 rhythms on your verses doesn't even have followpoints and on your choruses 1/4s are spaced like a lot and the spacing progression feels a bit disbalanced imo",
          "system": false,
          "updated_at": "2024-10-07T05:17:34+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619523,
          "created_at": "2024-10-07T05:22:07+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265154,
          "last_editor_id": null,
          "message": "also now that we are on it is it intended to have everything dsed on verses ? on choruses u use some ocassionally spacing bump to emphasize stuff liek 00:42:912 (7,1) - etc maybe u can add some of those on verses if u like, unless the intention is different",
          "system": false,
          "updated_at": "2024-10-07T05:22:07+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619523,
          "created_at": "2024-10-08T03:05:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268711,
          "last_editor_id": null,
          "message": "unsure about applying this and i'd like to get a few more opinions \n\nmy idea was for kiais to be double time and the calmer parts to act as essentially my noob attempt of mimicking an older style map with ds and gridsnap etc\n\nhowever I did think about if this extent of difficulty difference between verse and kiai was appropriate for ranked, i wondered if because the difficulty is kind of consistent/has a theme (kiai parts = harder, non kiai parts = easier), it might be alright?\n\nbut yeah i wonder if other ppl think its ok or if its too int",
          "system": false,
          "updated_at": "2024-10-08T03:05:54+00:00",
          "user_id": 12157130
        },
        {
          "beatmapset_discussion_id": 4619523,
          "created_at": "2024-10-08T10:06:30+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12269240,
          "last_editor_id": null,
          "message": "updating with the file i was sent",
          "system": false,
          "updated_at": "2024-10-08T10:06:30+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4619523,
          "created_at": "2024-10-08T10:33:20+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12269312,
          "last_editor_id": null,
          "message": "fwiw I think it's fine",
          "system": false,
          "updated_at": "2024-10-08T10:33:20+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4619523,
          "created_at": "2024-10-09T01:06:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12272143,
          "last_editor_id": null,
          "message": "i think it fine too",
          "system": false,
          "updated_at": "2024-10-09T01:06:26+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4619523,
          "created_at": "2024-10-09T01:32:53+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12272198,
          "last_editor_id": null,
          "message": "i clicke the circle",
          "system": false,
          "updated_at": "2024-10-09T01:32:53+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619523,
          "created_at": "2024-10-09T01:32:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12272199,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-09T01:32:54+00:00",
          "user_id": 10447058
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            12157130
          ],
          "down": []
        }
      }
    },
    {
      "id": 4619528,
      "beatmapset_id": 2237577,
      "beatmap_id": 4758261,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": null,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:15:48+00:00",
      "updated_at": "2024-10-09T22:04:20+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-09T22:04:20+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619528,
          "created_at": "2024-10-07T05:15:48+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265135,
          "last_editor_id": null,
          "message": "personally i think u can just use custom samples (like the same patamon used) on your choruses atleast cus the default normal sample with the 1/4 spam feels quite jarring in my opinionated onion",
          "system": false,
          "updated_at": "2024-10-07T05:15:48+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619528,
          "created_at": "2024-10-07T05:16:15+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265142,
          "last_editor_id": null,
          "message": "or not necessarily custom samples but maybe don't spam the normal sample that much ;;",
          "system": false,
          "updated_at": "2024-10-07T05:16:15+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619528,
          "created_at": "2024-10-07T16:23:15+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12267279,
          "last_editor_id": null,
          "message": "Hmm i really like the sound of the norm=hitnorm and idt its that spammy idk cuz its used as default sample in maps often\ni lowered the volume if that helps or someting",
          "system": false,
          "updated_at": "2024-10-07T16:23:15+00:00",
          "user_id": 12157130
        },
        {
          "beatmapset_discussion_id": 4619528,
          "created_at": "2024-10-07T16:23:15+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12267280,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T16:23:15+00:00",
          "user_id": 12157130
        },
        {
          "beatmapset_discussion_id": 4619528,
          "created_at": "2024-10-09T22:04:20+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12275656,
          "last_editor_id": null,
          "message": "the volume lowering actually helps a lot ty",
          "system": false,
          "updated_at": "2024-10-09T22:04:20+00:00",
          "user_id": 10447058
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            12157130
          ],
          "down": []
        }
      }
    },
    {
      "id": 4619535,
      "beatmapset_id": 2237577,
      "beatmap_id": 4758261,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 14683,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:19:18+00:00",
      "updated_at": "2024-10-08T02:44:10+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-08T02:44:10+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619535,
          "created_at": "2024-10-07T05:19:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265150,
          "last_editor_id": null,
          "message": "00:14:683 (1,2,3,4,5,1,2,3,4,5,6) - feels a bit too 1/4 spammy maybe add some 1/2 somwhere ?",
          "system": false,
          "updated_at": "2024-10-07T05:19:18+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619535,
          "created_at": "2024-10-08T02:44:10+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268689,
          "last_editor_id": null,
          "message": "idk where i can put 1/2 gap without it not being awkward but also the constant 1/4 here was intentional to make it feel high paced",
          "system": false,
          "updated_at": "2024-10-08T02:44:10+00:00",
          "user_id": 12157130
        },
        {
          "beatmapset_discussion_id": 4619535,
          "created_at": "2024-10-08T02:44:10+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268690,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-08T02:44:10+00:00",
          "user_id": 12157130
        }
      ],
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
      "id": 4619539,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 1454,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:26:49+00:00",
      "updated_at": "2024-10-07T08:18:05+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T08:18:05+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619539,
          "created_at": "2024-10-07T05:26:49+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265160,
          "last_editor_id": 10447058,
          "message": "00:01:454 (3) - whislte trust its epic addition",
          "system": false,
          "updated_at": "2024-10-07T05:36:33+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619539,
          "created_at": "2024-10-07T08:18:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265625,
          "last_editor_id": null,
          "message": "it kinda no difference but i dont mind clicking the button for u",
          "system": false,
          "updated_at": "2024-10-07T08:18:05+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4619539,
          "created_at": "2024-10-07T08:18:05+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265626,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T08:18:05+00:00",
          "user_id": 5286213
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            5286213
          ],
          "down": []
        }
      }
    },
    {
      "id": 4619540,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "praise",
      "parent_id": null,
      "timestamp": 80621,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-10-07T05:28:52+00:00",
      "updated_at": "2024-10-07T05:28:52+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T05:28:52+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619540,
          "created_at": "2024-10-07T05:28:52+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265166,
          "last_editor_id": null,
          "message": "01:20:621 (1,2,3,4) - LOL ?",
          "system": false,
          "updated_at": "2024-10-07T05:28:52+00:00",
          "user_id": 10447058
        }
      ],
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
      "id": 4619541,
      "beatmapset_id": 2237577,
      "beatmap_id": 4756508,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 90204,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:30:34+00:00",
      "updated_at": "2024-10-07T08:18:34+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T08:18:34+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619541,
          "created_at": "2024-10-07T05:30:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265169,
          "last_editor_id": 10447058,
          "message": "01:30:204 (9) - maybe delete this circle cus u are hard following vocal with 01:27:912 (2,3,4,5) - ?? :octopos:",
          "system": false,
          "updated_at": "2024-10-07T05:30:57+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619541,
          "created_at": "2024-10-07T08:18:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265628,
          "last_editor_id": null,
          "message": "no it makes too much sense if i do that",
          "system": false,
          "updated_at": "2024-10-07T08:18:34+00:00",
          "user_id": 5286213
        },
        {
          "beatmapset_discussion_id": 4619541,
          "created_at": "2024-10-07T08:18:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265629,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T08:18:34+00:00",
          "user_id": 5286213
        }
      ],
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
      "id": 4619544,
      "beatmapset_id": 2237577,
      "beatmap_id": 4791473,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": null,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:33:33+00:00",
      "updated_at": "2024-10-07T19:19:33+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T19:19:33+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619544,
          "created_at": "2024-10-07T05:33:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265172,
          "last_editor_id": null,
          "message": "lower hp a bit ? mayb hp 5",
          "system": false,
          "updated_at": "2024-10-07T05:33:33+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619544,
          "created_at": "2024-10-07T19:19:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12267922,
          "last_editor_id": null,
          "message": "yes",
          "system": false,
          "updated_at": "2024-10-07T19:19:33+00:00",
          "user_id": 7270089
        },
        {
          "beatmapset_discussion_id": 4619544,
          "created_at": "2024-10-07T19:19:33+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12267923,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T19:19:33+00:00",
          "user_id": 7270089
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            7270089
          ],
          "down": []
        }
      }
    },
    {
      "id": 4619550,
      "beatmapset_id": 2237577,
      "beatmap_id": 4787106,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 31037,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:39:54+00:00",
      "updated_at": "2024-10-07T20:12:18+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T20:12:18+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619550,
          "created_at": "2024-10-07T05:39:54+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265182,
          "last_editor_id": 10447058,
          "message": "00:31:037 (3,4) - maybe overlap cus its 1/4 rhythm\n\n rn feels like almost the same as  00:33:746 (7,1) - or 00:29:996 (6,7) -",
          "system": false,
          "updated_at": "2024-10-07T05:40:17+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619550,
          "created_at": "2024-10-07T05:41:14+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265184,
          "last_editor_id": null,
          "message": "01:02:287 (3,4) -",
          "system": false,
          "updated_at": "2024-10-07T05:41:14+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619550,
          "created_at": "2024-10-07T05:41:49+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265185,
          "last_editor_id": null,
          "message": "01:21:663 (3,4) -",
          "system": false,
          "updated_at": "2024-10-07T05:41:49+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619550,
          "created_at": "2024-10-07T20:12:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268096,
          "last_editor_id": null,
          "message": "yes to all",
          "system": false,
          "updated_at": "2024-10-07T20:12:18+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4619550,
          "created_at": "2024-10-07T20:12:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268097,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T20:12:18+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4619554,
      "beatmapset_id": 2237577,
      "beatmap_id": 4787106,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": null,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:42:59+00:00",
      "updated_at": "2024-10-07T20:12:24+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T20:12:24+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619554,
          "created_at": "2024-10-07T05:42:59+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265188,
          "last_editor_id": null,
          "message": "bump ar a bit like 7.5? with the amount of confusing patterns diff have feels a bit too dense visually/ harsh for bbeing hard diff imo",
          "system": false,
          "updated_at": "2024-10-07T05:42:59+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619554,
          "created_at": "2024-10-07T20:12:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268098,
          "last_editor_id": null,
          "message": "ok",
          "system": false,
          "updated_at": "2024-10-07T20:12:24+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4619554,
          "created_at": "2024-10-07T20:12:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268099,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T20:12:24+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4619557,
      "beatmapset_id": 2237577,
      "beatmap_id": 4786678,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 93537,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:48:07+00:00",
      "updated_at": "2024-10-07T20:09:34+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T20:09:34+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619557,
          "created_at": "2024-10-07T05:48:07+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265224,
          "last_editor_id": null,
          "message": "01:33:537 - Perhaps u can lower volume or mute it",
          "system": false,
          "updated_at": "2024-10-07T05:48:07+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619557,
          "created_at": "2024-10-07T20:09:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268092,
          "last_editor_id": null,
          "message": "even tho it's the last note I think feedback is important on a low diff + there's a clear sound so I'll keep it normal volume",
          "system": false,
          "updated_at": "2024-10-07T20:09:34+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4619557,
          "created_at": "2024-10-07T20:09:34+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268093,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T20:09:34+00:00",
          "user_id": 3181083
        }
      ],
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
      "id": 4619560,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": null,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-07T05:51:09+00:00",
      "updated_at": "2024-10-07T20:20:19+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T20:20:19+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4619560,
          "created_at": "2024-10-07T05:51:09+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12265227,
          "last_editor_id": 10447058,
          "message": "symphony visual novel vn eroge opening op video game videogame jpop j-pop version\n\nepic tag additions",
          "system": false,
          "updated_at": "2024-10-07T06:47:49+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4619560,
          "created_at": "2024-10-07T20:20:19+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268111,
          "last_editor_id": null,
          "message": "added all except er*ge",
          "system": false,
          "updated_at": "2024-10-07T20:20:19+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4619560,
          "created_at": "2024-10-07T20:20:19+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268112,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-07T20:20:19+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4620617,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 23059830,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-10-07T20:24:09+00:00",
      "updated_at": "2024-10-07T20:24:09+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-07T20:24:09+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4620617,
          "created_at": "2024-10-07T20:24:09+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12268115,
          "last_editor_id": null,
          "message": "hi :3c",
          "system": false,
          "updated_at": "2024-10-07T20:24:09+00:00",
          "user_id": 23059830
        }
      ],
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
      "id": 4622805,
      "beatmapset_id": 2237577,
      "beatmap_id": 4758261,
      "user_id": 9590557,
      "deleted_by_id": null,
      "message_type": "suggestion",
      "parent_id": null,
      "timestamp": 39579,
      "resolved": true,
      "can_be_resolved": true,
      "can_grant_kudosu": true,
      "created_at": "2024-10-09T13:16:59+00:00",
      "updated_at": "2024-10-09T14:40:24+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-09T14:40:24+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4622805,
          "created_at": "2024-10-09T13:16:59+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12273682,
          "last_editor_id": null,
          "message": "00:39:579 -  seems missing normal-hitnormal",
          "system": false,
          "updated_at": "2024-10-09T13:16:59+00:00",
          "user_id": 9590557
        },
        {
          "beatmapset_discussion_id": 4622805,
          "created_at": "2024-10-09T14:40:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12273975,
          "last_editor_id": null,
          "message": "fixed",
          "system": false,
          "updated_at": "2024-10-09T14:40:24+00:00",
          "user_id": 3181083
        },
        {
          "beatmapset_discussion_id": 4622805,
          "created_at": "2024-10-09T14:40:24+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12273976,
          "last_editor_id": null,
          "message": {
            "type": "resolved",
            "value": true
          },
          "system": true,
          "updated_at": "2024-10-09T14:40:24+00:00",
          "user_id": 3181083
        }
      ],
      "votes": {
        "up": 1,
        "down": 0,
        "voters": {
          "up": [
            3181083
          ],
          "down": []
        }
      }
    },
    {
      "id": 4622941,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 9590557,
      "deleted_by_id": null,
      "message_type": "praise",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-10-09T14:45:26+00:00",
      "updated_at": "2024-10-09T14:45:26+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-09T14:45:26+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4622941,
          "created_at": "2024-10-09T14:45:26+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12273996,
          "last_editor_id": null,
          "message": "👀",
          "system": false,
          "updated_at": "2024-10-09T14:45:26+00:00",
          "user_id": 9590557
        }
      ],
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
      "id": 4623697,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 10447058,
      "deleted_by_id": null,
      "message_type": "praise",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-10-09T23:50:18+00:00",
      "updated_at": "2024-10-12T15:28:18+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-12T15:28:18+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4623697,
          "created_at": "2024-10-09T23:50:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12275949,
          "last_editor_id": null,
          "message": "happy new year 2012",
          "system": false,
          "updated_at": "2024-10-09T23:50:18+00:00",
          "user_id": 10447058
        },
        {
          "beatmapset_discussion_id": 4623697,
          "created_at": "2024-10-12T15:28:18+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12284934,
          "last_editor_id": null,
          "message": "goat",
          "system": false,
          "updated_at": "2024-10-12T15:28:18+00:00",
          "user_id": 8247685
        }
      ],
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
      "id": 4623720,
      "beatmapset_id": 2237577,
      "beatmap_id": 4758261,
      "user_id": 11913657,
      "deleted_by_id": null,
      "message_type": "praise",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-10-10T00:14:29+00:00",
      "updated_at": "2024-10-10T00:14:29+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-10T00:14:29+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4623720,
          "created_at": "2024-10-10T00:14:29+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12275992,
          "last_editor_id": null,
          "message": "hp 7 0_0",
          "system": false,
          "updated_at": "2024-10-10T00:14:29+00:00",
          "user_id": 11913657
        }
      ],
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
      "id": 4624247,
      "beatmapset_id": 2237577,
      "beatmap_id": null,
      "user_id": 23906771,
      "deleted_by_id": null,
      "message_type": "hype",
      "parent_id": null,
      "timestamp": null,
      "resolved": false,
      "can_be_resolved": false,
      "can_grant_kudosu": false,
      "created_at": "2024-10-10T13:22:35+00:00",
      "updated_at": "2024-10-10T13:22:35+00:00",
      "deleted_at": null,
      "last_post_at": "2024-10-10T13:22:35+00:00",
      "kudosu_denied": false,
      "posts": [
        {
          "beatmapset_discussion_id": 4624247,
          "created_at": "2024-10-10T13:22:35+00:00",
          "deleted_at": null,
          "deleted_by_id": null,
          "id": 12277400,
          "last_editor_id": null,
          "message": "LOVE IS PURE WHITE!",
          "system": false,
          "updated_at": "2024-10-10T13:22:35+00:00",
          "user_id": 23906771
        }
      ],
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
  "eligible_main_rulesets": [
    "osu"
  ],
  "events": [
    {
      "id": 6107804,
      "type": "beatmap_owner_change",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "beatmap_id": 4756508,
        "beatmap_version": "Deppy's Insane",
        "new_user_id": 5286213,
        "new_user_username": "Deppyforce"
      },
      "created_at": "2024-08-25T11:21:27+00:00",
      "user_id": 3181083
    },
    {
      "id": 6114320,
      "type": "beatmap_owner_change",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "beatmap_id": 4758261,
        "beatmap_version": "Gorou's Expert",
        "new_user_id": 12157130,
        "new_user_username": "Gorou"
      },
      "created_at": "2024-08-27T22:12:28+00:00",
      "user_id": 3181083
    },
    {
      "id": 6163618,
      "type": "genre_edit",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "old": "Unspecified",
        "new": "Pop"
      },
      "created_at": "2024-09-17T02:04:07+00:00",
      "user_id": 3181083
    },
    {
      "id": 6163619,
      "type": "language_edit",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "old": "Unspecified",
        "new": "Japanese"
      },
      "created_at": "2024-09-17T02:04:07+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167893,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4591251,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-19T00:47:30+00:00",
      "user_id": 11771
    },
    {
      "id": 6167894,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591251,
        "beatmap_discussion_post_id": 12196884
      },
      "created_at": "2024-09-19T00:47:33+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167895,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4591252,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-19T00:47:35+00:00",
      "user_id": 11771
    },
    {
      "id": 6167896,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591252,
        "beatmap_discussion_post_id": 12196886
      },
      "created_at": "2024-09-19T00:47:45+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167899,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4591257,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-19T00:49:50+00:00",
      "user_id": 11771
    },
    {
      "id": 6167900,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591257,
        "beatmap_discussion_post_id": 12196892
      },
      "created_at": "2024-09-19T00:49:56+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167901,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4591253,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-19T00:50:49+00:00",
      "user_id": 11771
    },
    {
      "id": 6167902,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591253,
        "beatmap_discussion_post_id": 12196895
      },
      "created_at": "2024-09-19T00:50:50+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167907,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4591265,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-19T00:56:33+00:00",
      "user_id": 11771
    },
    {
      "id": 6167908,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591265,
        "beatmap_discussion_post_id": 12196903
      },
      "created_at": "2024-09-19T00:56:52+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167909,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4591267,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-19T00:57:35+00:00",
      "user_id": 11771
    },
    {
      "id": 6167910,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591267,
        "beatmap_discussion_post_id": 12196905
      },
      "created_at": "2024-09-19T00:57:46+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167911,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4591256,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-19T00:59:44+00:00",
      "user_id": 11771
    },
    {
      "id": 6167912,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591256,
        "beatmap_discussion_post_id": 12196910
      },
      "created_at": "2024-09-19T00:59:46+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167913,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591249,
        "beatmap_discussion_post_id": 12196912
      },
      "created_at": "2024-09-19T01:00:08+00:00",
      "user_id": 3181083
    },
    {
      "id": 6167914,
      "type": "issue_reopen",
      "comment": {
        "beatmap_discussion_id": 4591249,
        "beatmap_discussion_post_id": 12196914
      },
      "created_at": "2024-09-19T01:00:17+00:00",
      "user_id": 3181083
    },
    {
      "id": 6170175,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4592795,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-20T02:56:16+00:00",
      "user_id": 11771
    },
    {
      "id": 6170176,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592795,
        "beatmap_discussion_post_id": 12201014
      },
      "created_at": "2024-09-20T02:56:32+00:00",
      "user_id": 3181083
    },
    {
      "id": 6170179,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4592801,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-20T02:57:11+00:00",
      "user_id": 11771
    },
    {
      "id": 6170180,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592801,
        "beatmap_discussion_post_id": 12201017
      },
      "created_at": "2024-09-20T02:57:12+00:00",
      "user_id": 3181083
    },
    {
      "id": 6170181,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4592791,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-20T02:58:36+00:00",
      "user_id": 11771
    },
    {
      "id": 6170182,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592791,
        "beatmap_discussion_post_id": 12201021
      },
      "created_at": "2024-09-20T02:58:41+00:00",
      "user_id": 3181083
    },
    {
      "id": 6170183,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592773,
        "beatmap_discussion_post_id": 12201023
      },
      "created_at": "2024-09-20T02:59:24+00:00",
      "user_id": 3181083
    },
    {
      "id": 6170184,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592783,
        "beatmap_discussion_post_id": 12201026
      },
      "created_at": "2024-09-20T03:02:11+00:00",
      "user_id": 3181083
    },
    {
      "id": 6170185,
      "type": "beatmap_owner_change",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "beatmap_id": 4790302,
        "beatmap_version": "Sonnyc's Extra",
        "new_user_id": 11771,
        "new_user_username": "Sonnyc"
      },
      "created_at": "2024-09-20T03:02:44+00:00",
      "user_id": 3181083
    },
    {
      "id": 6170204,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592904,
        "beatmap_discussion_post_id": 12201053
      },
      "created_at": "2024-09-20T03:20:27+00:00",
      "user_id": 5286213
    },
    {
      "id": 6170206,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592899,
        "beatmap_discussion_post_id": 12201056
      },
      "created_at": "2024-09-20T03:23:14+00:00",
      "user_id": 5286213
    },
    {
      "id": 6170207,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592907,
        "beatmap_discussion_post_id": 12201061
      },
      "created_at": "2024-09-20T03:27:41+00:00",
      "user_id": 5286213
    },
    {
      "id": 6170210,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592903,
        "beatmap_discussion_post_id": 12201063
      },
      "created_at": "2024-09-20T03:28:56+00:00",
      "user_id": 5286213
    },
    {
      "id": 6170212,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592902,
        "beatmap_discussion_post_id": 12201068
      },
      "created_at": "2024-09-20T03:31:03+00:00",
      "user_id": 5286213
    },
    {
      "id": 6170264,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4592910,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 12157130,
          "score": 1
        },
        "votes": [
          {
            "user_id": 12157130,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-20T05:18:43+00:00",
      "user_id": 11771
    },
    {
      "id": 6170266,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4592910,
        "beatmap_discussion_post_id": 12201167
      },
      "created_at": "2024-09-20T05:20:19+00:00",
      "user_id": 12157130
    },
    {
      "id": 6171596,
      "type": "beatmap_owner_change",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "beatmap_id": 4791473,
        "beatmap_version": "Chanmann's Insane",
        "new_user_id": 7270089,
        "new_user_username": "Chanmann"
      },
      "created_at": "2024-09-20T21:00:58+00:00",
      "user_id": 3181083
    },
    {
      "id": 6181921,
      "type": "beatmap_owner_change",
      "comment": {
        "beatmap_discussion_id": null,
        "beatmap_discussion_post_id": null,
        "beatmap_id": 4796933,
        "beatmap_version": "Pata-Mon's Another",
        "new_user_id": 6149313,
        "new_user_username": "Pata-Mon"
      },
      "created_at": "2024-09-25T13:55:06+00:00",
      "user_id": 3181083
    },
    {
      "id": 6182923,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4592899,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 5286213,
          "score": 1
        },
        "votes": [
          {
            "user_id": 5286213,
            "score": 1
          }
        ]
      },
      "created_at": "2024-09-26T00:39:23+00:00",
      "user_id": 11771
    },
    {
      "id": 6190121,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4591249,
        "beatmap_discussion_post_id": 12236082
      },
      "created_at": "2024-09-29T17:56:29+00:00",
      "user_id": 3181083
    },
    {
      "id": 6206071,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4618365,
        "beatmap_discussion_post_id": 12265621
      },
      "created_at": "2024-10-07T08:17:07+00:00",
      "user_id": 5286213
    },
    {
      "id": 6206072,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4618365,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 5286213,
          "score": 1
        },
        "votes": [
          {
            "user_id": 5286213,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T08:17:08+00:00",
      "user_id": 9590557
    },
    {
      "id": 6206079,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4619539,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 5286213,
          "score": 1
        },
        "votes": [
          {
            "user_id": 5286213,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T08:17:55+00:00",
      "user_id": 10447058
    },
    {
      "id": 6206082,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619539,
        "beatmap_discussion_post_id": 12265625
      },
      "created_at": "2024-10-07T08:18:05+00:00",
      "user_id": 5286213
    },
    {
      "id": 6206088,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619541,
        "beatmap_discussion_post_id": 12265628
      },
      "created_at": "2024-10-07T08:18:34+00:00",
      "user_id": 5286213
    },
    {
      "id": 6206093,
      "type": "kudosu_lost",
      "comment": {
        "beatmap_discussion_id": 4618365,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 5286213,
          "score": 0
        },
        "votes": []
      },
      "created_at": "2024-10-07T08:22:32+00:00",
      "user_id": 9590557
    },
    {
      "id": 6206136,
      "type": "issue_reopen",
      "comment": {
        "beatmap_discussion_id": 4618365,
        "beatmap_discussion_post_id": 12265709
      },
      "created_at": "2024-10-07T09:00:17+00:00",
      "user_id": 9590557
    },
    {
      "id": 6206237,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4618365,
        "beatmap_discussion_post_id": 12265894
      },
      "created_at": "2024-10-07T09:55:35+00:00",
      "user_id": 9590557
    },
    {
      "id": 6206982,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4619528,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 12157130,
          "score": 1
        },
        "votes": [
          {
            "user_id": 12157130,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T16:23:11+00:00",
      "user_id": 10447058
    },
    {
      "id": 6206984,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619528,
        "beatmap_discussion_post_id": 12267279
      },
      "created_at": "2024-10-07T16:23:15+00:00",
      "user_id": 12157130
    },
    {
      "id": 6207370,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4619544,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 7270089,
          "score": 1
        },
        "votes": [
          {
            "user_id": 7270089,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T19:19:32+00:00",
      "user_id": 10447058
    },
    {
      "id": 6207371,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619544,
        "beatmap_discussion_post_id": 12267922
      },
      "created_at": "2024-10-07T19:19:33+00:00",
      "user_id": 7270089
    },
    {
      "id": 6207482,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619557,
        "beatmap_discussion_post_id": 12268092
      },
      "created_at": "2024-10-07T20:09:34+00:00",
      "user_id": 3181083
    },
    {
      "id": 6207483,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4618338,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T20:11:04+00:00",
      "user_id": 9590557
    },
    {
      "id": 6207484,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4618338,
        "beatmap_discussion_post_id": 12268094
      },
      "created_at": "2024-10-07T20:11:06+00:00",
      "user_id": 3181083
    },
    {
      "id": 6207485,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4619550,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T20:12:17+00:00",
      "user_id": 10447058
    },
    {
      "id": 6207486,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619550,
        "beatmap_discussion_post_id": 12268096
      },
      "created_at": "2024-10-07T20:12:18+00:00",
      "user_id": 3181083
    },
    {
      "id": 6207487,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4619554,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T20:12:23+00:00",
      "user_id": 10447058
    },
    {
      "id": 6207488,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619554,
        "beatmap_discussion_post_id": 12268098
      },
      "created_at": "2024-10-07T20:12:24+00:00",
      "user_id": 3181083
    },
    {
      "id": 6207489,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4619515,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T20:12:39+00:00",
      "user_id": 10447058
    },
    {
      "id": 6207490,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619515,
        "beatmap_discussion_post_id": 12268101
      },
      "created_at": "2024-10-07T20:12:52+00:00",
      "user_id": 3181083
    },
    {
      "id": 6207492,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4619560,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-07T20:19:08+00:00",
      "user_id": 10447058
    },
    {
      "id": 6207495,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619560,
        "beatmap_discussion_post_id": 12268111
      },
      "created_at": "2024-10-07T20:20:19+00:00",
      "user_id": 3181083
    },
    {
      "id": 6207802,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619535,
        "beatmap_discussion_post_id": 12268689
      },
      "created_at": "2024-10-08T02:44:10+00:00",
      "user_id": 12157130
    },
    {
      "id": 6207809,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4619523,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 12157130,
          "score": 1
        },
        "votes": [
          {
            "user_id": 12157130,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-08T03:05:55+00:00",
      "user_id": 10447058
    },
    {
      "id": 6209665,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4619523,
        "beatmap_discussion_post_id": 12272198
      },
      "created_at": "2024-10-09T01:32:54+00:00",
      "user_id": 10447058
    },
    {
      "id": 6210560,
      "type": "kudosu_gain",
      "comment": {
        "beatmap_discussion_id": 4622805,
        "beatmap_discussion_post_id": null,
        "new_vote": {
          "user_id": 3181083,
          "score": 1
        },
        "votes": [
          {
            "user_id": 3181083,
            "score": 1
          }
        ]
      },
      "created_at": "2024-10-09T14:40:20+00:00",
      "user_id": 9590557
    },
    {
      "id": 6210561,
      "type": "issue_resolve",
      "comment": {
        "beatmap_discussion_id": 4622805,
        "beatmap_discussion_post_id": 12273975
      },
      "created_at": "2024-10-09T14:40:24+00:00",
      "user_id": 3181083
    },
    {
      "id": 6210571,
      "type": "nominate",
      "comment": {
        "modes": [
          "osu"
        ]
      },
      "created_at": "2024-10-09T14:45:30+00:00",
      "user_id": 9590557
    },
    {
      "id": 6211672,
      "type": "nominate",
      "comment": {
        "modes": [
          "osu"
        ]
      },
      "created_at": "2024-10-09T23:50:20+00:00",
      "user_id": 10447058
    },
    {
      "id": 6211673,
      "type": "qualify",
      "comment": null,
      "created_at": "2024-10-09T23:50:20+00:00",
      "user_id": null
    },
    {
      "id": 6227136,
      "type": "rank",
      "comment": null,
      "created_at": "2024-10-17T00:05:31+00:00",
      "user_id": null
    }
  ],
  "nominations": {
    "legacy_mode": false,
    "current": {
      "osu": 2
    },
    "required_meta": {
      "main_ruleset": 2,
      "non_main_ruleset": 1
    }
  },
  "related_users": [
    {
      "avatar_url": "https://a.ppy.sh/11771?1723301110.png",
      "country_code": "KR",
      "default_group": "default",
      "id": 11771,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Sonnyc",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/2490770?1723887545.jpeg",
      "country_code": "KR",
      "default_group": "bng",
      "id": 2490770,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": "#A347EB",
      "username": "Cellina",
      "groups": [
        {
          "colour": "#A347EB",
          "has_listing": true,
          "has_playmodes": true,
          "id": 28,
          "identifier": "bng",
          "is_probationary": false,
          "name": "Beatmap Nominators",
          "short_name": "BN",
          "playmodes": [
            "osu"
          ]
        }
      ]
    },
    {
      "avatar_url": "https://a.ppy.sh/3181083?1700508544.jpeg",
      "country_code": "GB",
      "default_group": "default",
      "id": 3181083,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "AJT",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/3648459?1692996216.png",
      "country_code": "GB",
      "default_group": "default",
      "id": 3648459,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Gaz",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/5286213?1681399349.png",
      "country_code": "TH",
      "default_group": "default",
      "id": 5286213,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-21T12:07:36+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Deppyforce",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/6149313?1616573635.gif",
      "country_code": "CN",
      "default_group": "default",
      "id": 6149313,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Pata-Mon",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/6260705?1668770993.jpeg",
      "country_code": "DE",
      "default_group": "default",
      "id": 6260705,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-21T11:33:16+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "jamesjan3",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/7270089?1729483334.jpeg",
      "country_code": "US",
      "default_group": "default",
      "id": 7270089,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": "2024-10-21T07:25:48+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Chanmann",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/8247685?1727068413.jpeg",
      "country_code": "US",
      "default_group": "default",
      "id": 8247685,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": true,
      "is_supporter": true,
      "last_visit": "2024-10-21T12:50:55+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "isle",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/9590557?1657109734.jpeg",
      "country_code": "CN",
      "default_group": "bng",
      "id": 9590557,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": true,
      "is_supporter": true,
      "last_visit": "2024-10-21T12:56:16+00:00",
      "pm_friends_only": false,
      "profile_colour": "#A347EB",
      "username": "Firika",
      "groups": [
        {
          "colour": "#A347EB",
          "has_listing": true,
          "has_playmodes": true,
          "id": 28,
          "identifier": "bng",
          "is_probationary": false,
          "name": "Beatmap Nominators",
          "short_name": "BN",
          "playmodes": [
            "osu"
          ]
        },
        {
          "colour": "#999999",
          "has_listing": true,
          "has_playmodes": false,
          "id": 16,
          "identifier": "alumni",
          "is_probationary": false,
          "name": "osu! Alumni",
          "short_name": "ALM",
          "playmodes": null
        }
      ]
    },
    {
      "avatar_url": "https://a.ppy.sh/9648246?1706685962.jpeg",
      "country_code": "US",
      "default_group": "default",
      "id": 9648246,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-20T18:02:45+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "delusional",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/10447058?1729020273.jpeg",
      "country_code": "PE",
      "default_group": "bng",
      "id": 10447058,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": "#A347EB",
      "username": "dakiwii",
      "groups": [
        {
          "colour": "#A347EB",
          "has_listing": true,
          "has_playmodes": true,
          "id": 28,
          "identifier": "bng",
          "is_probationary": false,
          "name": "Beatmap Nominators",
          "short_name": "BN",
          "playmodes": [
            "osu"
          ]
        }
      ]
    },
    {
      "avatar_url": "https://a.ppy.sh/10701418?1658609849.jpeg",
      "country_code": "IL",
      "default_group": "default",
      "id": 10701418,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "itay",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/11913657?1728517054.jpeg",
      "country_code": "RU",
      "default_group": "default",
      "id": 11913657,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "defreeyay",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/12157130?1722235836.jpeg",
      "country_code": "US",
      "default_group": "bng",
      "id": 12157130,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": "2024-10-21T05:27:00+00:00",
      "pm_friends_only": false,
      "profile_colour": "#A347EB",
      "username": "Gorou",
      "groups": [
        {
          "colour": "#A347EB",
          "has_listing": true,
          "has_playmodes": true,
          "id": 28,
          "identifier": "bng",
          "is_probationary": false,
          "name": "Beatmap Nominators",
          "short_name": "BN",
          "playmodes": [
            "osu"
          ]
        }
      ]
    },
    {
      "avatar_url": "https://a.ppy.sh/12751518?1729273310.jpeg",
      "country_code": "VN",
      "default_group": "default",
      "id": 12751518,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "shiritani",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/16680343?1729082046.jpeg",
      "country_code": "TW",
      "default_group": "default",
      "id": 16680343,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": true,
      "is_supporter": true,
      "last_visit": "2024-10-21T12:50:05+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "juices95",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/17916791?1724903875.jpeg",
      "country_code": "CA",
      "default_group": "default",
      "id": 17916791,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": true,
      "last_visit": null,
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "-Starlight",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/23059830?1728996354.jpeg",
      "country_code": "IL",
      "default_group": "default",
      "id": 23059830,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": true,
      "is_supporter": true,
      "last_visit": "2024-10-21T12:55:25+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "f2alon",
      "groups": []
    },
    {
      "avatar_url": "https://a.ppy.sh/23906771?1720748412.jpeg",
      "country_code": "PE",
      "default_group": "default",
      "id": 23906771,
      "is_active": true,
      "is_bot": false,
      "is_deleted": false,
      "is_online": false,
      "is_supporter": false,
      "last_visit": "2024-10-20T05:02:45+00:00",
      "pm_friends_only": false,
      "profile_colour": null,
      "username": "Shibukin",
      "groups": []
    }
  ]
}
"""