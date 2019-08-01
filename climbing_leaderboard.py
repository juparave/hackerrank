# Climbing leaderboard https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# python -m cProfile climbing_leaderboard.py
import random

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1

def binarySearch2(arr, k):
    lo = 0
    hi = len(arr) - 1

    while(lo <= hi):
        mid = int(lo + (hi - lo) / 2)
        if (arr[mid] == k):
            return mid
        elif arr[mid] < k and arr[mid - 1] > k:
            return mid
        elif arr[mid] > k and arr[mid + 1] <= k:
            return mid + 1
        elif arr[mid] < k:
            hi = mid -1
        elif arr[mid] > k:
            lo = mid + 1
    
    return -1


def climbingLeaderboard_brute(scores, alice):
    score_rank = dict()
    last = 0
    rank = 0
    alice_ranks = []
    for s in scores:
        if s != last:
            rank += 1
            score_rank[s] = rank
            last = s
    for ali in alice:
        if ali in score_rank.keys():
            # we have a score rank
            alice_ranks.append(score_rank[ali])
            continue
        else:
            scores.append(ali)
            scores.sort(reverse=True)
            rank = 0
            last = 0
            for s in scores:
                if s != last:
                    rank += 1
                    score_rank[s] = rank
                    last = s
            alice_ranks.append(score_rank[ali])

    return alice_ranks

def climbingLeaderboard(scores, alice):
    score_rank = [0]*len(scores)
    score_rank[0] = 1
    alice_ranks = []
    for i in range(1, len(scores)):
        if scores[i] == scores[i-1]:
            score_rank[i] = score_rank[i-1]
        else:
            score_rank[i] = score_rank[i-1] + 1

    for ali in alice:
        if ali > scores[0]:
            alice_ranks.append(1)
            continue
        elif ali < scores[len(scores) - 1]:
            alice_ranks.append(score_rank[len(scores) - 1] + 1)
            continue
        p = binarySearch2(scores, ali)
        alice_ranks.append(score_rank[p])

    return alice_ranks


if __name__ == "__main__":

    scores = [100, 90, 90, 80, 75, 60]
    alice = [50, 65, 77, 90, 102]

    print(climbingLeaderboard(scores, alice))

    scores = [100, 100, 50, 40, 40, 20, 10]
    alice = [5, 25, 50, 120]

    print(climbingLeaderboard(scores, alice))

    scores = [100, 100, 50, 40, 40, 20, 10]
    alice = [5, 25, 41, 42, 43, 50, 120]

    print(climbingLeaderboard(scores, alice))

    scores = [random.randint(1, 9999999) for _ in range(100000)]
    scores.sort(reverse=True)
    alice = [random.randint(1, 9999999) for _ in range(100)]
    alice.sort(reverse=True)

    print(climbingLeaderboard(scores, alice))
