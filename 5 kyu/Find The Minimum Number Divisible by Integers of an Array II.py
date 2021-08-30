from collections import Counter
from functools import reduce
def min_special_mult(arr):
    arr2=[i for i in arr if i!=None]
    invalid=[]
    for i in arr2:
        try:
            int(i)
        except:
            invalid.append(i)
    if invalid:
        if len(invalid)>1:
            return f"There are {len(invalid)} invalid entries: {str(invalid)}" 
        return f"There is 1 invalid entry: {invalid[0]}"
    num=set(arr2)
    total={}
    for i in num:
        temp=None
        if not isinstance(i, int):
            try:
                temp=factorization(abs(int(i)))
            except:
                continue
        else:
            temp=factorization(abs(i))
        for k,l in temp.items():
            if not total.get(k, None) or l>total[k]:
                total[k]=l
    largest=1
    for i,j in total.items():
        largest*=i**j
    return largest
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
    return Counter(res)