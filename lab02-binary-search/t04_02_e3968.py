#!/usr/bin/env python3
import math

# https://eolymp.com/problems/3968


def binary_approx(fn, target, max_error, left = 0, right = 1e10):
    while (right - left) > max_error:
        mid = (left + right) / 2
        attempt = fn(mid)
        if attempt > target:
            right = mid
        else:
            left = mid
    # Optional: integer solutions (kinda 0.99999 < x < 1.00001)
    #if math.ceil(left) == math.floor(right):
    #    return math.ceil(left)
    return left


if __name__ == '__main__':
    n = float(input())

    fn = lambda x: x**2 + math.sqrt(x)
    max_error = 1e-07

    print(binary_approx(fn, n, max_error))
