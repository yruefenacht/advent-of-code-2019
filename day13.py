#!/usr/bin/env python3

from day09 import IntCode

data = [line.rstrip('\n') for line in open('input/day13.txt')]
opcodes = data[0].split(',')

def solve1():
    intCode = IntCode(opcodes)
    intCode.running = True
    c = 0
    while intCode.running:
        x = intCode.run(0)
        y = intCode.run(0)
        id = intCode.run(0)
        if id == 2:
            c += 1
    print(c)

if __name__ == "__main__":
    solve1()