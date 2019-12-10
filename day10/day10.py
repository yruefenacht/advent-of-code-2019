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
    return neighbors

def get_slope(y, x):
    return math.atan2(y,x)

# PART 1
comets = get_comets()
part_one = max(len(count_visible(get_comets(), comet).keys()) for comet in comets)
print(part_one)

def split_quadrants(directions):
    quadrants = []
    quadrants.append([x for x in directions if x[0] >= 0 and x[1] < 0])
    quadrants.append([x for x in directions if x[0] > 0  and x[1] >= 0])
    quadrants.append([x for x in directions if x[0] <= 0 and x[1] > 0])
    quadrants.append([x for x in directions if x[0] < 0  and x[1] <= 0])
    return quadrants
    
def eliminate_comets(quadrants, base, comets, dim_x, dim_y):
    round = len(comets) - 200
    while True:
        for quadrant in quadrants:
            for direction in quadrant:
                c = 1
                while True:
                    p = (base[0] + direction[0] * c, base[1] + direction[1] * c)
                    if p[0] < 0 or p[0] > dim_x or \
                       p[1] < 0 or p[1] > dim_y:
                        break
                    if p in comets:
                        comets.remove(p)
                        if len(comets) == round:
                            return p
                        break
                    c += 1

def calc_angle(vector):
    if vector[1] == 0:
        return 90
    return math.degrees(math.atan(vector[0]/vector[1]))

def parse_directions(base, comets):
    d = set()
    for comet in comets:
        if comet == base:
            continue       
        vec = (comet[0] - base[0], comet[1] - base[1])
        gcd = math.gcd(vec[0], vec[1])
        vec = (vec[0] // gcd, vec[1] // gcd)
        d.add(vec)
    return d

base = []
for comet in comets:
    comet_directions = count_visible(get_comets(), comet)
    if len(comet_directions.keys()) == part_one:
        base = (comet[1], comet[0])

comets = [(x, y) for y in range(dim) for x in range(dim) if data[y][x] == "#"]
directions = list(parse_directions(base, comets))
directions.sort(key = lambda d:calc_angle(d), reverse = True)
quadrants = split_quadrants(directions)

# PART 2
comet_last = eliminate_comets(quadrants, base, comets, dim, dim)
part_two = (comet_last[0] * 100) + comet_last[1]
print(part_two)
