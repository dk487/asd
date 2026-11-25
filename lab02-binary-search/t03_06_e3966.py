#!/usr/bin/env python3

# https://github.com/dk487/asd/blob/main/lab02-binary-search/t03_06_e3966.py

def int_list(s):
    return [int(i) for i in s.split()]

def check(i):
    # це тупо заглушка
    # маємо зробити свій саморобний бінарний пошук
    return i in butterflies

n = int(input())
butterflies = int_list(input())
assert n >= 1 and n <= 100000 and n == len(butterflies)

m = int(input())
query = int_list(input())
assert m >= 1 and m <= 100000 and m == len(query)

for i in query:
    print(['NO', 'YES'][check(i)])
