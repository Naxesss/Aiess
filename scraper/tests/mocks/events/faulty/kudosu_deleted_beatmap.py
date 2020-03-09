from bs4 import BeautifulSoup, Tag

from requester import soupify

HTML = """
<div class="beatmapset-events__event">
    <div class="beatmapset-event">
        <span>deleted<br>beatmap</span>
        <div class="beatmapset-event__icon beatmapset-event__icon--kudosu-gain beatmapset-activities__event-icon-spacer"></div>
        <div>
            <div class="beatmapset-event__content">
                Discussion #1370674 by
                <a class="user-name js-usercard" data-user-id="3822808" href="https://osu.ppy.sh/users/3822808" style="">
                    ekisu
                </a>
                obtained enough votes for kudosu.
            </div>
            <div>
                <time class="timeago" datetime="2020-02-05T20:27:10+00:00" data-orig-title="February 5, 2020 at 8:27:10 PM UTC" data-hasqtip="40" aria-describedby="qtip-40">
                    about a month ago
                </time>
            </div>
        </div>
    </div>
</div>
"""
soup: BeautifulSoup = soupify(HTML)
tag: Tag = soup.find("div", {"class": "beatmapset-event"})