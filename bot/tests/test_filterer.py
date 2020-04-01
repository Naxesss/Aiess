import pytest
from datetime import datetime

from aiess import Event, User, Beatmapset, Discussion

from filterer import expand
from filterer import escape
from filterer import parenthesis_equal
from filterer import deepest_parentheses
from filterer import deepest_parentheses_range
from filterer import backwards_leveled
from filterer import forwards_leveled
from filterer import split_unescaped
from filterer import de_morgans_law
from filterer import negate
from filterer import flip_gate
from filterer import double_negation_elimination
from filterer import surround_nonspace
from filterer import dissect

def test_expand():
    assert expand("type:(nominate or qualify)") == "type:nominate or type:qualify"

def test_expand_redundancy():
    assert expand("(type:(qualify))") == "type:qualify"

def test_expand_and():
    assert expand("type:(nominate or qualify) and user:123") == "type:nominate and user:123 or type:qualify and user:123"

def test_expand_and_quotes():
    assert (expand("type:(nominate or qualify) and user:\"some user with and in their name\"") ==
        "type:nominate and user:\"some user with and in their name\" or type:qualify and user:\"some user with and in their name\"")

def test_expand_multiple_and():
    assert (expand("type:(nominate or qualify) and user:(123 or 456)") ==
        "type:nominate and user:123 or type:nominate and user:456 or type:qualify and user:123 or type:qualify and user:456")

def test_expand_not():
    assert expand("type: not (nominate or qualify)") == "not type:nominate and not type:qualify"

def test_expand_not_before_type():
    assert expand("not type:(nominate or qualify)") == "not type:nominate and not type:qualify"

def test_expand_mathematical():
    assert expand("A ∨ E ∧ ¬(B ∧ (C ∨ ¬D))") == "A ∨ ¬B ∧ E ∨ ¬C ∧ D ∧ E"



def test_escape():
    assert escape("withoutspace") == "withoutspace"
    assert escape("with space") == "\"with space\""

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
    assert next(generator, None) == None

def test_split_unescaped_special_quotes():
    generator = split_unescaped("type:“One & two “x | y””&user:“some two or three”", ["&", "|", " or "])
    assert next(generator, None) == ("type:“One & two “x | y””", "&")
    assert next(generator, None) == ("user:“some two or three”", None)
    assert next(generator, None) == None

def test_split_unescaped_long_delimiter():
    generator = split_unescaped("type:\"one and two\" and user:three", [" and "])
    assert next(generator, None) == ("type:\"one and two\"", " and ")
    assert next(generator, None) == ("user:three", None)
    assert next(generator, None) == None

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
    assert de_morgans_law("not type:(nominate or qualify)") == "not type:nominate and not type:qualify"

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

def test_surround_nonspace():
    assert surround_nonspace("  ab c    ", "(", ")") == "  (ab c)    "



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