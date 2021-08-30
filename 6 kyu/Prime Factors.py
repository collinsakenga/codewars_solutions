def prime_factors(n):
    res=[]
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            res.append(factor)
            n//=factor
            factor=2
        else:
            factor+=1
    return res if n==1 else res+[n]