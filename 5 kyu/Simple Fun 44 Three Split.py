def three_split(seq):
    target=sum(seq)/3
    cur=None
    res=[]
    for index,i in enumerate(seq):
        if cur==None:
            cur=i
        else:
            cur+=i
        if cur==target:
            res.append((seq[:index+1], index+1))
    res2=[]
    for i,j in res:
        cur=None
        for k,l in enumerate(seq[j:]):
            if cur==None:
                cur=l
            else:
                cur+=l
            if cur==target:
                res2.append(j+k+1)
    return sum(sum(seq[j:])==target for j in res2 if j!=len(seq))