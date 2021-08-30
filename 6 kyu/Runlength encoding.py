def run_length_encoding(s):
    res=[]
    index=0
    for i in s:
        if not res:
            res.append([1, i])
        elif res[index][1]==i:
            res[index][0]+=1
        else:
            res.append([1, i])
            index+=1
    return res