# Digit cancelling fractions
# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
# digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


def digits(number):
    div = number
    while div > 0:
        div, mod = divmod(div, 10)
        yield mod


def intersection(a, b):
    return set(digits(a)).intersection(set(digits(b)))


def synthesize(lst, little_endian=True):
    number = 0
    multiplier = 1
    digits = lst if little_endian else reversed(lst)
    for digit in digits:
        number += multiplier * digit
        multiplier *= 10
    return number


def remove(number, x):
    number_lst = list(digits(number))
    if x in number_lst:
        number_lst.remove(x)
    return synthesize(number_lst)


def in_range(numerator, denominator):
    return 9 < numerator < denominator < 100


def is_trivial(numerator, denominator):
    return numerator % 10 == denominator % 10 == 0


def is_valid(numerator, denominator):
    # less than one is implicitly true by in_range
    return in_range(numerator, denominator) and not is_trivial(numerator, denominator)


def is_digit_cancelling(numerator, denominator):
    if not is_valid(numerator, denominator):
        return False

    common_digits = intersection(numerator, denominator)
    for common_digit in common_digits:
        cancelled_numerator = remove(numerator, common_digit)
        cancelled_denominator = remove(denominator, common_digit)
        if cancelled_denominator == 0:
            continue
        if numerator / denominator == cancelled_numerator / cancelled_denominator:
            return True
    return False


digit_cancelling_fractions = [(numerator, denominator)
                              for numerator in range(11, 100)
                              for denominator in range(numerator + 1, 100)
                              if is_digit_cancelling(numerator, denominator)]
assert len(digit_cancelling_fractions) == 4
assert (49, 98) in digit_cancelling_fractions

print(digit_cancelling_fractions)

product_numerator = product_denominator = 1
for numerator, denominator in digit_cancelling_fractions:
    product_numerator *= numerator
    product_denominator *= denominator

print(product_numerator, product_denominator)

common_factors = ((factor, product_numerator / factor, product_denominator / factor)
                  for factor in range(product_numerator, 1, -1)
                  if product_numerator % factor == product_denominator % factor == 0)
print(next(common_factors))
