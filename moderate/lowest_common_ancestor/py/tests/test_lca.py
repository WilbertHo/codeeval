from nose.tools import eq_
import lca


def test_lca():
    bst = lca.build_tree()
    eq_(lca.lca(bst, 8, 52), 30)
    eq_(lca.lca(bst, 3, 20), 8)
    eq_(lca.lca(bst, 3, 8), 8)
    eq_(lca.lca(bst, 3, 10), 8)
    eq_(lca.lca(bst, 20, 29), 20)
