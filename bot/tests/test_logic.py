import sys
sys.path.append('..')

import pytest
from datetime import datetime

from bot.logic import expand
from bot.logic import distribute
from bot.logic import cleanup
from bot.logic import parenthesis_equal
from bot.logic import deepest_parentheses
from bot.logic import deepest_parentheses_range
from bot.logic import backwards_leveled
from bot.logic import forwards_leveled
from bot.logic import split_unescaped
from bot.logic import de_morgans_law
from bot.logic import negate
from bot.logic import flip_gate
from bot.logic import double_negation_elimination
from bot.logic import normalize_not
from bot.logic import extract_not
from bot.logic import surround_nonspace
from bot.logic import combined_captured_span

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
    assert expand("type:not (nominate or qualify)") == "not type:nominate and not type:qualify"

def test_expand_not_before_type():
    assert expand("not type:(nominate or qualify)") == "not type:nominate and not type:qualify"

def test_expand_complex():
    assert expand("A or E and not (B and (C or not D))") == "A or E and not B or E and not C and E and D"

def test_expand_complex_capital():
    assert expand("A OR E AND NOT (B AND (C OR NOT D))") == "A or E and not B or E and not C and E and D"

def test_expand_nested_leading_or():
    assert expand("type:(not B or (not C and D))") == "not type:B or not type:C and type:D"



def test_distribute():
    assert distribute("abc(type:(A and B))") == "abc(type:A and type:B)"

def test_cleanup():
    assert cleanup("((A &   B))") == "A & B"

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
    generator = split_unescaped("type:\"One & two \"x | y\"\"&user:\"some two or three\"", ("&", "|", " or "))
    assert next(generator, None) == ("type:\"One & two \"x | y\"\"", "&")
    assert next(generator, None) == ("user:\"some two or three\"", None)
    assert next(generator, None) is None

def test_split_unescaped_special_quotes():
    generator = split_unescaped("type:“One & two “x | y””&user:“some two or three”", ("&", "|", " or "))
    assert next(generator, None) == ("type:“One & two “x | y””", "&")
    assert next(generator, None) == ("user:“some two or three”", None)
    assert next(generator, None) is None

def test_split_unescaped_long_delimiter():
    generator = split_unescaped("type:\"one and two\" and user:three", (" and ",))
    assert next(generator, None) == ("type:\"one and two\"", " and ")
    assert next(generator, None) == ("user:three", None)
    assert next(generator, None) is None

def test_split_unescaped_cache_timing():
    iterations = 10000

    time = datetime.utcnow()
    generator = split_unescaped("type:\"one and two\" and user:three and " * iterations, (" and ",))
    for i in range(iterations - 1):
        assert next(generator, None) == ("type:\"one and two\"", " and ")
        assert next(generator, None) == ("user:three", " and ")
    delta_time_uncached = datetime.utcnow() - time
    
    assert delta_time_uncached.total_seconds() > 0.4
    
    time = datetime.utcnow()
    generator = split_unescaped("type:\"one and two\" and user:three and " * iterations, (" and ",))
    for i in range(iterations - 1):
        assert next(generator, None) == ("type:\"one and two\"", " and ")
        assert next(generator, None) == ("user:three", " and ")
    delta_time_cached = datetime.utcnow() - time

    # Retrieving from cache should be approximately 10 times faster.
    assert delta_time_cached.total_seconds() < 0.04

def test_de_morgans_law():
    assert de_morgans_law("not (A or B and C)") == "(not A and (not B or not C))"

    # !(A | B & C)      filter out x in first !(x) match
    # A | B & C         insert ! in front of all ground-level terms
    # !A | !B & !C      split by ground-level |
    # !A, !B & !C       replace ground-level & with | for each split
    # !A, !B | !C       surround any successful replacement with ()
    # !A, (!B | !C)     join splits by &
    # !A & (!B | !C)    surround by () and add back prefix and postfix
    # (!A & (!B | !C))  return

def test_de_morgans_law_complex():
    assert de_morgans_law("x not (D and not (A or B and C) or E and F)y") == "x ((not D or (A or B and C)) and (not E or not F))y"

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
    assert de_morgans_law("not not (A and B)") == "(A and B)"

def test_de_morgans_law_negated_word():
    assert de_morgans_law("not type:(nominate or qualify)") == "type:(not nominate and not qualify)"

def test_de_morgans_law_negated_word_with_gate():
    assert de_morgans_law("user:someone and not type:(nominate or qualify)") == "user:someone and type:(not nominate and not qualify)"

def test_de_morgans_law_negated_key_with_gate():
    a = de_morgans_law("content:hi and not (user or author or creator):someone")
    assert a == "content:hi and (not user and not author and not creator):someone"

def test_negate():
    assert negate("A or B and C") == "not A and (not B or not C)"

def test_negate_outside_parentheses():
    assert negate("A or (B and not D or E) and C") == "not A and (not (B and not D or E) or not C)"

def test_flip_gate():
    assert flip_gate(" or ") == " and "
    assert flip_gate(" and ") == " or "

def test_flip_gate_not_a_gate():
    with pytest.raises(ValueError) as err:
        flip_gate("not a gate")
    
    assert "Cannot flip" in str(err)

def test_double_negation_elimination():
    assert double_negation_elimination("not not (A and B)") == "(A and B)"

def test_double_negation_elimination_multiple():
    assert double_negation_elimination("not not not not not (A and B)") == "not (A and B)"
    assert double_negation_elimination("(not not not A and not not not not B)") == "(not A and B)"

def test_double_negation_elimination_word_between():
    assert double_negation_elimination("not type:not (A & B)") == "type:(A & B)"

def test_double_negation_elimination_gates_between():
    assert double_negation_elimination("not type and all between or not (A & B)") == "not type and all between or not (A & B)"

def test_double_negation_elimination_after_or_gate():
    assert double_negation_elimination("not B or not not D") == "not B or D"

def test_double_negation_elimination_note():
    assert double_negation_elimination("not B or not note and D") == "not B or not note and D"

def test_double_negation_elimination_keep_colon():
    assert double_negation_elimination("type:not not (A or B)") == "type:(A or B)"

def test_normalize_not():
    assert normalize_not("type:not nominate") == "not type:nominate"

def test_normalize_not_multiple():
    assert normalize_not("type:not nominate and type:not qualify") == "not type:nominate and not type:qualify"

def test_normalize_not_and_or():
    assert (
        normalize_not("type:not nominate and type:not qualify or type:not nominate and type:reply") ==
        "not type:nominate and not type:qualify or not type:nominate and type:reply"
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