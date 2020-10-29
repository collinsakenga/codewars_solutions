def shortest_to_char(s, c):
    if not s or not c:
        return []
    check=[i for i,j in enumerate(s) if j==c]
    if not check:
        return []
    index=0
    res=[]
    for i,j in enumerate(s):
        if index==0:
            res.append(check[index]-i)
        else:
            res.append(min(check[index]-i, i-check[index-1]))
        if check[index]==i:
            index+=1
        if index==len(check):
            break
    for i in range(1, len(s)-check[-1]):
        res.append(i)
    return res