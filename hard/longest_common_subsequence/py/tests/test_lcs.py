from nose.tools import eq_
import lcs

def test_longest_common_subsequence():
    eq_(lcs.longest_common_subsequence('XMJYAUZ', 'MZJAWXU'), 'MJAU')
    eq_(lcs.longest_common_subsequence('BANANA', 'ATANA'), 'AANA')
    eq_(lcs.longest_common_subsequence('ABDCDEF', 'AZD'), 'AD')
