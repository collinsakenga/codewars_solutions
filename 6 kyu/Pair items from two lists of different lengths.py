from itertools import combinations
def pair_items(iter1, iter2):
    if len(iter1)==0 or len(iter2)==0:
        return [[]]
    res=[]
    low=iter1 if len(iter1)<=len(iter2) else iter2
    high=iter2 if len(iter2)>=len(iter1) else iter1
    first=low==iter1
    for i in combinations(high, len(low)):
        arr=[]
        for index,j in enumerate(i):
            arr.append((j, low[index]) if not first else (low[index], j))
        res.append(arr)
    return res