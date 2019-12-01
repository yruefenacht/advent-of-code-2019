#!/usr/bin/env python3

data = [line.rstrip('\n') for line in open('day01/day01.txt')]

#PART 1
total_fuel = 0
for i in range(len(data)):
    module = int(data[i])
    module_fuel = int(module / 3) - 2
    total_fuel += module_fuel

print(total_fuel)

#PART 2
total_fuel = 0

def calc_fuel(module):
    fuel = int(module / 3) - 2
    if(fuel <= 0):
        return module
    else:
        return module + calc_fuel(fuel)

for i in range(len(data)):
    module = int(data[i])
    module_fuel = int(module / 3) - 2
    total_fuel += calc_fuel(module_fuel)

print(total_fuel)