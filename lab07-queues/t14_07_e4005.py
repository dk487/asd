#!/usr/bin/env python3

# https://eolymp.com/uk/problems/4005
# Вказівка. Використати чергу, дек або один із списків.

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
            return None

        value = self.head.value
        self.head = self.head.next
        self.size -= 1

        if not self.head:
            self.tail = None

        return value


def int_list(s):
    return [int(i) for i in s.split()]


if __name__ == '__main__':
    player1 = Queue()
    player2 = Queue()
    n = int(input())
    assert 2 <= n <= 100000 and n % 2 == 0

    cards = int_list(input())
    assert n//2 == len(cards)
    for card in cards:
        player1.push(card)

    cards = int_list(input())
    assert n//2 == len(cards)
    for card in cards:
        player2.push(card)

    moves = 0
    while moves < 200000 and player1.size and player2.size:
        card1 = player1.pop()
        card2 = player2.pop()

        round_winner = player1 if card1 > card2 else player2
        if card1 == 0 and card2 == n - 1:
            round_winner = player1
        if card2 == 0 and card1 == n - 1:
            round_winner = player2

        round_winner.push(card1)
        round_winner.push(card2)
        moves += 1

    if moves == 200000:
        print('draw')
    elif player1.size:
        print('first', moves)
    else:
        print('second', moves)
