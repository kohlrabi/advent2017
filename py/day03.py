#!/usr/bin/env python3

import fileinput


def part1(n):
    r = [0]
    o = 1
    
    while len(r) < n:
        v = []
        oo = o*2 - 1
        s = -1
        for i in range(o*2):
            v.append(oo)
            if oo == o:
                s = 1
            oo += s
        r += 4*v
        o += 1

    return r[n]

def part2(n):
   pass 
    


if __name__ == '__main__':
    l = fileinput.input()
    n = int(l.readline())
    print("Part 1: {}".format(part1(n-1)))
    #print("Part 2: {}".format(part2(rows)))
