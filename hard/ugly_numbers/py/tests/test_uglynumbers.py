from itertools import chain
from nose.tools import eq_
from uglynumbers import get_all_substrings, is_ugly


def test_isugly():
    eq_(is_ugly(0), True)
    eq_(is_ugly(9), True)
    eq_(is_ugly(39), True)
    eq_(is_ugly(1), False)
    eq_(is_ugly(121), False)


def test_get_all_substrings():
    gen = get_all_substrings('1')
    eq_(list(gen), [[1], [-1]])

    gen = get_all_substrings('12')
    eq_(list(gen), [[12], [-12], [1, 2], [1, -2], [-1, 2], [-1, -2]])
