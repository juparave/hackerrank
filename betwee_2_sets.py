# between two sets https://www.hackerrank.com/challenges/between-two-sets/problem
import sys
from functools import reduce


def gcd(x, y):
    """This function implements the Euclidian algorithm
    to find G.C.D. of two numbers"""
    while(y):
        x, y = y, x % y
    return x


def lcm(x, y):
    """This function takes two
    integers and returns the L.C.M."""
    lcm = (x*y)//gcd(x, y)
    return lcm


def getTotalX(a, b):
    alcm = reduce(lcm, a)
    bgcd = reduce(gcd, b)
    x = 1
    r = []
    while(x*alcm <= bgcd):
        if bgcd % (x*alcm) == 0:
            r.append(x*alcm)
        x += 1
    # print(r)
    return len(r)


if __name__ == "__main__":
    a = [2, 4]
    b = [16, 32, 96]

    print(getTotalX(a, b))

    a = [2, 3, 6]
    b = [42, 84]

    print(getTotalX(a, b))
