from collections import Counter
def f(n):
    total=1
    for i,j in factorization(n).items():
        total*=j*i**(j-1)
    return total
def factorization(n):
    res=Counter()
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            res[factor]+=1
            n//=factor
            factor=2
        else:
            factor+=1
    res[n]+=1
    return res