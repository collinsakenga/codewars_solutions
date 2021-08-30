from copy import deepcopy
import itertools
def locate(seq, value): 
    res=deepcopy(list(seq))
    while True:
        flag=True
        for i,j in enumerate(res):
            if not (isinstance(j, list)):
                res[i]=[j]
            else:
                flag=False
        res=list(itertools.chain.from_iterable(res))
        if flag:
            break
    return value in res