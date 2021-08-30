from collections import Counter
from math import ceil, log
def memo():
    dict={(1, 1, 1):Counter("1")}
    length=1
    for i in range(2, 201):
        for j in range(1, i+1):
            res=""
            length=0
            for k in range(j, i+1):
                temp=str(k)
                res+=temp
                length+=len(temp)
            dict[(j, i, length)]=Counter(res)
    return dict
res=memo()
def mystery_range(s,n):
    check={i:j for i,j in res.items() if i[-1]==len(s)}
    comp=Counter(s)
    final=[[i[0], i[1]] for i,j in check.items() if (i[1]-i[0]+1)==n and j==comp]
    if len(final)==1:
        return final[0]
    length=max(ceil(log(i[1], 10)) for i in final)
    upper=max(int(s[i:i+length]) for i in range(0, len(s), length))
    return next(i for i in final if i[1]==upper) 