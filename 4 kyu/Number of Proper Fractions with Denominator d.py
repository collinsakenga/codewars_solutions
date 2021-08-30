def proper_fractions(n):
    res=n
    factor=set()
    i=2
    while i*i<=n:
        if n%i!=0:
            i+=1
        else:            
            factor.add(i)
            n//=i
    if not factor: return res-1
    if n>1: factor.add(n)
    for i in factor:
        res=res*(i-1)//i
    return res