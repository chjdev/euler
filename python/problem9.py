# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
from functools import reduce


def pythagorean_tuples_1000():
    for a in range(1, 1000):
        for b in range(a + 1, 1000 - a):
            c = math.sqrt(a ** 2 + b ** 2)
            if c.is_integer():
                print("pythagorean tuple", (a, b, c))
                yield (a, b, c)

matching_1000 = filter(lambda tuple: sum(tuple) == 1000, pythagorean_tuples_1000())
products = map(lambda tuple: int(reduce(lambda a, b: a*b, tuple)), matching_1000)
print(list(products))
