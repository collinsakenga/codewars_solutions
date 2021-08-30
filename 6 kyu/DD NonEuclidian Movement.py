def calc_distance(path):
    total=0
    for i,j in enumerate(path[1:]):
        prev, cur=path[i], j
        total+=max(abs(k-l) for k,l in zip(prev, cur))
    return total*5