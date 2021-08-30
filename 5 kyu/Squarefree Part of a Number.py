from collections import Counter
def square_free_part(n):
    if n==True or not isinstance(n, int) or n<=0:
        return None
    for i in factors(n)[::-1]:
        if Counter(factorization(i)).most_common()[0][1]==1:
            return i
def factors(n):
    res={1, n}
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    return sorted(res)
def factorization(n):
    factor=2
    res=[]
    while factor*factor<=n:
        if n%factor==0:
            n//=factor
            res.append(factor)
            factor=2
        else:
            factor+=1
    res.append(n)
    return res