#!/usr/bin/env python


def multiplication_table(n):
    table = ''
    end = n + 1
    for i in range(1, end):
        for j in range(1, end):
            table += '{num: 4d}'.format(num=i*j)
        table += '\n'

    return table


if __name__ == '__main__':
    print multiplication_table(12)
