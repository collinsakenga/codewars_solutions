def trailing_zeros(number, base):
    temp=prime_factorization(base)
    res=float("inf")
    for i,j in temp.items():
        num=number
        total=0
        key=i
        while num>=key:
            total+=num//key
            num//=key
        res=min(total//j, res)
    return res
def prime_factorization(n):
    res={}
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            n//=factor
            res[factor]=res.get(factor, 0)+1
            factor=2
        else:
            factor+=1
    res[n]=res.get(n, 0)+1
    return res