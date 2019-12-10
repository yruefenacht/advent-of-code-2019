#!/usr/bin/env python3

from collections import defaultdict
import math

data = [line.rstrip('\n') for line in open('day10/day10.txt')]
dim = len(data[0])

def get_comets():
    comets = []
    for y in range(dim):
        for x in range(dim):
            if data[y][x] == '#':
                comets.append([y,x])
    return comets

def count_visible(comets, comet):
    neighbors = defaultdict(list)
    comets.remove(comet)
    for c in comets:
        y = c[0] - comet[0]
        x = c[1] - comet[1]
        slope = get_slope(y, x)
        neighbors[slope].append(c)
    return len(neighbors.keys())

def get_slope(y, x):
    return math.atan2(y,x)

print(max(count_visible(get_comets(), comet) for comet in get_comets()))
