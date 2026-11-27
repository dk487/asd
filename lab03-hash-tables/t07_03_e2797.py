#!/usr/bin/env python3

# https://eolymp.com/problems/2797


class MyOpenAddrHash:
    def __init__(self, size: int):
        assert size > 0
        self.data = [None] * size
        self.used = 0

    def rehash(self):
        new_self = MyOpenAddrHash(len(self.data) * 20)
        for row in self.data:
            if row is not None:
                new_self.add(row)
        self.data = new_self.data

    def add(self, number: int):
        if (self.used * 2 > len(self.data)):
            self.rehash()
        i = start_i = number % len(self.data)
        while True:
            if self.data[i] is None:
                self.data[i] = number
                self.used += 1
            if self.data[i] == number:
                return
            i = (i+1) % len(self.data)
            #if i == start_i:
            #    self.rehash()
            #    self.add(number)
            #    return


if __name__ == '__main__':
    contacts = MyOpenAddrHash(100)
    n = int(input())
    s = input()
    assert n * 10 - 1 == len(s)
    for i in range(n):
        num = int(s[i*10:i*10+9])
        contacts.add(num)
    print(contacts.used)
