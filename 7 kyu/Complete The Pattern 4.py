def pattern(n):
    res=""
    for i in range(n):
        for j in range(n-i):
            res+=str(i+j+1)
        res+="\n"
    return res[:-1]