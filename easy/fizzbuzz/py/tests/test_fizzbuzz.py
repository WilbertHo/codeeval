from nose.tools import eq_
from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    eq_(fizzbuzz(3, 5, 3), 'F')
    eq_(fizzbuzz(3, 5, 5), 'B')
    eq_(fizzbuzz(3, 5, 1), '1')

    eq_(fizzbuzz(2, 7, 2), 'F')
    eq_(fizzbuzz(2, 7, 7), 'B')
    eq_(fizzbuzz(2, 7, 15), '15')
