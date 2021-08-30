def padovan(n):
    res=[1,1,1]
    for i in range(n-2):
        res.append(res[-2]+res[-3])
    return res[n]