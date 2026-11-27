#!/usr/bin/env python3

# https://eolymp.com/problems/3987

def int_list(s):
    return [int(i) for i in s.split()]


if __name__ == '__main__':
    n, m = int_list(input())
    assert 1 <= n <= 100
    assert 1 <= m <= 10000
    matrix = [[0]*n for i in range(n)]

    for i in range(m):
        a, b = int_list(input())
        assert 1 <= a <= n
        assert 1 <= b <= n
        assert a != b
        matrix[a-1][b-1] = 1
        matrix[b-1][a-1] = 1

    full = True
    for row in matrix:
        if sum(row) != n-1:
            full = False
            break
    print(['NO', 'YES'][full])
