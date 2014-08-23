# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# bottom up approach. https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# prime factorizations of numbers are unique!

import math
import itertools

NUM = 600851475143


def is_divisible_by_one(x, factors):
    for factor in factors:
        if x % factor == 0:
            return True
    return False


def gen_primes(limit=-1):
    assert limit >= 2
    sieve = [2, 3]  # because 2 is the only even prime
    yield sieve[-2]
    yield sieve[-1]

    while True:
        generator = filter(lambda v: not is_divisible_by_one(v,
                                                             filter(lambda s: s < math.sqrt(v), sieve)),
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
    factors = []

    for prime in gen_primes(limit):
        while number % prime == 0:
            factors.append(prime)
            number /= prime
        if number == 1:
            break

    return factors


factorization = factorize(NUM)
print("factorization", factorization)
print("largest factor", max(factorization))
