def group_in_10s(*args):
    if not args:
        return []
    args=sorted(args)
    res=[None]*(max(args)//10+1)
    temp=[]
    for i in args:
        temp.append(i)
        if not res[i//10]:
            res[i//10]=[temp[-1]]
        else:
            res[i//10].append(temp[-1])
    return res