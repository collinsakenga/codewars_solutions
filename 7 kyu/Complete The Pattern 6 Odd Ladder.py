def pattern(n):
    if n<=0: return ""
    res=""
    for i in range(1,(n+1)//2+1):
        res+=str(i*2-1)*(i*2-1)+"\n"
    return res[:-1]
        