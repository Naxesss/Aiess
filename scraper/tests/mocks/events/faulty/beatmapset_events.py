import sys
sys.path.append('..')

from bs4 import BeautifulSoup

from scraper.requester import soupify

HTML = """
<div class="beatmapset-events" id="events">
    <div class="beatmapset-events__title"></div>
    <div class="beatmapset-events__event">
        <div class="beatmapset-event">
            <a href="https://osu.ppy.sh/beatmapsets/2/discussion#/1261263" title="
                    Ukakuf Kins - t+pazolite feat. Nanahira
                    (mapped by My Angel RangE)
                ">
                <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/978604/covers/list.jpg?1579575141" srcset="https://assets.ppy.sh/beatmaps/978604/covers/list.jpg?1579575141 1x, https://assets.ppy.sh/beatmaps/978604/covers/list@2x.jpg?1579575141 2x">
            </a>
            <div class="beatmapset-event__icon beatmapset-event__icon--issue-resolve beatmapset-activities__event-icon-spacer"></div>
            <div>
                <div class="beatmapset-event__content">
                    Issue <a href="https://osu.ppy.sh/beatmapsets/978604/discussion#/1261263">#1261263</a> marked as resolved.
                </div>
                <div>
                    <time class="js-timeago" datetime="2020-01-24T10:59:48+00:00" title="January 24, 2020 at 10:59:48 AM UTC">
                        less than a minute ago
                    </time>
                </div>
            </div>
        </div>
    </div>
    <div class="beatmapset-events__event">
        <div class="beatmapset-event">
            <a href="https://osu.ppy.sh/beatmapsets/1013400/discussion" title="
                    AsiaN distractive - Nekomata Gekidan
                    (mapped by Tofu1222)
                ">
                    <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/1013400/covers/list.jpg?1575275088" srcset="https://assets.ppy.sh/beatmaps/1013400/covers/list.jpg?1575275088 1x, https://assets.ppy.sh/beatmaps/1013400/covers/list@2x.jpg?1575275088 2x">
                </a>
                <div class="beatmapset-event__icon beatmapset-event__icon--nominate beatmapset-activities__event-icon-spacer"></div>
                <div>
                    <div class="beatmapset-event__content">
                        Nominated by <a class="user-name js-usercard" data-user-id="1653229" href="https://osu.ppy.sh/users/1653229" style="color: #6B3FA0">_Stan</a>.
                    </div>
                    <div><time class="js-timeago" datetime="2019-12-05T12:39:39+00:00" title="December 5, 2019 at 12:39:39 PM UTC">about 6 hours ago</time></div>
                </div>
        </div>
    </div>
</div>
"""
soup: BeautifulSoup = soupify(HTML)