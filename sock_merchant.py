# Sock Merchant https://www.hackerrank.com/challenges/sock-merchant/problem


def sockMerchant(n, ar):
    """
    param n: the number of socks in the pile
    param ar: the colors of each sock
    """
    a = [0]*101
    pairs = 0
    for i in range(n):
        if a[ar[i]] == 1:
            pairs += 1
            a[ar[i]] = 0
        else:
            a[ar[i]] = 1
    return pairs


if __name__ == "__main__":
    s = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    print(sockMerchant(len(s), s))

    s = [44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75, 36, 83, 78, 91, 17, 17,
         54, 65, 60, 21, 58, 98, 87, 45, 75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45,
         23, 38, 22, 44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20, 19, 64, 64, 93,
         60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, 43,
         15, 86, 5, 35, 63, 24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]

    print(sockMerchant(len(s), s))
