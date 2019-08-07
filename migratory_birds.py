# migratory birds https://www.hackerrank.com/challenges/migratory-birds/problem


def migratoryBirds(arr):
    c = [0] * (5 + 1)

    for i in arr:
        c[i] += 1

    return c.index(max(c))


if __name__ == "__main__":
    sightnings = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

    print(migratoryBirds(sightnings))
