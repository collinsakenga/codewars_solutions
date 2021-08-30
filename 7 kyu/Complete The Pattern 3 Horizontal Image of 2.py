def pattern(n):
    res=""
    for i in range(n):
        for j in range(i+1):
            res+=str(n-j)
        res+="\n"
    return res[:-1]