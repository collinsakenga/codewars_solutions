def unpack_sausages(truck):
    res=[]
    count=0
    for i in truck:
        for j in i:
            if len(j)!=6 or j[0]!="[" or j[-1]!="]":
                continue
            if len(set(j[1:-1]))==1:
                count+=1
                if count%5:
                    res.extend([i for i in j[1:-1]])
    return " ".join(res)