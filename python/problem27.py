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
import math

MAX_A = MAX_B = 1000


class Primes:
    def __init__(self):
        self.sieve = [False, False, True, True, False, True, False, True]  # init to 0 - 3

    def _expand(self):
        length = len(self.sieve)
        new_length = 2 * length
        right = [True,] * length
        for num in filter(lambda i: self.sieve[i], range(0, len(self.sieve))):
            i = math.ceil(length / num)
            pos = num * i
            while pos < new_length:
                right[pos - length] = False
                i += 1
                pos = num * i
        self.sieve = self.sieve + right

    def __getitem__(self, num):
        if num < 2:
            return False

        while num >= len(self.sieve):
            self._expand()

        return self.sieve[num]


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
              for b in range(-MAX_B + 1, MAX_B) if PRIMES[b]  # b has to be a prime, otherwise n=0 is prime
              for a in range(-MAX_A + 1, MAX_A) if a % 2 == 1)  # a has to be odd, so n=1 is odd
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
