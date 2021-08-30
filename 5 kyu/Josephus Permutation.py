def josephus(items,k):
    count=k
    result=[]
    while len(items)!=0:
        while count>len(items):
            count-=len(items)
        result.append(items[(count-1)])     
        del items[(count-1)]
        count+=k-1
    return result