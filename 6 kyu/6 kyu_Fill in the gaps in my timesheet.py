def fill_gaps(timesheet):
    res=[]
    temp=[]
    for i,j in enumerate(timesheet):
        res.append(None)
        if j!=None:
            temp.append([i, j])
            if len(temp)>=2:
                if temp[-2][1]==temp[-1][1]:
                    for k in range(temp[-2][0], i+1):
                        res[k]=j
                else:
                    res[temp[-2][0]]=temp[-2][1]
                    res[temp[-1][0]]=temp[-1][1]
    if len(temp)==1:
        res[temp[-1][0]]=temp[-1][1]
    return res