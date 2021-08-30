def stairs(n):
    res=[]
    s=["1"]
    for i in range(n):
        res.append(" "*((n-i-1)*4)+" ".join(s+s[::-1]))
        s.append(str((i+2)%10))
    return "\n".join(res)
        