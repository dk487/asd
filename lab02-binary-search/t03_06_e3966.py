#!/usr/bin/env python3

# https://github.com/dk487/asd/blob/main/lab02-binary-search/t03_06_e3966.py

def int_list(s):
    return [int(i) for i in s.split()]

import random
def check(i):
    return random.choice([True, False])

n = int(input())
butterfiles = int_list(input())
assert n == len(butterfiles)

m = int(input())
query = int_list(input())
assert m == len(query)

for i in query:
    print(['NO', 'YES'][check(i)])
