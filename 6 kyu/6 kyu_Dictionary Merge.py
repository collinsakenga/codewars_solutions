def merge(*dicts):
    res={}
    for i in dicts:
        for j,k in i.items():
            if not res.get(j, None):
                res[j]=[k]
            else:
                res[j].append(k)
    return res