# picking numbers https://www.hackerrank.com/challenges/picking-numbers/problem
# Given an array of integers, find and print the maximum number of integers you can
# select from the array such that the absolute difference between any two of the chosen 
# integers is less than or equal to . For example, if your array is a = [1, 1, 2, 2, 4, 4, 5, 5, 5],
# you can create two subarrays meeting the criterion: [1, 1, 2, 2] and [4, 4, 5, 5, 5]. 
# The maximum length subarray has 5 elements.


def pickingNumbers(a):
    m = [0]*100
    for i in a:
        m[i] += 1
    max = 0
    for i, j in zip(m[:-1], m[1:]):
        if (i + j) > max:
            max = i + j
    return max


if __name__ == "__main__":

    t1 = [1, 2, 2, 3, 1, 2]
    t2 = [4, 6, 5, 3, 3, 1]

    print(pickingNumbers(t1))
    print(pickingNumbers(t2))
