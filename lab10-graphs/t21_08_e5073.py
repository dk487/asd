#!/usr/bin/env python3

# https://eolymp.com/problems/5073

def int_list(s):
    return [int(i) for i in s.split()]


if __name__ == '__main__':
    n, m = int_list(input())
    assert 1 <= n <= 100
    assert 1 <= m <= 10000
    matrix = [[0]*n for i in range(n)]
    multi = False

    for j in range(m):
        o, i = int_list(input())
        assert 1 <= i <= n
        assert 1 <= o <= n
        if matrix[o-1][i-1]:
            multi = True
            break
        matrix[o-1][i-1] = True

    print(['NO', 'YES'][multi])
