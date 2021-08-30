def pattern(n):
    if n==0:
        return ""
    res=[] 
    for i in range(n-1):
        res.append(" "*(n-1)+str((i+1)%10))
    temp="".join(str(i%10) for i in range(1, n))
    res.append(temp+str(n%10)+temp[::-1])
    for i in range(n-1, 0, -1):
        res.append(" "*(n-1)+str(i%10))
    return "\n".join(res)+"\n"