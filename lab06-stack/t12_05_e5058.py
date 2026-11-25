#!/usr/bin/env python3

# https://eolymp.com/problems/5058


def validate(line, brackets):
    stack = []
    for c in line:
        if c in brackets:
            # це відкриваюча дужка; покладемо у стек відповідну їй
            stack.append(brackets[c])
        elif c in brackets.values():
            # це закриваюча дужка; порівняємо з вершиною стеку
            if len(stack) == 0:
                return False
            if c != stack.pop():
                return False
        else:
            # чи маю я щось робити, якщо тут інші символи?
            pass
    return len(stack) == 0
    

if __name__ == '__main__':
    # відкриваюча дужка як ключ, закриваюча як значення
    # BTW, hello unicode! <> «» ‹› 〈〉 🤪
    brackets = {'(': ')', '[': ']', '{': '}'}
    line = input()
    print(['no', 'yes'][validate(line, brackets)])
