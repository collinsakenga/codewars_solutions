def rule30(list_, n):
    res=[0]+list_+[0]
    for i in range(n):
        temp=res[:]
        for j,k in enumerate(res):
            if j==0:
                res[j]=(k or temp[j+1])
            elif j==len(temp)-1:
                res[j]=temp[j-1]^(k)
            else:
                res[j]=temp[j-1]^(k or temp[j+1])
        res=[0]+res+[0]
    return res[1:-1] 