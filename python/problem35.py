# Circular primes
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
# prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import math


def gen_primes(max):
    lst = list(range(2, max + 1))
    for i in range(0, math.ceil(math.sqrt(len(lst)))):
        prime = lst[i]
        if prime == 0:
            continue
        for j in range(i + prime, len(lst), prime):
            lst[j] = 0

    return filter(lambda p: p != 0, lst)


def gen_rotations(number_str):
    for _ in range(0, len(number_str)):
        number_str = number_str[-1] + number_str[:-1]
        yield number_str


def is_circular_prime(prime):
    if prime in CIRCULARS:
        return True

    prime_str = str(prime)
    if len(prime_str) == 1:
        return True
    for check in ['2', '4', '5', '6', '8']:  # can't be a prime
        if check in prime_str:
            return False
    rotations = gen_rotations(prime_str)
    for rot in rotations:
        if not int(rot) in PRIMES:
            return False
    for rotation in rotations:
        CIRCULARS.add(rotation)
    return True


CIRCULARS = set()
PRIMES = set(gen_primes(int(1e6)))

circular_primes = filter(is_circular_prime, PRIMES)
print(len(list(circular_primes)))
