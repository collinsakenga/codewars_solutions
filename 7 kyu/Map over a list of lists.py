def grid_map(inp, op):
    res=[]
    for i in inp:
        temp=[]
        for j in i:
            temp.append(op(j))
        res.append(temp)
    return res