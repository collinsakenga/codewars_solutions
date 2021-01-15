def bad_apples(apples):
    res=[]
    remain=[]
    indexes=[]
    index=0
    for i in apples:
        if i[0]==0 and i[1]==0:
            continue
        elif i[0]==0 or i[1]==0:
            remain.append(i[0]) if i[1]==0 else remain.append(i[1])
            indexes.append(index)
        index+=1
        res.append([i[0], i[1]])
    for i in range(len(remain)//2):
        if res[indexes[i*2]][0]==0: 
            res[indexes[i*2]][0]=remain[i*2] if remain[i*2]!=res[indexes[i*2]][1] else remain[i*2+1]
            res[indexes[i*2]][0], res[indexes[i*2]][1]=res[indexes[i*2]][1], res[indexes[i*2]][0]
        elif res[indexes[i*2]][1]==0:   
            res[indexes[i*2]][1]=remain[i*2] if remain[i*2]!=res[indexes[i*2]][0] else remain[i*2+1]
    return [i for i in res if (i[0]!=0 and i[1]!=0)]