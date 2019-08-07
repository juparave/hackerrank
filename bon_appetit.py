# bon appetit https://www.hackerrank.com/challenges/bon-appetit/problem


def bonAppetit(bill, k, b):
    """
    param bill: an array of integers representing the cost of each item ordered
    param k: an integer representing the zero-based index of the item Anna doesn't eat
    param b: the amount of money that Anna contributed to the bill
    """
    # t = sum([i for i in [bill[j] for j in range(len(bill)) if j != k]])
    t = sum(bill)
    if (t-bill[k])/2 == b:
        res = "Bon Appetit"
    else:
        res = b - (t-bill[k])/2

    return res


if __name__ == "__main__":
    anna = 1
    bill = [3, 10, 2, 9]
    charge = 12

    print(bonAppetit(bill, anna, charge))
