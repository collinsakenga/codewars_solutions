def boxes_packing(length, width, height):
    total=[sorted((i,j,k)) for i,j,k in zip(length, width, height)]
    res=sorted(total, key=lambda x: -min(x))
    for i,j in enumerate(res[1:]):
        if any((k-l)<=0 for k,l in zip(res[i], j)):
            return False 
    return True