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

from itertools import count
from utils.primes import Primes

MAX_A = MAX_B = 1000
PRIMES = Primes()


def quadratic_formula(n, factors):
    a, b = factors
    return n**2 + a*n + b


def calc_num_primes(factors):
    num = 0
    for n in count():
        possible_prime = quadratic_formula(n, factors)
        if PRIMES[possible_prime]:
            num += 1
        else:
            return num

candidates = ((a, b)
              for b in PRIMES.iterate(0, MAX_B)  # b must be prime for case n = 0
              for a in range(-b + 2, MAX_A) if a % 2 == 1)  # a has to be odd and > -b for case n = 1
num_primes = {}
for candidate in candidates:
    num = calc_num_primes(candidate)
    num_primes[candidate] = num

max = 0
max_candidate = (0, 0)
for a, b in num_primes:
    num = num_primes[(a, b)]
    if num > max:
        max = num
        max_candidate = (a, b)

print(max, max_candidate, max_candidate[0] * max_candidate[1])
