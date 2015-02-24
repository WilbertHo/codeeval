from nose.tools import eq_, nottest
# from stringpermutations import permutations, stringpermutations
from stringpermutations import permutations 


def test_stringpermutations():
    eq_(permutations('c'), 'c')
    eq_(set(permutations('bc')), set(['bc', 'cb']))
    eq_(set(permutations('abc')), set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))


@nottest
def test_sortordering():
    eq_(stringpermutations('hat'), 'aht,ath,hat,hta,tah,tha')
    eq_(stringpermutations('abc'), 'abc,acb,bac,bca,cab,cba')
    eq_(stringpermutations('Zu6'), '6Zu,6uZ,Z6u,Zu6,u6Z,uZ6')
