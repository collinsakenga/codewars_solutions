def Guess_it(n,m):
    center=0
    res=[]
    flag=False
    while (n>0):
        if m//n>=5 or (m//n==3 and m%n==0):
            flag=True
            break
        center+=1
        m-=4
        n-=1
    left=0
    right=0
    if n:
        left=n if m//n>=5 else 0
        right=0 if m//n>=5 else n
    while center>=0:
        res.append([left, center, right])
        left+=1
        right+=1
        center-=2
    return res