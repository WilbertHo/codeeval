from nose.tools import eq_
from stringsearching import StringSearch


def test_stringsearching():
    ss = StringSearch('Hello')
    eq_(ss.find_substring('ell'), True)

    ss = StringSearch('This is good')
    eq_(ss.find_substring('is'), True)

    ss = StringSearch('CodeEval')
    eq_(ss.find_substring('C*Eval'), True)

    ss = StringSearch('CodeEval')
    eq_(ss.find_substring('C*l'), True)

    ss = StringSearch('CodeEval')
    eq_(ss.find_substring('*C'), True)

    ss = StringSearch('CodeEval')
    eq_(ss.find_substring('C*'), True)

    ss = StringSearch('Old')
    eq_(ss.find_substring('Young'), False)
