#!/usr/bin/env python

from collections import defaultdict

data = [line.rstrip('\n') for line in open('day06/day06.txt')]

orbits = defaultdict(list)

for line in data:
    com1,com2 = line.split(')')
    orbits[com1].append(com2)

# PART 1

def count_orbits(key):
    sum = 0
    for value in orbits[key]:
        sum += 1 + count_orbits(value)
    return sum

def sum_orbits():
    sum = count_orbits("COM")
    for key in orbits.keys():
        if key != "COM":
            sum += count_orbits(key)
    return sum

print(sum_orbits())

# PART 2

orbits = defaultdict(list)

for line in data:
    com1,com2 = line.split(')')
    orbits[com2] = com1

def get_orbits(key):
    ors = []
    while(orbits[key]):
        key = orbits[key]
        ors.append(key)
    return ors


you_orbits = get_orbits("YOU")
san_orbits = get_orbits("SAN")

common = set(you_orbits).intersection(set(san_orbits))

min_orbits = 999999999
for i in common:
    o = you_orbits.index(i) + san_orbits.index(i)
    if o < min_orbits:
        min_orbits = o
        
print(min_orbits)