from heapq import *
def flip(d, a):
    if d in "LR":
        return [sorted(i, reverse=d=="L") for i in a]
    for j in range(len(a[0])):
        res=[-a[i][j] if d=="U" else a[i][j] for i in range(len(a))]
        heapify(res)
        for i in range(len(a)):
            a[i][j]=-heappop(res) if d=="U" else heappop(res)
    return a
            