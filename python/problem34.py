# Digit factorials
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# finding an upper limit:
# the biggest conceivable number consists of only (and at least 2) digit 9
# 9! + 9! = 725.760
# 9! + 9! + 9! = 1.088.640
# the RHS is of the form yr = x * 9! = x * 362.880
# the LHS is of the form yl = 10 ^ x - 1
# that means that the LHS will eventually overtake RHS
# a couple quick tries show that 9999999 > (9!*7 = 2.540.160)
# with that idea we can backtrack to 9991111 > (9!+9!+9!+1!+1!+1!+1! = 1.088.644) and cut the upper bound more
# than in half
# that means we need at least a 6 digit number

from math import factorial

FACTORIALS = [factorial(num) for num in range(0, 10)]
UPPER = 1088644


# # #naive brute force
# def to_digits(number):
#     yield from map(int, str(number))
#
#
# def is_digit_factorial_equivalent(number):
#     digits = to_digits(number)
#     digit_factorials = map(lambda digit: FACTORIALS[digit], digits)
#     return number == sum(digit_factorials)
#
# result = sum([number for number in range(11, UPPER) if is_digit_factorial_equivalent(number)])
# # >> 40730
# assert result == 40730


# optimized dynamic
# prevents recalculating the sums by reusing partial sums

PARTIAL_SUMS = [(0, 2), (1, 1)] + [(0, 0)] * 5


def add_one(idx=0):
    if idx >= len(PARTIAL_SUMS):
        raise "Cache exhausted!"
    digit, fac_sum = PARTIAL_SUMS[idx]
    if digit == 9:
        digit = 0
        fac_sum = 1 + add_one(idx + 1)
    else:
        digit += 1
        fac_sum = FACTORIALS[digit] + (PARTIAL_SUMS[idx+1][1] if idx < len(PARTIAL_SUMS) - 1 else 0)

    PARTIAL_SUMS[idx] = (digit, fac_sum)
    return fac_sum


def next_digit_factorial_sum_equivalent():
    for number in range(11, UPPER):
        fac_sum = add_one()
        if fac_sum == number:
            yield number

result = sum(next_digit_factorial_sum_equivalent())
print(result)
assert result == 40730  # guard optimization

