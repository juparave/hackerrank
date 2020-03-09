# Drawing Book https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    """
    param n: the number of pages in the book
    param p: the page number to turn to
    """
    pages = [(i, i+1) for i in range(0, n+2, 2) if i <= n]

    for t, i in enumerate(pages):
        if p in i:
            break
    return min([t, len(pages)-(t+1)])


if __name__ == "__main__":
    
    print(pageCount(6, 2))
    print(pageCount(5 ,4))