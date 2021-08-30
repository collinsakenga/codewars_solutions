def consec_kprimes(k, arr):
    return sum(k==factorization(arr[i])==factorization(arr[i-1]) for i in range(1, len(arr)))
def factorization(n):
    length=1
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            length+=1
            n//=factor
            factor=2
        else:
            factor+=1
    return length