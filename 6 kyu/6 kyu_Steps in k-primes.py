def kprimes_step(k, step, start, nd):
    primes=[i for i in range(start, nd+1) if factorization(i)==k]
    pairs={i:-1 for i in primes}
    return [[i, i+step] for i in primes if pairs.get(i+step, None)]
def factorization(n):
    count=1
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            count+=1
            n//=factor
            factor=2
        else:
            factor+=1
    return count