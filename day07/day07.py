#!/usr/bin/env python

from itertools import permutations

opcodes = "3,8,1001,8,10,8,105,1,0,0,21,38,63,88,97,118,199,280,361,442,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,101,3,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,3,9,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99"
#opcodes = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
#opcodes = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"

class IntCode:
    def __init__(self, opcodes):
        self.ops = [int(n) for n in opcodes.split(',')]
        self.ip = 0
        self.output = 0
        self.input_counter = 0
        self.stop = False

    def reset(self):
        self.ops = [int(n) for n in opcodes.split(',')]
        self.ip = 0
        self.input_counter = 0

    def set_param(self, mode1, mode2):
        par1 = self.ops[self.ops[self.ip + 1]] if mode1 == 0 else self.ops[self.ip + 1]
        par2 = self.ops[self.ops[self.ip + 2]] if mode2 == 0 else self.ops[self.ip + 2]
        return par1, par2

    def run(self, phase, input):
        while self.ip < len(self.ops):
            op = self.ops[self.ip]
            mode1 = 0
            mode2 = 0
            mode3 = 0
            if op >= 100:
                op_s = str(op)
                zeroes_to_add = 5 - len(op_s)
                op_s = "0"*zeroes_to_add + op_s
                mode3 = int(op_s[0])
                mode2 = int(op_s[1])
                mode1 = int(op_s[2])
                op = int(op_s[3:])
            if op == 1:
                par1, par2 = self.set_param(mode1, mode2)
                self.ops[self.ops[self.ip + 3]] = par1 + par2
                self.ip += 4
            if op == 2:
                par1, par2 = self.set_param(mode1, mode2)
                self.ops[self.ops[self.ip + 3]] = par1 * par2
                self.ip += 4
            if op == 3:
                self.ops[self.ops[self.ip+1]] = phase if not self.input_counter else input
                self.input_counter = 1
                self.ip += 2
            if op == 4:
                par1 = self.ops[self.ops[self.ip + 1]] if mode1 == 0 else self.ops[self.ip + 1]
                self.output = par1
                self.ip += 2
                return par1
            if op == 5:
                par1, par2 = self.set_param(mode1, mode2)
                self.ip = par2 if par1 != 0 else ip + 3
            if op == 6:
                par1, par2 = self.set_param(mode1, mode2)
                self.ip = par2 if par1 == 0 else ip + 3
            if op == 7:
                par1, par2 = self.set_param(mode1, mode2)
                self.ops[self.ops[self.ip + 3]] = 1 if par1 < par2 else 0
                self.ip += 4
            if op == 8:
                par1, par2 = self.set_param(mode1, mode2)
                self.ops[self.ops[self.ip + 3]] = 1 if par1 == par2 else 0
                self.ip += 4
            if op == 99:
                self.stop = True
                return 1

def process_sequence(sequence):
    intCode = IntCode(opcodes)
    output_a = intCode.run(sequence[0], 0)
    intCode.reset()
    output_b = intCode.run(sequence[1], output_a)
    intCode.reset()
    output_c = intCode.run(sequence[2], output_b)
    intCode.reset()
    output_d = intCode.run(sequence[3], output_c)
    intCode.reset()
    output_e = intCode.run(sequence[4], output_d)
    return output_e

combos = list(permutations(range(5), 5))

# PART 1
print(max(process_sequence(combo) for combo in combos))


def process_sequence_loop(sequence):
    intCodes = [IntCode(opcodes) for i in range(5)]
    pos = 0
    output = 0
    while not intCodes[4].stop:
        output = intCodes[pos % 5].run(sequence[pos % 5], output)
        pos += 1
    return intCodes[4].output

combos = list(permutations(range(5, 10), 5))

# PART 2
print(max(process_sequence_loop(combo) for combo in combos))
