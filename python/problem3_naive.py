# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# recursive method
# brute force prime generation
# doesn't work because of recursion depth limit

import math
import itertools

NUM = 13195


def is_divisible_by_one(x, factors):
    for factor in factors:
        if x % factor == 0:
            return True
    return False


def gen_prime(limit=-1):  # TODO limit is stupid
    assert limit >= 2
    sieve = [2, 3]  # because 2 is the only even prime
    yield sieve[-2]
    yield sieve[-1]

    while True:
        generator = filter(lambda v: not is_divisible_by_one(v, sieve),
                           itertools.count(sieve[-1] + 2, 2))
        new_prime = next(generator)
        if new_prime > limit > 0:
            return
        else:
            print("new prime: ", new_prime)
            sieve.append(new_prime)
            yield sieve[-1]


def factorize(number):
    limit = math.sqrt(number)
    candidates = list(gen_prime(limit))

    def _factorize(number, candidates, factors=[]):
        if len(candidates) == 0:
            return

        if number == 1:  # last one found
            return

        if number in candidates:
            print("found':", number)
            factors.append(int(number))
            return

        # try a division and recurse
        candidate = candidates[-1]
        division = number / candidate
        if division.is_integer():
            print("found: ", candidate)
            factors.append(candidate)
            _factorize(division, candidates, factors)
        else:
            _factorize(number, candidates[:-1], factors)

    factors = []
    _factorize(number, candidates, factors)

    return factors


print("factorization", factorize(NUM))