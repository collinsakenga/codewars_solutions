def a(n):
    if n<4:
        return ""
    n-=n%2
    res=[]
    for i in range(n):
        if not i:
            res.append(" "*(n-1)+"A"+" "*(n-1))
        elif i==n//2:
            res.append(" "*(n//2-1)+" ".join(["A"]*(n//2+1))+" "*(n//2-1))
        else:
            res.append(" "*(n-1-i)+"A"+" "*(i*2-1)+"A"+" "*(n-1-i))
    return "\n".join(res)