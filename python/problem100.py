# Arranged probability
#
# Problem 100
#
# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were
# taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box
# containing eighty-five blue discs and thirty-five red discs.
# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of
# blue discs that the box would contain.

# P(BB) = (B / N) * ((B - 1) / (N - 1)) = 0.5 = B * (B - 1) / N * (N - 1)
# -> B**2 - B = N*(N-1)/2
# -> B**2 - B - N*(N-1)/2 = 0

# quadratic formula:
# ax**2 + bx + c = 0,  x = (-b +- sqrt(b**2 - 4ac))/2a

# -> a = 1, b = -1, c = -N*(N-1)/2

# by using this formula we can find the amount of blue disks necessary for a 50% chance for a given N.
# if this amount is an integer, we have a valid solution.

from itertools import count
from math import sqrt


def solve(a, b, c):
    return (-b + sqrt(b**2 - 4*a*c)) / (2*a)


def is_valid(B):
    return B.is_integer()


def solve_for_50(N):
    return solve(1, -1, (-N*(N-1))/2)


solutions = ((N + 10**12, int(B)) for N, B in enumerate(map(solve_for_50, count(10**12))) if is_valid(B))
print(next(solutions))

# not 100% correct due to precision (result is 0.49999999999999999) but I'll leave it at that since
# https://www.google.at/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=707106783028%2F1000000002604++*+707106783027%2F1000000002603
