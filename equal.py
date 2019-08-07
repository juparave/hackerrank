# Equal
import sys


def equal(mates):
    """
    Get the minumum of operations to equalize chocolates on mates
    using 1, 2, 5 chocolates on each operation
    param mates: int array
    """
    m = min(mates)
    ans = sys.maxsize

    for i in range(5):
        ops = 0
        for j in range(len(mates)):
            t = mates[j] - (m - i)
            ops += int(t/5) + int(t%5/2) + int(t%5%2)
        ans = ans if ans < ops else ops

    return ans


if __name__ == "__main__":
    mates = [2, 2, 3, 7]

    print(equal(mates))