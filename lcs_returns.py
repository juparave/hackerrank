# LCS Return

# Given two strings,  and, find and print the total number of ways to insert a character at any position in string such that the length of the Longest Common Subsequence of characters in the two strings increases by one.

# Input Format

# The first line contains a single string denoting.
# The second line contains a single string denoting.


# function LCSLength(X[1..m], Y[1..n])
#     C = array(0..m, 0..n)
#     for i := 0..m
#        C[i,0] = 0
#     for j := 0..n
#        C[0,j] = 0
#     for i := 1..m
#         for j := 1..n
#             if X[i] = Y[j]
#                 C[i,j] := C[i-1,j-1] + 1
#             else
#                 C[i,j] := max(C[i,j-1], C[i-1,j])
#     return C[m,n]


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]

    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# end of function lcs


def tutzkiAndLcs(a, b):
    n = []
    # current lcs
    lcs = mylcs(a, b)
    len_a = len(a)
    for c in set(b):
        for i in range(len_a + 1):
            x = mylcs(a[:i] + c + a[i:], b)
            if x > lcs:
                # print(c, i, x, a[:i] + c + a[i:])
                # store way into list
                n.append((c, i, x, a[:i] + c + a[i:]))

    # return total number of way
    return len(n)

def mylcs(b, a):
    len_a = len(a)
    len_b = len(b)
    c = [[0] * (len_b + 1) for i in range(len_a + 1)]
    j_range = range(1, len_b + 1)
    for i in range(1, len_a + 1):
        for j in j_range:
            # if i == 0 or j == 0:
            #     c[i][j] = 0
            if a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                # c[i][j] = max(c[i-1][j], c[i][j-1])
                c[i][j] = c[i-1][j] if c[i-1][j] > c[i][j-1] else c[i][j-1]
    return c[len_a][len_b]


if __name__ == "__main__":
    a = "AGGTAB"
    b = "GXTXAYB"

    a = "Instead of printing the output at the end of the profile run, you can save the results to a file by specifying a filename to the run() function:"
    b = "The pstats.Stats class reads profile results from a file and formats them in various ways."

    print(tutzkiAndLcs(a, b))
    print(lcs(a, b))
