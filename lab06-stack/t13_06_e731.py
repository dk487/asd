#!/usr/bin/env python3

# https://eolymp.com/problems/731

class EquationItem:
    def __init__(self, value, priority):
        self.value = value
        self.prio = priority


s = input()
stack = []
op_prio = {'+': 1, '-': 1, '*': 2, '/': 2}
op_inv = ['-', '/']

for c in reversed(s):
    if c.isalnum():
        stack.append(EquationItem(c, 3))
        continue
    left = stack.pop()
    right = stack.pop()
    priority = op_prio[c]
    if left.prio < priority:
        left.value = '(' + left.value + ')'
    if right.prio < priority or (c in op_inv and right.prio == priority):
        right.value = '(' + right.value + ')'
    stack.append(EquationItem(left.value + c + right.value, priority))

print(stack.pop().value)
