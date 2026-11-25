#!/usr/bin/env python3

# https://github.com/dk487/asd/blob/main/lab02-binary-search/t03_06_e3966.py
# https://eolymp.com/problems/3966

def int_list(s):
    return [int(i) for i in s.split()]

def check(candidate):
    left = 0
    right = len(butterflies)-1
    while left <= right:
        mid = (left + right) // 2
        attempt = butterflies[mid]
        if attempt==candidate:
            return True
        elif attempt > candidate:
            right = mid-1
        else:
            left = mid+1
    return False
            
n = int(input())
butterflies = int_list(input())
assert n >= 1 and n <= 100000 and n == len(butterflies)

m = int(input())
query = int_list(input())
assert m >= 1 and m <= 100000 and m == len(query)

for i in query:
    print(['NO', 'YES'][check(i)])
