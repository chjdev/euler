# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math

MAX = 2000000


def gen_primes_elegant(max):  # apparently elegant and slow...
    def init(max):
        yield 2
        for i in range(3, max + 1, 2):
            yield i

    border = math.ceil(max / 2)
    primes = init(max)
    v = next(primes, None)
    num_generated = 1
    cumulated_generated = 0
    while not v is None:
        yield v
        if num_generated == 1000:
            cumulated_generated += num_generated
            num_generated = 0
            print("generated", cumulated_generated)
        if v < border:
            primes = filter(lambda n:
                            n > v and n % v != 0
                            , primes)
        v = next(primes, None)
        num_generated += 1


def gen_primes(max):
    lst = list(range(2, max + 1))
    for i in range(0, math.ceil(len(lst) / 2)):
        prime = lst[i]
        if prime == 0:
            continue
        for j in range(i + prime, len(lst), prime):
            lst[j] = 0

    return filter(lambda p: p != 0, lst)


print(sum(gen_primes(MAX)))



