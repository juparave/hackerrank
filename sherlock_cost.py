# Sherlock and cost


def cost(arr):
    """
    param arr: int array
    """
    msum = 0
    narr = arr[:]    # copy
    arrs = []
    arrs.append(narr[:])
    while sum(narr) != len(narr):
        for i in range(len(arr)):
            # 1 in minimun number on array
            nsum = sum([abs(y-x) for x,y in zip(narr[:-1], narr[1:])])
            msum = nsum if nsum > msum else msum
            if narr[i] == 1:
                continue
            narr[i] = narr[i] - 1
            arrs.append(narr[:])

    for a in arrs:
        print(a)
    return msum



if __name__ == "__main__":

    arr = [10, 1, 10, 1, 10]
    print(cost(arr))

    arr = [2, 4, 3]
    print(cost(arr))

    arr = [100, 2, 100, 2]
    print(cost(arr))
