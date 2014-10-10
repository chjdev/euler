# Digit fifth powers
#
# Problem 30
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def _minus_one(lst, i=0):
    if lst[i] > 0:
        lst[i] -= 1
        return lst
    if lst[i] == 0:
        if i == len(lst) - 1:
            lst = [9] * (len(lst) - 1)
        else:
            orig_len = len(lst)
            lst = _minus_one(lst, i + 1)
            if orig_len == len(lst):
                lst[i] = lst[i + 1]
    return lst


# inspired by silverfish's comment:
#   the sum of the digits is not dependent on the order of these!
#   -> create only unique lists of digits
def gen_candidates():
    # ok the biggest number conceivable is the break even of number of digits using 9
    # 9**5 * 6 = 354294 so 6 digit 9s yield this number which is the maximum possible number to reach
    # (actually it's quite less than that, but this is a good enough guess to start and can be optimized if necessary)
    init = [9] * 6
    while len(init) > 1:  # sums need 2 numbers
        init = _minus_one(init)
        yield init


pow5_sums = [(sum([d**5 for d in digit_representation]), "".join(map(str, digit_representation)))
             for digit_representation in gen_candidates()]
identical = [(a, b) for a, b in pow5_sums if sorted(list(str(a))) == sorted(list(b))]
print(sum([a for a, _ in identical]))  # 443839
