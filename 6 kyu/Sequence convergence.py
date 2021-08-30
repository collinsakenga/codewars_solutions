from functools import reduce
from itertools import count
def memo():
    res=[1,2,4,8,16]
    for i in range(10000):
        res.append(res[-1]+reduce(lambda x, y: x*y, [int(j) for j in str(res[-1]) if j !="0"]))
    return set(res)
check=memo()
def convergence(n):
    res=[n]
    for i in count():
        res.append(res[-1]*2) if res[-1]<10 else res.append(res[-1]+reduce(lambda x, y: x*y, [int(j) for j in str(res[-1]) if j !="0"]))
        if res[-1] in check:
            return i+1

    