# compareTriplets


def compareTriplets(a, b):
    bob = 0
    ali = 0
    for i in range(len(a)):
        ali += 1 if a[i] > b[i] else 0
        bob += 1 if b[i] > a[i] else 0
    return [ali, bob]


def compareTripletsC(alice, bob):
    result = map(lambda a_b: (a_b[0] > a_b[1],
                              a_b[1] > a_b[0]), zip(alice, bob))
    return map(sum, zip(*result))


def compareTripletsP3(a, b):
    return map(
        lambda t: sum([x > y for x, y in zip(*t)]),
        ((a, b), (b, a))
    )


if __name__ == "__main__":
    bob = [99, 16, 8]
    alice = [17, 28, 30]

    result = compareTriplets(alice, bob)
    print(' '.join(map(str, result)))
    result = compareTripletsC(alice, bob)
    print(' '.join(map(str, result)))
    result = compareTripletsP3(alice, bob)
    print(' '.join(map(str, result)))
