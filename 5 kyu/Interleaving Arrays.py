def interleave(*args):
    temp=list(args)
    compare=0
    for i in temp:
        compare=max(compare,len(i))
    for i in temp:
        if compare>len(i):
            i.extend([None]*(compare-len(i)))
    result=[]
    for i in range(0,compare):
        for j in range(0,len(temp)):
            result.append(temp[j][i])      
    return result