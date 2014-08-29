import math
import itertools


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



