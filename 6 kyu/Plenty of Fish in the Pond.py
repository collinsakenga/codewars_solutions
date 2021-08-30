def fish(shoal):
    res=1
    xp=0
    limit=8
    total=4
    for i in "".join(sorted(shoal)):
        if i=="0" or res<int(i):
            continue
        xp+=int(i)
        if xp>=total:
            total+=limit
            limit+=4
            res+=1
    return res
        
        