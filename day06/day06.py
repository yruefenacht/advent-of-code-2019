#!/usr/bin/env python3

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