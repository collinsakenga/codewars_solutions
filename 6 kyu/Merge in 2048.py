def merge(line):
    index=0
    res=[]
    length=len(line)
    while index<length:
        if line[index]==0:
            index+=1
            continue
        if res and res[-1]==line[index]:
            res.pop()
            res.append(line[index]*2)
            if (index+1)<length:
                res.append(line[index+1])
            index+=2
        else:
            res.append(line[index])
            index+=1
    while 0 in res:
        res.remove(0)
    return res+[0]*(length-len(res))
