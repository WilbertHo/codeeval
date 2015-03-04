from nose.tools import eq_
import reversegroups


def test_reverse_groups():
    eq_(reversegroups.reverse_groups([1,2,3,4,5], 2), [2,1,4,3,5])
    eq_(reversegroups.reverse_groups([1,2,3,4,5], 3), [3,2,1,4,5])
