from nose.tools import eq_
from detectingcycles import detect_cycle


def test_detect_cycle():
    eq_(detect_cycle(['1']), ['1'])
    eq_(detect_cycle(['2']), ['2'])
    eq_(detect_cycle(['3']), ['3'])
    eq_(detect_cycle(['2', '0', '6', '3', '1', '6', '3', '1', '6', '3', '1']),
        ['6', '3', '1'])
    eq_(detect_cycle(['3', '4', '8', '0', '11', '9', '7', '2', '5', '6', '10', '1', '49', '49', '49', '49']),
        ['49'])
    eq_(detect_cycle(['1', '2', '3', '1', '2', '3', '1', '2', '3']),
        ['1', '2', '3'])
