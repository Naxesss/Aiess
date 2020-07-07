import sys
sys.path.append('..')

from bs4 import BeautifulSoup

from scraper.requester import soupify

JSON = r"""
{
  "beatmapset": {
    "artist": "artist",
    "creator": "someone",
    "id": 4,
    "title": "title",
    "user_id": 1,
    "discussions": [
      {
        "id": 20,
        "user_id": 2,
        "message_type": "praise",
        "created_at": "2020-01-01T00:00:00+00:00",
        "posts": [
          {
            "id": 400,
            "user_id": 2,
            "created_at": "2020-01-01T00:00:00+00:00",
            "message": "wow"
          },
          {
            "id": 401,
            "user_id": 2,
            "created_at": "2020-01-01T00:00:00+00:00",
            "message": "please reply"
          },
          {
            "id": 402,
            "user_id": 1,
            "created_at": "2020-01-01T00:30:00+00:00",
            "message": "yes?"
          },
          {
            "id": 403,
            "user_id": 2,
            "created_at": "2020-01-01T00:31:00+00:00",
            "message": "say hi back"
          },
          {
            "id": 404,
            "user_id": 1,
            "created_at": "2020-01-01T01:00:00+00:00",
            "message": "hi"
          },
          {
            "id": 405,
            "user_id": 2,
            "created_at": "2020-01-01T01:04:00+00:00",
            "message": "thanks"
          }
        ]
      },
      {
        "id": 21,
        "user_id": 2,
        "message_type": "hype",
        "created_at": "2020-01-01T02:30:00+00:00",
        "posts": [
          {
            "id": 500,
            "user_id": 2,
            "created_at": "2020-01-01T02:30:00+00:00",
            "message": "hype"
          }
        ]
      },
      {
        "id": 22,
        "user_id": 2,
        "message_type": "problem",
        "created_at": "2020-01-01T03:00:00+00:00",
        "posts": [
          {
            "id": 600,
            "user_id": 2,
            "created_at": "2020-01-01T03:00:00+00:00",
            "message": "no wait"
          }
        ]
      }
    ],
    "events": [
      {
        "type": "issue_resolve",
        "comment": {
          "beatmap_discussion_id": 20,
          "beatmap_discussion_post_id": 404
        },
        "created_at": "2020-01-01T01:00:00+00:00",
        "user_id": 1
      },
      {
        "type": "nominate",
        "created_at": "2020-01-01T02:30:30+00:00",
        "user_id": 2
      },
      {
        "type": "nominate",
        "created_at": "2020-01-01T02:31:00+00:00",
        "user_id": 1
      },
      {
        "type": "qualify",
        "comment": null,
        "created_at": "2020-01-01T02:31:00+00:00",
        "user_id": null
      },
      {
        "type": "disqualify",
        "comment": {
          "beatmap_discussion_id": 22,
          "beatmap_discussion_post_id": 600
        },
        "created_at": "2020-01-01T03:00:00+00:00",
        "user_id": 2
      }
    ],
    "related_users": [
      {
        "id": 1,
        "username": "someone"
      },
      {
        "id": 2,
        "username": "sometwo"
      }
    ]
  }
}
"""