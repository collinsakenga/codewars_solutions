def triangle_type(a, b, c):
    res=[a, b, c]
    if max(res)>=sum(res)-max(res):
        return 0
    return 1 if sum(j**2 for i,j in enumerate(res) if i!=res.index(max(res)))>max(res)**2 else 2 if sum(j**2 for i,j in enumerate(res) if i!=res.index(max(res)))==max(res)**2 else 3
