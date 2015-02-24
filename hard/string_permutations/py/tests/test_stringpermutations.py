from nose.tools import eq_, nottest
from stringpermutations import permutations, sorter, stringpermutations


def test_permutations():
    eq_(permutations('c'), 'c')
    eq_(set(permutations('bc')), set(['bc', 'cb']))
    eq_(set(permutations('abc')), set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))


def test_sorter():
    eq_(sorted(['a', '00', '0', 'ppp', '000'], key=sorter),
        ['0', '00', '000', 'a', 'ppp'])
    eq_(sorted(['a', 'Z', '0', '00Z'], key=sorter), ['0', '00Z', 'Z', 'a'])


def test_stringpermutations():
    eq_(stringpermutations('hat'), 'aht,ath,hat,hta,tah,tha')
    eq_(stringpermutations('abc'), 'abc,acb,bac,bca,cab,cba')
    eq_(stringpermutations('Zu6'), '6Zu,6uZ,Z6u,Zu6,u6Z,uZ6')
