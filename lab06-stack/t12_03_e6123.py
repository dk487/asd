#!/usr/bin/env python3

# https://eolymp.com/problems/6123


class MyStackItem:
    def __init__(self, value, base):
        self.value = value
        self.base = base


class MyStack:
    def __init__(self):
        self.stack = None

    def push(self, n):
        self.stack = MyStackItem(n, self.stack)
        print('ok')

    def pop(self):
        if self.stack is None:
            print('error')
        else:
            print(self.stack.value)
            self.stack = self.stack.base

    def back(self):
        if self.stack is None:
            print('error')
        else:
            print(self.stack.value)

    def size(self):
        current = self.stack
        count = 0
        while current is not None:
            count += 1
            current = current.base
        print(count)

    def clear(self):
        self.stack = None
        print('ok')


if __name__ == '__main__':
    stack = MyStack()
    while True:
        args = input().split(' ')
        match args[0]:
            case 'push':
                stack.push(int(args[1]))
            case 'pop':
                stack.pop()
            case 'back':
                stack.back()
            case 'size':
                stack.size()
            case 'clear':
                stack.clear()
            case 'exit':
                print('bye')
                break
