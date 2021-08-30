def ranks(a):
    if not a: return []
    dict={}
    for i in set(a):
        dict[i]=dict.get(i, 0)+a.count(i)
    temp=sorted(dict.items(), key=lambda x: -x[0])
    for i,j in enumerate(temp):
        temp[i]=list(j)
    dict.clear()
    count=0
    for i,j in enumerate(temp):
        if i==0:
            temp[i][1]=1
        else:
            temp[i][1]=count+1
        count+=a.count(j[0])
    for i in temp:
        dict[i[0]]=i[1]
    return [dict[i] for i in a]