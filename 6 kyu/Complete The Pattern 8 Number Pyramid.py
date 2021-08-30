def pattern(n):
    if n<=0: return ""
    res=""
    for i in range(n):
        res+=" "*(n-1-i)
        for j in range(1,i+1):
            res+=str(j%10)
        for j in range(i+1,0,-1):
            res+=str(j%10)
        res+=" "*(n-1-i)
        res+="\n"
    return res[:-1]