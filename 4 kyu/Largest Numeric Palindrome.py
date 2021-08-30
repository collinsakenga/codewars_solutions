from itertools import combinations
from functools import reduce
from collections import Counter
def numeric_palindrome(*args):
    res=[i for i in args if i>1]
    if not res:
        return 1 if args.count(1)>1 else 0
    elif 1 in args:
        res+=[1]
    total=0
    for i in range(len(res), 1, -1):
        for j in combinations(res, i):
            product=reduce(lambda x, y: x*y, j)
            total=max(total, helper(Counter(str(product))))
    return total
def helper(count):
    center=""
    palin=[]
    for i,j in count.items():
        if (j%2==1) and (not center or i>center):
            center=i
        palin.extend([i]*(j//2))
    ans="".join(sorted(palin, reverse=True))
    return int(center) if ans.startswith("0") else int(ans+center+ans[::-1])