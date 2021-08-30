def pattern(n):
    if n<=1: return ""
    res=""
    for i in range(1,n//2+1):
        res+=str(i*2)*(i*2)+"\n"
    return res[:-1]