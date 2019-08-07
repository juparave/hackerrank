# divisible sum pairs https://www.hackerrank.com/challenges/divisible-sum-pairs


def divisibleSumPairs(n, k, ar):
    pairs = 0
    m = dict()
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i == j:
                # we will no process not same index
                continue
            key = ",".join(map(str, [i, j] if i < j else [j, i]))
            if key in m.keys():
                # we will no reprocess same calculation
                continue
            r = (ar[i] + ar[j]) % k
            m[key] = r
            if r == 0:
                pairs += 1
    return pairs

def divisibleSumPairs2(n, k, ar):
    return sum(1 for i in range(n) for j in range(n) if i < j and (ar[i]+ar[j])%k == 0)


if __name__ == "__main__":
    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]
    print(divisibleSumPairs(n, k, ar))
    print(divisibleSumPairs2(n, k, ar))
    n = 16
    k = 3
    ar = [1, 3, 2, 6, 1, 2, 3, 5 ,6 ,7 ,8 ,9, 4, 3, 11, 13]
    print(divisibleSumPairs(n, k, ar))
    print(divisibleSumPairs2(n, k, ar))
