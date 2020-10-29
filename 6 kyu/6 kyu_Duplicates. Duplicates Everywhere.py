def remove_duplicate_ids(obj):
    data={k:v for k,v in sorted(obj.items(), key=lambda x: (-int(x[0])))}
    res={}
    dict={}
    for i,j in data.items():
        temp=[]
        for k in j:
            if not dict.get(k, None):
                dict[k]=1
                temp.append(k)
        res[i]=temp
    return {k:v for k,v in sorted(res.items(), key=lambda x: (int(x[0])))}