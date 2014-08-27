# 10001st prime
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

import itertools

N = 10001


def is_divisible_by_one(x, factors):
    for factor in factors:
        if x % factor == 0:
            return True
    return False


def gen_prime(limit=None):
    assert limit is None or limit >= 2
    sieve = [2, 3]  # because 2 is the only even prime
    yield sieve[-2]
    yield sieve[-1]

    while True:
        generator = filter(lambda v: not is_divisible_by_one(v, sieve),
                           itertools.count(sieve[-1] + 2, 2))
        new_prime = next(generator)
        if not limit is None and new_prime > limit > 0:
            return
        else:
            sieve.append(new_prime)
            print(new_prime)
            yield sieve[-1]


# https://docs.python.org/2/library/itertools.html#recipes
def nth(iterable, n, default=None):
    """Returns the nth item or a default value"""
    return next(itertools.islice(iterable, n, None), default)


print(nth(gen_prime(), N - 1))
