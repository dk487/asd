#!/usr/bin/env python3

# https://eolymp.com/problems/6130
# Вказівка. Реалізувати дек як рекурсивну структуру.

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        node = Node(value)

        if self.size:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node

        self.head = node
        self.size += 1

    def push_back(self, value):
        node = Node(value)

        if self.size:
            node.prev = self.tail
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        self.size += 1

    def pop_front(self):
        if not self.size:
            return 'error'

        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.size:
            self.head.prev = None
        else:
            self.tail = None

        return value

    def pop_back(self):
        if not self.size:
            return 'error'

        value = self.tail.value
        self.tail = self.tail.prev
        self.size -= 1
        if self.size:
            self.tail.next = None
        else:
            self.head = None

        return value

    def front(self):
        return self.head.value if self.size else 'error'

    def back(self):
        return self.tail.value if self.size else 'error'

    def clear(self):
        self.head = self.tail = None
        self.size = 0

if __name__ == '__main__':
    d = Deque()

    while True:
        try:
            cmd, arg = input(), None
        except EOFError:
            break
        if ' ' in cmd:
            cmd, arg = cmd.split(' ')
        match cmd:
            case 'push_front':
                d.push_front(arg)
                print('ok')
            case 'push_back':
                d.push_back(arg)
                print('ok')
            case 'pop_front':
                print(d.pop_front())
            case 'pop_back':
                print(d.pop_back())
            case 'front':
                print(d.front())
            case 'back':
                print(d.back())
            case 'size':
                print(d.size)
            case 'clear':
                d.clear()
                print('ok')
            case 'exit':
                print('bye')
                break
