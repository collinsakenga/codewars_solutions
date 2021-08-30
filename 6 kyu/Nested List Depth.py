import itertools
def list_depth(l):
    total=1
    while True:
        flag=True
        for i,j in enumerate(l):
            if isinstance(j, list):
                flag=False
            else:
                l[i]=[j]
        if flag:
            break
        l=list(itertools.chain.from_iterable(l))
        total+=1
    return total