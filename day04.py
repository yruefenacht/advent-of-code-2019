#!/usr/bin/env python3

pw_min = 278384
pw_max = 824795

# PART 1

def has_double(string):
    for i in range(len(string)-1):
        if string[i] == string[i + 1]:
            return True
    return False

def decreases(string):
    for i in range(len(string)-1):
        if int(string[i]) > int(string[i+1]):
            return True
    return False

valid_pws = 0
for pw in range(pw_min, pw_max + 1):
    if decreases(str(pw)):
        continue
    if not has_double(str(pw)):
        continue
    valid_pws += 1

print(valid_pws)

# PART 2

def has_double_strict(string, count):
    for i in string:
        c = 0
        for j in string:
            if i == j:
                c += 1
        if c == count:
            return True
    return False

valid_pws = 0
for pw in range(pw_min, pw_max + 1):
    if decreases(str(pw)):
        continue
    if not has_double_strict(str(pw), 2):
        continue
    valid_pws += 1

print(valid_pws)