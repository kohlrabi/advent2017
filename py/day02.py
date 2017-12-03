#!/usr/bin/env python3

import fileinput


def part1(rows):
    s = sum((max(r)-min(r) for i, r in enumerate(rows)))

    return s

def part2(rows):
    s = 0
    for row in rows:
        for i, elem in enumerate(row):
            for j in range(i+1, len(row)):
                m = max(elem, row[j])
                mi = min(elem, row[j])
                if m % mi == 0:
                    s += m//mi
                    break

    return s


    


if __name__ == '__main__':
    l = fileinput.input()
    rows = [map(int, ll.strip().split()) for ll in l]
    print("Part 1: {}".format(part1(rows)))
    print("Part 2: {}".format(part2(rows)))
