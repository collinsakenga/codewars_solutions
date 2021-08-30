def pattern(n):
    res=""
    for i in range(1,n+1):
        res+=str(i)*i+"\n"
    return res[:-1]