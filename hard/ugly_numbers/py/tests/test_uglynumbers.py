from itertools import chain
from nose.tools import eq_
from uglynumbers import get_all_substrings, is_ugly


def test_isugly():
    eq_(is_ugly(0), True)
    eq_(is_ugly(9), True)
    eq_(is_ugly(39), True)
    eq_(is_ugly(1), False)
    eq_(is_ugly(121), False)
