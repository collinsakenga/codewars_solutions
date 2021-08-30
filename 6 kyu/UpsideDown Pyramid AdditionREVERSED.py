def reverse(right):
    res=[]
    for i,j in enumerate(right):
        res.append([j])
        for k in range(i):
            res[i].append(res[i-1][k]-res[i][k])        
    return res[-1][::-1]