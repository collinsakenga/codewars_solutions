def josephus_survivor(n,k):
    count=k
    result=[]
    comp=[k for k in range(1,n+1)]
    while len(comp)!=1:
        while count>len(comp):
            count-=len(comp)
        result.append(comp[(count-1)])     
        del comp[(count-1)]
        count+=k-1
    return comp[0]