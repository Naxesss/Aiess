from bs4 import BeautifulSoup, Tag

from requester import soupify

HTML = """
<div class="beatmapset-events__event">
    <div class="beatmapset-event">
        <span>deleted<br>beatmap</span>
        <div class="beatmapset-event__icon beatmapset-event__icon--issue-resolve beatmapset-activities__event-icon-spacer"></div>
        <div>
            <div class="beatmapset-event__content">
                Issue #1336967 marked as resolved.
            </div>
            <div><time class="timeago" datetime="2020-01-03T21:08:34+00:00" data-orig-title="January 3, 2020 at 9:08:34 PM UTC" data-hasqtip="8" aria-describedby="qtip-8">about a month ago</time></div>
        </div>
    </div>
</div>
"""
soup: BeautifulSoup = soupify(HTML)
tag: Tag = soup.find("div", {"class": "beatmapset-event"})