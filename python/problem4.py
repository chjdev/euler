# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

LOWER = 100
UPPER = 999


def is_palindrome(num):
    snum = str(num)
    half_len = int(len(snum) / 2)
    return snum.endswith(snum[half_len-1::-1])


def ordered_palindromes():
    for a in range(UPPER, LOWER - 1, -1):
        for b in range(UPPER, a - 1, -1):
            product = a * b
            if is_palindrome(product):
                print(a, ' * ', b, ' = ', product)
                yield product


print(max(ordered_palindromes()))
