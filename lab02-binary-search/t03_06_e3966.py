#!/usr/bin/env python3

# https://eolymp.com/problems/3966

def int_list(s):
    return [int(i) for i in s.split()]


def binary_search(haystack, needle):
    left = 0
    right = len(haystack)-1
    while left <= right:
        mid = (left + right) // 2
        attempt = haystack[mid]
        if attempt == needle:
            return True
        if attempt > needle:
            right = mid-1
        else:
            left = mid+1
    return False


if __name__ == '__main__':
    n = int(input())
    butterflies = int_list(input())
    assert 1 <= n <= 100000 and n == len(butterflies)

    m = int(input())
    query = int_list(input())
    assert 1 <= m <= 100000 and m == len(query)

    for i in query:
        print(['NO', 'YES'][binary_search(butterflies, i)])
