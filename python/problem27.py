# Quadratic primes
#
# Problem 27
#
# Euler discovered the remarkable quadratic formula:
#
# n² + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40,
# 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by
# 41.
#
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to
# 79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n² + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
# primes for consecutive values of n, starting with n = 0.

import math


def _gen_sub_primes(cur, primes, lst_size):
    lst = list(range(cur, cur + lst_size * 2))

    lst[0] = 0
    for prime in filter(lambda p: p > 0, primes):
        for j in range(prime - (cur % prime), len(lst), prime):
            lst[j] = 0

    return lst


def _spout_primes(cur, primes):
    for i in range(cur, len(primes)):
        prime = primes[i]
        if prime != 0:
            yield primes[i]


def gen_primes():
    cur = 0
    primes = [0, 0, 2, 3]
    lst_size = len(primes)

    while True:
        yield from _spout_primes(cur, primes)
        cur = len(primes)
        lst_size *= 2
        primes += _gen_sub_primes(cur, primes, lst_size)


def create_candidates():
    return [(a, b) for a in range(-1000, 1000) for b in range(-1000, 1000)]


candidates = create_candidates()
n = 0
    candidates = filter(lambda pair: pai)
