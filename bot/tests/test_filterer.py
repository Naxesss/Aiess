import sys
sys.path.append('..')

import pytest
from datetime import datetime

from aiess import Event, User, Beatmapset, Discussion

from bot.filterer import expand
from bot.filterer import distribute
from bot.filterer import cleanup
from bot.filterer import escape
from bot.filterer import parenthesis_equal
from bot.filterer import deepest_parentheses
from bot.filterer import deepest_parentheses_range
from bot.filterer import backwards_leveled
from bot.filterer import forwards_leveled
from bot.filterer import split_unescaped
from bot.filterer import de_morgans_law
from bot.filterer import negate
from bot.filterer import flip_gate
from bot.filterer import double_negation_elimination
from bot.filterer import normalize_not
from bot.filterer import extract_not
from bot.filterer import surround_nonspace
from bot.filterer import combined_captured_span
from bot.filterer import dissect
from bot.filterer import passes_filter

def test_expand():
    assert expand("type:(nominate or qualify)") == "type:nominate or type:qualify"

def test_expand_redundancy():
    assert expand("(type:(qualify))") == "type:qualify"

def test_expand_and():
    assert expand("type:(nominate or qualify) and user:123") == "type:nominate and user:123 or type:qualify and user:123"

def test_expand_and_quotes():
    assert (
        expand("type:(nominate or qualify) and user:\"some user with and in their name\"") ==
        "type:nominate and user:\"some user with and in their name\" or type:qualify and user:\"some user with and in their name\""
    )

def test_expand_multiple_and():
    assert (
        expand("type:(nominate or qualify) and user:(123 or 456)") ==
        "type:nominate and user:123 or type:nominate and user:456 or type:qualify and user:123 or type:qualify and user:456"
    )

def test_expand_not():
    assert expand("type: not (nominate or qualify)") == "not type:nominate and not type:qualify"

def test_expand_not_before_type():
    assert expand("not type:(nominate or qualify)") == "not type:nominate and not type:qualify"

def test_expand_mathematical():
   assert expand("A ∨ E ∧ ¬(B ∧ (C ∨ ¬D))") == "A ∨ E ∧ ¬B ∨ E ∧ ¬C ∧ E ∧ D"

def test_expand_nested_leading_or():
    assert expand("type:(¬B ∨ (¬C ∧ D))") == "¬type:B ∨ ¬type:C ∧ type:D"



def test_distribute():
    assert distribute("abc(type:(A and B))") == "abc(type:A and type:B)"

def test_cleanup():
    assert cleanup("((A &   B))") == "A & B"

def test_escape():
    assert escape("withoutspace") == "withoutspace"
    assert escape("with space") == "\"with space\""

def test_escape_int():
    assert escape(42) == "42"

def test_parenthesis_equality():
    assert parenthesis_equal("A or (B and (C or D))")

def test_parenthesis_inequality_opening():
    assert not parenthesis_equal("A and (B or not (C and D)")

def test_parenthesis_inequality_closing():
    assert not parenthesis_equal("A and (B or not C and D))")

def test_deepest_parentheses():
    assert deepest_parentheses("abc(def((ghi)jkl(mno)))") == "ghi"

def test_deepest_parentheses_raise():
    with pytest.raises(ValueError) as err:
        deepest_parentheses("(()")
    
    assert "equal" in str(err)

def test_deepest_parentheses_range():
    assert deepest_parentheses_range("abc(def(ghi))") == (7, 11)

def test_deepest_parentheses_range_multiple():
    assert deepest_parentheses_range("abc(def(ghi)) and then (some other ((even deeper) parentheses))") == (36, 48)

def test_deepest_parentheses_range_raise():
    with pytest.raises(ValueError) as err:
        deepest_parentheses_range("(()")
    
    assert "equal" in str(err)

def test_backwards_leveled():
    assert backwards_leveled("a(ab(c)de)fg"[:4]) == "ab"

def test_forwards_leveled():
    assert forwards_leveled("a(ab(c)de)fg"[6+1:]) == "de"

def test_split_unescaped():
    generator = split_unescaped("type:\"One & two \"x | y\"\"&user:\"some two or three\"", ["&", "|", " or "])
    assert next(generator, None) == ("type:\"One & two \"x | y\"\"", "&")
    assert next(generator, None) == ("user:\"some two or three\"", None)
    assert next(generator, None) is None

def test_split_unescaped_special_quotes():
    generator = split_unescaped("type:“One & two “x | y””&user:“some two or three”", ["&", "|", " or "])
    assert next(generator, None) == ("type:“One & two “x | y””", "&")
    assert next(generator, None) == ("user:“some two or three”", None)
    assert next(generator, None) is None

def test_split_unescaped_long_delimiter():
    generator = split_unescaped("type:\"one and two\" and user:three", [" and "])
    assert next(generator, None) == ("type:\"one and two\"", " and ")
    assert next(generator, None) == ("user:three", None)
    assert next(generator, None) is None

def test_de_morgans_law():
    assert de_morgans_law("!(A | B & C)") == "(!A & (!B | !C))"

    # !(A | B & C)      filter out x in first !(x) match
    # A | B & C         insert ! in front of all ground-level terms
    # !A | !B & !C      split by ground-level |
    # !A, !B & !C       replace ground-level & with | for each split
    # !A, !B | !C       surround any successful replacement with ()
    # !A, (!B | !C)     join splits by &
    # !A & (!B | !C)    surround by () and add back prefix and postfix
    # (!A & (!B | !C))  return

def test_de_morgans_law_complex():
    assert de_morgans_law("x!(D & !(A | B & C) | E & F)y") == "x((!D | (A | B & C)) & (!E | !F))y"

    # x!(D & !(A | B & C) | E & F)y         filter out x in first !(x) match
    # D & !(A | B & C) | E & F              insert ! in front of all ground-level terms
    # !D & !!(A | B & C) | !E & !F          split by ground-level |
    # !D & !!(A | B & C), !E & !F           replace ground-level & with | for each split
    # !D | !!(A | B & C), !E | !F           surround any successful replacement with ()
    # (!D | !!(A | B & C)), (!E | !F)       join splits by &
    # (!D | !!(A | B & C)) & (!E | !F)      double negation elimination
    # (!D | (A | B & C)) & (!E | !F)        surround by () and add back prefix and postfix
    # x((!D | (A | B & C)) & (!E | !F))y    return, rest is cleaned up by expand

def test_de_morgans_law_elimination():
    assert de_morgans_law("!!(A & B)") == "(A & B)"

def test_de_morgans_law_negated_word():
    assert de_morgans_law("not type:(nominate or qualify)") == "type:(not nominate and not qualify)"

def test_negate():
    assert negate("A | B & C") == "!A & (!B | !C)"

def test_negate_outside_parentheses():
    assert negate("A | (B & !D | E) & C") == "!A & (!(B & !D | E) | !C)"

def test_negate_literal():
    assert negate("A or B and C", "not ") == "not A and (not B or not C)"

def test_negate_mathematical():
    assert negate("A ∨ B ∧ C", "¬") == "¬A ∧ (¬B ∨ ¬C)"

def test_flip_gate():
    assert flip_gate(" or ") == " and "
    assert flip_gate(" and ") == " or "
    assert flip_gate("|") == "&"
    assert flip_gate("&") == "|"
    assert flip_gate("∨") == "∧"
    assert flip_gate("∧") == "∨"

def test_flip_gate_not_a_gate():
    with pytest.raises(ValueError) as err:
        flip_gate("not a gate")
    
    assert "Cannot flip" in str(err)

def test_double_negation_elimination():
    assert double_negation_elimination("!!(A & B)") == "(A & B)"

def test_double_negation_elimination_multiple():
    assert double_negation_elimination("!!!!!(A & B)") == "!(A & B)"
    assert double_negation_elimination("(!!!A & !!!!B)") == "(!A & B)"

def test_double_negation_elimination_literal():
    assert double_negation_elimination("not not (A & not B) Anot not B") == "(A & not B) Anot not B"

def test_double_negation_elimination_mathematical():
    assert double_negation_elimination("¬¬¬(A & ¬¬B)") == "¬(A & B)"

def test_double_negation_elimination_word_between():
    assert double_negation_elimination("not type: not (A & B)") == "type:(A & B)"

def test_double_negation_elimination_gates_between():
    assert double_negation_elimination("not type and all between or not (A & B)") == "not type and all between or not (A & B)"

def test_double_negation_elimination_mixed():
    assert double_negation_elimination("not !(A & !¬¬B)") == "(A & ¬B)"

def test_double_negation_elimination_word_between_and_mixed():
    assert double_negation_elimination("not type:!A") == "type:A"

def test_double_negation_elimination_keep_colon():
    assert double_negation_elimination("type:not not (A or B)") == "type:(A or B)"

def test_normalize_not():
    assert normalize_not("type:not nominate") == "not type:nominate"

def test_normalize_not_multiple():
    assert normalize_not("type:not nominate and type:not qualify") == "not type:nominate and not type:qualify"

def test_normalize_not_programatic():
    assert normalize_not("type:!nominate & type:!qualify") == "!type:nominate & !type:qualify"

def test_normalize_not_mathematical():
    assert normalize_not("type:¬nominate ∧ type:¬qualify") == "¬type:nominate ∧ ¬type:qualify"

def test_normalize_not_and_or():
    assert (
        normalize_not("type:¬nominate ∧ type:¬qualify ∨ type:¬nominate ∧ type:reply") ==
        "¬type:nominate ∧ ¬type:qualify ∨ ¬type:nominate ∧ type:reply"
    )

def test_normalize_not_spacing():
    assert normalize_not("  some long type:not nominate  ") == "  not some long type:nominate  "

def test_normalize_not_no_spaces():
    assert normalize_not("type:not(A or B)") == "not type:(A or B)"

def test_extract_not():
    without_not_gate, not_gate = extract_not("not me, not you")
    assert without_not_gate == "me, not you"
    assert not_gate == "not "

def test_surround_nonspace():
    assert surround_nonspace("  ab c    ", "(", ")") == "  (ab c)    "

class MockMatch():
    def __init__(self, regs):
        self.regs = regs

def test_combined_captured_span():
    start, end = combined_captured_span(MockMatch([(0, 8), (-1, -1), (1, 0), (1, 4), (2, 2)]))
    assert start == 1
    assert end == 4, "If this is 8, the first group (i.e. the entire match) is being considered."



def test_dissect_simple():
    event = Event(_type="test", time=datetime.utcnow())
    assert dissect(event) == ["type:test"]

def test_dissect_user():
    user = User(2, "some two")
    event = Event(_type="test", time=datetime.utcnow(), user=user)
    assert dissect(user) == [
        "user:\"some two\"",
        "user-id:2"
    ]
    assert dissect(event) == ["type:test"] + dissect(user)

def test_dissect_beatmapset():
    user = User(2, "some two")
    beatmapset = Beatmapset(4, artist="yes", title="no", creator=user, modes=["osu", "catch"])
    event = Event(_type="test", time=datetime.utcnow(), beatmapset=beatmapset)
    assert dissect(beatmapset) == [
        "mapset-id:4",
        "artist:yes",
        "title:no",
        "creator:\"some two\"",
        "creator-id:2",
        "mode:osu",
        "mode:catch"
    ]
    assert dissect(event) == ["type:test"] + dissect(beatmapset)

def test_dissect_discussion():
    user = User(1, "some one")
    creator = User(2, "some two")
    beatmapset = Beatmapset(4, artist="yes", title="no", creator=creator, modes=["osu", "catch"])
    discussion = Discussion(3, beatmapset=beatmapset, user=user, content="hello")
    event = Event(_type="test", time=datetime.utcnow(), beatmapset=beatmapset, discussion=discussion, user=user, content="hello")
    assert dissect(beatmapset) == [
        "mapset-id:4",
        "artist:yes",
        "title:no",
        "creator:\"some two\"",
        "creator-id:2",
        "mode:osu",
        "mode:catch"
    ]
    assert dissect(discussion) == dissect(beatmapset) + [
        "discussion-id:3",
        "author:\"some one\"",
        "author-id:1",
        "discussion-content:hello"
    ]
    assert dissect(event) == ["type:test"] + dissect(discussion) + dissect(user) + ["content:hello"]

def test_dissect_discussion_reply():
    user = User(1, "some one")
    creator = User(2, "some two")
    replier = User(3, "some three")
    beatmapset = Beatmapset(4, artist="yes", title="no", creator=creator, modes=["osu", "catch"])
    discussion = Discussion(3, beatmapset=beatmapset, user=user, content="hello")
    event = Event(_type="reply", time=datetime.utcnow(), beatmapset=beatmapset, discussion=discussion, user=replier, content="there")
    assert dissect(beatmapset) == [
        "mapset-id:4",
        "artist:yes",
        "title:no",
        "creator:\"some two\"",
        "creator-id:2",
        "mode:osu",
        "mode:catch"
    ]
    assert dissect(discussion) == dissect(beatmapset) + [
        "discussion-id:3",
        "author:\"some one\"",
        "author-id:1",
        "discussion-content:hello"
    ]
    assert dissect(event) == ["type:reply"] + dissect(discussion) + dissect(replier) + ["content:there"]

def test_dissect_aliases():
    event = Event(_type="nominate", time=datetime.utcnow())

    assert "type:nominate" in dissect(event)
    assert "type:nomination" in dissect(event)
    assert "type:nominated" in dissect(event)
    assert "type:bubbled" in dissect(event)

def test_passes_filter():
    assert passes_filter("type:reply", ["mode:osu", "type:reply"])
    assert not passes_filter("type:qualify", ["mode:osu", "type:reply"])

def test_passes_filter_or():
    assert passes_filter("type:reply or mode:taiko", ["mode:osu", "type:reply"])
    assert passes_filter("type:reply or mode:taiko", ["mode:taiko", "type:qualify"])
    assert not passes_filter("type:reply or mode:taiko", ["mode:osu", "type:qualify"])

def test_passes_filter_and():
    assert passes_filter("type:reply and mode:taiko", ["mode:taiko", "type:reply"])
    assert not passes_filter("type:reply and mode:taiko", ["mode:osu", "type:reply"])
    assert not passes_filter("type:reply and mode:taiko", ["mode:taiko", "type:qualify"])

def test_passes_filter_and_not():
    assert passes_filter("type:reply and not mode:taiko", ["mode:catch", "type:reply"])
    assert passes_filter("type:reply and !mode:taiko", ["mode:catch", "type:reply"])
    assert not passes_filter("type:reply and not mode:taiko", ["mode:taiko", "type:reply"])
    assert not passes_filter("type:reply and not mode:taiko", ["mode:osu", "type:qualify"])

def test_passes_filter_missing_field():
    assert not passes_filter("content:hi", ["user:sometwo", "type:nominate"])
    assert passes_filter("not content:hi", ["user:sometwo", "type:nominate"])

def test_passes_filter_case_sensitivity():
    assert passes_filter("type:Reply AND mode:OSU", ["mode:osu", "type:reply"])
    assert not passes_filter("TYPE:QUALIFY", ["mode:osu", "type:reply"])