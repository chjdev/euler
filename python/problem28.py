# Number spiral diagonals
#
# Problem 28
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31

# 3x3 -> 1
# 5x5 -> +2 -> 3
# 7x7 -> +2 -> 5
# 1 (2) 3 (4) 5 (6) 7 (8) 9
# (10) (11) (12) 13 (14) (15) (16) 17 (18) (19) (20) 21 (22) (23) (24) 25
# (26) (27) (28) (29) (30) 31  and so on
# in english: iterate 4 times using steps according to the sequence above

import itertools


def spiral_numbers(max_dim=None):
    dim = 1
    num = 1
    yield num
    for offset in itertools.count(2, 2):
        dim += 2
        for i in range(0, 4):
            num += offset
            yield num
        if not max_dim is None and dim >= max_dim:
            break


print(sum(spiral_numbers(1001)))

