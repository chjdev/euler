# Double-base palindromes
# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#
#  1
#  11
#  22
#  ...
#  121
#  131
#  ...
#  212
#  222
#  ...
#  1221
#  1441
#  32323
#  32423


def check_palindrome_b2(number_b10):
    binary = "{0:b}".format(number_b10)
    return binary == binary[::-1]


def next_palindrome_b10():
    yield from range(0, 10)
    lower = 1
    while True:
        upper = lower * 10
        for i in range(lower, upper):  # even num digits
            i_str = str(i)
            yield int(i_str + i_str[::-1])
        for i in range(lower, upper):  # odd num digits
            i_str = str(i)
            for j in range(0, 10):
                yield int(i_str + str(j) + i_str[::-1])
        lower *= 10


def next_palindrome_b10_below(maximum):
    for plaindrome_b10 in next_palindrome_b10():
        if plaindrome_b10 >= maximum:
            return
        yield plaindrome_b10

result = sum([palindrome_b10 for palindrome_b10 in next_palindrome_b10_below(1e6)
              if check_palindrome_b2(palindrome_b10)])
print(result)
assert 872187 == result  # optimization guard






