#!/usr/bin/env python3

# https://eolymp.com/problems/3970

def int_list(s):
    return [int(i) for i in s.split()]


def lower_bound(haystack, needle):
    left = 0
    right = len(haystack)
    while left < right:
        mid = (left + right) // 2
        if haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(haystack, needle):
    left = 0
    right = len(haystack)
    while left < right:
        mid = (left + right) // 2
        if haystack[mid] <= needle:
            left = mid + 1
        else:
            right = mid
    return left


def range_count(haystack, needle):
    return upper_bound(haystack, needle) - lower_bound(haystack, needle)


if __name__ == '__main__':
    n = int(input())
    colors = int_list(input())
    assert 1 <= n <= 100000 and n == len(colors)

    m = int(input())
    query = int_list(input())
    assert 1 <= m <= 100000 and m == len(query)

    for i in query:
        print(range_count(colors, i))
