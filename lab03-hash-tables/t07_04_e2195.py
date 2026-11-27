#!/usr/bin/env python3
import re

# https://eolymp.com/problems/2195


class MyOpenAddrHash:
    def __init__(self, size: int):
        assert size > 0
        self.data = [None] * size
        self.used = 0

    def mkhash(self, key: str):
        r = 0
        for c in key:
            r = (r * 31 + ord(c)) & 0xFFFFFFFF
        return r

    def rehash(self):
        new_self = MyOpenAddrHash(len(self.data) * 20)
        for row in self.data:
            if row is not None:
                new_self.add(row)
        self.data = new_self.data

    def add(self, word: str):
        if (self.used * 2 > len(self.data)):
            self.rehash()
        i = self.mkhash(word) % len(self.data)
        while True:
            if self.data[i] is None:
                self.data[i] = word
                self.used += 1
            if self.data[i] == word:
                return
            i = (i+1) % len(self.data)

    def find(self, word: str):
        i = start_i = self.mkhash(word) % len(self.data)
        while True:
            if self.data[i] is None:
                return False
            if self.data[i] == word:
                return True
            i = (i+1) % len(self.data)
            if i == start_i:
                return False


class WrongWordUsed(Exception):
    pass


if __name__ == '__main__':
    words_allowed = MyOpenAddrHash(100)
    words_used = MyOpenAddrHash(100)
    n, m = [int(i) for i in input().split()]

    for i in range(n):
        words_allowed.add(input().upper())

    try:
        for i in range(m):
            text = input()
            word_cut = re.compile(r'(\w+)')
            is_word = re.compile(r'\w')
            for word in word_cut.split(text):
                if is_word.match(word):
                    word = word.upper()
                    if not words_allowed.find(word):
                        raise WrongWordUsed()
                    words_used.add(word)
        if words_allowed.used == words_used.used:
            print('Everything is going to be OK.')
        else:
            print('The usage of the vocabulary is not perfect.')
    except WrongWordUsed:
        print('Some words from the text are unknown.')
