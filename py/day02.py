#!/usr/bin/env python3

import fileinput


def part1(rows):
    s = sum((max(r)-min(r) for i, r in enumerate(rows)))

    return s

def part2(l):
    pass


if __name__ == '__main__':
    l = fileinput.input()
    rows = (map(int, ll.strip().split()) for ll in l)
    print("Part 1: {}".format(part1(rows)))
    #print("Part 2: {}".format(part2(l)))
