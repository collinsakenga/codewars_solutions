def x(n):
    res=[[0]*n for i in range(n)]
    for i in range(n):
        res[i][i]=res[n-1-i][i]=1
    return res