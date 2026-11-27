#!/usr/bin/env python3

# https://eolymp.com/problems/5074

def int_list(s):
    return [int(i) for i in s.split()]


if __name__ == '__main__':
    n, m = int_list(input())
    assert 1 <= n <= 100
    assert 1 <= m <= n*(n-1)//2
    v = [0] * n

    for j in range(m):
        o, i = int_list(input())
        assert 1 <= i <= n
        assert 1 <= o <= n
        assert o != i
        v[i-1] += 1
        v[o-1] += 1

    for i in range(n):
        print(v[i])
