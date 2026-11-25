#!/usr/bin/env python3
import math

# Умова: на відрізку [1.6, 3] знайдіть корінь рівняння sin x = x/3
# Результат: 2.2788626600755384

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
    fn = lambda x: x/3 - math.sin(x)
    max_error = 1e-12
    left = 1.6
    right = 3

    print(binary_approx(fn, 0, max_error, left, right))
