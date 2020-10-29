def pair_of_shoes(shoes):
    res={}
    if len(shoes)%2:
        return False
    for i in shoes:
        if not res.get(i[1], None):
            res[i[1]]=[i[0]]
        else:
            res[i[1]].append(i[0])
    return not any(v.count(0)!=v.count(1) for v in res.values())