def my_crib(n):
    res=[]
    for i in range(n+1):
        res.append(" "*(n-i)+"/"+" "*(i*2)+"\\"+" "*(n-i)) if i!=n else res.append("/"+"_"*(i*2)+"\\")
    for i in range(n):
        res.append("|"+" "*(n*2)+"|") if i!=(n-1) else  res.append("|"+"_"*(n*2)+"|")
    return "\n".join(res)

