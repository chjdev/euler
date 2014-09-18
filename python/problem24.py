# Lexicographic permutations
# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
# the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012 021 102 120 201 210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import math


def nth_lexicographical(n, k):
    digits = list(range(0, k))
    permutation = []
    num_permutations = n - 1
    while num_permutations > 0:
        fac = math.factorial(len(digits[1:]))
        num_number = int(num_permutations / fac)
        num_permutations %= fac
        permutation.append(digits.pop(num_number))

    return permutation + digits


print(str(nth_lexicographical(1000000, 10)).strip('[]').replace(', ', ''))

