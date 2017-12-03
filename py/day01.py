#!/usr/bin/env python3

import fileinput


def part1(l):
    i = None
    p = None
    s = 0
    for ll in l:
        if ll == '\n':
            if i == p:
                s += i
            break
        c = int(ll)
        if i is None:
            i = c
        if p == c:
            s += p
        p = c
    return s

if __name__ == '__main__':
    l = fileinput.input()[0]
    print("Part 1: {}".format(part1(l)))


