# Breaking records https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(scores):
    # Index 0 is for breaking most points records,
    # and index 1 is for breaking least points records.

    # init records with first score
    records = scores[:1]*2
    broken = [0]*2

    for score in scores[1:]:
        # loop without first score
        if score > records[0]:
            records[0] = score
            broken[0] += 1
        if score < records[1]:
            records[1] = score
            broken[1] += 1

    return 


if __name__ == "__main__":

    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    print(breakingRecords(scores))

    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    print(breakingRecords(scores))
