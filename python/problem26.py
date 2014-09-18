# Reciprocal cycles
# Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
# 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
# recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#
# 1 / 7 = 0.
# 10 / 7 = 1
# 3 / 7
# 30 / 7 = 4
# 2 / 7
# 20 / 7 = 2
# 6 / 7
# 60 / 7 = 8
# 4 / 7
# 40 / 7 = 5
# 5 / 7
# 50 / 7 = 7
# 1
# ...
#
#
# 1 / 6 = 0.
# 10 / 6 = 1
# 4 / 6 =
# 40 / 6 = 6
# 40 / 6 = 6
# 40 / 6
# and so on


def divide(n, k):
    if n < k:
        n *= 10
    return int(n / k), n % k


def detect_reciprocal_cycles(k):
    result = []
    rest_path = []
    rest = 1
    size = 0
    while rest != 0:
        div, rest = divide(rest, k)
        if rest in rest_path:  # found circle
            size = len(rest_path) - rest_path.index(rest)
            break
        rest_path.append(rest)
        result.append(div)
    return result, size  # no cycle


test_numbers = range(1, 1000)
result = ((k, detect_reciprocal_cycles(k)[1]) for k in test_numbers)
max = (0, 0)
for k, size in result:
    if size > max[1]:
        max = (k, size)
print(max)
