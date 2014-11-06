# Pandigital products
#
# Problem 32
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
# through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
# pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# man, this took forever to solve... stupid brute force only solutions :(


def is_pandigital(number, completeness=False):
    if number < 10:
        return True

    digits = orig = 1
    num_digits = 0
    while number > 0:
        num_digits += 1
        rest, digit = divmod(number, 10)
        digits |= 1 << digit
        if digits == orig:
            return False
        number, orig = rest, digits
    return True if not completeness else num_digits == 9


def gen_construct(*args):
    return int("".join(map(str, args)))


def add_if_pandigital(multiplicand, multiplier, results):
    result = multiplier * multiplicand
    construct = gen_construct(multiplicand, multiplier, result)
    if result >= 1e4:
        return False
    elif is_pandigital(construct):
        results.append(result)
    return True


def find_unique_pandigitals():
    results = []

    def _enumerate(multiplicand_lower, multiplicand_higher, multiplier_lower, multiplier_higher):
        for multiplicand in range(multiplicand_lower, multiplicand_higher + 1):
            for multiplier in (range(multiplier_lower, multiplier_higher + 1)):
                if not add_if_pandigital(multiplicand, multiplier, results):
                    break

    _enumerate(2, 9, 1234, 9876)
    _enumerate(11, 98, 123, 987)
    return set(results)


print(sum(find_unique_pandigitals()))