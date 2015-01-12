#!/usr/bin/env python
import fileinput


def reverse_words(words):
    return ' '.join(words.split()[::-1])


def main():
    input = [line.strip() for line in fileinput.input()]

    for words in input:
        print reverse_words(words)


if __name__ == '__main__':
    main()
