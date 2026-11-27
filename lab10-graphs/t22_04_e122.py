#!/usr/bin/env python3

# https://eolymp.com/problems/122

def int_list(s):
    return [int(i) for i in s.split()]


def routes(matrix, v_from, v_to, max_depth, visited):
    if max_depth == 0:
        return
    row = matrix[v_from]
    for i in range(len(row)):
        if not row[i] or i == v_from or i in visited:
            continue
        if i == v_to:
            yield [v_to]
        else:
            for subroute in routes(matrix, i, v_to, max_depth - 1, visited + [i]):
                yield [v_from] + subroute


if __name__ == '__main__':
    n, k, a, b, d = int_list(input())
    assert 1 <= n <= 50
    assert 1 <= d <= 10
    matrix = [[0]*n for i in range(n)]

    for j in range(k):
        o, i = int_list(input())
        assert 1 <= o <= n
        assert 1 <= i <= n
        matrix[o-1][i-1] = 1

    print(len(list(routes(matrix, a-1, b-1, d, [a-1]))))
