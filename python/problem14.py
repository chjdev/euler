# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import numpy as np

MAX = 1000000


def collatz(n):
    candidate = n / 2
    if candidate.is_integer():
        return candidate
    else:
        return 3 * n + 1


cache = {1: (1, 1)}
def build(n, cache):
    if n in cache:
        return cache[n]
    else:
        cont = collatz(n)
        _, length = build(cont, cache)
        cache[n] = (cont, length + 1)
        return cache[n]


lengths = [build(i, cache)[1] for i in range(1, MAX)]
print(np.argmax(lengths) + 1)  # +1 because of list index


