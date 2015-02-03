from nose.tools import eq_
import lcs

def test_lcs():
    eq_(lcs.lcs['XMJYAUZ', 'MZJAWXU'], 'MJAU')
    eq_(lcs.lcs['BANANA', 'ATANA'], 'AANA')
