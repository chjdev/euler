import math


class Primes:
    _sieve = [False, False, True, True, False, True, False, True]  # init to 0 - 3

    def _expand(self):
        length = len(self._sieve)
        new_length = 2 * length
        right = [True] * length
        for num in (s for s in range(0, math.ceil(math.sqrt(new_length))) if self._sieve[s]):
            i = math.ceil(length / num)
            pos = num * i
            while pos < new_length:
                right[pos - length] = False
                i += 1
                pos = num * i
        self._sieve.extend(right)

    def __getitem__(self, num):
        if num < 2:
            return False

        while num >= len(self._sieve):
            self._expand()

        return self._sieve[num]

    def iterate(self, lower, upper):
        for number in range(lower, upper):
            if self[number]:
                yield number

    def iterate_unbounded(self, lower=2):
        number = lower
        while True:
            if self[number]:
                yield number
            number += 1

