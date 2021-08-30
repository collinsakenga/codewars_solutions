def pattern(n):
    res=""
    for i in range(n,0,-1):
        for j in range(i):
            res+=str(n-j)
        res+="\n"
    return res[:-1]