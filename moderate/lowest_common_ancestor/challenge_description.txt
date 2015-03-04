CHALLENGE DESCRIPTION:


Write a program to determine the lowest common ancestor of two nodes in a binary search tree. You may hardcode the following binary search tree in your program:

    30
    |
  ____
  |   |
  8   52
  |
____
|   |
3  20
    |
   ____
  |   |
  10 29

INPUT SAMPLE:

The first argument is a path to a file that contains two values. These values represent two nodes within the tree, one per line. E.g.:

8 52
3 29

OUTPUT SAMPLE:

Print to stdout the lowest common ancestor, one per line. Lowest means the lowest depth in the tree, not the lowest value. E.g.:

30
8
