from nose.tools import eq_
from longestlines import longest_lines


def test_longest_lines():
    eq_(longest_lines(2, ['Hello World',
                          'CodeEval',
                          'Quick Fox',
                          'A',
                          'San Francisco']),
        ['San Francisco', 'Hello World'])
