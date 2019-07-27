# Kangaroo
# profile:
#   $ python -m cProfile kangaroo.py

def kangaroo(x1, v1, x2, v2):
    # brute solution
    jump = 0
    p1 = x1
    p2 = x2
    while(p1 != p2):
        jump += 1
        p1 = x1 + (v1 * jump)
        p2 = x2 + (v2 * jump)
        if (v1 > v2 and p1 > p2) or (v2 > v1 and p2 > p1):
            # will never reach
            return 'NO'
    return 'YES'

def kangaroo_m(x1, v1, x2, v2):
    # math solution
    if v1 == v2 and x1 != x2:
        # same speed diff position, never meet
        # and we avoid div by zero
        return 'NO'
    j = (x1 - x2) / (v2 - v1)
    return 'YES' if j == abs(int(j)) else 'NO'

if __name__ == "__main__":
    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    # print(kangaroo(x1, v1, x2, v2))
    print(kangaroo_m(x1, v1, x2, v2))

    x1 = 43
    v1 = 2
    x2 = 70
    v2 = 2

    # print(kangaroo(x1, v1, x2, v2))
    print(kangaroo_m(x1, v1, x2, v2))
