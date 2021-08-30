def Zeckendorf_rep(n):
    if n<0:
        return None
    res=[1, 1]
    while res[-1]<n:
        res.append(res[-1]+res[-2])
    arr=[]
    num=n
    for i in res[::-1]:
        if num==0:
            break
        elif num>=i:
            arr.append(i)
            num-=i
    return arr