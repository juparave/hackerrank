# Coin change problem
# $ python -m cProfile coin_change.py

def get_ways(amount, coins):
    """
    param amount: int amount number
    param coins:  int array of posible coins
    """
    combos = [0] * (amount + 1)
    combos[0] = 1
    for coin in coins:
        for i in range(len(combos)):
            if i >= coin:
                combos[i] += combos[i - coin]
    return combos[amount]


def get_ways_recursive(amount, coins, current_coin=0):
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    ways = 0
    for i in range(current_coin, len(coins)):
        ways += get_ways_recursive(amount - coins[i], coins, i)

    return ways


def get_ways_recursive_with_memo(amount, coins, current_coin=0, memo=dict()):
    """ Recursive with Memoization """

    if amount == 0:
        return 1
    if amount < 0:
        return 0

    key = "%s-%s" % (amount, current_coin)
    if key in memo.keys():
        return memo[key]

    ways = 0
    for i in range(current_coin, len(coins)):
        ways += get_ways_recursive_with_memo(amount - coins[i], coins, i, memo)

    memo[key] = ways
    return ways


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 1]
    amount = 88

    print(get_ways_recursive(amount, coins))
    print(get_ways_recursive_with_memo(amount, coins))
    print(get_ways(amount, coins))
