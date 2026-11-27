#!/usr/bin/env python3

# https://eolymp.com/problems/5075

def int_list(s):
    return [int(i) for i in s.split()]


if __name__ == '__main__':
    n, m = int_list(input())
    assert 1 <= n <= 100
    assert 1 <= m <= n*(n-1)
    v_i = [0] * n   # Vertex In
    v_o = [0] * n   # Vertex Out

    for j in range(m):
        o, i = int_list(input())
        assert 1 <= i <= n
        assert 1 <= o <= n
        v_i[i-1] += 1
        v_o[o-1] += 1

    for i in range(n):
        print(v_i[i], v_o[i])
