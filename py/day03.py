#!/usr/bin/env python3

import fileinput


class Spiralmem:
    def __init__(self, d=1):
        if not d%2:
            raise ValueError("Spiralmem dimension needs to be odd.")
        self.d = d
        self.mem = [[0 for i in range(d)] for j in range(d)]

    def __str__(self):
        return str(self.mem)

    def __repr__(self):
        return self.__str__()

    def realloc(self, d=1):
        new = Spiralmem(d)

        diff = self.d - new.d

        if diff > 0:
            for i in range(0, new.d):
                for j in range(0, new.d):
                    new.mem[i][j] = self.mem[i+diff//2][j+diff//2]
        elif diff < 0:
            diff *= -1
            for i in range(0, self.d):
                for j in range(0, self.d):
                    new.mem[i+diff//2][j+diff//2] = self.mem[i][j]
        else:
            return self

        self.mem = new.mem
        return self



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
