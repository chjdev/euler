# Non-abundant sums
# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For
# example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a
# perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if
# this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the
# sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further
# by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant
# numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math


def even_divisors(num):
    if num == 0:
        return  # empty list for 0
    max_divisor = int(math.sqrt(num))
    yield 1
    for d in range(2, max_divisor + 1):
        if num % d == 0:
            yield d
            division = int(num / d)
            if d != division:
                yield division


MAX_NUM = 28123
abundable_numbers = list(map(lambda v_s: v_s[0], filter(lambda i_v: i_v[0] < i_v[1],
                                                        enumerate(map(sum, map(even_divisors, range(0, MAX_NUM)))))))
cache = [1] * (MAX_NUM + 1)
for idx, abundable in enumerate(abundable_numbers):
    j = idx
    test = abundable + abundable_numbers[j]
    while test <= MAX_NUM:
        cache[test] = 0
        j += 1
        test = abundable + abundable_numbers[j]
    if abundable > MAX_NUM:
        break
print(sum(map(lambda i_v: i_v[0] * i_v[1], enumerate(cache))))



