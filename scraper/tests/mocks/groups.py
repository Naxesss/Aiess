import sys
sys.path.append('..')

from scraper.requester import soupify

JSON = r"""
[
  {
    "avatar_url": "https://a.ppy.sh/1653229?1657618519.jpeg",
    "country_code": "CN",
    "default_group": "nat",
    "id": 1653229,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T15:51:10+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "_Stan",
    "country": {
      "code": "CN",
      "name": "China"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/1653229/af03382af5b170c90cb5baedf1d043068fa4b9eae9ddfbf966c0c9bf7292f244.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/1653229/af03382af5b170c90cb5baedf1d043068fa4b9eae9ddfbf966c0c9bf7292f244.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "mania"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 43,
        "progress": 62
      },
      "global_rank": 714095,
      "pp": 623.664,
      "ranked_score": 255335411,
      "hit_accuracy": 95.5078,
      "play_count": 1539,
      "play_time": 116563,
      "total_score": 544110384,
      "total_hits": 314378,
      "maximum_combo": 791,
      "replays_watched_by_others": 0,
      "is_ranked": true,
      "grade_counts": {
        "ss": 36,
        "ssh": 4,
        "s": 79,
        "sh": 10,
        "a": 77
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/2202163?1621774329.jpeg",
    "country_code": "GB",
    "default_group": "nat",
    "id": 2202163,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "-Mo-",
    "country": {
      "code": "GB",
      "name": "United Kingdom"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/2202163/55c4bb3e468973bcd24578528eaa6a57ebee7d780fdf40510f74755aa5096469.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/2202163/55c4bb3e468973bcd24578528eaa6a57ebee7d780fdf40510f74755aa5096469.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 47
      },
      "global_rank": 54598,
      "pp": 5087.96,
      "ranked_score": 18636112580,
      "hit_accuracy": 98.9963,
      "play_count": 37169,
      "play_time": 2343346,
      "total_score": 74372065962,
      "total_hits": 9721310,
      "maximum_combo": 3589,
      "replays_watched_by_others": 157,
      "is_ranked": true,
      "grade_counts": {
        "ss": 0,
        "ssh": 90,
        "s": 0,
        "sh": 973,
        "a": 856
      }
    },
    "support_level": 3
  },
  {
    "avatar_url": "https://a.ppy.sh/5579871?1665614546.jpeg",
    "country_code": "CA",
    "default_group": "nat",
    "id": 5579871,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Agatsu",
    "country": {
      "code": "CA",
      "name": "Canada"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/5579871/ed61d0fb2b02ce4aa8cc435d4a9aac18d9632d1720123c566a79cd4370475197.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/5579871/ed61d0fb2b02ce4aa8cc435d4a9aac18d9632d1720123c566a79cd4370475197.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 19
      },
      "global_rank": 19019,
      "pp": 6741.43,
      "ranked_score": 14511249452,
      "hit_accuracy": 98.0064,
      "play_count": 43513,
      "play_time": 1849335,
      "total_score": 46648082467,
      "total_hits": 6282687,
      "maximum_combo": 2706,
      "replays_watched_by_others": 217,
      "is_ranked": true,
      "grade_counts": {
        "ss": 28,
        "ssh": 38,
        "s": 338,
        "sh": 604,
        "a": 774
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/11119539?1667164953.jpeg",
    "country_code": "BY",
    "default_group": "nat",
    "id": 11119539,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T22:20:32+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "AirinCat",
    "country": {
      "code": "BY",
      "name": "Belarus"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/11119539/e2e518ff379373ac040fdd6bfdb90f0465da749aad929b2412ceab569c001684.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/11119539/e2e518ff379373ac040fdd6bfdb90f0465da749aad929b2412ceab569c001684.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 98,
        "progress": 43
      },
      "global_rank": 296008,
      "pp": 2032.82,
      "ranked_score": 5005479942,
      "hit_accuracy": 97.2293,
      "play_count": 14093,
      "play_time": 1199563,
      "total_score": 14785753388,
      "total_hits": 3701793,
      "maximum_combo": 1378,
      "replays_watched_by_others": 40,
      "is_ranked": true,
      "grade_counts": {
        "ss": 15,
        "ssh": 2,
        "s": 413,
        "sh": 47,
        "a": 754
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/2596306?1666891690.jpeg",
    "country_code": "VN",
    "default_group": "nat",
    "id": 2596306,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Akasha-",
    "country": {
      "code": "VN",
      "name": "Vietnam"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/2596306/cad3d80fed72573d0440fc61bb05d362d0cd651aeb3a8b5c461f2308b37c2b90.jpeg",
      "url": "https://osu.ppy.sh/images/headers/profile-covers/c3.jpg",
      "id": "3"
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "mania"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 79,
        "progress": 56
      },
      "global_rank": 407463,
      "pp": 1447.93,
      "ranked_score": 1338090985,
      "hit_accuracy": 97.0337,
      "play_count": 4697,
      "play_time": 257762,
      "total_score": 3326419883,
      "total_hits": 712703,
      "maximum_combo": 1304,
      "replays_watched_by_others": 7,
      "is_ranked": true,
      "grade_counts": {
        "ss": 18,
        "ssh": 12,
        "s": 137,
        "sh": 42,
        "a": 210
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/2474015?1635531058.png",
    "country_code": "DE",
    "default_group": "nat",
    "id": 2474015,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T21:13:25+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Capu",
    "country": {
      "code": "DE",
      "name": "Germany"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/2474015/8d52409d156fb401c0bc4720c8e5736424459ce9cc98be15d95dc0e8258fc977.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/2474015/8d52409d156fb401c0bc4720c8e5736424459ce9cc98be15d95dc0e8258fc977.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "taiko"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 91
      },
      "global_rank": 8214,
      "pp": 8014.55,
      "ranked_score": 23854254113,
      "hit_accuracy": 99.2964,
      "play_count": 66954,
      "play_time": 3404022,
      "total_score": 118267691353,
      "total_hits": 15104664,
      "maximum_combo": 3139,
      "replays_watched_by_others": 553,
      "is_ranked": true,
      "grade_counts": {
        "ss": 42,
        "ssh": 36,
        "s": 660,
        "sh": 364,
        "a": 1474
      }
    },
    "support_level": 3
  },
  {
    "avatar_url": "https://a.ppy.sh/3621552?1656959062.png",
    "country_code": "HK",
    "default_group": "nat",
    "id": 3621552,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Chaoslitz",
    "country": {
      "code": "HK",
      "name": "Hong Kong"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/3621552/7a4c0872df350f1443a34fcecc8dc974dc1ddf0492996805165218719678c4b7.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/3621552/7a4c0872df350f1443a34fcecc8dc974dc1ddf0492996805165218719678c4b7.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 103,
        "progress": 21
      },
      "global_rank": 3640,
      "pp": 9283.37,
      "ranked_score": 55904272605,
      "hit_accuracy": 99.9874,
      "play_count": 121640,
      "play_time": 6180243,
      "total_score": 348588642083,
      "total_hits": 22433155,
      "maximum_combo": 5936,
      "replays_watched_by_others": 24208,
      "is_ranked": true,
      "grade_counts": {
        "ss": 9700,
        "ssh": 450,
        "s": 458,
        "sh": 71,
        "a": 0
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/318565?1557425901.png",
    "country_code": "ES",
    "default_group": "nat",
    "id": 318565,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Deif",
    "country": {
      "code": "ES",
      "name": "Spain"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/318565/0c64a88f8032091ae16be8184d5d67f1baaa5ba1721a0839fb4dd3b7b56989e5.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/318565/0c64a88f8032091ae16be8184d5d67f1baaa5ba1721a0839fb4dd3b7b56989e5.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "fruits"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 4
      },
      "global_rank": 138550,
      "pp": 3462.56,
      "ranked_score": 8703179540,
      "hit_accuracy": 98.0552,
      "play_count": 21828,
      "play_time": 1310796,
      "total_score": 31675818693,
      "total_hits": 5714687,
      "maximum_combo": 2141,
      "replays_watched_by_others": 5,
      "is_ranked": true,
      "grade_counts": {
        "ss": 1,
        "ssh": 4,
        "s": 231,
        "sh": 138,
        "a": 927
      }
    },
    "support_level": 3
  },
  {
    "avatar_url": "https://a.ppy.sh/8039342?1667052308.jpeg",
    "country_code": "AU",
    "default_group": "nat",
    "id": 8039342,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T21:58:55+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "elicz1",
    "country": {
      "code": "AU",
      "name": "Australia"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/8039342/b5e97fc28769daf97cbe6d83487607bb16defe94cb08c660f3701bad0639282c.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/8039342/b5e97fc28769daf97cbe6d83487607bb16defe94cb08c660f3701bad0639282c.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 25
      },
      "global_rank": 44595,
      "pp": 5404.07,
      "ranked_score": 11833342130,
      "hit_accuracy": 99.032,
      "play_count": 37325,
      "play_time": 2699605,
      "total_score": 52805346212,
      "total_hits": 9705763,
      "maximum_combo": 1943,
      "replays_watched_by_others": 39,
      "is_ranked": true,
      "grade_counts": {
        "ss": 14,
        "ssh": 15,
        "s": 397,
        "sh": 54,
        "a": 1166
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/845733?1666691897.jpeg",
    "country_code": "HK",
    "default_group": "nat",
    "id": 845733,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Faputa",
    "country": {
      "code": "HK",
      "name": "Hong Kong"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/845733/110f3dc9376dd6ee327f0fdedbb46fae6501611863be2b44282c04aa31a1a9bb.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/845733/110f3dc9376dd6ee327f0fdedbb46fae6501611863be2b44282c04aa31a1a9bb.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "taiko"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 98,
        "progress": 12
      },
      "global_rank": 65363,
      "pp": 4794.53,
      "ranked_score": 4442897523,
      "hit_accuracy": 98.6076,
      "play_count": 16039,
      "play_time": 766529,
      "total_score": 13169917362,
      "total_hits": 2710587,
      "maximum_combo": 1372,
      "replays_watched_by_others": 14,
      "is_ranked": true,
      "grade_counts": {
        "ss": 37,
        "ssh": 27,
        "s": 334,
        "sh": 113,
        "a": 741
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/9590557?1657109734.jpeg",
    "country_code": "CN",
    "default_group": "nat",
    "id": 9590557,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-02T23:35:11+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Firika",
    "country": {
      "code": "CN",
      "name": "China"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/9590557/46e06b19dd84ae76eda63ce2a093ea0867dc3538d52faf2f8e714df8f0b7967c.gif",
      "url": "https://assets.ppy.sh/user-profile-covers/9590557/46e06b19dd84ae76eda63ce2a093ea0867dc3538d52faf2f8e714df8f0b7967c.gif",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      },
      {
        "colour": "#99EB47",
        "has_listing": true,
        "has_playmodes": false,
        "id": 4,
        "identifier": "gmt",
        "is_probationary": false,
        "name": "Global Moderation Team",
        "short_name": "GMT",
        "playmodes": null
      }
    ],
    "statistics": {
      "level": {
        "current": 101,
        "progress": 88
      },
      "global_rank": 5032,
      "pp": 8749.19,
      "ranked_score": 30183050236,
      "hit_accuracy": 98.1751,
      "play_count": 115340,
      "play_time": 6526259,
      "total_score": 215371077878,
      "total_hits": 28300583,
      "maximum_combo": 4140,
      "replays_watched_by_others": 9151,
      "is_ranked": true,
      "grade_counts": {
        "ss": 10,
        "ssh": 161,
        "s": 9,
        "sh": 833,
        "a": 1164
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/10773882?1667164889.jpeg",
    "country_code": "DE",
    "default_group": "nat",
    "id": 10773882,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "FuJu",
    "country": {
      "code": "DE",
      "name": "Germany"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/10773882/52b104c4ac0594421c3de768ac56a016f3d795d0acfcdab1c93fa820705ef63e.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/10773882/52b104c4ac0594421c3de768ac56a016f3d795d0acfcdab1c93fa820705ef63e.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 30
      },
      "global_rank": 37141,
      "pp": 5698.55,
      "ranked_score": 17133247376,
      "hit_accuracy": 98.4613,
      "play_count": 34157,
      "play_time": 1953798,
      "total_score": 57536319559,
      "total_hits": 7046329,
      "maximum_combo": 2230,
      "replays_watched_by_others": 44,
      "is_ranked": true,
      "grade_counts": {
        "ss": 36,
        "ssh": 6,
        "s": 895,
        "sh": 51,
        "a": 1426
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/2369776?1609605030.png",
    "country_code": "NL",
    "default_group": "nat",
    "id": 2369776,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T19:13:04+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Greaper",
    "country": {
      "code": "NL",
      "name": "Netherlands"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/2369776/282393948d76014dea483e92a766859662850a24cafb1af84737972875a6ba91.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/2369776/282393948d76014dea483e92a766859662850a24cafb1af84737972875a6ba91.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "fruits"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 89,
        "progress": 69
      },
      "global_rank": null,
      "pp": 0,
      "ranked_score": 1251629691,
      "hit_accuracy": 96.1726,
      "play_count": 9215,
      "play_time": 457428,
      "total_score": 4820303428,
      "total_hits": 1391752,
      "maximum_combo": 1056,
      "replays_watched_by_others": 0,
      "is_ranked": false,
      "grade_counts": {
        "ss": 0,
        "ssh": 0,
        "s": 92,
        "sh": 0,
        "a": 328
      }
    },
    "support_level": 3
  },
  {
    "avatar_url": "https://a.ppy.sh/7823498?1656744521.png",
    "country_code": "SG",
    "default_group": "nat",
    "id": 7823498,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Kotoha",
    "country": {
      "code": "SG",
      "name": "Singapore"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/7823498/c6b99e31f3802d19a33ea5308b0aa8dc2e59ba2da4261db0fb5098c2528bd781.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/7823498/c6b99e31f3802d19a33ea5308b0aa8dc2e59ba2da4261db0fb5098c2528bd781.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 52
      },
      "global_rank": 12716,
      "pp": 7357.61,
      "ranked_score": 12602174672,
      "hit_accuracy": 97.7938,
      "play_count": 85261,
      "play_time": 3336268,
      "total_score": 79866292190,
      "total_hits": 12013198,
      "maximum_combo": 3673,
      "replays_watched_by_others": 226,
      "is_ranked": true,
      "grade_counts": {
        "ss": 16,
        "ssh": 10,
        "s": 283,
        "sh": 340,
        "a": 798
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/4335785?1666500858.png",
    "country_code": "ID",
    "default_group": "nat",
    "id": 4335785,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2022-11-03T23:57:30+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Maxus",
    "country": {
      "code": "ID",
      "name": "Indonesia"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/4335785/ba879b059dcfc3f95e98798779ce40a324ca9ecf37b81ad9cf3468922a21e297.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/4335785/ba879b059dcfc3f95e98798779ce40a324ca9ecf37b81ad9cf3468922a21e297.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "mania"
        ]
      },
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
          "mania"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 44,
        "progress": 46
      },
      "global_rank": 843507,
      "pp": 455.04,
      "ranked_score": 322037998,
      "hit_accuracy": 95.7534,
      "play_count": 1176,
      "play_time": 76658,
      "total_score": 576529806,
      "total_hits": 161497,
      "maximum_combo": 1133,
      "replays_watched_by_others": 0,
      "is_ranked": true,
      "grade_counts": {
        "ss": 1,
        "ssh": 1,
        "s": 65,
        "sh": 34,
        "a": 85
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/8129817?1637040307.jpeg",
    "country_code": "SE",
    "default_group": "nat",
    "id": 8129817,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2022-11-03T23:58:14+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Naxess",
    "country": {
      "code": "SE",
      "name": "Sweden"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/8129817/b723ded20a013b63f7d3d3ddaa8daf27d3a8487d0987639b9c69a99bd41012b7.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/8129817/b723ded20a013b63f7d3d3ddaa8daf27d3a8487d0987639b9c69a99bd41012b7.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 16
      },
      "global_rank": null,
      "pp": 0,
      "ranked_score": 9309240880,
      "hit_accuracy": 99.1641,
      "play_count": 20031,
      "play_time": 1328070,
      "total_score": 43439327203,
      "total_hits": 5199290,
      "maximum_combo": 2008,
      "replays_watched_by_others": 100,
      "is_ranked": false,
      "grade_counts": {
        "ss": 0,
        "ssh": 45,
        "s": 28,
        "sh": 473,
        "a": 346
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/13822800?1664228063.jpeg",
    "country_code": "GB",
    "default_group": "nat",
    "id": 13822800,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "NexusQI",
    "country": {
      "code": "GB",
      "name": "United Kingdom"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/13822800/e45a6eeb06516d08c1c445fa89c461fe84a9faff4408891f5fdf985f40c99a4d.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/13822800/e45a6eeb06516d08c1c445fa89c461fe84a9faff4408891f5fdf985f40c99a4d.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 13
      },
      "global_rank": 43369,
      "pp": 5447.53,
      "ranked_score": 8595996846,
      "hit_accuracy": 98.9688,
      "play_count": 29690,
      "play_time": 1943395,
      "total_score": 40610158428,
      "total_hits": 7139785,
      "maximum_combo": 2015,
      "replays_watched_by_others": 20,
      "is_ranked": true,
      "grade_counts": {
        "ss": 19,
        "ssh": 6,
        "s": 338,
        "sh": 41,
        "a": 1062
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/3178418?1597522210.png",
    "country_code": "US",
    "default_group": "nat",
    "id": 3178418,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T23:02:23+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "pishifat",
    "country": {
      "code": "US",
      "name": "United States"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/3178418/0380c8d135523002db14fbf3af2a355fe461ae6cc4ef71a6ad9d2c9eac31b658.png",
      "url": "https://assets.ppy.sh/user-profile-covers/3178418/0380c8d135523002db14fbf3af2a355fe461ae6cc4ef71a6ad9d2c9eac31b658.png",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 101,
        "progress": 66
      },
      "global_rank": 26808,
      "pp": 6204.39,
      "ranked_score": 80612353379,
      "hit_accuracy": 98.841,
      "play_count": 98035,
      "play_time": 4232653,
      "total_score": 193063503738,
      "total_hits": 18449326,
      "maximum_combo": 5221,
      "replays_watched_by_others": 3784,
      "is_ranked": true,
      "grade_counts": {
        "ss": 117,
        "ssh": 97,
        "s": 1628,
        "sh": 2834,
        "a": 1771
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/4725379?1647298554.jpeg",
    "country_code": "ES",
    "default_group": "nat",
    "id": 4725379,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2022-11-03T23:57:09+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Quenlla",
    "country": {
      "code": "ES",
      "name": "Spain"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/4725379/65815d485e111baff306df142428be9eb047175c8e52d0d581dc7c934d574ad2.png",
      "url": "https://assets.ppy.sh/user-profile-covers/4725379/65815d485e111baff306df142428be9eb047175c8e52d0d581dc7c934d574ad2.png",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "mania"
        ]
      },
      {
        "colour": "#FFD1DC",
        "has_listing": true,
        "has_playmodes": true,
        "id": 31,
        "identifier": "loved",
        "is_probationary": false,
        "name": "Project Loved",
        "short_name": "LVD",
        "playmodes": []
      }
    ],
    "statistics": {
      "level": {
        "current": 97,
        "progress": 12
      },
      "global_rank": null,
      "pp": 0,
      "ranked_score": 2090074161,
      "hit_accuracy": 94.1101,
      "play_count": 16827,
      "play_time": 1056084,
      "total_score": 9893218391,
      "total_hits": 3936365,
      "maximum_combo": 1055,
      "replays_watched_by_others": 2,
      "is_ranked": false,
      "grade_counts": {
        "ss": 23,
        "ssh": 0,
        "s": 138,
        "sh": 0,
        "a": 304
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/7131099?1667486264.jpeg",
    "country_code": "US",
    "default_group": "nat",
    "id": 7131099,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "radar",
    "country": {
      "code": "US",
      "name": "United States"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/7131099/b0fc88a15acd8652bc888079a0d5ed0e8664c7139decb951a77ad47f8bd0d670.png",
      "url": "https://assets.ppy.sh/user-profile-covers/7131099/b0fc88a15acd8652bc888079a0d5ed0e8664c7139decb951a77ad47f8bd0d670.png",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "taiko"
        ]
      },
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
          "taiko",
          "fruits"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 98,
        "progress": 76
      },
      "global_rank": 56643,
      "pp": 5029.18,
      "ranked_score": 1577894027,
      "hit_accuracy": 96.5817,
      "play_count": 20527,
      "play_time": 1018830,
      "total_score": 16491545860,
      "total_hits": 3311781,
      "maximum_combo": 1923,
      "replays_watched_by_others": 44,
      "is_ranked": true,
      "grade_counts": {
        "ss": 4,
        "ssh": 1,
        "s": 42,
        "sh": 23,
        "a": 106
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/2306637?1656982647.png",
    "country_code": "US",
    "default_group": "nat",
    "id": 2306637,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T23:45:17+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Secre",
    "country": {
      "code": "US",
      "name": "United States"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/2306637/311c9b80839f4c555d9d2c559fb9dfe09afc0cb11d94c4a58b6cb1aacad6630d.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/2306637/311c9b80839f4c555d9d2c559fb9dfe09afc0cb11d94c4a58b6cb1aacad6630d.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "fruits"
        ]
      },
      {
        "colour": "#FFD1DC",
        "has_listing": true,
        "has_playmodes": true,
        "id": 31,
        "identifier": "loved",
        "is_probationary": false,
        "name": "Project Loved",
        "short_name": "LVD",
        "playmodes": [
          "fruits"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 94,
        "progress": 98
      },
      "global_rank": null,
      "pp": 0,
      "ranked_score": 2129675028,
      "hit_accuracy": 98.1211,
      "play_count": 11280,
      "play_time": 482008,
      "total_score": 6732594066,
      "total_hits": 1599676,
      "maximum_combo": 1212,
      "replays_watched_by_others": 0,
      "is_ranked": false,
      "grade_counts": {
        "ss": 6,
        "ssh": 3,
        "s": 125,
        "sh": 27,
        "a": 235
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/12402453?1647328702.jpeg",
    "country_code": "US",
    "default_group": "nat",
    "id": 12402453,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T18:46:55+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "StarCastler",
    "country": {
      "code": "US",
      "name": "United States"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/12402453/61920d0b496147cf78796a3d6d3fd833b9805e26befd9c227328e5b33dfa2fc3.png",
      "url": "https://osu.ppy.sh/images/headers/profile-covers/c7.jpg",
      "id": "7"
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 40
      },
      "global_rank": null,
      "pp": 0,
      "ranked_score": 15186651563,
      "hit_accuracy": 98.5956,
      "play_count": 77515,
      "play_time": 3599966,
      "total_score": 67206756354,
      "total_hits": 9578068,
      "maximum_combo": 3320,
      "replays_watched_by_others": 551,
      "is_ranked": false,
      "grade_counts": {
        "ss": 118,
        "ssh": 132,
        "s": 1213,
        "sh": 840,
        "a": 814
      }
    },
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/9000308?1649518719.jpeg",
    "country_code": "AT",
    "default_group": "nat",
    "id": 9000308,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T13:07:12+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Stixy",
    "country": {
      "code": "AT",
      "name": "Austria"
    },
    "cover": {
      "custom_url": null,
      "url": "https://osu.ppy.sh/images/headers/profile-covers/c2.jpg",
      "id": "2"
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 97,
        "progress": 33
      },
      "global_rank": 75812,
      "pp": 4550.49,
      "ranked_score": 2330609508,
      "hit_accuracy": 98.8308,
      "play_count": 16203,
      "play_time": 730398,
      "total_score": 10512351045,
      "total_hits": 2431661,
      "maximum_combo": 1324,
      "replays_watched_by_others": 3,
      "is_ranked": true,
      "grade_counts": {
        "ss": 10,
        "ssh": 0,
        "s": 123,
        "sh": 0,
        "a": 376
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/8646059?1662751277.jpeg",
    "country_code": "US",
    "default_group": "nat",
    "id": 8646059,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T22:20:34+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "UberFazz",
    "country": {
      "code": "US",
      "name": "United States"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/8646059/7e80974eb446b736a0b3386d93c498f1ffdaa0bf3afe4cfb66011d7c055d3d5a.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/8646059/7e80974eb446b736a0b3386d93c498f1ffdaa0bf3afe4cfb66011d7c055d3d5a.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      },
      {
        "colour": "#FFD1DC",
        "has_listing": true,
        "has_playmodes": true,
        "id": 31,
        "identifier": "loved",
        "is_probationary": false,
        "name": "Project Loved",
        "short_name": "LVD",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 102,
        "progress": 39
      },
      "global_rank": 1460,
      "pp": 10726.6,
      "ranked_score": 53924397130,
      "hit_accuracy": 98.4735,
      "play_count": 96546,
      "play_time": 6170885,
      "total_score": 266807532813,
      "total_hits": 28024029,
      "maximum_combo": 4617,
      "replays_watched_by_others": 10221,
      "is_ranked": true,
      "grade_counts": {
        "ss": 8,
        "ssh": 51,
        "s": 77,
        "sh": 643,
        "a": 2172
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/7560872?1667112763.jpeg",
    "country_code": "US",
    "default_group": "nat",
    "id": 7560872,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T17:43:47+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Unpredictable",
    "country": {
      "code": "US",
      "name": "United States"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/7560872/f9a9199e3dfd8552d42e23b265dffe03d7919b0abcbbbb92468b77db072c9bfd.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/7560872/f9a9199e3dfd8552d42e23b265dffe03d7919b0abcbbbb92468b77db072c9bfd.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "mania"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 9
      },
      "global_rank": 124965,
      "pp": 3664.87,
      "ranked_score": 2425254118,
      "hit_accuracy": 99.4536,
      "play_count": 69874,
      "play_time": 2301299,
      "total_score": 36641742515,
      "total_hits": 6247132,
      "maximum_combo": 1698,
      "replays_watched_by_others": 8,
      "is_ranked": true,
      "grade_counts": {
        "ss": 32,
        "ssh": 13,
        "s": 384,
        "sh": 6,
        "a": 115
      }
    },
    "support_level": 3
  },
  {
    "avatar_url": "https://a.ppy.sh/4945926?1450105653.jpg",
    "country_code": "BE",
    "default_group": "nat",
    "id": 4945926,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2022-11-03T21:41:08+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "yaspo",
    "country": {
      "code": "BE",
      "name": "Belgium"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/4945926/cee3ac889dc5183039d3ed077053ec84d5396c33eb908913e50dad032c220529.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/4945926/cee3ac889dc5183039d3ed077053ec84d5396c33eb908913e50dad032c220529.jpeg",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      }
    ],
    "statistics": {
      "level": {
        "current": 100,
        "progress": 83
      },
      "global_rank": 25882,
      "pp": 6261.28,
      "ranked_score": 39715047897,
      "hit_accuracy": 98.7848,
      "play_count": 64734,
      "play_time": 4450962,
      "total_score": 110729033798,
      "total_hits": 18116243,
      "maximum_combo": 2283,
      "replays_watched_by_others": 37,
      "is_ranked": true,
      "grade_counts": {
        "ss": 42,
        "ssh": 7,
        "s": 1403,
        "sh": 84,
        "a": 3189
      }
    },
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/8953955?1667052869.jpeg",
    "country_code": "PL",
    "default_group": "nat",
    "id": 8953955,
    "is_active": true,
    "is_bot": false,
    "is_deleted": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Zelq",
    "country": {
      "code": "PL",
      "name": "Poland"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/8953955/1f5544f00efc826e63675b64f37db8f36ce0a22481e8ba7c6dc9f37e4a17b8c5.png",
      "url": "https://assets.ppy.sh/user-profile-covers/8953955/1f5544f00efc826e63675b64f37db8f36ce0a22481e8ba7c6dc9f37e4a17b8c5.png",
      "id": null
    },
    "groups": [
      {
        "colour": "#EB8C47",
        "has_listing": true,
        "has_playmodes": true,
        "id": 7,
        "identifier": "nat",
        "is_probationary": false,
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "playmodes": [
          "osu"
        ]
      },
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
    ],
    "statistics": {
      "level": {
        "current": 103,
        "progress": 64
      },
      "global_rank": 1027,
      "pp": 11336,
      "ranked_score": 58188786588,
      "hit_accuracy": 99.4194,
      "play_count": 151372,
      "play_time": 7463225,
      "total_score": 391288005885,
      "total_hits": 30696008,
      "maximum_combo": 6369,
      "replays_watched_by_others": 647,
      "is_ranked": true,
      "grade_counts": {
        "ss": 100,
        "ssh": 120,
        "s": 1048,
        "sh": 359,
        "a": 1667
      }
    },
    "support_level": 2
  }
]
"""

HTML = f"""
<script id="json-users" type="application/json">
    {JSON}
</script>
"""

soup = soupify(HTML)