# birthday chocolate https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Lily has a chocolate bar that she wants to share it with Ron for his birthday.
# Each of the squares has an integer on it. She decides to share a contiguous segment
# of the bar selected such that the length of the segment matches Ron's birth month
# and the sum of the integers on the squares is equal to his birth day.
# You must determine how many ways she can divide the chocolate.


def birthday(s, d, m):
    """
    param s: an array of integers, the numbers on each of the squares of chocolate
    param d: an integer, Ron's birth day, the sum
    param m: an integer, Ron's birth month, the number of pieces
    """
    ways = 0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d and len(s[i:m+i]) == m:
            ways += 1
    return ways


def birthday_sliding_window(s, d, m):
    """
    param s: an array of integers, the numbers on each of the squares of chocolate
    param d: an integer, Ron's birth day, the sum
    param m: an integer, Ron's birth month, the number of pieces

    If you already have the sum of a subarray (like the starred elements in [***___]), 
    then you can get sum of the subarray with indices shifted right by 1 
    (for the previous example, [_***__]) by adding one element and subtracting another.
    """
    l = len(s)
    if l < m:
        return 0
    ways = 0
    t = sum(s[:m])
    if t == d:
        ways += 1
    for i in range(l-m):
        t = t - s[i-1] + s[i]
        if t == d:
            ways += 1
    return ways


if __name__ == "__main__":
    s, d, m = [1, 2, 1, 3, 2], 3, 2
    print(birthday(s, d, m))
    print(birthday_sliding_window(s, d, m))
    s, d, m = [4], 4, 1
    print(birthday(s, d, m))
    print(birthday_sliding_window(s, d, m))
    s, d, m = [1, 1, 1, 1, 1, 1], 3, 2
    print(birthday(s, d, m))
    print(birthday_sliding_window(s, d, m))
