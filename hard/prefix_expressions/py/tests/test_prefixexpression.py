from nose.tools import eq_
from prefixexpression import prefix_expression
from foo import prefix

def test_prefixexpression():
    eq_(prefix_expression('* + 2 3 4'.split()), 20)
    eq_(prefix_expression('* + 2  3 4'.split()), 20)
    eq_(prefix_expression('+ -2 2'.split()), 0)
    eq_(prefix_expression('+ * -2 2 4'.split()), 0)
    eq_(prefix_expression('/ 10 5'.split()), 2)
