def odd_row(n):
    start=1
    res=[]
    for i in range(1, n):
        start+=2*i
    for i in range(n):
        res.append(start+2*i)
    return res