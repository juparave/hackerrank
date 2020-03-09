#!/usr/bin/env python
# bunny-prisoner-locating on google foobar

# Bunny Prisoner Locating
# =======================

# Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

# The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

# | 16
# | 11 17
# |  7 12 18
# |  4  8 13 19
# |  2  5  9 14 20
# |  1  3  6 10 15 21

# Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.

# For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners).

# Write a function solution(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your solution as a string representation of the number.


def print_row(r, h):
    """  """
    r = get_row(r, h)
    print(" ".join([str(n) for n in r]))


def get_row(r, h):
    """ print row `r` of a triagle of height `h` """
    # row index
    ri = 0
    for i in range(r - 1):
        ri = ri + i
    value = []
    # columns
    t = 0 + (ri)
    # to draw triangle `range(h - (r - 1))`
    for i in range(h):
        t = t + (r + i)
        value.append(t)

    return value


def solution(x, y):

    row = get_row(y, max(x, y)+1)
    return str(row[x-1])


if __name__ == "__main__":
    print(solution(1,10))
    print(solution(5,10))
    print(solution(10,5))

    # print(solution(5, 10))
    # print(solution(3, 2))
    print_row(1, 10)
    print()
    print_row(2, 10)
    print()
    print_row(3, 10)
    print()
    print_row(4, 10)
    print()
    print_row(5, 10)
    print()
    print_row(6, 10)
    print()
    print_row(7, 10)
    print()
    print_row(8, 10)
    print()
    print_row(9, 10)
    print()
    print_row(10, 10)
    print()
