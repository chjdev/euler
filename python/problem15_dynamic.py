# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
# routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?


def num_paths(x, y):
    cache = {(0, 0): 1}

    def _num_paths(x, y, cache):
        if (x, y) in cache:
            return cache[(x, y)]

        if x == 0 or y == 0:
            return 1

        if x == y:  # diagonal
            cache[(x, y)] = 2 * _num_paths(x, y - 1, cache)  # symmetric grid
        else:
            cache[(x, y)] = _num_paths(x - 1, y, cache) + _num_paths(x, y - 1, cache)
        return cache[(x, y)]

    return _num_paths(x, y, cache)


print(num_paths(20, 20))

