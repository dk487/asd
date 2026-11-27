#!/usr/bin/env python3

# https://eolymp.com/problems/6126
# Вказівка. Реалізувати чергу як рекурсивну структуру.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        node = Node(value)

        if self.size:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        self.size += 1

    def pop(self):
        if not self.size:
            return 'error'

        value = self.head.value
        self.head = self.head.next
        self.size -= 1

        if not self.head:
            self.tail = None

        return value

    def front(self):
        return self.head.value if self.head else 'error'

    def clear(self):
        self.head = self.tail = None
        self.size = 0

if __name__ == '__main__':
    q = Queue()

    while True:
        try:
            cmd, arg = input(), None
        except EOFError:
            break
        if ' ' in cmd:
            cmd, arg = cmd.split(' ')
        match cmd:
            case 'push':
                q.push(arg)
                print('ok')
            case 'pop':
                print(q.pop())
            case 'front':
                print(q.front())
            case 'size':
                print(q.size)
            case 'clear':
                q.clear()
                print('ok')
            case 'exit':
                print('bye')
                break
