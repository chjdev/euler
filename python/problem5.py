# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import itertools


def is_divisible_by_one(x, factors):
    for factor in factors:
        if x % factor == 0:
            return True
    return False


def is_divisible_by_all(x, factors):
    for factor in factors:
        if x % factor != 0:
            return False
    return True


def lcm(factors, return_generator=False):
    max_factor = max(factors)
    generator = (f
                 for f in itertools.count(max_factor, max_factor)
                 if is_divisible_by_all(f, factors))
    if return_generator:
        return generator
    else:
        return next(generator)


print(lcm(range(1, 20)))
