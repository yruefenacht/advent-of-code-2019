#!/usr/bin/env python3

import math

class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_energy(self):
        pot = abs(self.x) + abs(self.y) + abs(self.z)
        kin = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return pot * kin

def print_moons(moons):
    for m in moons:
        print("x="+str(m.x)+" y="+str(m.y)+" z="+str(m.z)+"; ", end="")
        print("vx="+str(m.vx)+" vy="+str(m.vy)+" vz="+str(m.vz))

def apply_gravity(m1, m2):
    if m1.x > m2.x: m1.vx -= 1
    elif m1.x < m2.x: m1.vx += 1

    if m1.y > m2.y: m1.vy -= 1
    elif m1.y < m2.y: m1.vy += 1

    if m1.z > m2.z: m1.vz -= 1
    elif m1.z < m2.z: m1.vz += 1

def solve1(moons, steps):
    for step in range(steps):
        #1. Apply gravity to velocity
        for moon in moons:
            for m in moons:
                if m is moon: continue
                apply_gravity(moon, m)
        #2. Apply velocity to position
        for moon in moons:
            moon.apply_velocity()
    
    part_one = sum(moon.get_energy() for moon in moons)
    print(part_one)

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solve2(moons):
    steps = 0
    x_found = y_found = z_found = None
    x_history = y_history = z_history = set()

    while True:
        if x_found and y_found and z_found:
            break

        #1. Apply gravity to velocity
        for moon in moons:
            for m in moons:
                if m is moon: continue
                apply_gravity(moon, m)
        #2. Apply velocity to position
        for moon in moons:
            moon.apply_velocity()

        x = y = z = ""
        for moon in moons:
            x += str(moon.x) + str(moon.vx)
            y += str(moon.y) + str(moon.vy)
            z += str(moon.z) + str(moon.vz)
        
        if not x_found:
            if x in x_history:
                x_found = steps
            else:
                x_history.add(x)
        if not y_found:
            if y in y_history:
                y_found = steps
            else:
                y_history.add(y)
        if not z_found:
            if z in z_history:
                z_found = steps
            else:
                z_history.add(z)

        steps += 1

    part_two = lcm(lcm(x_found, y_found), z_found)
    print(part_two)

if __name__ == "__main__":
    moon1 = Moon(3, 3, 0)
    moon2 = Moon(4, -16, 2)
    moon3 = Moon(-10, -6, 5)
    moon4 = Moon(-3, 0, -13)
    solve1((moon1, moon2, moon3, moon4), 1000)
    solve2((moon1, moon2, moon3, moon4))