# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import math
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


FACTORS = [3, 5]
N = 1000

lcm = lcm(FACTORS)
mod_lcm = [i for i in range(0, lcm) if is_divisible_by_one(i, FACTORS)]
print("modulo lcm numbers\t", mod_lcm)

N_lcm = math.ceil(N / lcm)
print("number of modulos\t", N_lcm)

num_below_1000 = [i
                  for m in range(0, N_lcm)
                  for i in map(lambda j: j + (m * lcm), mod_lcm)
                  if i < N]
print("numbers below N\t\t", num_below_1000)

result = sum(num_below_1000)
print("final result\t\t", result)
