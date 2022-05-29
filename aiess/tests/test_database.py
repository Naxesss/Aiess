import pytest
from mysql.connector.errors import ProgrammingError
from datetime import datetime, timedelta

from aiess import event_types as types
from aiess.objects import User, Beatmapset, BeatmapsetStatus, Beatmap, Discussion, Event, NewsPost, Usergroup
from aiess.database import Database, CachedDatabase, SCRAPER_TEST_DB_NAME
from aiess.common import anext
from aiess.timestamp import from_string
from aiess.tests.mocks.api import old_beatmap as mock_old_beatmap

@pytest.fixture
def test_database():
    database = Database(SCRAPER_TEST_DB_NAME)
    # Reset database to state before any tests ran.
    database.clear_table_data("events")
    database.clear_table_data("discussions")
    database.clear_table_data("discussion_obv_sev")
    database.clear_table_data("beatmapsets")
    database.clear_table_data("beatmaps")
    database.clear_table_data("beatmapset_status")
    database.clear_table_data("status_nominators")
    database.clear_table_data("beatmapset_modes")
    database.clear_table_data("newsposts")
    database.clear_table_data("group_users")
    database.clear_table_data("users")

    return database

def test_correct_setup(test_database):
    assert not test_database.retrieve_table_data("events")
    assert not test_database.retrieve_table_data("discussions")
    assert not test_database.retrieve_table_data("discussion_obv_sev")
    assert not test_database.retrieve_table_data("beatmapsets")
    assert not test_database.retrieve_table_data("beatmaps")
    assert not test_database.retrieve_table_data("beatmapset_status")
    assert not test_database.retrieve_table_data("status_nominators")
    assert not test_database.retrieve_table_data("beatmapset_modes")
    assert not test_database.retrieve_table_data("newsposts")
    assert not test_database.retrieve_table_data("group_users")
    assert not test_database.retrieve_table_data("users")

def test_insert_delete(test_database):
    test_database.insert_table_data("users", dict(id=1, name="test"))
    assert test_database.retrieve_table_data("users", "id=1")

    test_database.delete_table_data("users", "id=1")
    assert not test_database.retrieve_table_data("users")

def test_auto_reconnect(test_database):
    test_database.connection.close()
    
    test_database.insert_table_data("users", dict(id=1, name="test"))
    assert test_database.retrieve_user("id=1")

def test_missing_table(test_database):
    with pytest.raises(ProgrammingError) as error:
        test_database.insert_table_data("missing_table", dict(id=1, name="test"))
    assert "Table 'aiess_test.missing_table' doesn't exist" in str(error.value)

def test_maximum_execution_time(test_database):
    too_long_ms = test_database.timeout_ms + 1000

    time = datetime.utcnow()
    with pytest.raises(TimeoutError):
        test_database._execute(f"SELECT SLEEP({too_long_ms/1000});")
    delta_time = datetime.utcnow() - time

    assert delta_time >= timedelta(milliseconds=test_database.timeout_ms)
    assert delta_time <  timedelta(milliseconds=too_long_ms)

@pytest.mark.asyncio
async def test_insert_retrieve_event(test_database):
    time = datetime.utcnow()

    user = User(1, allow_api=False)
    beatmapset = Beatmapset(1, creator=user, allow_api=False)
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing", tab="tab", difficulty="diff")
    event = Event(_type="test", time=time, beatmapset=beatmapset, discussion=discussion, user=user)

    test_database.insert_event(event)

    retrieved_event = await test_database.retrieve_event("type=%s", ("test",))
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.beatmapset == event.beatmapset
    assert retrieved_event.discussion == event.discussion
    assert retrieved_event.user == event.user
    assert retrieved_event.content == event.content
    assert retrieved_event == event

@pytest.mark.asyncio
async def test_insert_retrieve_event_with_newspost(test_database):
    time = datetime.utcnow()

    author = User(1, name="test")
    newspost = NewsPost(_id=3, title="title", preview="preview", author=author, slug="slug", image_url="image_url")
    event = Event(_type="news", time=time, newspost=newspost, user=author)

    test_database.insert_event(event)

    retrieved_event = await test_database.retrieve_event("type=%s", ("news",))
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.newspost == event.newspost
    assert retrieved_event.user == event.user
    assert retrieved_event.content == event.content
    assert retrieved_event == event

@pytest.mark.asyncio
async def test_insert_retrieve_event_group_change(test_database):
    event = Event(_type="add", time=datetime.utcnow(), user=User(2, name="sometwo"), group=Usergroup(7, mode="osu"))
    test_database.insert_event(event)

    retrieved_event = await test_database.retrieve_event("type=%s", ("add",))
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.group == event.group
    assert retrieved_event.group.mode == event.group.mode
    assert retrieved_event.user == event.user
    assert retrieved_event == event

@pytest.mark.asyncio
async def test_insert_retrieve_event_group_change_hybrid(test_database):
    event_old = Event(_type="add", time=from_string("2020-01-01 00:00:00"), user=User(2, name="sometwo"), group=Usergroup(7, mode="osu"))
    event = Event(_type="add", time=datetime.utcnow(), user=User(2, name="sometwo"), group=Usergroup(7, mode="taiko"))

    test_database.insert_event(event_old)
    test_database.insert_event(event)

    retrieved_event = await test_database.retrieve_event("type=%s", ("add",), order_by="time DESC")
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.group == event.group
    assert retrieved_event.group.mode == event.group.mode
    assert retrieved_event.user == event.user
    assert retrieved_event == event

@pytest.mark.asyncio
async def test_insert_retrieve_event_group_change_extensive(test_database):
    event = Event(_type="add", time=datetime.utcnow(), user=User(2, name="sometwo"), group=Usergroup(7, mode="osu"))
    test_database.insert_event(event)

    retrieved_event = await test_database.retrieve_event("type=%s", ("add",), extensive=True)
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.group == event.group
    assert retrieved_event.group.mode == event.group.mode
    assert retrieved_event.user == event.user
    assert retrieved_event == event

@pytest.mark.asyncio
async def test_insert_retrieve_small_event(test_database):
    event = Event(_type="test", time=datetime.utcnow())
    test_database.insert_event(event)

    retrieved_event = await test_database.retrieve_event(where="type=%s", where_values=("test",))
    assert retrieved_event.type == event.type
    assert retrieved_event.time == event.time
    assert retrieved_event.beatmapset == event.beatmapset
    assert retrieved_event.discussion == event.discussion
    assert retrieved_event.user == event.user
    assert retrieved_event.content == event.content
    assert retrieved_event == event

@pytest.mark.asyncio
async def test_insert_retrieve_event_digit_properties(test_database):
    user = User(1, "497")
    beatmapset = Beatmapset(3, artist="5", title="2", creator=user, allow_api=False)
    discussion = Discussion(2, beatmapset, user, content="8", tab="tab", difficulty="diff")
    event = Event(_type="test", time=datetime.utcnow(), user=user, beatmapset=beatmapset, discussion=discussion, content="4")
    test_database.insert_event(event)

    retrieved_event = await test_database.retrieve_event(where="type=%s", where_values=("test",))
    # Ensures the database field retrieval retains the `str` type, rather than reinterpreting as `int`.
    assert retrieved_event.content == "4"
    assert retrieved_event.user.name == "497"
    assert retrieved_event.beatmapset.artist == "5"
    assert retrieved_event.beatmapset.title == "2"
    assert retrieved_event.discussion.content == "8"

def test_insert_retrieve_user(test_database):
    user = User(1, name="test")
    test_database.insert_user(user)

    retrieved_user = test_database.retrieve_user(where="id=%s", where_values=(1,))
    assert retrieved_user.id == user.id
    assert retrieved_user.name == user.name
    assert retrieved_user == user

def test_insert_retrieve_beatmapset_modes(test_database):
    modes = ["osu", "taiko"]
    beatmapset = Beatmapset(1, modes=modes, allow_api=False)
    test_database.insert_beatmapset_modes(beatmapset)

    retrieved_modes = test_database.retrieve_beatmapset_modes(1)
    assert retrieved_modes == modes

def test_insert_retrieve_beatmapset(test_database):
    beatmapset = Beatmapset(1, allow_api=False)
    test_database.insert_beatmapset(beatmapset)

    retrieved_beatmapset = test_database.retrieve_beatmapset(where="id=%s", where_values=(1,))
    assert retrieved_beatmapset.id == beatmapset.id
    assert retrieved_beatmapset.artist == beatmapset.artist
    assert retrieved_beatmapset.title == beatmapset.title
    assert retrieved_beatmapset.creator == beatmapset.creator
    assert retrieved_beatmapset.modes == beatmapset.modes
    assert retrieved_beatmapset.genre == beatmapset.genre
    assert retrieved_beatmapset.language == beatmapset.language
    assert retrieved_beatmapset.beatmaps == beatmapset.beatmaps
    assert retrieved_beatmapset == beatmapset

def test_insert_retrieve_beatmapset_with_beatmaps(test_database):
    # Major difference between `allow_api=False` and from json is
    # that latter actually makes the `beatmaps` field populated, and
    # so we test whether that's inserted and retrieved properly here.
    beatmapset = Beatmapset(41823, beatmapset_json=mock_old_beatmap.JSON)
    test_database.insert_beatmapset(beatmapset)

    retrieved_beatmapset = test_database.retrieve_beatmapset(where="id=%s", where_values=(41823,))
    assert retrieved_beatmapset.id == beatmapset.id
    assert retrieved_beatmapset.artist == beatmapset.artist
    assert retrieved_beatmapset.title == beatmapset.title
    assert retrieved_beatmapset.creator == beatmapset.creator
    assert retrieved_beatmapset.modes == beatmapset.modes
    assert retrieved_beatmapset.genre == beatmapset.genre
    assert retrieved_beatmapset.language == beatmapset.language
    assert retrieved_beatmapset.beatmaps == beatmapset.beatmaps
    assert retrieved_beatmapset == beatmapset

def test_insert_retrieve_beatmap(test_database):
    beatmap = Beatmap.from_raw(
        _id           = 1,
        beatmapset_id = 3,
        version       = "test",
        draintime     = 93.4,
        sr_total      = 3.428924,
        favourites    = 13,
        userrating    = 9.23,
        playcount     = 42938,
        passcount     = 1202,
        updated_at    = datetime.utcnow()
    )
    test_database.insert_beatmap(beatmap)

    retrieved_beatmap = test_database.retrieve_beatmap(where="id=%s", where_values=(1,))
    assert retrieved_beatmap.id == beatmap.id
    assert retrieved_beatmap.beatmapset_id == beatmap.beatmapset_id
    assert retrieved_beatmap.version == beatmap.version
    assert retrieved_beatmap.draintime == beatmap.draintime
    assert retrieved_beatmap.sr_total == beatmap.sr_total
    assert retrieved_beatmap.favourites == beatmap.favourites
    assert retrieved_beatmap.userrating == beatmap.userrating
    assert retrieved_beatmap.playcount == beatmap.playcount
    assert retrieved_beatmap.passcount == beatmap.passcount
    assert retrieved_beatmap == beatmap

def test_insert_retrieve_discussion(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, creator=user, allow_api=False)
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing", tab="tab", difficulty="diff")
    test_database.insert_discussion(discussion)

    retrieved_discussion = test_database.retrieve_discussion(where="id=%s", where_values=(1,))
    assert retrieved_discussion.id == discussion.id
    assert retrieved_discussion.beatmapset == discussion.beatmapset
    assert retrieved_discussion.user == discussion.user
    assert retrieved_discussion.content == discussion.content
    assert retrieved_discussion.tab == discussion.tab
    assert retrieved_discussion.difficulty == discussion.difficulty
    assert retrieved_discussion == discussion

def test_insert_incomplete_discussion(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, creator=user, allow_api=False)
    discussion = Discussion(1, beatmapset=beatmapset)

    with pytest.raises(ValueError) as error:
        test_database.insert_discussion(discussion)
    assert "missing from discussion" in str(error.value)

def test_insert_retrieve_discussion_and_replies(test_database):
    time = datetime.utcnow()

    author = User(1, name="one")
    replier = User(2, name="two")

    beatmapset = Beatmapset(1, creator=replier, allow_api=False)
    discussion = Discussion(1, beatmapset=beatmapset, user=author, content="ping", tab="tab", difficulty="diff")

    problem = Event(_type="problem", time=time, beatmapset=beatmapset, discussion=discussion, user=author, content="ping")
    reply1 = Event(_type="reply", time=time, beatmapset=beatmapset, discussion=discussion, user=replier, content="pong")
    reply2 = Event(_type="reply", time=time, beatmapset=beatmapset, discussion=discussion, user=author, content="miss")

    test_database.insert_event(problem)
    test_database.insert_event(reply1)
    test_database.insert_event(reply2)

    retrieved_problem = test_database.retrieve_event(where="type=%s", where_values=("problem",))
    retrieved_reply1 = test_database.retrieve_event(where="type=%s AND user_id=%s", where_values=("reply", replier.id))
    retrieved_reply2 = test_database.retrieve_event(where="type=%s AND user_id=%s", where_values=("reply", author.id))

    assert retrieved_problem
    assert retrieved_reply1
    assert retrieved_reply2

def test_insert_retrieve_beatmapset_status(test_database):
    creator = User(3, name="test")
    user1 = User(1, name="someone")
    user2 = User(2, name="sometwo")
    beatmapset = Beatmapset(1, creator=creator, allow_api=False)
    status = BeatmapsetStatus(
        _id        = 1,
        beatmapset = beatmapset,
        status     = "qualified",
        time       = from_string("2020-01-01 00:00:00"),
        nominators = [user1, user2]
    )
    test_database.insert_beatmapset_status(status)

    retrieved_status = test_database.retrieve_beatmapset_status("beatmapset_id=%s", (beatmapset.id,))
    assert retrieved_status.beatmapset == status.beatmapset
    assert retrieved_status.status == status.status
    assert retrieved_status.time == status.time
    assert retrieved_status.nominators == status.nominators
    assert retrieved_status == status

def test_update_beatmapset_status_nom(test_database):
    creator = User(3, name="test")
    user = User(1, name="someone")
    beatmapset = Beatmapset(1, creator=creator, allow_api=False)
    event = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=user)

    test_database.insert_event(event)  # Should call `update_beatmapset_status`.

    retrieved_status = test_database.retrieve_beatmapset_status("beatmapset_id=%s", (beatmapset.id,))
    assert retrieved_status.status == "nominated"
    assert retrieved_status.nominators == [user]

def test_update_beatmapset_status_nom_qual(test_database):
    creator = User(3, name="test")
    user1 = User(1, name="someone")
    user2 = User(2, name="sometwo")
    beatmapset = Beatmapset(1, creator=creator, allow_api=False)
    event1 = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=user1)
    event2 = Event("qualify", from_string("2020-01-01 00:01:00"), beatmapset, user=user2)

    test_database.insert_event(event1)
    test_database.insert_event(event2)

    retrieved_status = test_database.retrieve_beatmapset_status("beatmapset_id=%s ORDER BY time DESC", (beatmapset.id,))
    assert retrieved_status.status == "qualified"
    assert retrieved_status.nominators == [user1, user2]

def test_update_beatmapset_status_nom_qual_dq(test_database):
    creator = User(3, name="test")
    user1 = User(1, name="someone")
    user2 = User(2, name="sometwo")
    beatmapset = Beatmapset(1, creator=creator, allow_api=False)
    event1 = Event("nominate", from_string("2020-01-01 00:00:00"), beatmapset, user=user1)
    event2 = Event("qualify", from_string("2020-01-01 00:01:00"), beatmapset, user=user2)
    event3 = Event("disqualify", from_string("2020-01-02 00:00:00"), beatmapset, user=user1)

    test_database.insert_event(event1)
    test_database.insert_event(event2)
    test_database.insert_event(event3)

    retrieved_status = test_database.retrieve_beatmapset_status("beatmapset_id=%s ORDER BY time DESC", (beatmapset.id,))
    assert retrieved_status.status == "pending"
    assert retrieved_status.nominators == []
    
    retrieved_status = test_database.retrieve_beatmapset_status("beatmapset_id=%s AND time=%s", (beatmapset.id, from_string("2020-01-01 00:01:00")))
    assert retrieved_status.status == "qualified"
    assert retrieved_status.nominators == [user1, user2]

def test_insert_retrieve_obv_sev(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, creator=user, allow_api=False)
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing", tab="tab", difficulty="diff")
    test_database.insert_obv_sev(discussion, obv=2, sev=0)

    obv, sev = test_database.retrieve_obv_sev(discussion_id=1)
    assert obv == 2
    assert sev == 0

def test_insert_retrieve_obv_sev_missing(test_database):
    obv, sev = test_database.retrieve_obv_sev(discussion_id=3)
    assert obv is None
    assert sev is None

def test_insert_retrieve_obv_sev_event(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, creator=user, allow_api=False)
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing", tab="tab", difficulty="diff")
    event = Event(_type=types.SEV, time=from_string("2020-01-01 00:00:00"), beatmapset=beatmapset, discussion=discussion, content="2/0")
    test_database.insert_obv_sev_event(event)

    obv, sev = test_database.retrieve_obv_sev(discussion_id=1)
    assert obv == 2
    assert sev == 0

def test_insert_retrieve_newspost(test_database):
    author = User(1, name="test")
    newspost = NewsPost(_id=3, title="title", preview="preview", author=author, slug="slug", image_url="image_url")
    test_database.insert_newspost(newspost)

    retrieved_newspost = test_database.retrieve_newspost(where="id=%s", where_values=(3,))
    assert retrieved_newspost.id == newspost.id
    assert retrieved_newspost.title == newspost.title
    assert retrieved_newspost.preview == newspost.preview
    assert retrieved_newspost.author.id == newspost.author.id
    assert retrieved_newspost.author.name == newspost.author.name
    assert retrieved_newspost.slug == newspost.slug
    assert retrieved_newspost.image_url == newspost.image_url
    assert retrieved_newspost == newspost

def test_insert_retrieve_delete_group_user(test_database):
    user = User(1, name="test")
    test_database.insert_group_user(group=Usergroup(4), user=user)

    retrieved_group, retrieved_user = test_database.retrieve_group_user(where="group_id=%s AND user_id=%s", where_values=(4, 1))
    assert retrieved_group.id == 4
    assert retrieved_group.name == "Global Moderation Team"
    assert retrieved_group.mode is None
    assert retrieved_user.id == 1
    assert retrieved_user.name == "test"

    test_database.delete_group_user(group=Usergroup(4), user=user)

    retrieved_group_user_relation = test_database.retrieve_group_user(where="group_id=%s AND user_id=%s", where_values=(4, 1))
    assert retrieved_group_user_relation is None

def test_insert_retrieve_multiple_users(test_database):
    user1 = User(1, name="test")
    user2 = User(2, name="test")

    test_database.insert_user(user1)
    test_database.insert_user(user2)

    retrieved_users = test_database.retrieve_users(where="name=%s", where_values=(user1.name,))
    assert next(retrieved_users, None) == user1
    assert next(retrieved_users, None) == user2

def test_insert_retrieve_multiple_beatmapsets(test_database):
    user = User(1, name="test")
    beatmapset1 = Beatmapset(1, artist="123", title="456", creator=user, modes=["osu", "taiko"], allow_api=False)
    beatmapset2 = Beatmapset(2, artist="456", title="789", creator=user, modes=["osu"], allow_api=False)

    test_database.insert_beatmapset(beatmapset1)
    test_database.insert_beatmapset(beatmapset2)

    retrieved_beatmapsets = test_database.retrieve_beatmapsets(where="creator_id=%s", where_values=(user.id,))
    assert next(retrieved_beatmapsets, None) == beatmapset1
    assert next(retrieved_beatmapsets, None) == beatmapset2

def test_insert_retrieve_multiple_discussions(test_database):
    user = User(1, name="test")
    beatmapset = Beatmapset(1, creator=user, allow_api=False)
    discussion1 = Discussion(1, beatmapset=beatmapset, user=user, content="testing", tab="tab", difficulty="diff")
    discussion2 = Discussion(2, beatmapset=beatmapset, user=user, content="real testing", tab="tab", difficulty="diff")

    test_database.insert_discussion(discussion1)
    test_database.insert_discussion(discussion2)

    retrieved_discussions = test_database.retrieve_discussions(where="beatmapset_id=%s", where_values=(beatmapset.id,))
    assert next(retrieved_discussions, None) == discussion1
    assert next(retrieved_discussions, None) == discussion2

def test_insert_retrieve_multiple_newsposts(test_database):
    author = User(_id=1, name="test")
    newspost1 = NewsPost(_id=1, title="title", preview="preview", author=author, slug="slug", image_url="image_url")
    newspost2 = NewsPost(_id=2, title="title2", preview="preview2", author=author, slug="slug2", image_url="image_url2")

    test_database.insert_newspost(newspost1)
    test_database.insert_newspost(newspost2)

    retrieved_newsposts = test_database.retrieve_newsposts(where="author_id=%s", where_values=(author.id,))
    assert next(retrieved_newsposts, None) == newspost1
    assert next(retrieved_newsposts, None) == newspost2

def test_insert_retrieve_multiple_group_users(test_database):
    user = User(1, name="test")
    test_database.insert_group_user(group=Usergroup(4), user=user)
    test_database.insert_group_user(group=Usergroup(4), user=User(2, name="test2"))
    test_database.insert_group_user(group=Usergroup(7), user=user)

    retrieved_group_user_relations = test_database.retrieve_group_users(where="user_id=%s", where_values=(1,))
    retrieved_groups = []
    retrieved_users = []
    for retrieved_group, retrieved_user in retrieved_group_user_relations:
        retrieved_groups.append(retrieved_group)
        retrieved_users.append(retrieved_user)
    
    assert Usergroup(4) in retrieved_groups
    assert Usergroup(7) in retrieved_groups
    assert retrieved_users == [user, user]

@pytest.mark.asyncio
async def test_insert_retrieve_multiple_events(test_database):
    time = datetime.utcnow()

    user = User(1, name="test")
    beatmapset = Beatmapset(1, creator=user, allow_api=False)
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing", tab="tab", difficulty="diff")
    event1 = Event(_type="test", time=time, beatmapset=beatmapset, discussion=discussion, user=user)
    event2 = Event(_type="123", time=time, beatmapset=beatmapset, discussion=discussion, user=user)

    test_database.insert_event(event1)
    test_database.insert_event(event2)

    retrieved_events = test_database.retrieve_events(where="beatmapset_id=%s", where_values=(beatmapset.id,))
    assert await anext(retrieved_events, None) == event1
    assert await anext(retrieved_events, None) == event2



@pytest.fixture
def cached_database():
    database = CachedDatabase(SCRAPER_TEST_DB_NAME)
    # Reset database to state before any tests ran.
    database.clear_table_data("events")
    database.clear_table_data("discussions")
    database.clear_table_data("discussion_obv_sev")
    database.clear_table_data("beatmapsets")
    database.clear_table_data("beatmapset_status")
    database.clear_table_data("status_nominators")
    database.clear_table_data("beatmapset_modes")
    database.clear_table_data("newsposts")
    database.clear_table_data("group_users")
    database.clear_table_data("users")

    return database

@pytest.mark.asyncio
async def test_insert_retrieve_event_cached(cached_database):
    time = datetime.utcnow()

    user = User(1, name="test")
    beatmapset = Beatmapset(1, creator=user, allow_api=False)
    discussion = Discussion(1, beatmapset=beatmapset, user=user, content="testing", tab="tab", difficulty="diff")

    for i in range(100):
        event = Event(_type=f"{i}", time=time, beatmapset=beatmapset, discussion=discussion, user=user)
        cached_database.insert_event(event)

    start_time = datetime.utcnow()
    retrieved_events_uncached = cached_database.retrieve_events(where="beatmapset_id=%s", where_values=(beatmapset.id,))
    async for event in retrieved_events_uncached:
        assert event.beatmapset == beatmapset
    delta_time_uncached = datetime.utcnow() - start_time

    start_time = datetime.utcnow()
    retrieved_events_cached = cached_database.retrieve_events(where="beatmapset_id=%s", where_values=(beatmapset.id,))
    async for event in retrieved_events_cached:
        assert event.beatmapset == beatmapset
    delta_time_cached = datetime.utcnow() - start_time

    assert await anext(retrieved_events_uncached, None) == await anext(retrieved_events_cached, None)
    assert delta_time_uncached > delta_time_cached