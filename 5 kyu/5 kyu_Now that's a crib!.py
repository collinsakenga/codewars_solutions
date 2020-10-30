def my_crib(n):
    res = [" "*(2*n)+"_"*(2*n+1)+" "*(2*n)]
    for i in range(n*2):
        res.append(" "*(n*2-1-i)+"/"+"_"*(2*n+1+i*2)+"\\"+" "*(n*2-1-i))
    for i in range(n-1):
        res.append("|"+" "*(6*n-1)+"|")
    res.append("|"+" "*(2*n)+"_"*(2*n-1)+" "*(2*n)+"|")
    for i in range(n-1):
        res.append("|"+"|".join([" "*(2*n-1)]*3)+"|")
    res.append("|"+"|".join(["_"*(2*n-1)]*3)+"|")
    return "\n".join(res)