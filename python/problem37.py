# Truncatable primes
# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
# left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
# 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


from utils.primes import Primes


PRIMES = Primes()
TRUNCATABLE_PRIMES = [3797, 797, 37, 23, 53, 73]  # some trivial examples


def is_truncateable(number):
    if number < 11:
        return False

    if number in TRUNCATABLE_PRIMES:
        return True

    # right to left
    split = 10
    truncateable = None
    while truncateable is None:
        div, mod = divmod(number, split)
        if mod == number:
            truncateable = True
        else:
            if not PRIMES[mod] or not PRIMES[int(div)]:
                truncateable = False
            split *= 10

    if truncateable:
        TRUNCATABLE_PRIMES.append(number)

    return truncateable

sum_truncateable_primes = 0
num_found = 0
for prime in PRIMES.iterate_unbounded():
    if num_found >= 11:
        break
    if is_truncateable(prime):
        sum_truncateable_primes += prime
        num_found += 1

print(TRUNCATABLE_PRIMES)
print(sum_truncateable_primes)
assert 748317 == sum_truncateable_primes  # guard optimization

