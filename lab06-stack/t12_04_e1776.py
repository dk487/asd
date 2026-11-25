#!/usr/bin/env python3

# https://eolymp.com/problems/1776

def int_list(s):
    return [int(i) for i in s.split()]


def is_permutation_possible(request):
    inbound = list(range(1, len(request)+1))
    stack = []
    for wanted in request:
        while not stack or stack[-1] != wanted:
            if not inbound:
                return False
            stack.append(inbound.pop(0))
        stack.pop()
    return True


if __name__ == '__main__':
    n = None
    while True:
        prev_n, n = n, int(input())
        if n == 0:
            break
        if prev_n is not None:
            print()
        while True:
            line = input()
            if line == '0':
                break
            request = int_list(line)
            assert n == len(request)
            print(['No', 'Yes'][is_permutation_possible(request)])
