def binarray(s)->int:
    table={}
    table[0]=-1
    res=cur=0
    for i,j in enumerate(s):
        cur+=1 if j==0 else -1
        if cur in table:
            res=max(res, i-table[cur])
        else:
            table[cur]=i
    return res