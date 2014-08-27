# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math
import functools


def even_divisors(num):
    if num == 0:
        return  # empty list for 0
    max_divisor = int(math.sqrt(num))
    yield 1
    for d in range(2, max_divisor + 1):
        if num % d == 0:
            yield d
            division = int(num / d)
            if d != division:
                yield division


def test():
    # just thought it would be a nifty way to check :)
    xor = lambda a, b: a ^ b
    test_fun = functools.reduce(xor, even_divisors(220))
    test_hand = functools.reduce(xor, [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
    assert test_fun == test_hand


# test()
N = 10000
even_divisor_list = (even_divisors(num) for num in range(0, N))
sums = [sum(lst) for lst in even_divisor_list]
amicables = [index for index, d in enumerate(sums) if index != d and d < len(sums) and index == sums[d]]
print(sum(amicables))

