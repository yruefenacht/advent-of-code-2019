#!/usr/bin/env python3

from day09 import IntCode
from collections import defaultdict

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

def solve2():
    opcodes[0] = "2"
    intCode = IntCode(opcodes)
    intCode.running = True
    input = 0
    score = 0
    tiles = defaultdict(list)
    paddle = ball = False

    while intCode.running:
        x = intCode.run(input)
        y = intCode.run(input)
        id = intCode.run(input)
        if x == -1 and y == 0:
            score = id
        else:
            if id == 3:
                paddle = True
            elif id == 4:
                ball = True
            elif id == 0:
                for i in range(5):
                    if (x,y) in tiles[i]:
                        tiles[i].remove((x,y))
                        if i == 3: paddle = False
                        if i == 4: ball = False
            tiles[id].append((x,y))

            if paddle and ball:
                input = 0
                if tiles[3][0][0] < tiles[4][0][0]:
                    input = 1
                elif tiles[3][0][0] > tiles[4][0][0]:
                    input = -1
    print(score)

if __name__ == "__main__":
    solve1()
    solve2()
    