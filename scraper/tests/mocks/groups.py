import sys
sys.path.append('..')

from scraper.requester import soupify

JSON = r"""
[
  {
    "avatar_url": "https://a.ppy.sh/2202163?1474069711.png",
    "country_code": "GB",
    "default_group": "nat",
    "id": 2202163,
    "is_active": true,
    "is_bot": false,
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
    "current_mode_rank": 42545,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 3
  },
  {
    "avatar_url": "https://a.ppy.sh/3621552?1582298449.png",
    "country_code": "HK",
    "default_group": "nat",
    "id": 3621552,
    "is_active": true,
    "is_bot": false,
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
      "custom_url": "https://assets.ppy.sh/user-profile-covers/3621552/4b2abc5bf98ceedd78810f0de666bb946508dc8f10bf6692732f4ea2b3cab9ec.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/3621552/4b2abc5bf98ceedd78810f0de666bb946508dc8f10bf6692732f4ea2b3cab9ec.jpeg",
      "id": null
    },
    "current_mode_rank": 2265,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/318565?1557425901.png",
    "country_code": "ES",
    "default_group": "nat",
    "id": 318565,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2020-07-28T01:49:00+00:00",
    "pm_friends_only": false,
    "profile_colour": "#6eac0a",
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
    "current_mode_rank": 99932,
    "groups": [
      {
        "id": 4,
        "identifier": "gmt",
        "name": "Global Moderation Team",
        "short_name": "GMT",
        "description": "",
        "colour": "#99EB47"
      },
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 3
  },
  {
    "avatar_url": "https://a.ppy.sh/845733?1589346712.jpeg",
    "country_code": "HK",
    "default_group": "nat",
    "id": 845733,
    "is_active": true,
    "is_bot": false,
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
    "current_mode_rank": 52765,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/4815717?1564177091.jpeg",
    "country_code": "DE",
    "default_group": "nat",
    "id": 4815717,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Feerum",
    "country": {
      "code": "DE",
      "name": "Germany"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/4815717/0e42eab352c2a8ef2dedc2b1f917f981e8f1f299b2218df1d50ab21753e2df26.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/4815717/0e42eab352c2a8ef2dedc2b1f917f981e8f1f299b2218df1d50ab21753e2df26.jpeg",
      "id": null
    },
    "current_mode_rank": 65473,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/2369776?1559216117.png",
    "country_code": "NL",
    "default_group": "nat",
    "id": 2369776,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2020-07-27T22:30:00+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Greaper",
    "country": {
      "code": "NL",
      "name": "Netherlands"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/2369776/fc52dbcf21bbca64c83f58a89c17a8d8eef2dbd6a19dbd23cde3430e516cba54.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/2369776/fc52dbcf21bbca64c83f58a89c17a8d8eef2dbd6a19dbd23cde3430e516cba54.jpeg",
      "id": null
    },
    "current_mode_rank": 176618,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 3
  },
  {
    "avatar_url": "https://a.ppy.sh/3193504?1512374286.jpeg",
    "country_code": "CA",
    "default_group": "nat",
    "id": 3193504,
    "is_active": true,
    "is_bot": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2020-07-28T03:55:00+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Kibbleru",
    "country": {
      "code": "CA",
      "name": "Canada"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/3193504/964392afa3931d51e492ecc8441420ff5d2049980a3eaf51aed47db5505778e6.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/3193504/964392afa3931d51e492ecc8441420ff5d2049980a3eaf51aed47db5505778e6.jpeg",
      "id": null
    },
    "current_mode_rank": 66040,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/896613?1552063537.png",
    "country_code": "DE",
    "default_group": "nat",
    "id": 896613,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2020-07-28T00:28:00+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Lasse",
    "country": {
      "code": "DE",
      "name": "Germany"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/896613/cb62b77af634dab1b2b59c2936e29550a10e069b5ef2fcbc5f22d525ef9a97b4.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/896613/cb62b77af634dab1b2b59c2936e29550a10e069b5ef2fcbc5f22d525ef9a97b4.jpeg",
      "id": null
    },
    "current_mode_rank": 40467,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/7138602?1595790161.jpeg",
    "country_code": "NL",
    "default_group": "nat",
    "id": 7138602,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2020-07-27T18:43:00+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Leniane",
    "country": {
      "code": "NL",
      "name": "Netherlands"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/7138602/40832e3dd28c81e73625cb153fb07c798d7d684d038e805d490cf7b40ec137cc.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/7138602/40832e3dd28c81e73625cb153fb07c798d7d684d038e805d490cf7b40ec137cc.jpeg",
      "id": null
    },
    "current_mode_rank": 99160,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 3
  },
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
    "country": {
      "code": "DE",
      "name": "Germany"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/2204515/044f2220b73380eef623b694e432958e47163235d6570c8d0adee3edefdd8e1f.png",
      "url": "https://assets.ppy.sh/user-profile-covers/2204515/044f2220b73380eef623b694e432958e47163235d6570c8d0adee3edefdd8e1f.png",
      "id": null
    },
    "current_mode_rank": 19437,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/8129817?1472484830.png",
    "country_code": "SE",
    "default_group": "nat",
    "id": 8129817,
    "is_active": true,
    "is_bot": false,
    "is_online": true,
    "is_supporter": true,
    "last_visit": "2020-07-28T04:02:00+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Naxess",
    "country": {
      "code": "SE",
      "name": "Sweden"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/8129817/361684f2bae04774ab34755a37722015b3df66e07cb70b06185d56e0c34fb571.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/8129817/361684f2bae04774ab34755a37722015b3df66e07cb70b06185d56e0c34fb571.jpeg",
      "id": null
    },
    "current_mode_rank": 22125,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/6637817?1595804924.jpeg",
    "country_code": "DE",
    "default_group": "nat",
    "id": 6637817,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Nepuri",
    "country": {
      "code": "DE",
      "name": "Germany"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/6637817/592edd86b81e26fef3fcb00cca790082bfe87dd8c75b2f491ff12c4c21ed40b8.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/6637817/592edd86b81e26fef3fcb00cca790082bfe87dd8c75b2f491ff12c4c21ed40b8.jpeg",
      "id": null
    },
    "current_mode_rank": 71311,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/1541323?1595351037.png",
    "country_code": "US",
    "default_group": "nat",
    "id": 1541323,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2020-07-28T02:14:00+00:00",
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Noffy",
    "country": {
      "code": "US",
      "name": "United States"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/1541323/ba01e6f0b169b86f34ecacc2ed90c19438af17af3af9c3dc969231dfdcf8bf98.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/1541323/ba01e6f0b169b86f34ecacc2ed90c19438af17af3af9c3dc969231dfdcf8bf98.jpeg",
      "id": null
    },
    "current_mode_rank": 260902,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/3178418?1575186754.jpeg",
    "country_code": "US",
    "default_group": "nat",
    "id": 3178418,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2020-07-28T02:17:00+00:00",
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
    "current_mode_rank": 17109,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 2
  },
  {
    "avatar_url": "https://a.ppy.sh/2857314?1592176184.png",
    "country_code": "BR",
    "default_group": "nat",
    "id": 2857314,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Seto Kousuke",
    "country": {
      "code": "BR",
      "name": "Brazil"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/2857314/166f8ca003b838385069662c5c3bd4d2dff07fce96f85a5e63d9b683da99c0a3.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/2857314/166f8ca003b838385069662c5c3bd4d2dff07fce96f85a5e63d9b683da99c0a3.jpeg",
      "id": null
    },
    "current_mode_rank": null,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/1421452?1593152188.jpeg",
    "country_code": "TH",
    "default_group": "nat",
    "id": 1421452,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": null,
    "pm_friends_only": false,
    "profile_colour": "#fa3703",
    "username": "Tyistiana",
    "country": {
      "code": "TH",
      "name": "Thailand"
    },
    "cover": {
      "custom_url": "https://assets.ppy.sh/user-profile-covers/1421452/9c5294796c8c48f5676ed66c4cc7d76ac4c9e051e9dee58c6b01a31483b9e422.jpeg",
      "url": "https://assets.ppy.sh/user-profile-covers/1421452/9c5294796c8c48f5676ed66c4cc7d76ac4c9e051e9dee58c6b01a31483b9e422.jpeg",
      "id": null
    },
    "current_mode_rank": 384972,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 1
  },
  {
    "avatar_url": "https://a.ppy.sh/4945926?1450105653.jpg",
    "country_code": "BE",
    "default_group": "nat",
    "id": 4945926,
    "is_active": true,
    "is_bot": false,
    "is_online": false,
    "is_supporter": true,
    "last_visit": "2020-07-28T01:18:00+00:00",
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
    "current_mode_rank": 20773,
    "groups": [
      {
        "id": 7,
        "identifier": "nat",
        "name": "Nomination Assessment Team",
        "short_name": "NAT",
        "description": "",
        "colour": "#EB8C47"
      }
    ],
    "support_level": 1
  }
]
"""

HTML = f"""
<script id="json-users" type="application/json">
    {JSON}
</script>
"""

soup = soupify(HTML)