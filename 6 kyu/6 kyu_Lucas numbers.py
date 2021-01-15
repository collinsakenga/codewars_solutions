def lucasnum(n):
    num=abs(n)
    res=[2, 1]
    for i in range(2, num+1):
        res.append(res[-1]+res[-2])
    return res[num]*(-1 if (n<0 and n%2) else 1)