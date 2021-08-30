def as_sum_of_powers_of_3(n):
    if n==0:
        return "0"
    res=[]
    num=n
    n=abs(n)
    while n:
        n, r = divmod(n, 3)
        res.append(r)
    for i,j in enumerate(res):
        if j>=2:
            res[i]-=3
            if i==len(res)-1:
                res.append(1)
            else:
                res[i+1]+=1        
    if num>0:
        return "".join(["-","0","+"][i+1] for i in res)
    return "".join(["+","0","-"][i+1] for i in res)