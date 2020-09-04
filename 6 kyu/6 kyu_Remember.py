def remember(str):
    dict = {}
    res = []
    for i in str:
        dict[i] = dict.get(i, 0)+1
        if dict[i] >= 2 and i not in res:
            res.append(i)
    return res
