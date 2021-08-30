def pattern(n):
    if n<=0: return ""
    res=""
    for i in range(n):
        if (i+1)!=n:
            res+=" "*i+str((i+1)%10)+" "*((n-1-i)*2-1)+str((i+1)%10)+" "*i+"\n"
        else: 
            res+=" "*i+str((i+1)%10)+" "*i+"\n"   
    for i in range(n-2,-1,-1):
        res+=" "*i+str((i+1)%10)+" "*((n-1-i)*2-1)+str((i+1)%10)+" "*i+"\n"
    return res[:-1]