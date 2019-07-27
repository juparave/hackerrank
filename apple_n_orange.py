# Apple and Orange


def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    param s: integer, starting point of Sam's house location.
    param t: integer, ending location of Sam's house location.
    param a: integer, location of the Apple tree.
    param b: integer, location of the Orange tree.
    param apples: integer array, distances at which each apple falls from the tree.
    param oranges: integer array, distances at which each orange falls from the tree.
    """

    house = range(s, t+1)
    apple_tree = a
    orange_tree = b
    capples = 0
    coranges = 0
    for i in apples:
        capples = capples + (1 if i+apple_tree in house else 0)
    for i in oranges:
        coranges = coranges + (1 if i+orange_tree in house else 0)

    print('%s\n%s' % (capples, coranges))


if __name__ == "__main__":
    s = 7
    t = 11
    a = 5
    b = 15
    m = 3
    n = 2
    apples = [-2, 2, 1]
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
