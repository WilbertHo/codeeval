"""
You are given two strings. Determine if the second string is a substring of
the first (Do NOT use any substr type library function). The second string
may contain an asterisk(*) which should be treated as a regular expression
i.e. matches zero or more characters. The asterisk can be escaped by
a \ char in which case it should be interpreted as a regular '*' character.
To summarize: the strings can contain alphabets, numbers, * and \ characters.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. The
input file contains two comma delimited strings per line. E.g.

Hello,ell
This is good, is
CodeEval,C*Eval
Old,Young

OUTPUT SAMPLE:

If the second string is indeed a substring of the first, print out a
'true'(lowercase), else print out a 'false'(lowercase), one per line. E.g.

true
true
true
false
"""
from collections import defaultdict
import fileinput
import re
import UserDict


#class Tree(dict):
#    def __init__(self, *args, **kwargs):
#        super(self.__class__, self).__init__(*args, **kwargs)
class Tree(UserDict.UserDict):
    def __str__(self):
        string = []
        tree = dict(self)
        while tree:
            string += tree.keys()
            tree = tree.values()[0]
        return ''.join(string)


class StringSearch(object):
    def __init__(self, string):
        self.tree = self.make_tree(string)

    def make_tree(self, string):
        tree = Tree()

        for substring in [string[i:] for i in xrange(len(string) - 1, -1, -1)]:
            root = tree
            for letter in substring:
                root = root.setdefault(letter, Tree())

        return tree

    def find_substring(self, substr):
        root = self.tree
        # Remove leading and trailing * if not prefixed with a '\'
        substr = re.sub(r'(?<=^)\*', '', substr)
        substr = re.sub(r'(?<!\\)\*$', '', substr)
        i = 0
        while i < len(substr):
            letter = substr[i]

            # wildcard
            # Do a BFS down through the tree until we find the next
            # character in the search string
            if letter == '*':
                next_letter = substr[i + 1]
                queue = root.values()
                while queue and not next_letter in root:
                    root = queue.pop(0)
                    queue.extend(root.values())
                if not next_letter in root:
                    return False
                i += 1
                letter = substr[i]
                root = StringSearch(str(root)).tree

            if substr[i:].startswith('\*'):
                # Skip past the \\ and consume the '*' so we don't
                # match as a wildcard on the next iteration
                i += 1
                letter = substr[i]

            root = root.get(letter)

            if root is None:
                return False

            i += 1

        return True


def main():
    lines = [line.strip('\n') for line in fileinput.input() if line]

    for line in lines:
        string, substr = line.split(',')
        ss = StringSearch(string)
        found = ss.find_substring(substr)
        print 'true' if found else 'false'


if __name__ == '__main__':
    main()
