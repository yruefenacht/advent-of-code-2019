#!/usr/bin/env python3

data = [line.rstrip('\n') for line in open('day08/day08.txt')]
nums = [int(x) for x in data[0]]

class Layer:
    def __init__(self):
        self.width = 25
        self.height = 6
        self.matrix = [[0 for i in range(self.width)] for j in range(self.height)]

    def count_contains_num(self, num):
        sum = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] == num:
                    sum += 1
        return sum
  
layers = []
l = Layer()
size = l.width * l.height
p = 0
while p < len(nums):
    if not p % size:
        l = Layer()
        layers.append(l)
    for x in range(l.height):
        for y in range(l.width):
            l.matrix[x][y] = nums[p]
            p += 1

# PART 1

min_layer = Layer()
for layer in layers:
    if layer.count_contains_num(0) < min_layer.count_contains_num(0):
        min_layer = layer

part_one = min_layer.count_contains_num(1) * min_layer.count_contains_num(2)
print(part_one)

# PART 2

for y in range(6):
    for x in range(25):
        for layer in layers:
            if layer.matrix[y][x] != 2:
                if layer.matrix[y][x] == 1:
                    print('░', end="")
                else:
                    print(' ', end="")
                break
    print()
     