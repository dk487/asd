#!/usr/bin/env python3
import math

# Умова: на відрізку [0, 2] знайдіть корінь рівняння x^3+4x^2+x−6=0.
# Результат: 1.0

def binary_approx(fn, target, max_error, left = 0, right = 1e10):
    while (right - left) > max_error:
        mid = (left + right) / 2
        attempt = fn(mid)
        # Буде працювати, якщо функція неспадна
        if attempt > target:
            right = mid
        else:
            left = mid
    return left


if __name__ == '__main__':
    fn = lambda x: x**3 + 4 * x**2 + x - 6
    max_error = 1e-12
    left = 0
    right = 2

    print(binary_approx(fn, 0, max_error, left, right))
