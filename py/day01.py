#!/usr/bin/env python3

import fileinput


def part1(l):
    s = sum((int(p) for p,n in zip(l, l[1:]+l[0]) if p == n))

    return s

def part2(l):
    pass


if __name__ == '__main__':
    l = fileinput.input()[0].strip()
    print("Part 1: {}".format(part1(l)))


