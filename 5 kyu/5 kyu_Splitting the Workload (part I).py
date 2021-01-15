from itertools import combinations, product, permutations
from collections import Counter
def splitlist(lst):
    if len(lst)<=1:
        return ([], []) if len(lst)==0 else (lst, [])
    equals=Counter(lst)
    check=sum(lst)
    dict={}
    for i in range(1, len(lst)):
        for j in combinations(lst, i):
            if not dict.get(sum(j), None):
                dict[sum(j)]=[j]
            else:
                dict[sum(j)].append(j)
    diff=float("inf")
    res1, res2=[], []
    for i in dict.keys():
        if dict.get(check-i) and abs(i-(check-i))<diff:
            for j in permutations((dict[check-i]+dict[i]), 2):
                if Counter(j[0]+j[1])==equals:
                    diff=abs(i-(check-i))
                    res1=j[0]
                    res2=j[1]
                    break             
    return (res1, res2)