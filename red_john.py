# Red John is back

def sieve(n):
    A = [1]*(n+1)
    A[0], A[1] = 0, 0
    
    for i in range(2,n+1):
        if A[i] == 1:
            A[i*i::i] = [0 for k in A[i*i::i]]
            
    return [k for k in range(n+1) if A[k] == 1]
		

def f(n):
    # assert(n > 0)
    if n < 0:
        return 0
    if n < 4:
        return 1
    if n == 4:
        return 2
    return f(n-1) + f(n-4)

if __name__ == "__main__":
    for i in range(1, 10):
        print("N=", i, f(i))
