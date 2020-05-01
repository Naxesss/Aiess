import sys
sys.path.append('..')

from bs4 import BeautifulSoup, Tag

from scraper.requester import soupify

HTML = """
<div class="beatmap-discussions__discussion beatmapset-activities__discussion-post">
    <div class="beatmap-discussion beatmapset-activities__post-grow">
        <div class="beatmap-discussion-timestamp__icons-container">
            <div class="beatmap-discussion-timestamp__icons">
                <a href="https://osu.ppy.sh/beatmapsets/1074596/discussion#/1295203">
                    <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/1074596/covers/list.jpg?1575564822" srcset="https://assets.ppy.sh/beatmaps/1074596/covers/list.jpg?1575564822 1x, https://assets.ppy.sh/beatmaps/1074596/covers/list@2x.jpg?1575564822 2x">
                </a>
                <div class="beatmap-discussion-timestamp__icon beatmapset-activities__timeline-icon-margin">
                    <span class="beatmap-discussion-message-type beatmap-discussion-message-type--problem">
                        <span class="fas fa-exclamation-circle"></span>
                    </span>
                </div>
            </div>
        </div>
        <div class="beatmap-discussion__discussion">
            <div class="beatmap-discussion__top">
                <div class="beatmap-discussion-post beatmap-discussion-post--discussion">
                    <div class="beatmap-discussion-post__content">
                        <div class="beatmap-discussion-user-card beatmap-discussion-user-card--alumni">
                            <div class="beatmap-discussion-user-card__avatar">
                                <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/197805">
                                    <div class="avatar avatar--full-rounded" style="background-image: url(https://a.ppy.sh/197805?1531219665.jpeg)"></div>
                                </a>
                            </div>
                            <div class="beatmap-discussion-user-card__user">
                                <div class="beatmap-discussion-user-card__user-row">
                                    <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/197805">
                                        <span class="beatmap-discussion-user-card__user-text u-ellipsis-overflow">Niva</span>
                                    </a>
                                    <a class="beatmap-discussion-user-card__user-modding-history-link" href="https://osu.ppy.sh/users/197805/modding" title="View modding history">
                                        <i class="fas fa-align-left"></i>
                                    </a>
                                </div>
                                <div class="beatmap-discussion-user-card__user-badge">
                                    <div class="user-group-badge user-group-badge--alumni"></div>
                                </div>
                            </div>
                            <div class="beatmap-discussion-user-card__user-stripe"></div>
                        </div>

                        <div class="beatmap-discussion-post__message-container">
                            <div class="beatmap-discussion-post__message">((in a more serious note tho : 04:05:694 (1) - aimod tells that this slider's end is not snapped properly))</div>
                            <div class="beatmap-discussion-post__info-container">
                                <span class="beatmap-discussion-post__info"><time class="timeago" datetime="2019-12-05T16:50:10+00:00" title="December 5, 2019 at 4:50:10 PM UTC">about 2 hours ago</time></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="beatmap-discussion__line beatmap-discussion__line--resolved"></div>
        </div>
    </div>
</div>
"""
CONTENT = "((in a more serious note tho : 04:05:694 (1) - aimod tells that this slider's end is not snapped properly))"
soup: BeautifulSoup = soupify(HTML)
tag: Tag = soup.find("div", {"class": "beatmapset-activities__discussion-post"})