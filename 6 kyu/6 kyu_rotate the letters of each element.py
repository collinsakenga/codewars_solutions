def group_cities(seq): 
    res=[]
    for i in seq:
        if not res:
            res.append([i])
            continue
        temp1=i.lower()
        flag=False
        for index,j in enumerate(res):   
            if len(i)!=len(j[0]):
                continue
            temp2=j[0].lower()
            for k in range(len(i)):
                temp2=temp2[1:]+temp2[0]
                if temp2==temp1:
                    flag=True
                    res[index].append(i)
                    break
            if flag:
                break
        if not flag:
            res.append([i])
    res=[sorted(set(i)) for i in res]
    result=sorted(res, key=lambda x: (-len(x), x[0]))
    return result