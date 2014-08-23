# Lattice paths
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
# routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?


def move(coord):
    x, y = coord

    if x == y == 0:
        return 1

    num_paths = 0
    if x > 0:
        num_paths += move((x-1, y))
    if y > 0:
        num_paths += move((x, y-1))

    return num_paths

print(move((20, 20)))
