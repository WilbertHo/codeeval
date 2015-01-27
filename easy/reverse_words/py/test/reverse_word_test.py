from solution import reverse_words

from nose.tools import eq_

def test_reverse_words():
    eq_("", reverse_words(""))
    eq_("World Hello", reverse_words("Hello World"))
    eq_("CodeEval Hello", reverse_words("Hello CodeEval"))
