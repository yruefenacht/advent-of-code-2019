#!/usr/bin/env python

opcodes = "3,8,1001,8,10,8,105,1,0,0,21,38,63,88,97,118,199,280,361,442,99999,3,9,1002,9,3,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,101,3,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,3,9,9,101,2,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,102,4,9,9,101,5,9,9,102,2,9,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99"
#opcodes = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"

class IntCode:
    def __init__(self, opcodes):
        self.opcodes = opcodes
        self.ops = [int(n) for n in opcodes.split(',')]

    def set_param(self, ip, mode1, mode2):
        par1 = self.ops[self.ops[ip + 1]] if mode1 == 0 else self.ops[ip + 1]
        par2 = self.ops[self.ops[ip + 2]] if mode2 == 0 else self.ops[ip + 2]
        return par1, par2

    def process_codes(self, input1, input2):
        self.ops = [int(n) for n in opcodes.split(',')]
        inputs = [input1, input2]
        inputs_set = 0
        ip = 0
        while ip < len(self.ops):
            op = self.ops[ip]
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
                par1, par2 = self.set_param(ip, mode1, mode2)
                self.ops[self.ops[ip + 3]] = par1 + par2
                ip += 4
            if op == 2:
                par1, par2 = self.set_param(ip, mode1, mode2)
                self.ops[self.ops[ip + 3]] = par1 * par2
                ip += 4
            if op == 3:
                self.ops[self.ops[ip+1]] = inputs[inputs_set]
                inputs_set += 1
                ip += 2
            if op == 4:
                par1 = self.ops[self.ops[ip + 1]] if mode1 == 0 else self.ops[ip + 1]
                return par1
                ip += 2
            if op == 5:
                par1, par2 = self.set_param(ip, mode1, mode2)
                if par1 != 0:
                    ip = par2
                else:
                    ip += 3
            if op == 6:
                par1, par2 = self.set_param(ip, mode1, mode2)
                if par1 == 0:
                    ip = par2
                else:
                    ip += 3
            if op == 7:
                par1, par2 = self.set_param(ip, mode1, mode2)
                if par1 < par2:
                    self.ops[self.ops[ip + 3]] = 1
                else:
                    self.ops[self.ops[ip + 3]] = 0
                ip += 4
            if op == 8:
                par1, par2 = self.set_param(ip, mode1, mode2)
                if par1 == par2:
                    self.ops[self.ops[ip + 3]] = 1
                else:
                    self.ops[self.ops[ip + 3]] = 0
                ip += 4
            if op == 99:
                break
        
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def process_sequence(sequence):
    output_a = intCode.process_codes(sequence[0], 0)
    output_b = intCode.process_codes(sequence[1], output_a)
    output_c = intCode.process_codes(sequence[2], output_b)
    output_d = intCode.process_codes(sequence[3], output_c)
    output_e = intCode.process_codes(sequence[4], output_d)
    return output_e


intCode = IntCode(opcodes)
combos = list(permutations(range(5), 5))

# PART 1
print(max(process_sequence(combo) for combo in combos))
