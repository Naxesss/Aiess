import sys
sys.path.append('..')

JSON = r"""
{
  "beatmapset": {
    "artist": "Carpool Tunnel",
    "covers": {
      "cover": "https://assets.ppy.sh/beatmaps/1001546/covers/cover.jpg?1572180029",
      "cover@2x": "https://assets.ppy.sh/beatmaps/1001546/covers/cover@2x.jpg?1572180029",
      "card": "https://assets.ppy.sh/beatmaps/1001546/covers/card.jpg?1572180029",
      "card@2x": "https://assets.ppy.sh/beatmaps/1001546/covers/card@2x.jpg?1572180029",
      "list": "https://assets.ppy.sh/beatmaps/1001546/covers/list.jpg?1572180029",
      "list@2x": "https://assets.ppy.sh/beatmaps/1001546/covers/list@2x.jpg?1572180029",
      "slimcover": "https://assets.ppy.sh/beatmaps/1001546/covers/slimcover.jpg?1572180029",
      "slimcover@2x": "https://assets.ppy.sh/beatmaps/1001546/covers/slimcover@2x.jpg?1572180029"
    },
    "creator": "_Epreus",
    "favourite_count": 32,
    "id": 1001546,
    "play_count": 32886,
    "preview_url": "//b.ppy.sh/preview/1001546.mp3",
    "source": "",
    "status": "ranked",
    "title": "Afterlight",
    "user_id": 7342798,
    "video": false,
    "availability": {
      "download_disabled": false,
      "more_information": null
    },
    "bpm": 178,
    "can_be_hyped": false,
    "discussion_enabled": true,
    "discussion_locked": false,
    "hype": {
      "current": 10,
      "required": 5
    },
    "is_scoreable": true,
    "last_updated": "2019-10-27T12:39:02+00:00",
    "legacy_thread_url": "https://osu.ppy.sh/community/forums/topics/932860",
    "nominations": {
      "current": 2,
      "required": 2
    },
    "ranked": 1,
    "ranked_date": "2019-10-31T00:43:44+00:00",
    "storyboard": false,
    "submitted_date": "2019-07-11T12:43:49+00:00",
    "tags": "osu! featured artist indie rock squirrelpascals mappers' guild mapper's",
    "beatmaps": [
      {
        "difficulty_rating": 5.33,
        "id": 2096611,
        "mode": "osu",
        "version": "Expert",
        "accuracy": 8,
        "ar": 7.5,
        "beatmapset_id": 1001546,
        "bpm": 178,
        "convert": null,
        "count_circles": 393,
        "count_sliders": 194,
        "count_spinners": 2,
        "count_total": 787,
        "cs": 5.3,
        "deleted_at": null,
        "drain": 5.5,
        "hit_length": 158,
        "is_scoreable": true,
        "last_updated": "2019-10-27T12:39:03+00:00",
        "mode_int": 0,
        "passcount": 360,
        "playcount": 5121,
        "ranked": 1,
        "status": "ranked",
        "total_length": 177,
        "url": "https://osu.ppy.sh/beatmaps/2096611"
      },
      {
        "difficulty_rating": 2.36,
        "id": 2105912,
        "mode": "osu",
        "version": "Normal",
        "accuracy": 4,
        "ar": 5,
        "beatmapset_id": 1001546,
        "bpm": 178,
        "convert": null,
        "count_circles": 102,
        "count_sliders": 167,
        "count_spinners": 1,
        "count_total": 439,
        "cs": 4,
        "deleted_at": null,
        "drain": 4,
        "hit_length": 143,
        "is_scoreable": true,
        "last_updated": "2019-10-27T12:39:04+00:00",
        "mode_int": 0,
        "passcount": 1989,
        "playcount": 5409,
        "ranked": 1,
        "status": "ranked",
        "total_length": 177,
        "url": "https://osu.ppy.sh/beatmaps/2105912"
      },
      {
        "difficulty_rating": 5.39,
        "id": 2105913,
        "mode": "osu",
        "version": "squirrelp's Traffic Jam Dreams",
        "accuracy": 8,
        "ar": 9.3,
        "beatmapset_id": 1001546,
        "bpm": 178,
        "convert": null,
        "count_circles": 329,
        "count_sliders": 279,
        "count_spinners": 1,
        "count_total": 890,
        "cs": 5.4,
        "deleted_at": null,
        "drain": 5,
        "hit_length": 167,
        "is_scoreable": true,
        "last_updated": "2019-10-27T12:39:04+00:00",
        "mode_int": 0,
        "passcount": 1062,
        "playcount": 6903,
        "ranked": 1,
        "status": "ranked",
        "total_length": 177,
        "url": "https://osu.ppy.sh/beatmaps/2105913"
      },
      {
        "difficulty_rating": 3.26,
        "id": 2126008,
        "mode": "osu",
        "version": "Hard",
        "accuracy": 6,
        "ar": 8,
        "beatmapset_id": 1001546,
        "bpm": 178,
        "convert": null,
        "count_circles": 131,
        "count_sliders": 236,
        "count_spinners": 2,
        "count_total": 609,
        "cs": 4.5,
        "deleted_at": null,
        "drain": 4,
        "hit_length": 141,
        "is_scoreable": true,
        "last_updated": "2019-10-27T12:39:05+00:00",
        "mode_int": 0,
        "passcount": 3438,
        "playcount": 9567,
        "ranked": 1,
        "status": "ranked",
        "total_length": 177,
        "url": "https://osu.ppy.sh/beatmaps/2126008"
      },
      {
        "difficulty_rating": 4.38,
        "id": 2162331,
        "mode": "osu",
        "version": "Insane",
        "accuracy": 7,
        "ar": 8,
        "beatmapset_id": 1001546,
        "bpm": 178,
        "convert": null,
        "count_circles": 237,
        "count_sliders": 235,
        "count_spinners": 2,
        "count_total": 713,
        "cs": 5,
        "deleted_at": null,
        "drain": 5,
        "hit_length": 142,
        "is_scoreable": true,
        "last_updated": "2019-10-27T12:39:05+00:00",
        "mode_int": 0,
        "passcount": 504,
        "playcount": 5886,
        "ranked": 1,
        "status": "ranked",
        "total_length": 177,
        "url": "https://osu.ppy.sh/beatmaps/2162331"
      }
    ],
    "discussions": [
      {
        "id": 1067441,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 1372608,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-07-13T04:25:40+00:00",
        "updated_at": "2019-07-13T04:25:40+00:00",
        "deleted_at": null,
        "last_post_at": "2019-07-13T04:25:40+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3016640,
            "beatmap_discussion_id": 1067441,
            "user_id": 1372608,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "I'm hyping this, I can see this map being an interesting mapset!",
            "created_at": "2019-07-13T04:25:40+00:00",
            "updated_at": "2019-07-13T04:25:40+00:00",
            "deleted_at": null
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
        "id": 1081661,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 1555865,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-07-20T18:26:51+00:00",
        "updated_at": "2019-07-20T18:26:51+00:00",
        "deleted_at": null,
        "last_post_at": "2019-07-20T18:26:51+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3056324,
            "beatmap_discussion_id": 1081661,
            "user_id": 1555865,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "(:",
            "created_at": "2019-07-20T18:26:51+00:00",
            "updated_at": "2019-07-20T18:26:51+00:00",
            "deleted_at": null
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
        "id": 1089140,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 1249323,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-07-25T07:05:20+00:00",
        "updated_at": "2019-07-25T07:05:20+00:00",
        "deleted_at": null,
        "last_post_at": "2019-07-25T07:05:20+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3077704,
            "beatmap_discussion_id": 1089140,
            "user_id": 1249323,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "wat dis",
            "created_at": "2019-07-25T07:05:20+00:00",
            "updated_at": "2019-07-25T07:05:20+00:00",
            "deleted_at": null
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
        "id": 1103785,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 197805,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-08-03T09:44:49+00:00",
        "updated_at": "2019-08-07T07:02:43+00:00",
        "deleted_at": null,
        "last_post_at": "2019-08-07T07:02:43+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3118551,
            "beatmap_discussion_id": 1103785,
            "user_id": 197805,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "http://cdn.discordapp.com/attachments/548378597476532236/607146667170594836/unknown.png\n\n\"mappes' guild\" :(",
            "created_at": "2019-08-03T09:44:49+00:00",
            "updated_at": "2019-08-03T09:44:49+00:00",
            "deleted_at": null
          },
          {
            "id": 3135904,
            "beatmap_discussion_id": 1103785,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fix e dt ha nk s ow o",
            "created_at": "2019-08-07T07:02:43+00:00",
            "updated_at": "2019-08-07T07:02:43+00:00",
            "deleted_at": null
          },
          {
            "id": 3135905,
            "beatmap_discussion_id": 1103785,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-08-07T07:02:43+00:00",
            "updated_at": "2019-08-07T07:02:43+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1103786,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 197805,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-08-03T09:44:52+00:00",
        "updated_at": "2019-08-03T09:44:52+00:00",
        "deleted_at": null,
        "last_post_at": "2019-08-03T09:44:52+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3118552,
            "beatmap_discussion_id": 1103786,
            "user_id": 197805,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "owo",
            "created_at": "2019-08-03T09:44:52+00:00",
            "updated_at": "2019-08-03T09:44:52+00:00",
            "deleted_at": null
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
        "id": 1131775,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 6151332,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-08-19T04:20:58+00:00",
        "updated_at": "2019-08-19T08:42:15+00:00",
        "deleted_at": null,
        "last_post_at": "2019-08-19T08:42:15+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3194765,
            "beatmap_discussion_id": 1131775,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "cute owo",
            "created_at": "2019-08-19T04:20:58+00:00",
            "updated_at": "2019-08-19T04:20:58+00:00",
            "deleted_at": null
          },
          {
            "id": 3195382,
            "beatmap_discussion_id": 1131775,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "no u",
            "created_at": "2019-08-19T08:42:15+00:00",
            "updated_at": "2019-08-19T08:42:15+00:00",
            "deleted_at": null
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
        "id": 1173741,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 7614055,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-09-15T14:35:47+00:00",
        "updated_at": "2019-09-15T14:35:47+00:00",
        "deleted_at": null,
        "last_post_at": "2019-09-15T14:35:47+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3310840,
            "beatmap_discussion_id": 1173741,
            "user_id": 7614055,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": ".",
            "created_at": "2019-09-15T14:35:47+00:00",
            "updated_at": "2019-09-15T14:35:47+00:00",
            "deleted_at": null
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
        "id": 1181961,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105912,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 7709,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T03:45:18+00:00",
        "updated_at": "2019-10-08T02:56:06+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:56:06+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333513,
            "beatmap_discussion_id": 1181961,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:07:709 (4) - Hmmmmm, there is nothing I guess. Maybe its better to follow 00:08:058 -.",
            "created_at": "2019-09-21T03:45:18+00:00",
            "updated_at": "2019-09-21T03:45:18+00:00",
            "deleted_at": null
          },
          {
            "id": 3333519,
            "beatmap_discussion_id": 1181961,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:12:593 (3) -  ↑  00:13:639 - following here is better",
            "created_at": "2019-09-21T03:46:08+00:00",
            "updated_at": "2019-09-21T03:46:08+00:00",
            "deleted_at": null
          },
          {
            "id": 3333524,
            "beatmap_discussion_id": 1181961,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:16:081 (2) - ↑  00:15:035 - ↑",
            "created_at": "2019-09-21T03:46:58+00:00",
            "updated_at": "2019-09-21T03:46:58+00:00",
            "deleted_at": null
          },
          {
            "id": 3401648,
            "beatmap_discussion_id": 1181961,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "every 1/2 ticks have guitar sound so every 1/2 rhythms are fine to be clickable, but I just prioritized the instrument sounds. but I would like to fill those because without them there would be way much 1/1 rhythms and be less interesting to play : /",
            "created_at": "2019-10-08T02:56:06+00:00",
            "updated_at": "2019-10-08T02:56:06+00:00",
            "deleted_at": null
          },
          {
            "id": 3401649,
            "beatmap_discussion_id": 1181961,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:56:06+00:00",
            "updated_at": "2019-10-08T02:56:06+00:00",
            "deleted_at": null
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
        "id": 1181966,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105912,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 122477,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T03:52:02+00:00",
        "updated_at": "2019-10-08T02:59:17+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:59:17+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333540,
            "beatmap_discussion_id": 1181966,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:02:477 (6,7) - maybe ctrl+g rhythm is better",
            "created_at": "2019-09-21T03:52:02+00:00",
            "updated_at": "2019-09-21T03:52:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3401661,
            "beatmap_discussion_id": 1181966,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "having a circle at drum 02:02:825 - emphasizes the instrument better i think, also intensity of drum drops at 02:02:477 - so i thought 02:02:651 - should not be clickable in order to follow the song's mood",
            "created_at": "2019-10-08T02:59:17+00:00",
            "updated_at": "2019-10-08T02:59:17+00:00",
            "deleted_at": null
          },
          {
            "id": 3401662,
            "beatmap_discussion_id": 1181966,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:59:17+00:00",
            "updated_at": "2019-10-08T02:59:17+00:00",
            "deleted_at": null
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
        "id": 1181972,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105912,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 81139,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T03:56:26+00:00",
        "updated_at": "2019-10-08T02:58:28+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:58:28+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333550,
            "beatmap_discussion_id": 1181972,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:21:139 (1,1) - It's unnecessary imo, how about use 1/2 reverse sliders here. Its not best choice to make the space in normal diff. Btw u should remove NC if u change them :3",
            "created_at": "2019-09-21T03:56:26+00:00",
            "updated_at": "2019-09-21T03:56:26+00:00",
            "deleted_at": null
          },
          {
            "id": 3401659,
            "beatmap_discussion_id": 1181972,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "removed the yellow 1 to give more break",
            "created_at": "2019-10-08T02:58:28+00:00",
            "updated_at": "2019-10-08T02:58:28+00:00",
            "deleted_at": null
          },
          {
            "id": 3401660,
            "beatmap_discussion_id": 1181972,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:58:28+00:00",
            "updated_at": "2019-10-08T02:58:28+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1181975,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105912,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 136256,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:03:02+00:00",
        "updated_at": "2019-10-08T03:01:14+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T03:01:14+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333559,
            "beatmap_discussion_id": 1181975,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:16:256 (2,3,4,5,6,7,8,9) - maybe its a bit long, u can try something like http://osu.ppy.sh/ss/13866130/3859",
            "created_at": "2019-09-21T04:03:02+00:00",
            "updated_at": "2019-09-21T04:03:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3401666,
            "beatmap_discussion_id": 1181975,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "oki",
            "created_at": "2019-10-08T03:01:14+00:00",
            "updated_at": "2019-10-08T03:01:14+00:00",
            "deleted_at": null
          },
          {
            "id": 3401667,
            "beatmap_discussion_id": 1181975,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T03:01:14+00:00",
            "updated_at": "2019-10-08T03:01:14+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1181977,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105912,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 174628,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:05:26+00:00",
        "updated_at": "2019-10-08T03:01:47+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T03:01:47+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333561,
            "beatmap_discussion_id": 1181977,
            "user_id": 9590557,
            "last_editor_id": 9590557,
            "deleted_by_id": null,
            "system": false,
            "message": "02:54:628 (1,2) - how about making 1/2 sliders? There are all clear sound and it would be better to play imo",
            "created_at": "2019-09-21T04:05:26+00:00",
            "updated_at": "2019-09-21T04:05:48+00:00",
            "deleted_at": null
          },
          {
            "id": 3401669,
            "beatmap_discussion_id": 1181977,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i would like to emphasize the snare sound :ablobwob:",
            "created_at": "2019-10-08T03:01:47+00:00",
            "updated_at": "2019-10-08T03:01:47+00:00",
            "deleted_at": null
          },
          {
            "id": 3401670,
            "beatmap_discussion_id": 1181977,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T03:01:47+00:00",
            "updated_at": "2019-10-08T03:01:47+00:00",
            "deleted_at": null
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
        "id": 1181978,
        "beatmapset_id": 1001546,
        "beatmap_id": 2126008,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 34395,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:08:46+00:00",
        "updated_at": "2019-10-08T02:48:18+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:48:18+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333562,
            "beatmap_discussion_id": 1181978,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:34:395 - how about following here? I dont think 3/2 slider is a good idea, cause the vocal and drum are clear.",
            "created_at": "2019-09-21T04:08:46+00:00",
            "updated_at": "2019-09-21T04:08:46+00:00",
            "deleted_at": null
          },
          {
            "id": 3401613,
            "beatmap_discussion_id": 1181978,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok",
            "created_at": "2019-10-08T02:48:18+00:00",
            "updated_at": "2019-10-08T02:48:18+00:00",
            "deleted_at": null
          },
          {
            "id": 3401614,
            "beatmap_discussion_id": 1181978,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:48:18+00:00",
            "updated_at": "2019-10-08T02:48:18+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1181980,
        "beatmapset_id": 1001546,
        "beatmap_id": 2126008,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 38581,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:12:19+00:00",
        "updated_at": "2019-10-08T02:50:30+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:50:30+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333573,
            "beatmap_discussion_id": 1181980,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:38:581 (2) - maybe it would be better if u change the slider into 1/4 reverse sliders. You follow the drums with 1/4 rhythm like 00:16:779 (2,3,4) - 00:11:197 (2,3,1) -, so u'd better keep consistence.",
            "created_at": "2019-09-21T04:12:19+00:00",
            "updated_at": "2019-09-21T04:12:19+00:00",
            "deleted_at": null
          },
          {
            "id": 3333575,
            "beatmap_discussion_id": 1181980,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:49:046 (1) - u can make it like 00:44:511 (6,7,1) -",
            "created_at": "2019-09-21T04:13:28+00:00",
            "updated_at": "2019-09-21T04:13:28+00:00",
            "deleted_at": null
          },
          {
            "id": 3333839,
            "beatmap_discussion_id": 1181980,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "I think two single reverse 1/4 sliders would be more fitting for a hard diff just to simplify it a bit, the slider doesn't really fit at all imo",
            "created_at": "2019-09-21T05:40:39+00:00",
            "updated_at": "2019-09-21T05:40:39+00:00",
            "deleted_at": null
          },
          {
            "id": 3401620,
            "beatmap_discussion_id": 1181980,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "mainly I want to keep the least triplets except sections like 02:14:163 (1,2,3,4,5,6,1,2,3,4,5,1,2,1,2,3,4,5,6,1,2,3) - or kiai moment, as the entire diff don't share a lot of streams and having a lot of stream pattern on hard would make the play harder. so I used same slider length with red node which gives emphasize enougly, also the differentiation with 01:23:232 (2,3,4) - is the reason too",
            "created_at": "2019-10-08T02:50:30+00:00",
            "updated_at": "2019-10-08T02:50:30+00:00",
            "deleted_at": null
          },
          {
            "id": 3401621,
            "beatmap_discussion_id": 1181980,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:50:30+00:00",
            "updated_at": "2019-10-08T02:50:30+00:00",
            "deleted_at": null
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
        "id": 1181992,
        "beatmapset_id": 1001546,
        "beatmap_id": 2126008,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 81488,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:21:36+00:00",
        "updated_at": "2019-10-08T02:51:35+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:51:35+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333607,
            "beatmap_discussion_id": 1181992,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:21:488 (1) - There are powerful drums, the reverse slider is a bit weird with the music. Just like http://osu.ppy.sh/ss/13866172/2da7",
            "created_at": "2019-09-21T04:21:36+00:00",
            "updated_at": "2019-09-21T04:21:36+00:00",
            "deleted_at": null
          },
          {
            "id": 3401629,
            "beatmap_discussion_id": 1181992,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "as the intensity suddenly drops 01:21:139 - i want to use loose rhythm here :ablobnom:",
            "created_at": "2019-10-08T02:51:35+00:00",
            "updated_at": "2019-10-08T02:51:35+00:00",
            "deleted_at": null
          },
          {
            "id": 3401630,
            "beatmap_discussion_id": 1181992,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:51:35+00:00",
            "updated_at": "2019-10-08T02:51:35+00:00",
            "deleted_at": null
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
        "id": 1181995,
        "beatmapset_id": 1001546,
        "beatmap_id": 2126008,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 139570,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:23:03+00:00",
        "updated_at": "2019-10-08T02:53:07+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:53:07+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333618,
            "beatmap_discussion_id": 1181995,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:19:570 (3) - how about making a 1/4 reverse slider?",
            "created_at": "2019-09-21T04:23:03+00:00",
            "updated_at": "2019-09-21T04:23:03+00:00",
            "deleted_at": null
          },
          {
            "id": 3401636,
            "beatmap_discussion_id": 1181995,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i think sliderend of 1/4 reverse rolls are a lot stronger than 1/2 sliders. also the intensity suddenly drops and fade outs at 02:19:744 - so I wanted to use object with minimum intensity I could use here, which indicates 1/2 rhythm usage. so i would like to keep this",
            "created_at": "2019-10-08T02:53:07+00:00",
            "updated_at": "2019-10-08T02:53:07+00:00",
            "deleted_at": null
          },
          {
            "id": 3401637,
            "beatmap_discussion_id": 1181995,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:53:07+00:00",
            "updated_at": "2019-10-08T02:53:07+00:00",
            "deleted_at": null
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
        "id": 1182000,
        "beatmapset_id": 1001546,
        "beatmap_id": 2162331,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 11022,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:28:57+00:00",
        "updated_at": "2019-10-04T11:52:57+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:52:57+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333635,
            "beatmap_discussion_id": 1182000,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:11:022 (3,4,5,1) - u can stress the sound by making the circles like http://puu.sh/EjC3H/1a072eded2.png",
            "created_at": "2019-09-21T04:28:57+00:00",
            "updated_at": "2019-09-21T04:28:57+00:00",
            "deleted_at": null
          },
          {
            "id": 3385177,
            "beatmap_discussion_id": 1182000,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "tried something different",
            "created_at": "2019-10-04T11:52:57+00:00",
            "updated_at": "2019-10-04T11:52:57+00:00",
            "deleted_at": null
          },
          {
            "id": 3385178,
            "beatmap_discussion_id": 1182000,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:52:57+00:00",
            "updated_at": "2019-10-04T11:52:57+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182008,
        "beatmapset_id": 1001546,
        "beatmap_id": 2162331,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 80442,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:34:42+00:00",
        "updated_at": "2019-10-04T11:53:45+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:53:45+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333653,
            "beatmap_discussion_id": 1182008,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:20:442 (3,4,5) - ctrl+g ? 01:19:918 (2,3) -  the space is weird to play imo.",
            "created_at": "2019-09-21T04:34:42+00:00",
            "updated_at": "2019-09-21T04:34:42+00:00",
            "deleted_at": null
          },
          {
            "id": 3385180,
            "beatmap_discussion_id": 1182008,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i think current one should be fine",
            "created_at": "2019-10-04T11:53:45+00:00",
            "updated_at": "2019-10-04T11:53:45+00:00",
            "deleted_at": null
          },
          {
            "id": 3385181,
            "beatmap_discussion_id": 1182008,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:53:45+00:00",
            "updated_at": "2019-10-04T11:53:45+00:00",
            "deleted_at": null
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
        "id": 1182010,
        "beatmapset_id": 1001546,
        "beatmap_id": 2162331,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:36:55+00:00",
        "updated_at": "2019-10-08T02:44:52+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:44:52+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333656,
            "beatmap_discussion_id": 1182010,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:33:872 (1,2,3,1,2,3) - etc. maybe u need fix the triples like them...  they are not in line.",
            "created_at": "2019-09-21T04:36:55+00:00",
            "updated_at": "2019-09-21T04:36:55+00:00",
            "deleted_at": null
          },
          {
            "id": 3401607,
            "beatmap_discussion_id": 1182010,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "not quite sure if i really should fix this but tried to polish those more",
            "created_at": "2019-10-08T02:44:52+00:00",
            "updated_at": "2019-10-08T02:44:52+00:00",
            "deleted_at": null
          },
          {
            "id": 3401608,
            "beatmap_discussion_id": 1182010,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:44:52+00:00",
            "updated_at": "2019-10-08T02:44:52+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182011,
        "beatmapset_id": 1001546,
        "beatmap_id": 2162331,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 159104,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:38:31+00:00",
        "updated_at": "2019-10-04T11:54:24+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:54:24+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333657,
            "beatmap_discussion_id": 1182011,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:39:104 (4,1) - maybe triple is better",
            "created_at": "2019-09-21T04:38:31+00:00",
            "updated_at": "2019-09-21T04:38:31+00:00",
            "deleted_at": null
          },
          {
            "id": 3385185,
            "beatmap_discussion_id": 1182011,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i would keep the structure 02:38:581 (3,1) - here which i cant keep when using triple. I really like this one and wanna maintain it : /",
            "created_at": "2019-10-04T11:54:24+00:00",
            "updated_at": "2019-10-04T11:54:24+00:00",
            "deleted_at": null
          },
          {
            "id": 3385186,
            "beatmap_discussion_id": 1182011,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:54:24+00:00",
            "updated_at": "2019-10-04T11:54:24+00:00",
            "deleted_at": null
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
        "id": 1182017,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:40:46+00:00",
        "updated_at": "2019-10-04T11:50:41+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:50:41+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333663,
            "beatmap_discussion_id": 1182017,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:08:232 (5) - need fix too ;-;",
            "created_at": "2019-09-21T04:40:46+00:00",
            "updated_at": "2019-09-21T04:40:46+00:00",
            "deleted_at": null
          },
          {
            "id": 3385169,
            "beatmap_discussion_id": 1182017,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "done",
            "created_at": "2019-10-04T11:50:41+00:00",
            "updated_at": "2019-10-04T11:50:41+00:00",
            "deleted_at": null
          },
          {
            "id": 3385170,
            "beatmap_discussion_id": 1182017,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:50:41+00:00",
            "updated_at": "2019-10-04T11:50:41+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182021,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 573,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:43:11+00:00",
        "updated_at": "2019-10-08T02:42:31+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:42:31+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333669,
            "beatmap_discussion_id": 1182021,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:00:573 (3,4,1) - maybe a rhythm like this would work better? https://osu.ppy.sh/ss/13866203/2664 right now it doesn't feel like the guitar notes are being emphasized as they should",
            "created_at": "2019-09-21T04:43:11+00:00",
            "updated_at": "2019-09-21T04:43:11+00:00",
            "deleted_at": null
          },
          {
            "id": 3333676,
            "beatmap_discussion_id": 1182021,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:01:257 - also the timing point here means this slider end is unsnapped 00:01:085 (4) - so if you want to keep this rhythm you should move the timing point to 00:01:429 - instead",
            "created_at": "2019-09-21T04:45:10+00:00",
            "updated_at": "2019-09-21T04:45:10+00:00",
            "deleted_at": null
          },
          {
            "id": 3386388,
            "beatmap_discussion_id": 1182021,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "want to keep this longer slider because this is a more chill section + it adds rhythm variety from the other 1/2 sliders in the intro. snapped the slider end",
            "created_at": "2019-10-04T19:11:02+00:00",
            "updated_at": "2019-10-04T19:11:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3401578,
            "beatmap_discussion_id": 1182021,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "!",
            "created_at": "2019-10-08T02:42:31+00:00",
            "updated_at": "2019-10-08T02:42:31+00:00",
            "deleted_at": null
          },
          {
            "id": 3401579,
            "beatmap_discussion_id": 1182021,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:42:31+00:00",
            "updated_at": "2019-10-08T02:42:31+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6151332
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182025,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 33523,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:46:18+00:00",
        "updated_at": "2019-10-04T11:40:08+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:40:08+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333678,
            "beatmap_discussion_id": 1182025,
            "user_id": 9590557,
            "last_editor_id": 9590557,
            "deleted_by_id": null,
            "system": false,
            "message": "00:33:523 (1,2,3) - need nerf. \n1. The space is weird with slight sound here.\n2. 00:38:581 (1,2,3,4,5,6,7,8) - the powerful drums stream u make is 0.25x. The sound shouldn't be made with 2.0x\n3. 00:44:686 (8,9,1) - the drums in kiai is powerful and u make it with 1.0x. \nAbove all, stacking the triple is better.",
            "created_at": "2019-09-21T04:46:18+00:00",
            "updated_at": "2019-09-21T04:51:06+00:00",
            "deleted_at": null
          },
          {
            "id": 3333734,
            "beatmap_discussion_id": 1182025,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:00:035 (1,2,1) - ↑",
            "created_at": "2019-09-21T05:04:06+00:00",
            "updated_at": "2019-09-21T05:04:06+00:00",
            "deleted_at": null
          },
          {
            "id": 3385124,
            "beatmap_discussion_id": 1182025,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "cool",
            "created_at": "2019-10-04T11:40:08+00:00",
            "updated_at": "2019-10-04T11:40:08+00:00",
            "deleted_at": null
          },
          {
            "id": 3385125,
            "beatmap_discussion_id": 1182025,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:40:08+00:00",
            "updated_at": "2019-10-04T11:40:08+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182028,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 38930,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:48:44+00:00",
        "updated_at": "2019-10-08T02:42:34+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:42:34+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333683,
            "beatmap_discussion_id": 1182028,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:38:930 (1,2,3) - these drums sound the same as 00:38:581 (1,2,3) - to me so I think keeping equal spacing would be more fitting",
            "created_at": "2019-09-21T04:48:44+00:00",
            "updated_at": "2019-09-21T04:48:44+00:00",
            "deleted_at": null
          },
          {
            "id": 3333796,
            "beatmap_discussion_id": 1182028,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "or keep consistent space with 01:23:582 (1,2,3,4) -",
            "created_at": "2019-09-21T05:25:01+00:00",
            "updated_at": "2019-09-21T05:25:01+00:00",
            "deleted_at": null
          },
          {
            "id": 3386389,
            "beatmap_discussion_id": 1182028,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "did the equal spacing",
            "created_at": "2019-10-04T19:12:31+00:00",
            "updated_at": "2019-10-04T19:12:31+00:00",
            "deleted_at": null
          },
          {
            "id": 3401580,
            "beatmap_discussion_id": 1182028,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "v!",
            "created_at": "2019-10-08T02:42:34+00:00",
            "updated_at": "2019-10-08T02:42:34+00:00",
            "deleted_at": null
          },
          {
            "id": 3401581,
            "beatmap_discussion_id": 1182028,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:42:34+00:00",
            "updated_at": "2019-10-08T02:42:34+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6151332
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182033,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 55325,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:50:59+00:00",
        "updated_at": "2019-10-08T02:42:39+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:42:39+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333690,
            "beatmap_discussion_id": 1182033,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:55:325 (5,6,7) - I don't think stopping movement entirely makes much sense here, there should be contrast with 00:54:628 (1,2,3,4) - though so maybe a more linear movement like this would work better? https://osu.ppy.sh/ss/13866225/a012",
            "created_at": "2019-09-21T04:50:59+00:00",
            "updated_at": "2019-09-21T04:50:59+00:00",
            "deleted_at": null
          },
          {
            "id": 3333696,
            "beatmap_discussion_id": 1182033,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:01:081 (7,8,1) - you actually did this here so it'd also make sense for consistency",
            "created_at": "2019-09-21T04:53:06+00:00",
            "updated_at": "2019-09-21T04:53:06+00:00",
            "deleted_at": null
          },
          {
            "id": 3386414,
            "beatmap_discussion_id": 1182033,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i wanted there to be movement between the high guitar notes 00:54:628 (1,2,3,4) - and no movement between the low ones 00:55:325 (5,6,7) -  i made this consistent with what you pointed out :3c",
            "created_at": "2019-10-04T19:25:35+00:00",
            "updated_at": "2019-10-04T19:25:35+00:00",
            "deleted_at": null
          },
          {
            "id": 3401584,
            "beatmap_discussion_id": 1182033,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "!",
            "created_at": "2019-10-08T02:42:39+00:00",
            "updated_at": "2019-10-08T02:42:39+00:00",
            "deleted_at": null
          },
          {
            "id": 3401585,
            "beatmap_discussion_id": 1182033,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:42:39+00:00",
            "updated_at": "2019-10-08T02:42:39+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6151332
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182036,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 58639,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:53:53+00:00",
        "updated_at": "2019-10-04T11:43:02+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:43:02+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333699,
            "beatmap_discussion_id": 1182036,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:58:639 (1,2,3) - ctrl+g is better imo. 00:58:465 (3,1) - no movement is weird here, cause the powerful drum.",
            "created_at": "2019-09-21T04:53:53+00:00",
            "updated_at": "2019-09-21T04:53:53+00:00",
            "deleted_at": null
          },
          {
            "id": 3333720,
            "beatmap_discussion_id": 1182036,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:43:291 (1,2,3) - ↑",
            "created_at": "2019-09-21T05:00:35+00:00",
            "updated_at": "2019-09-21T05:00:35+00:00",
            "deleted_at": null
          },
          {
            "id": 3385133,
            "beatmap_discussion_id": 1182036,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "having stack for coming intense triple could give more emphasizing effect i think. as the map concept (limited structure) blocks giving a lot high spacing and I would use antijump stuff here",
            "created_at": "2019-10-04T11:43:02+00:00",
            "updated_at": "2019-10-04T11:43:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3385134,
            "beatmap_discussion_id": 1182036,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:43:02+00:00",
            "updated_at": "2019-10-04T11:43:02+00:00",
            "deleted_at": null
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
        "id": 1182039,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 61605,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:55:29+00:00",
        "updated_at": "2019-10-04T11:43:58+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:43:58+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333702,
            "beatmap_discussion_id": 1182039,
            "user_id": 9590557,
            "last_editor_id": 9590557,
            "deleted_by_id": null,
            "system": false,
            "message": "01:01:605 (1,1,1) - maybe you could enlarge the space here to 1.0x. Like 01:45:907 (7,8,1) -",
            "created_at": "2019-09-21T04:55:29+00:00",
            "updated_at": "2019-09-21T05:01:04+00:00",
            "deleted_at": null
          },
          {
            "id": 3333790,
            "beatmap_discussion_id": 1182039,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "this could also be misread as a triple since it has similar spacing to 00:58:639 (1,2,3) - etc., an overlap like this with increased spacing looks nice imo https://osu.ppy.sh/ss/13866284/6823 but this map is also heavily based on reading, so keeping it the same should be fine too",
            "created_at": "2019-09-21T05:21:27+00:00",
            "updated_at": "2019-09-21T05:21:27+00:00",
            "deleted_at": null
          },
          {
            "id": 3385135,
            "beatmap_discussion_id": 1182039,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nice idea but I think it should work fine since the nc spam says its different than 01:01:256 (1,2,1) - this triplets. also as its a part of reading too",
            "created_at": "2019-10-04T11:43:58+00:00",
            "updated_at": "2019-10-04T11:43:58+00:00",
            "deleted_at": null
          },
          {
            "id": 3385136,
            "beatmap_discussion_id": 1182039,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:43:58+00:00",
            "updated_at": "2019-10-04T11:43:58+00:00",
            "deleted_at": null
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
        "id": 1182041,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 79308,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:56:33+00:00",
        "updated_at": "2019-10-08T02:42:43+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:42:43+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333704,
            "beatmap_discussion_id": 1182041,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:19:308 (2) - a double w/ a 1/2 slider would fit the drums better while still emphasizing the vocals imo",
            "created_at": "2019-09-21T04:56:33+00:00",
            "updated_at": "2019-09-21T04:56:33+00:00",
            "deleted_at": null
          },
          {
            "id": 3386420,
            "beatmap_discussion_id": 1182041,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "trying to avoid rhythm being too dense here because it's a slower section. personally i'd rather save doubles for more noticeable notes like 01:18:261 (3,1) -",
            "created_at": "2019-10-04T19:27:40+00:00",
            "updated_at": "2019-10-04T19:27:40+00:00",
            "deleted_at": null
          },
          {
            "id": 3401588,
            "beatmap_discussion_id": 1182041,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "!",
            "created_at": "2019-10-08T02:42:43+00:00",
            "updated_at": "2019-10-08T02:42:43+00:00",
            "deleted_at": null
          },
          {
            "id": 3401589,
            "beatmap_discussion_id": 1182041,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:42:43+00:00",
            "updated_at": "2019-10-08T02:42:43+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6151332
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182042,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 83580,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T04:57:41+00:00",
        "updated_at": "2019-10-04T11:44:26+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:44:26+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333707,
            "beatmap_discussion_id": 1182042,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:23:580 (5,6,7,8) - the sound here is powerful, enlarge the space is better. Its different with 01:23:232 (1,2,3,4) -.",
            "created_at": "2019-09-21T04:57:41+00:00",
            "updated_at": "2019-09-21T04:57:41+00:00",
            "deleted_at": null
          },
          {
            "id": 3385139,
            "beatmap_discussion_id": 1182042,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "NCed 5",
            "created_at": "2019-10-04T11:44:26+00:00",
            "updated_at": "2019-10-04T11:44:26+00:00",
            "deleted_at": null
          },
          {
            "id": 3385140,
            "beatmap_discussion_id": 1182042,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:44:26+00:00",
            "updated_at": "2019-10-04T11:44:26+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182044,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 94221,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:00:06+00:00",
        "updated_at": "2019-10-04T11:45:02+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:45:02+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333719,
            "beatmap_discussion_id": 1182044,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:34:221 (1,2,3) - u need change it to (3,1,2), the flow here is weird.  Just like u do at 01:34:570 (1,2,3) - 00:49:570 (1,2,3) - 00:49:919 (1,2,1) -.",
            "created_at": "2019-09-21T05:00:06+00:00",
            "updated_at": "2019-09-21T05:00:06+00:00",
            "deleted_at": null
          },
          {
            "id": 3385143,
            "beatmap_discussion_id": 1182044,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "makes sense",
            "created_at": "2019-10-04T11:45:02+00:00",
            "updated_at": "2019-10-04T11:45:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3385144,
            "beatmap_discussion_id": 1182044,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:45:02+00:00",
            "updated_at": "2019-10-04T11:45:02+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182046,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 102767,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:00:37+00:00",
        "updated_at": "2019-10-08T02:43:30+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:42:45+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333722,
            "beatmap_discussion_id": 1182046,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:42:767 (3) - It feels kinda weird to only map a triple when there's 5 snares in the music, I think it'd be better to just remove the reverse here and add notes to 01:43:116 - and 01:43:203 - instead",
            "created_at": "2019-09-21T05:00:37+00:00",
            "updated_at": "2019-09-21T05:00:37+00:00",
            "deleted_at": null
          },
          {
            "id": 3333723,
            "beatmap_discussion_id": 1182046,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:42:963 - also sounds like there should maybe be a timing point here? just to correct the drum kick, 01:43:116 - and afterwards sound fine to me",
            "created_at": "2019-09-21T05:02:08+00:00",
            "updated_at": "2019-09-21T05:02:08+00:00",
            "deleted_at": null
          },
          {
            "id": 3386424,
            "beatmap_discussion_id": 1182046,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "really want to prioritize vocals in these sections, especially this unique rhythm that the slider is mapped to rn. the 3 sliders before it in this section 01:40:674 (1,3,1) - all have 3/4 or 1/1 hold rhythms on the vocal note",
            "created_at": "2019-10-04T19:30:59+00:00",
            "updated_at": "2019-10-04T19:30:59+00:00",
            "deleted_at": null
          },
          {
            "id": 3401590,
            "beatmap_discussion_id": 1182046,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "!",
            "created_at": "2019-10-08T02:42:45+00:00",
            "updated_at": "2019-10-08T02:42:45+00:00",
            "deleted_at": null
          },
          {
            "id": 3401591,
            "beatmap_discussion_id": 1182046,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:42:45+00:00",
            "updated_at": "2019-10-08T02:42:45+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182048,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 139395,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:05:14+00:00",
        "updated_at": "2019-10-08T02:42:59+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:42:59+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333756,
            "beatmap_discussion_id": 1182048,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:19:395 (1) - I would either decrease SV a bit or increase the angle of the curve, it seems pretty easy to sliderbreak here if you're not expecting this to be a 1/4 slider",
            "created_at": "2019-09-21T05:05:14+00:00",
            "updated_at": "2019-09-21T05:05:14+00:00",
            "deleted_at": null
          },
          {
            "id": 3333762,
            "beatmap_discussion_id": 1182048,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:54:628 (1) - similar thing here as well",
            "created_at": "2019-09-21T05:07:17+00:00",
            "updated_at": "2019-09-21T05:07:17+00:00",
            "deleted_at": null
          },
          {
            "id": 3386428,
            "beatmap_discussion_id": 1182048,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nerfed first one from 1.8 -> 1.6. second one is a lot easier to read than it look. cant explain why but i was worried about it too then testplayers seemed to have no problem",
            "created_at": "2019-10-04T19:32:54+00:00",
            "updated_at": "2019-10-04T19:32:54+00:00",
            "deleted_at": null
          },
          {
            "id": 3401596,
            "beatmap_discussion_id": 1182048,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "!",
            "created_at": "2019-10-08T02:42:59+00:00",
            "updated_at": "2019-10-08T02:42:59+00:00",
            "deleted_at": null
          },
          {
            "id": 3401597,
            "beatmap_discussion_id": 1182048,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:42:59+00:00",
            "updated_at": "2019-10-08T02:42:59+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      [],
      {
        "id": 1182053,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 122651,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:07:02+00:00",
        "updated_at": "2019-10-04T11:45:24+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:45:24+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333761,
            "beatmap_discussion_id": 1182053,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:02:651 (1,2) - how about ctrl+g? 02:02:477 (3,1) - need large space",
            "created_at": "2019-09-21T05:07:02+00:00",
            "updated_at": "2019-09-21T05:07:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3385145,
            "beatmap_discussion_id": 1182053,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nc tells the different rhythm so should be i think",
            "created_at": "2019-10-04T11:45:24+00:00",
            "updated_at": "2019-10-04T11:45:24+00:00",
            "deleted_at": null
          },
          {
            "id": 3385146,
            "beatmap_discussion_id": 1182053,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:45:24+00:00",
            "updated_at": "2019-10-04T11:45:24+00:00",
            "deleted_at": null
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
        "id": 1182055,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 134075,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:09:20+00:00",
        "updated_at": "2019-10-04T11:45:46+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:45:46+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333764,
            "beatmap_discussion_id": 1182055,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:14:075 (5) - no sound here.  02:13:639 (2) - 02:13:988 (4) - are same, u'd better delete it if u dont follow the sound at 02:13:727 - .",
            "created_at": "2019-09-21T05:09:20+00:00",
            "updated_at": "2019-09-21T05:09:20+00:00",
            "deleted_at": null
          },
          {
            "id": 3385147,
            "beatmap_discussion_id": 1182055,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "oki",
            "created_at": "2019-10-04T11:45:46+00:00",
            "updated_at": "2019-10-04T11:45:46+00:00",
            "deleted_at": null
          },
          {
            "id": 3385148,
            "beatmap_discussion_id": 1182055,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:45:46+00:00",
            "updated_at": "2019-10-04T11:45:46+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182059,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 137128,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:09:50+00:00",
        "updated_at": "2019-10-04T11:46:49+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:46:49+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333768,
            "beatmap_discussion_id": 1182059,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:17:128 (3) - triple is better I guess",
            "created_at": "2019-09-21T05:09:50+00:00",
            "updated_at": "2019-09-21T05:09:50+00:00",
            "deleted_at": null
          },
          {
            "id": 3385151,
            "beatmap_discussion_id": 1182059,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "theres a drum sound but since 02:16:953 - starts to have different things on the music (vocals + instrument and etc) than 02:14:163 - I would like to differentiate to emphasize the triple sequences 02:14:163 (1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3) - here",
            "created_at": "2019-10-04T11:46:49+00:00",
            "updated_at": "2019-10-04T11:46:49+00:00",
            "deleted_at": null
          },
          {
            "id": 3385152,
            "beatmap_discussion_id": 1182059,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:46:49+00:00",
            "updated_at": "2019-10-04T11:46:49+00:00",
            "deleted_at": null
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
        "id": 1182060,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:10:54+00:00",
        "updated_at": "2019-10-08T03:02:17+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T03:02:17+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333769,
            "beatmap_discussion_id": 1182060,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Squirrel's diff has different combo colors from all the other diffs, I couldn't find anything in the ranking criteria about this, but I think they all have to be the same? I could be wrong tho",
            "created_at": "2019-09-21T05:10:54+00:00",
            "updated_at": "2019-09-21T05:10:54+00:00",
            "deleted_at": null
          },
          {
            "id": 3401672,
            "beatmap_discussion_id": 1182060,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "its fine to have different combo colors uwu",
            "created_at": "2019-10-08T03:02:17+00:00",
            "updated_at": "2019-10-08T03:02:17+00:00",
            "deleted_at": null
          },
          {
            "id": 3401673,
            "beatmap_discussion_id": 1182060,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T03:02:17+00:00",
            "updated_at": "2019-10-08T03:02:17+00:00",
            "deleted_at": null
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
        "id": 1182063,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 152825,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:14:45+00:00",
        "updated_at": "2019-10-04T11:48:53+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:48:53+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333774,
            "beatmap_discussion_id": 1182063,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:32:825 (1,2,3,1,2,3,4,5,6,1,1) - same weird flow. It would be better to play like http://puu.sh/EjCJD/b3bd0d3f65.png",
            "created_at": "2019-09-21T05:14:45+00:00",
            "updated_at": "2019-09-21T05:14:45+00:00",
            "deleted_at": null
          },
          {
            "id": 3385158,
            "beatmap_discussion_id": 1182063,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nice",
            "created_at": "2019-10-04T11:48:53+00:00",
            "updated_at": "2019-10-04T11:48:53+00:00",
            "deleted_at": null
          },
          {
            "id": 3385159,
            "beatmap_discussion_id": 1182063,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:48:53+00:00",
            "updated_at": "2019-10-04T11:48:53+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182065,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 166604,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:15:41+00:00",
        "updated_at": "2019-10-04T11:49:35+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:49:35+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333777,
            "beatmap_discussion_id": 1182065,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:46:604 (2,3) - need ctrl+g the rhythm",
            "created_at": "2019-09-21T05:15:41+00:00",
            "updated_at": "2019-09-21T05:15:41+00:00",
            "deleted_at": null
          },
          {
            "id": 3385161,
            "beatmap_discussion_id": 1182065,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "i believe it should be fine",
            "created_at": "2019-10-04T11:49:35+00:00",
            "updated_at": "2019-10-04T11:49:35+00:00",
            "deleted_at": null
          },
          {
            "id": 3385162,
            "beatmap_discussion_id": 1182065,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:49:35+00:00",
            "updated_at": "2019-10-04T11:49:35+00:00",
            "deleted_at": null
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
        "id": 1182067,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 42070,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:16:55+00:00",
        "updated_at": "2019-10-04T11:41:25+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:41:25+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333779,
            "beatmap_discussion_id": 1182067,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:42:070 (1) - the slider overlap is a bit uneven here, raise the red anchor a bit",
            "created_at": "2019-09-21T05:16:55+00:00",
            "updated_at": "2019-09-21T05:16:55+00:00",
            "deleted_at": null
          },
          {
            "id": 3333791,
            "beatmap_discussion_id": 1182067,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:27:418 (2) -",
            "created_at": "2019-09-21T05:22:54+00:00",
            "updated_at": "2019-09-21T05:22:54+00:00",
            "deleted_at": null
          },
          {
            "id": 3333794,
            "beatmap_discussion_id": 1182067,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:35:616 (7) -",
            "created_at": "2019-09-21T05:24:33+00:00",
            "updated_at": "2019-09-21T05:24:33+00:00",
            "deleted_at": null
          },
          {
            "id": 3333797,
            "beatmap_discussion_id": 1182067,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:40:325 (5) -",
            "created_at": "2019-09-21T05:25:06+00:00",
            "updated_at": "2019-09-21T05:25:06+00:00",
            "deleted_at": null
          },
          {
            "id": 3333798,
            "beatmap_discussion_id": 1182067,
            "user_id": 13009214,
            "last_editor_id": 13009214,
            "deleted_by_id": null,
            "system": false,
            "message": "02:42:418 (2,4) - these are snapped on the slider end, but the editor is weird so a quick ctrl+down arrow makes them overlap correctly",
            "created_at": "2019-09-21T05:25:55+00:00",
            "updated_at": "2019-09-21T05:26:24+00:00",
            "deleted_at": null
          },
          {
            "id": 3333800,
            "beatmap_discussion_id": 1182067,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:48:348 (2) -",
            "created_at": "2019-09-21T05:26:41+00:00",
            "updated_at": "2019-09-21T05:26:41+00:00",
            "deleted_at": null
          },
          {
            "id": 3385129,
            "beatmap_discussion_id": 1182067,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "id like to say perfectly snapped sliders are for reading challenge, as I think only giving approach circle to read would be interesting stuff and perfectly slider routes are not unrankable anymore so I would like to keep this",
            "created_at": "2019-10-04T11:41:25+00:00",
            "updated_at": "2019-10-04T11:41:25+00:00",
            "deleted_at": null
          },
          {
            "id": 3385130,
            "beatmap_discussion_id": 1182067,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:41:25+00:00",
            "updated_at": "2019-10-04T11:41:25+00:00",
            "deleted_at": null
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
        "id": 1182069,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 175325,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:17:54+00:00",
        "updated_at": "2019-10-04T11:50:02+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-04T11:50:02+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333782,
            "beatmap_discussion_id": 1182069,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:55:325 (1,2) - how about making something different with 02:54:628 (1,2) -? Just like your insane diff :3",
            "created_at": "2019-09-21T05:17:54+00:00",
            "updated_at": "2019-09-21T05:17:54+00:00",
            "deleted_at": null
          },
          {
            "id": 3385165,
            "beatmap_discussion_id": 1182069,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok",
            "created_at": "2019-10-04T11:50:02+00:00",
            "updated_at": "2019-10-04T11:50:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3385166,
            "beatmap_discussion_id": 1182069,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-04T11:50:02+00:00",
            "updated_at": "2019-10-04T11:50:02+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182075,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 58116,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:29:27+00:00",
        "updated_at": "2019-10-08T02:42:41+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:42:41+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333806,
            "beatmap_discussion_id": 1182075,
            "user_id": 9590557,
            "last_editor_id": 9590557,
            "deleted_by_id": null,
            "system": false,
            "message": "00:58:116 (1) - too slow to read. You'd better change the sv in to 0.8 or 0.75.",
            "created_at": "2019-09-21T05:29:27+00:00",
            "updated_at": "2019-09-21T05:40:56+00:00",
            "deleted_at": null
          },
          {
            "id": 3386418,
            "beatmap_discussion_id": 1182075,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "with the sv i use before the player will read this to end at 00:58:465 - so by then i think they should realize this is a reverse slider",
            "created_at": "2019-10-04T19:26:29+00:00",
            "updated_at": "2019-10-04T19:26:29+00:00",
            "deleted_at": null
          },
          {
            "id": 3401586,
            "beatmap_discussion_id": 1182075,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "!",
            "created_at": "2019-10-08T02:42:41+00:00",
            "updated_at": "2019-10-08T02:42:41+00:00",
            "deleted_at": null
          },
          {
            "id": 3401587,
            "beatmap_discussion_id": 1182075,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:42:41+00:00",
            "updated_at": "2019-10-08T02:42:41+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6151332
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182079,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 144628,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:32:19+00:00",
        "updated_at": "2019-10-08T02:43:32+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:43:07+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333810,
            "beatmap_discussion_id": 1182079,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:24:628 (1,2,3,4) - need change the spacing of 02:24:628 (1,2) - .  Like you do at 00:41:372 (1,2,3,4) - 01:26:023 (1,2,3,4) -",
            "created_at": "2019-09-21T05:32:19+00:00",
            "updated_at": "2019-09-21T05:32:19+00:00",
            "deleted_at": null
          },
          {
            "id": 3386434,
            "beatmap_discussion_id": 1182079,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "the intention behind this spacing is to have high spacing when the \"AAAYYYYYY\" is audible in the vocals (02:24:628 (1,2,3) - ) and lowering it after when the vocal note ends (02:24:976 (3,4) - ). i adjusted the patterns you mentioned to do this a little more accurately",
            "created_at": "2019-10-04T19:35:43+00:00",
            "updated_at": "2019-10-04T19:35:43+00:00",
            "deleted_at": null
          },
          {
            "id": 3401598,
            "beatmap_discussion_id": 1182079,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "AAAYYYYYYYYYYYY",
            "created_at": "2019-10-08T02:43:06+00:00",
            "updated_at": "2019-10-08T02:43:06+00:00",
            "deleted_at": null
          },
          {
            "id": 3401599,
            "beatmap_discussion_id": 1182079,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:43:07+00:00",
            "updated_at": "2019-10-08T02:43:07+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182081,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 49918,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:36:09+00:00",
        "updated_at": "2019-10-08T02:42:36+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:42:36+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333812,
            "beatmap_discussion_id": 1182081,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:49:918 (1) - ctrl+g is better, it's weird to play now. 00:49:918 (1) - and 00:50:093 (1,2,3,4) -  are same. Why not make a better flow here?",
            "created_at": "2019-09-21T05:36:09+00:00",
            "updated_at": "2019-09-21T05:36:09+00:00",
            "deleted_at": null
          },
          {
            "id": 3333817,
            "beatmap_discussion_id": 1182081,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:34:570 (1) - 02:33:174 (1) - ↑",
            "created_at": "2019-09-21T05:36:40+00:00",
            "updated_at": "2019-09-21T05:36:40+00:00",
            "deleted_at": null
          },
          {
            "id": 3386410,
            "beatmap_discussion_id": 1182081,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yeah someone told me these played weird because of how cursor movement mattered on the sliders. since i want cursor movement to stay still between slider + first circle that problem should be fixed",
            "created_at": "2019-10-04T19:22:49+00:00",
            "updated_at": "2019-10-04T19:22:49+00:00",
            "deleted_at": null
          },
          {
            "id": 3401582,
            "beatmap_discussion_id": 1182081,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "!",
            "created_at": "2019-10-08T02:42:36+00:00",
            "updated_at": "2019-10-08T02:42:36+00:00",
            "deleted_at": null
          },
          {
            "id": 3401583,
            "beatmap_discussion_id": 1182081,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:42:36+00:00",
            "updated_at": "2019-10-08T02:42:36+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              6151332
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182088,
        "beatmapset_id": 1001546,
        "beatmap_id": 2126008,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 79395,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:42:04+00:00",
        "updated_at": "2019-10-08T02:50:56+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:50:56+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333844,
            "beatmap_discussion_id": 1182088,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:19:395 - missing clap hitsound",
            "created_at": "2019-09-21T05:42:04+00:00",
            "updated_at": "2019-09-21T05:42:04+00:00",
            "deleted_at": null
          },
          {
            "id": 3333852,
            "beatmap_discussion_id": 1182088,
            "user_id": 13009214,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:44:163 (3) - here as well, with soft addition since it sounds like there's a kick and a snare at the same time",
            "created_at": "2019-09-21T05:44:13+00:00",
            "updated_at": "2019-09-21T05:44:13+00:00",
            "deleted_at": null
          },
          {
            "id": 3401626,
            "beatmap_discussion_id": 1182088,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "good",
            "created_at": "2019-10-08T02:50:56+00:00",
            "updated_at": "2019-10-08T02:50:56+00:00",
            "deleted_at": null
          },
          {
            "id": 3401627,
            "beatmap_discussion_id": 1182088,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:50:56+00:00",
            "updated_at": "2019-10-08T02:50:56+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182089,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 174628,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:42:50+00:00",
        "updated_at": "2019-10-08T02:43:33+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:43:09+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333846,
            "beatmap_discussion_id": 1182089,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:54:628 (1) - is it powerful enough to use 2.0x sv here？ 1.5x is better.    What's more, 02:55:325 (2,3,4,5) - the circles are not fitting, you should enlarge the spacing.",
            "created_at": "2019-09-21T05:42:50+00:00",
            "updated_at": "2019-09-21T05:42:50+00:00",
            "deleted_at": null
          },
          {
            "id": 3386437,
            "beatmap_discussion_id": 1182089,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "final guitar notes feel intense enough for this to fit for me. your right about the second thing, the goal was to exaggerate 02:56:023 (1) - . so i changed it to a slowdown in spacing",
            "created_at": "2019-10-04T19:38:16+00:00",
            "updated_at": "2019-10-04T19:38:16+00:00",
            "deleted_at": null
          },
          {
            "id": 3401600,
            "beatmap_discussion_id": 1182089,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "!",
            "created_at": "2019-10-08T02:43:09+00:00",
            "updated_at": "2019-10-08T02:43:09+00:00",
            "deleted_at": null
          },
          {
            "id": 3401601,
            "beatmap_discussion_id": 1182089,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:43:09+00:00",
            "updated_at": "2019-10-08T02:43:09+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1182091,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 9590557,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-09-21T05:45:39+00:00",
        "updated_at": "2019-09-21T05:45:39+00:00",
        "deleted_at": null,
        "last_post_at": "2019-09-21T05:45:39+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333858,
            "beatmap_discussion_id": 1182091,
            "user_id": 9590557,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "Nice mapset, good luck :D",
            "created_at": "2019-09-21T05:45:39+00:00",
            "updated_at": "2019-09-21T05:45:39+00:00",
            "deleted_at": null
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
        "id": 1182092,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105912,
        "user_id": 13009214,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 36314,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-09-21T05:45:43+00:00",
        "updated_at": "2019-10-08T02:58:02+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-08T02:58:02+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3333859,
            "beatmap_discussion_id": 1182092,
            "user_id": 13009214,
            "last_editor_id": 13009214,
            "deleted_by_id": null,
            "system": false,
            "message": "00:36:314 (6) - removing this note would emphasize the pause in the vocals better imo",
            "created_at": "2019-09-21T05:45:43+00:00",
            "updated_at": "2019-09-21T05:49:11+00:00",
            "deleted_at": null
          },
          {
            "id": 3401657,
            "beatmap_discussion_id": 1182092,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nice idea",
            "created_at": "2019-10-08T02:58:02+00:00",
            "updated_at": "2019-10-08T02:58:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3401658,
            "beatmap_discussion_id": 1182092,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-08T02:58:02+00:00",
            "updated_at": "2019-10-08T02:58:02+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1205109,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 14551330,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-10-07T00:17:56+00:00",
        "updated_at": "2019-10-07T00:17:56+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-07T00:17:56+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3397712,
            "beatmap_discussion_id": 1205109,
            "user_id": 14551330,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "nice",
            "created_at": "2019-10-07T00:17:56+00:00",
            "updated_at": "2019-10-07T00:17:56+00:00",
            "deleted_at": null
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
        "id": 1212261,
        "beatmapset_id": 1001546,
        "beatmap_id": 2126008,
        "user_id": 9505704,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-12T13:25:32+00:00",
        "updated_at": "2019-10-19T15:55:36+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-19T15:55:36+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3417520,
            "beatmap_discussion_id": 1212261,
            "user_id": 9505704,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ur 1/2 clickables are perfectly stacked which is literally the one rc rule in hard diffs, pls raise stack leniency >:(",
            "created_at": "2019-10-12T13:25:32+00:00",
            "updated_at": "2019-10-12T13:25:32+00:00",
            "deleted_at": null
          },
          {
            "id": 3446542,
            "beatmap_discussion_id": 1212261,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "raised to 7",
            "created_at": "2019-10-19T15:55:36+00:00",
            "updated_at": "2019-10-19T15:55:36+00:00",
            "deleted_at": null
          },
          {
            "id": 3446543,
            "beatmap_discussion_id": 1212261,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-19T15:55:36+00:00",
            "updated_at": "2019-10-19T15:55:36+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1221022,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 5128277,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 82884,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-18T10:52:25+00:00",
        "updated_at": "2019-10-19T15:49:26+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-19T15:49:26+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3441463,
            "beatmap_discussion_id": 1221022,
            "user_id": 5128277,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:22:884 (1,2,3) - I don't know about this spacing here, having so much higher spacing for specific part of the drum fill while the drum fill is pretty much same all the way through (well, not the last 1/1 but that difference is not relevant here) feels weird",
            "created_at": "2019-10-18T10:52:25+00:00",
            "updated_at": "2019-10-18T10:52:25+00:00",
            "deleted_at": null
          },
          {
            "id": 3446477,
            "beatmap_discussion_id": 1221022,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "its technically fine since the spacing is exactly the half of previous 1/2 notes 01:22:535 (1,2) - here and it was designed for players to figure out the rhythm by remembering the distance logic on the map. also 01:22:884 (1,2,3) - drums are rare and i would like to emphasize this since this doesnt happen to anywhere at 00:38:581 (1,2,3,4,5,6,7,8) - or 02:19:831 (1) -",
            "created_at": "2019-10-19T15:49:26+00:00",
            "updated_at": "2019-10-19T15:49:26+00:00",
            "deleted_at": null
          },
          {
            "id": 3446478,
            "beatmap_discussion_id": 1221022,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-19T15:49:26+00:00",
            "updated_at": "2019-10-19T15:49:26+00:00",
            "deleted_at": null
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
        "id": 1221023,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 5128277,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 94744,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-18T10:52:49+00:00",
        "updated_at": "2019-10-19T15:49:50+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-19T15:49:50+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3441464,
            "beatmap_discussion_id": 1221023,
            "user_id": 5128277,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:34:744 (3) - should prob NC like last time",
            "created_at": "2019-10-18T10:52:49+00:00",
            "updated_at": "2019-10-18T10:52:49+00:00",
            "deleted_at": null
          },
          {
            "id": 3446481,
            "beatmap_discussion_id": 1221023,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok",
            "created_at": "2019-10-19T15:49:49+00:00",
            "updated_at": "2019-10-19T15:49:49+00:00",
            "deleted_at": null
          },
          {
            "id": 3446482,
            "beatmap_discussion_id": 1221023,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-19T15:49:50+00:00",
            "updated_at": "2019-10-19T15:49:50+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1221024,
        "beatmapset_id": 1001546,
        "beatmap_id": 2096611,
        "user_id": 5128277,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 153348,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-18T10:55:29+00:00",
        "updated_at": "2019-10-19T15:50:02+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-19T15:50:02+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3441470,
            "beatmap_discussion_id": 1221024,
            "user_id": 5128277,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:33:348 (3) - should prob NC here as well for consistency's sake (or since 2 of the three are like this, could just remove the NC from teh first one I guess",
            "created_at": "2019-10-18T10:55:29+00:00",
            "updated_at": "2019-10-18T10:55:29+00:00",
            "deleted_at": null
          },
          {
            "id": 3446484,
            "beatmap_discussion_id": 1221024,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yep was supposed to have one combo system",
            "created_at": "2019-10-19T15:50:02+00:00",
            "updated_at": "2019-10-19T15:50:02+00:00",
            "deleted_at": null
          },
          {
            "id": 3446485,
            "beatmap_discussion_id": 1221024,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-19T15:50:02+00:00",
            "updated_at": "2019-10-19T15:50:02+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1221027,
        "beatmapset_id": 1001546,
        "beatmap_id": 2162331,
        "user_id": 5128277,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 146197,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-18T11:02:29+00:00",
        "updated_at": "2019-10-19T15:54:24+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-19T15:54:24+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3441481,
            "beatmap_discussion_id": 1221027,
            "user_id": 5128277,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:26:197 (3,4) - wouldn't ctrl+g rhythm work better?",
            "created_at": "2019-10-18T11:02:29+00:00",
            "updated_at": "2019-10-18T11:02:29+00:00",
            "deleted_at": null
          },
          {
            "id": 3446531,
            "beatmap_discussion_id": 1221027,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:26:546 - vocal and instrument starts a bit later (around at blue tick). and having distance pattern or rhythmwise would help to emphasize the gap around here. 02:26:372 (4,1) - having consistent object here would do it and having non-clickable gap by using sliderend object to where the regular rhythm is supposed to have circle also helps to give its own characteristic i think. so i would like to keep it",
            "created_at": "2019-10-19T15:54:24+00:00",
            "updated_at": "2019-10-19T15:54:24+00:00",
            "deleted_at": null
          },
          {
            "id": 3446532,
            "beatmap_discussion_id": 1221027,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-19T15:54:24+00:00",
            "updated_at": "2019-10-19T15:54:24+00:00",
            "deleted_at": null
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
        "id": 1221045,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 5128277,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 180209,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-18T11:25:36+00:00",
        "updated_at": "2019-10-20T01:32:45+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-20T01:32:45+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3441566,
            "beatmap_discussion_id": 1221045,
            "user_id": 5128277,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "03:00:209 - end spinner here instead to be consistent with all the other diffs? I mean, not like it's necessary but it'd be nice lil' touch",
            "created_at": "2019-10-18T11:25:36+00:00",
            "updated_at": "2019-10-18T11:25:36+00:00",
            "deleted_at": null
          },
          {
            "id": 3448467,
            "beatmap_discussion_id": 1221045,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "sure why not",
            "created_at": "2019-10-20T01:22:10+00:00",
            "updated_at": "2019-10-20T01:22:10+00:00",
            "deleted_at": null
          },
          {
            "id": 3448502,
            "beatmap_discussion_id": 1221045,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "w",
            "created_at": "2019-10-20T01:32:45+00:00",
            "updated_at": "2019-10-20T01:32:45+00:00",
            "deleted_at": null
          },
          {
            "id": 3448503,
            "beatmap_discussion_id": 1221045,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-20T01:32:45+00:00",
            "updated_at": "2019-10-20T01:32:45+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1221052,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105912,
        "user_id": 5128277,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 8581,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-18T11:29:06+00:00",
        "updated_at": "2019-10-19T15:58:48+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-19T15:58:48+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3441575,
            "beatmap_discussion_id": 1221052,
            "user_id": 5128277,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "00:08:581 (1,2,3,4,1,2,3,4,1) - break up somewhere?\n\n\"Include a 1/1 or longer gap in rhythm for every two measures of gameplay.\" in guidelines for lowest diff Normals such as this, and this goes over 2 measures.\n\nNot only that, but it's the only one like this in the diff so not like you are \"using this kind of stuff\" either, just get it in line.\n\nMaybe remove 00:09:453 (3) - for example? But just any is fine, choose whichever you prefer lo",
            "created_at": "2019-10-18T11:29:06+00:00",
            "updated_at": "2019-10-18T11:29:06+00:00",
            "deleted_at": null
          },
          {
            "id": 3446561,
            "beatmap_discussion_id": 1221052,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "did that !",
            "created_at": "2019-10-19T15:58:48+00:00",
            "updated_at": "2019-10-19T15:58:48+00:00",
            "deleted_at": null
          },
          {
            "id": 3446562,
            "beatmap_discussion_id": 1221052,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-19T15:58:48+00:00",
            "updated_at": "2019-10-19T15:58:48+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1221057,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 5128277,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-10-18T11:35:02+00:00",
        "updated_at": "2019-10-18T11:35:02+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-18T11:35:02+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3441583,
            "beatmap_discussion_id": 1221057,
            "user_id": 5128277,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "k this is pretty cool fix pending and hmu for some :eyes:",
            "created_at": "2019-10-18T11:35:02+00:00",
            "updated_at": "2019-10-18T11:35:02+00:00",
            "deleted_at": null
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
        "id": 1223501,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 9505704,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-19T21:59:17+00:00",
        "updated_at": "2019-10-20T01:41:41+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-20T01:41:41+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3447838,
            "beatmap_discussion_id": 1223501,
            "user_id": 9505704,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "never seen this before (or heard of it being a problem) but MV is saying to rename squirrel's diff to its actual name to prevent problems with updating - never seen this as a problem before but prob a good idea to fix it just to be safe ?",
            "created_at": "2019-10-19T21:59:17+00:00",
            "updated_at": "2019-10-19T21:59:17+00:00",
            "deleted_at": null
          },
          {
            "id": 3448420,
            "beatmap_discussion_id": 1223501,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "I've never used the new MV before so I have no idea what this means. What does it mean by the \"actual\" diff name lol",
            "created_at": "2019-10-20T01:06:55+00:00",
            "updated_at": "2019-10-20T01:06:55+00:00",
            "deleted_at": null
          },
          {
            "id": 3448505,
            "beatmap_discussion_id": 1223501,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "talked with him and adjusted it (changing osz file's name)",
            "created_at": "2019-10-20T01:33:08+00:00",
            "updated_at": "2019-10-20T01:33:08+00:00",
            "deleted_at": null
          },
          {
            "id": 3448506,
            "beatmap_discussion_id": 1223501,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-20T01:33:08+00:00",
            "updated_at": "2019-10-20T01:33:08+00:00",
            "deleted_at": null
          },
          {
            "id": 3448554,
            "beatmap_discussion_id": 1223501,
            "user_id": 9505704,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "yea sorry for the poor explanation, should be good now x)",
            "created_at": "2019-10-20T01:41:41+00:00",
            "updated_at": "2019-10-20T01:41:41+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1223503,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 9505704,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-19T22:01:51+00:00",
        "updated_at": "2019-10-20T01:33:54+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-20T01:33:54+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3447854,
            "beatmap_discussion_id": 1223503,
            "user_id": 9505704,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "soft-hitwhistle4.wav is much much louder on the right stereo channel and has some delay, mind cutting it and normalizing the channels? it's used often as a feedback hitsound so this should be done rly",
            "created_at": "2019-10-19T22:01:51+00:00",
            "updated_at": "2019-10-19T22:01:51+00:00",
            "deleted_at": null
          },
          {
            "id": 3448510,
            "beatmap_discussion_id": 1223503,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "removed since I wasnt sure if this is really fitting or not",
            "created_at": "2019-10-20T01:33:54+00:00",
            "updated_at": "2019-10-20T01:33:54+00:00",
            "deleted_at": null
          },
          {
            "id": 3448511,
            "beatmap_discussion_id": 1223503,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-20T01:33:54+00:00",
            "updated_at": "2019-10-20T01:33:54+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1223510,
        "beatmapset_id": 1001546,
        "beatmap_id": 2162331,
        "user_id": 9505704,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": 134163,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-19T22:09:37+00:00",
        "updated_at": "2019-10-20T01:39:01+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-20T01:39:01+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3447883,
            "beatmap_discussion_id": 1223510,
            "user_id": 9505704,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:14:163 (1,2,3,1,1,2,3,1,1,2,3,1,1,2,3,1) - in this section you're perfectly covering slider repeats with circles which results in them being barely readable before they need to be clicked; there's a guidline for this on insanes though it states \"within a 1/2 of the reverse being reached\", whereas these ones are three ticks: https://imgur.com/a/8JcmxtU\n\ni think this should still be considered, since even though reading is somewhat of a gimmick presented across the higher diffs, this kind of patterning on the insane seems pretty difficult for me - even if it is just kicksliders, I had read them as 1/2 sliders when playing since the reverse is hard to see. I'd like to hear ur thoughts before proceeding ^^",
            "created_at": "2019-10-19T22:09:37+00:00",
            "updated_at": "2019-10-19T22:09:37+00:00",
            "deleted_at": null
          },
          {
            "id": 3448541,
            "beatmap_discussion_id": 1223510,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "oki",
            "created_at": "2019-10-20T01:39:01+00:00",
            "updated_at": "2019-10-20T01:39:01+00:00",
            "deleted_at": null
          },
          {
            "id": 3448542,
            "beatmap_discussion_id": 1223510,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-20T01:39:01+00:00",
            "updated_at": "2019-10-20T01:39:01+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1223542,
        "beatmapset_id": 1001546,
        "beatmap_id": 2105913,
        "user_id": 9505704,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 104163,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-19T22:29:14+00:00",
        "updated_at": "2019-10-20T01:32:42+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-20T01:32:42+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3447993,
            "beatmap_discussion_id": 1223542,
            "user_id": 9505704,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "01:44:163 (1) - looks like normal sampleset got set here by mistake, should be on auto to use the custom snare",
            "created_at": "2019-10-19T22:29:14+00:00",
            "updated_at": "2019-10-19T22:29:14+00:00",
            "deleted_at": null
          },
          {
            "id": 3448422,
            "beatmap_discussion_id": 1223542,
            "user_id": 6151332,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "oopsies",
            "created_at": "2019-10-20T01:07:29+00:00",
            "updated_at": "2019-10-20T01:07:29+00:00",
            "deleted_at": null
          },
          {
            "id": 3448500,
            "beatmap_discussion_id": 1223542,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "w",
            "created_at": "2019-10-20T01:32:42+00:00",
            "updated_at": "2019-10-20T01:32:42+00:00",
            "deleted_at": null
          },
          {
            "id": 3448501,
            "beatmap_discussion_id": 1223542,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-20T01:32:42+00:00",
            "updated_at": "2019-10-20T01:32:42+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1223550,
        "beatmapset_id": 1001546,
        "beatmap_id": 2126008,
        "user_id": 9505704,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": 139952,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-19T22:32:04+00:00",
        "updated_at": "2019-10-20T01:40:51+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-20T01:40:51+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3448007,
            "beatmap_discussion_id": 1223550,
            "user_id": 9505704,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "02:19:952 - could we have a spinner here for the hard like the other diffs please :(",
            "created_at": "2019-10-19T22:32:04+00:00",
            "updated_at": "2019-10-19T22:32:04+00:00",
            "deleted_at": null
          },
          {
            "id": 3448551,
            "beatmap_discussion_id": 1223550,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "fixed",
            "created_at": "2019-10-20T01:40:51+00:00",
            "updated_at": "2019-10-20T01:40:51+00:00",
            "deleted_at": null
          },
          {
            "id": 3448552,
            "beatmap_discussion_id": 1223550,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-20T01:40:51+00:00",
            "updated_at": "2019-10-20T01:40:51+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1224450,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 3,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-20T12:08:01+00:00",
        "updated_at": "2019-10-20T12:09:54+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-20T12:09:54+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3450550,
            "beatmap_discussion_id": 1224450,
            "user_id": 3,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "This beatmap set was updated by the mapper after a nomination. Please ensure to re-check the beatmaps for new issues. If you are the mapper, please comment in this thread on what you changed.",
            "created_at": "2019-10-20T12:08:01+00:00",
            "updated_at": "2019-10-20T12:08:01+00:00",
            "deleted_at": null
          },
          {
            "id": 3450556,
            "beatmap_discussion_id": 1224450,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "subjective",
            "created_at": "2019-10-20T12:09:04+00:00",
            "updated_at": "2019-10-20T12:09:04+00:00",
            "deleted_at": null
          },
          {
            "id": 3450557,
            "beatmap_discussion_id": 1224450,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-20T12:09:04+00:00",
            "updated_at": "2019-10-20T12:09:04+00:00",
            "deleted_at": null
          },
          {
            "id": 3450560,
            "beatmap_discussion_id": 1224450,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "jk i adjusted one pattern",
            "created_at": "2019-10-20T12:09:54+00:00",
            "updated_at": "2019-10-20T12:09:54+00:00",
            "deleted_at": null
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
        "id": 1227619,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 12914832,
        "deleted_by_id": null,
        "message_type": "hype",
        "parent_id": null,
        "timestamp": null,
        "resolved": false,
        "can_be_resolved": false,
        "can_grant_kudosu": false,
        "created_at": "2019-10-22T09:43:18+00:00",
        "updated_at": "2019-10-22T09:43:18+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-22T09:43:18+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3459941,
            "beatmap_discussion_id": 1227619,
            "user_id": 12914832,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "owo",
            "created_at": "2019-10-22T09:43:18+00:00",
            "updated_at": "2019-10-22T09:43:18+00:00",
            "deleted_at": null
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
        "id": 1228459,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 3533958,
        "deleted_by_id": null,
        "message_type": "suggestion",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": true,
        "created_at": "2019-10-23T01:33:05+00:00",
        "updated_at": "2019-10-27T09:00:03+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-27T09:00:03+00:00",
        "kudosu_denied": false,
        "posts": [
          {
            "id": 3462450,
            "beatmap_discussion_id": 1228459,
            "user_id": 3533958,
            "last_editor_id": 3533958,
            "deleted_by_id": null,
            "system": false,
            "message": "hello main offsets are wrong\n\n00:01:605 (1) - should be -5 from where it is currently (change 00:01:257 (4) - this one to 174.9 bpm and it fixes the transition here bpm-wise)*\n02:22:535 (1) - should be +5 from where it is currently\n\n* some beats will be late with this offset but from what it sounds like, a majority of the song is way too early as it is right now so this should at least average it out a bit better imo\n\nnot gonna dq over this as greenhue has more pressing issues that he's gonna be posting soon, just figured i would put this out here for now",
            "created_at": "2019-10-23T01:33:05+00:00",
            "updated_at": "2019-10-23T01:34:47+00:00",
            "deleted_at": null
          },
          {
            "id": 3463050,
            "beatmap_discussion_id": 1228459,
            "user_id": 4967662,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "gotta check all timings that come with mappers guild LOL",
            "created_at": "2019-10-23T06:12:22+00:00",
            "updated_at": "2019-10-23T06:12:22+00:00",
            "deleted_at": null
          },
          {
            "id": 3463324,
            "beatmap_discussion_id": 1228459,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "greenhue where are you",
            "created_at": "2019-10-23T08:54:08+00:00",
            "updated_at": "2019-10-23T08:54:08+00:00",
            "deleted_at": null
          },
          {
            "id": 3480976,
            "beatmap_discussion_id": 1228459,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok",
            "created_at": "2019-10-27T09:00:03+00:00",
            "updated_at": "2019-10-27T09:00:03+00:00",
            "deleted_at": null
          },
          {
            "id": 3480977,
            "beatmap_discussion_id": 1228459,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-27T09:00:03+00:00",
            "updated_at": "2019-10-27T09:00:03+00:00",
            "deleted_at": null
          }
        ],
        "votes": {
          "up": 1,
          "down": 0,
          "voters": {
            "up": [
              7342798
            ],
            "down": []
          }
        }
      },
      {
        "id": 1234956,
        "beatmapset_id": 1001546,
        "beatmap_id": null,
        "user_id": 4967662,
        "deleted_by_id": null,
        "message_type": "problem",
        "parent_id": null,
        "timestamp": null,
        "resolved": true,
        "can_be_resolved": true,
        "can_grant_kudosu": false,
        "created_at": "2019-10-27T04:23:20+00:00",
        "updated_at": "2019-10-27T09:00:00+00:00",
        "deleted_at": null,
        "last_post_at": "2019-10-27T09:00:00+00:00",
        "kudosu_denied": true,
        "posts": [
          {
            "id": 3480330,
            "beatmap_discussion_id": 1234956,
            "user_id": 4967662,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "since it ranks soon gonna just dq for fierys discussion https://osu.ppy.sh/beatmapsets/1001546/discussion/-/generalAll#/1228459 plus thought about points i brought up privately in dms.",
            "created_at": "2019-10-27T04:23:20+00:00",
            "updated_at": "2019-10-27T04:23:20+00:00",
            "deleted_at": null
          },
          {
            "id": 3480479,
            "beatmap_discussion_id": 1234956,
            "user_id": 7342798,
            "last_editor_id": 7342798,
            "deleted_by_id": null,
            "system": false,
            "message": "1 . fixed timing per fiery's suggestion\n2 . changed ar from 6 to 7.5 on topdiff to enhance playability\n3 . adjusted some patterns on insane to keep the spread between hard and insane better\n\nwill resolve when i update the map",
            "created_at": "2019-10-27T05:07:30+00:00",
            "updated_at": "2019-10-27T05:07:42+00:00",
            "deleted_at": null
          },
          {
            "id": 3480974,
            "beatmap_discussion_id": 1234956,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": false,
            "message": "ok",
            "created_at": "2019-10-27T09:00:00+00:00",
            "updated_at": "2019-10-27T09:00:00+00:00",
            "deleted_at": null
          },
          {
            "id": 3480975,
            "beatmap_discussion_id": 1234956,
            "user_id": 7342798,
            "last_editor_id": null,
            "deleted_by_id": null,
            "system": true,
            "message": {
              "type": "resolved",
              "value": true
            },
            "created_at": "2019-10-27T09:00:00+00:00",
            "updated_at": "2019-10-27T09:00:00+00:00",
            "deleted_at": null
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
    "events": [
      {
        "id": 1407209,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1103785,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-08-07T07:02:34+00:00",
        "user_id": 197805
      },
      {
        "id": 1407210,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1103785,
          "beatmap_discussion_post_id": 3135904
        },
        "created_at": "2019-08-07T07:02:43+00:00"
      },
      {
        "id": 1514897,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182025,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T11:40:08+00:00",
        "user_id": 9590557
      },
      {
        "id": 1514898,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182025,
          "beatmap_discussion_post_id": 3385124
        },
        "created_at": "2019-10-04T11:40:08+00:00"
      },
      {
        "id": 1514901,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182067,
          "beatmap_discussion_post_id": 3385129
        },
        "created_at": "2019-10-04T11:41:25+00:00"
      },
      {
        "id": 1514903,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182036,
          "beatmap_discussion_post_id": 3385133
        },
        "created_at": "2019-10-04T11:43:02+00:00"
      },
      {
        "id": 1514904,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182039,
          "beatmap_discussion_post_id": 3385135
        },
        "created_at": "2019-10-04T11:43:58+00:00"
      },
      {
        "id": 1514906,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182042,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T11:44:24+00:00",
        "user_id": 9590557
      },
      {
        "id": 1514908,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182042,
          "beatmap_discussion_post_id": 3385139
        },
        "created_at": "2019-10-04T11:44:26+00:00"
      },
      {
        "id": 1514909,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182044,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T11:45:00+00:00",
        "user_id": 9590557
      },
      {
        "id": 1514910,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182044,
          "beatmap_discussion_post_id": 3385143
        },
        "created_at": "2019-10-04T11:45:02+00:00"
      },
      {
        "id": 1514911,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182053,
          "beatmap_discussion_post_id": 3385145
        },
        "created_at": "2019-10-04T11:45:24+00:00"
      },
      {
        "id": 1514912,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182055,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T11:45:46+00:00",
        "user_id": 9590557
      },
      {
        "id": 1514913,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182055,
          "beatmap_discussion_post_id": 3385147
        },
        "created_at": "2019-10-04T11:45:46+00:00"
      },
      {
        "id": 1514915,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182059,
          "beatmap_discussion_post_id": 3385151
        },
        "created_at": "2019-10-04T11:46:49+00:00"
      },
      {
        "id": 1514917,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182063,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T11:48:53+00:00",
        "user_id": 9590557
      },
      {
        "id": 1514918,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182063,
          "beatmap_discussion_post_id": 3385158
        },
        "created_at": "2019-10-04T11:48:53+00:00"
      },
      {
        "id": 1514919,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182065,
          "beatmap_discussion_post_id": 3385161
        },
        "created_at": "2019-10-04T11:49:35+00:00"
      },
      {
        "id": 1514920,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182069,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T11:50:02+00:00",
        "user_id": 9590557
      },
      {
        "id": 1514921,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182069,
          "beatmap_discussion_post_id": 3385165
        },
        "created_at": "2019-10-04T11:50:02+00:00"
      },
      {
        "id": 1514922,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182017,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T11:50:40+00:00",
        "user_id": 9590557
      },
      {
        "id": 1514923,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182017,
          "beatmap_discussion_post_id": 3385169
        },
        "created_at": "2019-10-04T11:50:41+00:00"
      },
      {
        "id": 1514924,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182000,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T11:52:56+00:00",
        "user_id": 9590557
      },
      {
        "id": 1514925,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182000,
          "beatmap_discussion_post_id": 3385177
        },
        "created_at": "2019-10-04T11:52:57+00:00"
      },
      {
        "id": 1514926,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182008,
          "beatmap_discussion_post_id": 3385180
        },
        "created_at": "2019-10-04T11:53:45+00:00"
      },
      {
        "id": 1514928,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182011,
          "beatmap_discussion_post_id": 3385185
        },
        "created_at": "2019-10-04T11:54:24+00:00"
      },
      {
        "id": 1515512,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182021,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6151332,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6151332,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T19:11:05+00:00",
        "user_id": 13009214
      },
      {
        "id": 1515513,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182028,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6151332,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6151332,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T19:12:33+00:00",
        "user_id": 13009214
      },
      {
        "id": 1515524,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182081,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6151332,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6151332,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T19:22:53+00:00",
        "user_id": 9590557
      },
      {
        "id": 1515526,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182033,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6151332,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6151332,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T19:25:37+00:00",
        "user_id": 13009214
      },
      {
        "id": 1515528,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182075,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6151332,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6151332,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T19:26:29+00:00",
        "user_id": 9590557
      },
      {
        "id": 1515529,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182041,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 6151332,
            "score": 1
          },
          "votes": [
            {
              "user_id": 6151332,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-04T19:27:38+00:00",
        "user_id": 13009214
      },
      {
        "id": 1522410,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182021,
          "beatmap_discussion_post_id": 3401578
        },
        "created_at": "2019-10-08T02:42:31+00:00"
      },
      {
        "id": 1522411,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182028,
          "beatmap_discussion_post_id": 3401580
        },
        "created_at": "2019-10-08T02:42:34+00:00"
      },
      {
        "id": 1522412,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182081,
          "beatmap_discussion_post_id": 3401582
        },
        "created_at": "2019-10-08T02:42:36+00:00"
      },
      {
        "id": 1522413,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182033,
          "beatmap_discussion_post_id": 3401584
        },
        "created_at": "2019-10-08T02:42:39+00:00"
      },
      {
        "id": 1522414,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182075,
          "beatmap_discussion_post_id": 3401586
        },
        "created_at": "2019-10-08T02:42:41+00:00"
      },
      {
        "id": 1522415,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182041,
          "beatmap_discussion_post_id": 3401588
        },
        "created_at": "2019-10-08T02:42:43+00:00"
      },
      {
        "id": 1522416,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182046,
          "beatmap_discussion_post_id": 3401590
        },
        "created_at": "2019-10-08T02:42:46+00:00"
      },
      {
        "id": 1522419,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182048,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:42:58+00:00",
        "user_id": 13009214
      },
      {
        "id": 1522420,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182048,
          "beatmap_discussion_post_id": 3401596
        },
        "created_at": "2019-10-08T02:42:59+00:00"
      },
      {
        "id": 1522421,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182079,
          "beatmap_discussion_post_id": 3401598
        },
        "created_at": "2019-10-08T02:43:07+00:00"
      },
      {
        "id": 1522422,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182089,
          "beatmap_discussion_post_id": 3401600
        },
        "created_at": "2019-10-08T02:43:09+00:00"
      },
      {
        "id": 1522424,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182046,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:43:31+00:00",
        "user_id": 13009214
      },
      {
        "id": 1522425,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182079,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:43:35+00:00",
        "user_id": 9590557
      },
      {
        "id": 1522426,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182089,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:43:36+00:00",
        "user_id": 9590557
      },
      {
        "id": 1522428,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182010,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:44:52+00:00",
        "user_id": 9590557
      },
      {
        "id": 1522429,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182010,
          "beatmap_discussion_post_id": 3401607
        },
        "created_at": "2019-10-08T02:44:52+00:00"
      },
      {
        "id": 1522434,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1181978,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:48:18+00:00",
        "user_id": 9590557
      },
      {
        "id": 1522435,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181978,
          "beatmap_discussion_post_id": 3401613
        },
        "created_at": "2019-10-08T02:48:18+00:00"
      },
      {
        "id": 1522438,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181980,
          "beatmap_discussion_post_id": 3401620
        },
        "created_at": "2019-10-08T02:50:30+00:00"
      },
      {
        "id": 1522440,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182088,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:50:54+00:00",
        "user_id": 13009214
      },
      {
        "id": 1522441,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182088,
          "beatmap_discussion_post_id": 3401626
        },
        "created_at": "2019-10-08T02:50:56+00:00"
      },
      {
        "id": 1522443,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181992,
          "beatmap_discussion_post_id": 3401629
        },
        "created_at": "2019-10-08T02:51:35+00:00"
      },
      {
        "id": 1522447,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181995,
          "beatmap_discussion_post_id": 3401636
        },
        "created_at": "2019-10-08T02:53:07+00:00"
      },
      {
        "id": 1522452,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181961,
          "beatmap_discussion_post_id": 3401648
        },
        "created_at": "2019-10-08T02:56:06+00:00"
      },
      {
        "id": 1522456,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1182092,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:58:00+00:00",
        "user_id": 13009214
      },
      {
        "id": 1522457,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182092,
          "beatmap_discussion_post_id": 3401657
        },
        "created_at": "2019-10-08T02:58:02+00:00"
      },
      {
        "id": 1522458,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1181972,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T02:58:28+00:00",
        "user_id": 9590557
      },
      {
        "id": 1522459,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181972,
          "beatmap_discussion_post_id": 3401659
        },
        "created_at": "2019-10-08T02:58:28+00:00"
      },
      {
        "id": 1522460,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181966,
          "beatmap_discussion_post_id": 3401661
        },
        "created_at": "2019-10-08T02:59:17+00:00"
      },
      {
        "id": 1522462,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1181975,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-08T03:01:13+00:00",
        "user_id": 9590557
      },
      {
        "id": 1522463,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181975,
          "beatmap_discussion_post_id": 3401666
        },
        "created_at": "2019-10-08T03:01:14+00:00"
      },
      {
        "id": 1522464,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1181977,
          "beatmap_discussion_post_id": 3401669
        },
        "created_at": "2019-10-08T03:01:47+00:00"
      },
      {
        "id": 1522465,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1182060,
          "beatmap_discussion_post_id": 3401672
        },
        "created_at": "2019-10-08T03:02:17+00:00"
      },
      {
        "id": 1541861,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1221022,
          "beatmap_discussion_post_id": 3446477
        },
        "created_at": "2019-10-19T15:49:26+00:00"
      },
      {
        "id": 1541864,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1221023,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-19T15:49:46+00:00",
        "user_id": 5128277
      },
      {
        "id": 1541865,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1221023,
          "beatmap_discussion_post_id": 3446481
        },
        "created_at": "2019-10-19T15:49:50+00:00"
      },
      {
        "id": 1541866,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1221024,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-19T15:49:52+00:00",
        "user_id": 5128277
      },
      {
        "id": 1541867,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1221024,
          "beatmap_discussion_post_id": 3446484
        },
        "created_at": "2019-10-19T15:50:02+00:00"
      },
      {
        "id": 1541889,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1221027,
          "beatmap_discussion_post_id": 3446531
        },
        "created_at": "2019-10-19T15:54:24+00:00"
      },
      {
        "id": 1541893,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1212261,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-19T15:55:31+00:00",
        "user_id": 9505704
      },
      {
        "id": 1541894,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1212261,
          "beatmap_discussion_post_id": 3446542
        },
        "created_at": "2019-10-19T15:55:36+00:00"
      },
      {
        "id": 1541902,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1221052,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-19T15:58:44+00:00",
        "user_id": 5128277
      },
      {
        "id": 1541904,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1221052,
          "beatmap_discussion_post_id": 3446561
        },
        "created_at": "2019-10-19T15:58:48+00:00"
      },
      {
        "id": 1542695,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1223542,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-20T01:32:41+00:00",
        "user_id": 9505704
      },
      {
        "id": 1542696,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1223542,
          "beatmap_discussion_post_id": 3448500
        },
        "created_at": "2019-10-20T01:32:42+00:00"
      },
      {
        "id": 1542697,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1221045,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-20T01:32:44+00:00",
        "user_id": 5128277
      },
      {
        "id": 1542698,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1221045,
          "beatmap_discussion_post_id": 3448502
        },
        "created_at": "2019-10-20T01:32:45+00:00"
      },
      {
        "id": 1542699,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1223501,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-20T01:32:51+00:00",
        "user_id": 9505704
      },
      {
        "id": 1542701,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1223501,
          "beatmap_discussion_post_id": 3448505
        },
        "created_at": "2019-10-20T01:33:08+00:00"
      },
      {
        "id": 1542702,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1223503,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-20T01:33:53+00:00",
        "user_id": 9505704
      },
      {
        "id": 1542703,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1223503,
          "beatmap_discussion_post_id": 3448510
        },
        "created_at": "2019-10-20T01:33:54+00:00"
      },
      {
        "id": 1542723,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1223510,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-20T01:38:58+00:00",
        "user_id": 9505704
      },
      {
        "id": 1542724,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1223510,
          "beatmap_discussion_post_id": 3448541
        },
        "created_at": "2019-10-20T01:39:01+00:00"
      },
      {
        "id": 1542731,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1223550,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-20T01:40:49+00:00",
        "user_id": 9505704
      },
      {
        "id": 1542732,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1223550,
          "beatmap_discussion_post_id": 3448551
        },
        "created_at": "2019-10-20T01:40:51+00:00"
      },
      {
        "id": 1543219,
        "type": "nominate",
        "comment": null,
        "created_at": "2019-10-20T07:44:05+00:00",
        "user_id": 5128277
      },
      {
        "id": 1543543,
        "type": "nomination_reset",
        "comment": {
          "beatmap_discussion_id": 1224450,
          "beatmap_discussion_post_id": 3450550
        },
        "created_at": "2019-10-20T12:08:01+00:00",
        "user_id": 3
      },
      {
        "id": 1543545,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1224450,
          "beatmap_discussion_post_id": 3450556
        },
        "created_at": "2019-10-20T12:09:04+00:00"
      },
      {
        "id": 1543550,
        "type": "nominate",
        "comment": null,
        "created_at": "2019-10-20T12:17:09+00:00",
        "user_id": 9505704
      },
      {
        "id": 1543603,
        "type": "nominate",
        "comment": null,
        "created_at": "2019-10-20T12:48:03+00:00",
        "user_id": 5128277
      },
      {
        "id": 1543604,
        "type": "qualify",
        "comment": null,
        "created_at": "2019-10-20T12:48:03+00:00",
        "user_id": null
      },
      {
        "id": 1549083,
        "type": "kudosu_gain",
        "comment": {
          "beatmap_discussion_id": 1228459,
          "beatmap_discussion_post_id": null,
          "new_vote": {
            "user_id": 7342798,
            "score": 1
          },
          "votes": [
            {
              "user_id": 7342798,
              "score": 1
            }
          ]
        },
        "created_at": "2019-10-23T01:58:36+00:00",
        "user_id": 3533958
      },
      {
        "id": 1556905,
        "type": "disqualify",
        "comment": {
          "beatmap_discussion_id": 1234956,
          "beatmap_discussion_post_id": 3480330
        },
        "created_at": "2019-10-27T04:23:20+00:00",
        "user_id": 4967662
      },
      {
        "id": 1556914,
        "type": "kudosu_deny",
        "comment": {
          "beatmap_discussion_id": 1234956,
          "beatmap_discussion_post_id": null
        },
        "created_at": "2019-10-27T04:32:55+00:00"
      },
      {
        "id": 1557244,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1234956,
          "beatmap_discussion_post_id": 3480974
        },
        "created_at": "2019-10-27T09:00:00+00:00"
      },
      {
        "id": 1557245,
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 1228459,
          "beatmap_discussion_post_id": 3480976
        },
        "created_at": "2019-10-27T09:00:03+00:00"
      },
      {
        "id": 1560498,
        "type": "nominate",
        "comment": null,
        "created_at": "2019-10-28T21:56:02+00:00",
        "user_id": 9505704
      },
      {
        "id": 1561517,
        "type": "nominate",
        "comment": null,
        "created_at": "2019-10-29T14:59:55+00:00",
        "user_id": 5128277
      },
      {
        "id": 1561518,
        "type": "qualify",
        "comment": null,
        "created_at": "2019-10-29T14:59:55+00:00",
        "user_id": null
      },
      {
        "id": 1563803,
        "type": "rank",
        "comment": null,
        "created_at": "2019-10-31T00:43:44+00:00",
        "user_id": null
      }
    ],
    "related_users": [
      {
        "avatar_url": "https://a.ppy.sh/3?1528948612.png",
        "country_code": "SH",
        "default_group": "bot",
        "id": 3,
        "is_active": false,
        "is_bot": true,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-04-08T12:39:53+00:00",
        "pm_friends_only": false,
        "profile_colour": "#e45678",
        "username": "BanchoBot",
        "group_badge": {
          "id": 29,
          "identifier": "bot",
          "name": "Chat Bots",
          "short_name": "BOT",
          "description": "",
          "colour": null
        }
      },
      {
        "avatar_url": "https://a.ppy.sh/197805?1531219665.jpeg",
        "country_code": "ID",
        "default_group": "alumni",
        "id": 197805,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-05-15T17:40:00+00:00",
        "pm_friends_only": false,
        "profile_colour": "#888888",
        "username": "Niva",
        "group_badge": {
          "id": 16,
          "identifier": "alumni",
          "name": "osu! Alumni",
          "short_name": "ALM",
          "description": "Those known for their contributions who have since moved on. Were the resources available, for each member: a statue we would erect in the town square.",
          "colour": "#999999"
        }
      },
      {
        "avatar_url": "https://a.ppy.sh/1249323?1589457428.jpeg",
        "country_code": "ID",
        "default_group": "bng",
        "id": 1249323,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-05-15T17:42:00+00:00",
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "Hinsvar",
        "group_badge": {
          "id": 28,
          "identifier": "bng",
          "name": "Beatmap Nominators",
          "short_name": "BN",
          "description": "Upon the tides of change, a new ship sets sail. Hark! The qualifiers are nigh - may all maps rejoice in knowing their approval is upon them.",
          "colour": "#A347EB"
        }
      },
      {
        "avatar_url": "https://a.ppy.sh/1372608?1553854878.jpeg",
        "country_code": "ID",
        "default_group": "default",
        "id": 1372608,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-05-15T17:36:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "nya10"
      },
      {
        "avatar_url": "https://a.ppy.sh/1555865?1497711691.jpg",
        "country_code": "DE",
        "default_group": "default",
        "id": 1555865,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-05-15T17:01:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "tacokatze"
      },
      {
        "avatar_url": "https://a.ppy.sh/3533958?1582499200.jpeg",
        "country_code": "US",
        "default_group": "bng",
        "id": 3533958,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-05-15T03:59:00+00:00",
        "pm_friends_only": true,
        "profile_colour": "#6B3FA0",
        "username": "fieryrage",
        "group_badge": {
          "id": 28,
          "identifier": "bng",
          "name": "Beatmap Nominators",
          "short_name": "BN",
          "description": "Upon the tides of change, a new ship sets sail. Hark! The qualifiers are nigh - may all maps rejoice in knowing their approval is upon them.",
          "colour": "#A347EB"
        }
      },
      {
        "avatar_url": "https://a.ppy.sh/4967662?1576373589.png",
        "country_code": "AU",
        "default_group": "default",
        "id": 4967662,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-05-15T18:12:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "greenhue"
      },
      {
        "avatar_url": "https://a.ppy.sh/5128277?1524647004.png",
        "country_code": "FI",
        "default_group": "bng",
        "id": 5128277,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "TheKingHenry",
        "group_badge": {
          "id": 28,
          "identifier": "bng",
          "name": "Beatmap Nominators",
          "short_name": "BN",
          "description": "Upon the tides of change, a new ship sets sail. Hark! The qualifiers are nigh - may all maps rejoice in knowing their approval is upon them.",
          "colour": "#A347EB"
        }
      },
      {
        "avatar_url": "https://a.ppy.sh/6151332?1587344898.jpeg",
        "country_code": "US",
        "default_group": "default",
        "id": 6151332,
        "is_active": true,
        "is_bot": false,
        "is_online": true,
        "is_supporter": true,
        "last_visit": "2020-05-15T18:10:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "squirrelpascals"
      },
      {
        "avatar_url": "https://a.ppy.sh/7342798?1586700065.jpeg",
        "country_code": "KR",
        "default_group": "default",
        "id": 7342798,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-05-15T16:17:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "_Epreus"
      },
      {
        "avatar_url": "https://a.ppy.sh/7614055?1588090765.jpeg",
        "country_code": "MY",
        "default_group": "default",
        "id": 7614055,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-05-13T09:04:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Aasheda_"
      },
      {
        "avatar_url": "https://a.ppy.sh/9505704?1585499762.jpeg",
        "country_code": "GB",
        "default_group": "bng",
        "id": 9505704,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-05-15T17:53:00+00:00",
        "pm_friends_only": false,
        "profile_colour": "#6B3FA0",
        "username": "spoes",
        "group_badge": {
          "id": 28,
          "identifier": "bng",
          "name": "Beatmap Nominators",
          "short_name": "BN",
          "description": "Upon the tides of change, a new ship sets sail. Hark! The qualifiers are nigh - may all maps rejoice in knowing their approval is upon them.",
          "colour": "#A347EB"
        }
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
        "last_visit": "2020-05-15T16:46:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Firika"
      },
      {
        "avatar_url": "https://a.ppy.sh/12914832?1587661676.jpeg",
        "country_code": "RU",
        "default_group": "default",
        "id": 12914832,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": "2020-05-15T18:02:00+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Sviblow"
      },
      {
        "avatar_url": "https://a.ppy.sh/13009214?1589539975.jpeg",
        "country_code": "US",
        "default_group": "default",
        "id": 13009214,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": true,
        "last_visit": "2020-05-15T11:02:42+00:00",
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "Severon"
      },
      {
        "avatar_url": "https://a.ppy.sh/14551330?1588384115.jpeg",
        "country_code": "PE",
        "default_group": "default",
        "id": 14551330,
        "is_active": true,
        "is_bot": false,
        "is_online": false,
        "is_supporter": false,
        "last_visit": null,
        "pm_friends_only": false,
        "profile_colour": null,
        "username": "FAJIFBEFJHA"
      }
    ]
  },
  "reviews_enabled": false
}
"""