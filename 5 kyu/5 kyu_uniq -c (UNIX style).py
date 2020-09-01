def uniq_c(seq):
    res = []
    comp = {}
    index = 0
    for i in seq:
        if comp.get(i, 0) == 0:
            res.append([i, 1])
            if comp and res:
                index += 1
                comp.clear()
            comp[i] = 1
        else:
            res[index][1] += 1
            comp[i] += 1
    return [tuple(i) for i in res]
