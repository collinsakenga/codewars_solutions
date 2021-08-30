def count_Kprimes(k, start, nd):
    numbers=[]
    for i in range(start, nd+1):
        if len(factorization(i))==k:
            numbers.append(i)
    return numbers
def factorization(n):
    res=[]
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            res.append(factor)
            n//=factor
            factor=2
        else:
            factor+=1
    res.append(n)
    return res
def puzzle(s):
    first, second, third=count_Kprimes(1, 2, s), count_Kprimes(3, 2, s), count_Kprimes(7, 2, s)
    target={(s-i):"" for i in third}
    total=0
    for i in second:
        for j in first:
            if (i+j) in target:
                total+=1
    return total