#!/usr/bin/env python3

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

def solve():
    moon1 = Moon(3, 3, 0)
    moon2 = Moon(4, -16, 2)
    moon3 = Moon(-10, -6, 5)
    moon4 = Moon(-3, 0, -13)
    moons = (moon1, moon2, moon3, moon4)
    steps = 1000

    for step in range(steps):
        #1. Apply gravity to velocity
        for moon in moons:
            for m in moons:
                if m is moon: continue

                if moon.x > m.x: moon.vx -= 1
                elif moon.x < m.x: moon.vx += 1

                if moon.y > m.y: moon.vy -= 1
                elif moon.y < m.y: moon.vy += 1

                if moon.z > m.z: moon.vz -= 1
                elif moon.z < m.z: moon.vz += 1
        #2. Apply velocity to position
        for moon in moons:
            moon.apply_velocity()
    
    part_one = sum(moon.get_energy() for moon in moons)
    print(part_one)

if __name__ == "__main__":
    solve()