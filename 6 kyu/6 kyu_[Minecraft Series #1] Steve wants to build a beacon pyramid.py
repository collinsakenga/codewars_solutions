def blocks_to_collect(level):
    res=[0,0,0,0]
    base=3
    for i in range(level):
        res[i%4]+=base**2
        base+=2
    return {"total": sum(res), "gold": res[0], "diamond": res[1], "emerald": res[2], "iron": res[3]}