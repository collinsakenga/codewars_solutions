def recycle(a):
    res = {"paper": [], "glass": [], "organic": [], "plastic": []}
    for i in a:
        for k, v in i.items():
            if k != "type":
                res[v].append(i["type"])
    return tuple(v for v in res.values())