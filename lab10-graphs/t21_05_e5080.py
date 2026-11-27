#!/usr/bin/env python3

# https://eolymp.com/problems/5080

count = 0
n = int(input())

for i in range(n):
    row = [int(i) for i in input().split()]
    assert len(row) == n
    if sum(row) == 1:
        count += 1

print(count)
