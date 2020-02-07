from bs4 import BeautifulSoup, Tag

from web.scraper import soupify

FAULTY_HTML = """
<div class="beatmapset-events__event">
    <div class="beatmapset-event">
        <span>Something isn't right here...</span>
    </div>
</div>
"""
ISSUE_RESOLVE_HTML = """
<div class="beatmapset-events__event">
    <div class="beatmapset-event">
        <a href="https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675" title="
            Tokyo's Starlight - HyuN
            (mapped by Heilia)
        ">
            <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/1011055/covers/list.jpg?1575541706" srcset="https://assets.ppy.sh/beatmaps/1011055/covers/list.jpg?1575541706 1x, https://assets.ppy.sh/beatmaps/1011055/covers/list@2x.jpg?1575541706 2x">
        </a>
        <div class="beatmapset-event__icon beatmapset-event__icon--issue-resolve beatmapset-activities__event-icon-spacer"></div>
        <div>
            <div class="beatmapset-event__content">
                Issue <a href="https://osu.ppy.sh/beatmapsets/1011055/discussion#/1294675">#1294675</a> marked as resolved.
            </div>
            <div><time class="timeago" datetime="2019-12-05T10:26:54+00:00" title="December 5, 2019 at 10:26:54 AM UTC">about 7 hours ago</time></div>
        </div>
    </div>
</div>
"""
NOMINATE_HTML = """
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
                <div><time class="timeago" datetime="2019-12-05T12:39:39+00:00" title="December 5, 2019 at 12:39:39 PM UTC">about 6 hours ago</time></div>
            </div>
    </div>
</div>
"""
PROBLEM_HTML = """
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
FIRST_FAULTY_SECOND_CORRECT_HTML_BEATMAPSETS = """
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
                    <time class="timeago" datetime="2020-01-24T10:59:48+00:00" title="January 24, 2020 at 10:59:48 AM UTC">
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
                    <div><time class="timeago" datetime="2019-12-05T12:39:39+00:00" title="December 5, 2019 at 12:39:39 PM UTC">about 6 hours ago</time></div>
                </div>
        </div>
    </div>
</div>
"""
FIRST_CORRECT_SECOND_FAULTY_HTML_DISCUSSIONS = """
<div class="beatmap-discussions__discussion">
    <div class="beatmap-discussions__discussion beatmapset-activities__discussion-post">
        <div class="beatmap-discussion beatmapset-activities__post-grow">
            <div class="beatmap-discussion-timestamp__icons-container">
                <div class="beatmap-discussion-timestamp__icons">
                    <a href="https://osu.ppy.sh/beatmapsets/1094899/discussion#/1367171">
                        <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/1094899/covers/list.jpg?1579725281" srcset="https://assets.ppy.sh/beatmaps/1094899/covers/list.jpg?1579725281 1x, https://assets.ppy.sh/beatmaps/1094899/covers/list@2x.jpg?1579725281 2x">
                    </a>
                    <div class="beatmap-discussion-timestamp__icon beatmapset-activities__timeline-icon-margin">
                        <span class="beatmap-discussion-message-type beatmap-discussion-message-type--suggestion">
                            <span class="far fa-circle"></span>
                        </span>
                    </div>
                </div>
            </div>
            <div class="beatmap-discussion__discussion">
                <div class="beatmap-discussion__top">
                    <div class="beatmap-discussion-post beatmap-discussion-post--discussion">
                        <div class="beatmap-discussion-post__content">
                            <div class="beatmap-discussion-user-card beatmap-discussion-user-card--{&quot;group_id&quot;:32,&quot;group_type&quot;:1,&quot;group_founder_manage&quot;:0,&quot;group_name&quot;:&quot;Beatmap Nominators (Probationary)&quot;,&quot;group_desc&quot;:&quot;&quot;,&quot;group_desc_bitfield&quot;:&quot;&quot;,&quot;group_desc_options&quot;:7,&quot;group_desc_uid&quot;:&quot;&quot;,&quot;group_display&quot;:0,&quot;group_avatar&quot;:&quot;&quot;,&quot;group_avatar_type&quot;:0,&quot;group_avatar_width&quot;:0,&quot;group_avatar_height&quot;:0,&quot;group_rank&quot;:0,&quot;group_colour&quot;:&quot;#6B3FA0&quot;,&quot;group_sig_chars&quot;:0,&quot;group_receive_pm&quot;:0,&quot;group_message_limit&quot;:0,&quot;group_legend&quot;:1,&quot;identifier&quot;:&quot;bng_limited&quot;,&quot;short_name&quot;:&quot;BN&quot;,&quot;display_order&quot;:5,&quot;colour&quot;:&quot;A347EB&quot;}">
                                <div class="beatmap-discussion-user-card__avatar">
                                    <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/9327302">
                                        <div class="avatar avatar--full-rounded" style="background-image: url(https://a.ppy.sh/9327302?1578169305.jpeg)"></div>
                                    </a>
                                </div>
                                <div class="beatmap-discussion-user-card__user">
                                    <div class="beatmap-discussion-user-card__user-row">
                                        <a class="beatmap-discussion-user-card__user-link" href="https://osu.ppy.sh/users/9327302">
                                            <span class="beatmap-discussion-user-card__user-text u-ellipsis-overflow">SMOKELIND</span>
                                        </a>
                                        <a class="beatmap-discussion-user-card__user-modding-history-link" href="https://osu.ppy.sh/users/9327302/modding" title="View modding history">
                                            <i class="fas fa-align-left"></i>
                                        </a>
                                    </div>
                                    <div class="beatmap-discussion-user-card__user-badge">
                                        <div class="user-group-badge user-group-badge--{&quot;group_id&quot;:32,&quot;group_type&quot;:1,&quot;group_founder_manage&quot;:0,&quot;group_name&quot;:&quot;Beatmap Nominators (Probationary)&quot;,&quot;group_desc&quot;:&quot;&quot;,&quot;group_desc_bitfield&quot;:&quot;&quot;,&quot;group_desc_options&quot;:7,&quot;group_desc_uid&quot;:&quot;&quot;,&quot;group_display&quot;:0,&quot;group_avatar&quot;:&quot;&quot;,&quot;group_avatar_type&quot;:0,&quot;group_avatar_width&quot;:0,&quot;group_avatar_height&quot;:0,&quot;group_rank&quot;:0,&quot;group_colour&quot;:&quot;#6B3FA0&quot;,&quot;group_sig_chars&quot;:0,&quot;group_receive_pm&quot;:0,&quot;group_message_limit&quot;:0,&quot;group_legend&quot;:1,&quot;identifier&quot;:&quot;bng_limited&quot;,&quot;short_name&quot;:&quot;BN&quot;,&quot;display_order&quot;:5,&quot;colour&quot;:&quot;A347EB&quot;}"></div>
                                    </div>
                                </div>
                                <div class="beatmap-discussion-user-card__user-stripe"></div>
                            </div>

                            <div class="beatmap-discussion-post__message-container">
                                <div class="beatmap-discussion-post__message">
                                    if you decided to your svs in the diff, could change some values a bit to fit different sections nicer
                                    Considering overall intensity parts like 
                                    00:02:313 - 00:23:411
                                    00:44:510 - 01:05:609
                                    01:16:159 - 01:21:433
                                    Deserve to have slightly lower value, 0.8 or smth, so the difference can be more clear in comparison with other stuff which is more intense in some way 00:23:411, 01:05:609 etc.
                                </div>
                                <div class="beatmap-discussion-post__info-container">
                                    <span class="beatmap-discussion-post__info"><time class="timeago" datetime="2020-01-24T11:17:51+00:00" title="January 24, 2020 at 11:17:51 AM UTC">about a minute ago</time></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="beatmap-discussions__discussion beatmapset-activities__discussion-post">
        <div class="beatmap-discussion beatmapset-activities__post-grow">
            <div class="beatmap-discussion-timestamp__icons-container">
                <div class="beatmap-discussion-timestamp__icons">
                    <a href="https://osu.ppy.sh/beatmapsets/2/discussion#/1295203">
                        <img class="beatmapset-activities__beatmapset-cover" src="https://assets.ppy.sh/beatmaps/2/covers/list.jpg?1575564822" srcset="https://assets.ppy.sh/beatmaps/2/covers/list.jpg?1575564822 1x, https://assets.ppy.sh/beatmaps/2/covers/list@2x.jpg?1575564822 2x">
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
</div>
"""

PROBLEM_CONTENT = "((in a more serious note tho : 04:05:694 (1) - aimod tells that this slider's end is not snapped properly))"

faulty_soup: BeautifulSoup = soupify(FAULTY_HTML)
issue_resolve_soup: BeautifulSoup = soupify(ISSUE_RESOLVE_HTML)
nominate_soup: BeautifulSoup = soupify(NOMINATE_HTML)
discussion_soup: BeautifulSoup = soupify(PROBLEM_HTML)
first_faulty_second_correct_beatmapsets_soup: BeautifulSoup = soupify(FIRST_FAULTY_SECOND_CORRECT_HTML_BEATMAPSETS)
first_correct_second_faulty_discussions_soup: BeautifulSoup = soupify(FIRST_CORRECT_SECOND_FAULTY_HTML_DISCUSSIONS)

faulty_tag: Tag = faulty_soup.find("div", {"class": "beatmapset-event"})
issue_resolve_tag: Tag = issue_resolve_soup.find("div", {"class": "beatmapset-event"})
nominate_tag: Tag = nominate_soup.find("div", {"class": "beatmapset-event"})
discussion_tag: Tag = discussion_soup.find("div", {"class": "beatmapset-activities__discussion-post"})