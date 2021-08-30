from collections import deque
def pac_man(N, PM, enemies):
    if not enemies:
        return N**2-1
    memo=set()
    res=deque([(PM[0], PM[1])])
    total=-1
    limity=set(i[0] for i in enemies)
    limitx=set(i[1] for i in enemies)
    while res:
        y, x=res.popleft()
        if (y, x) in memo or y in limity or x in limitx:
            continue
        memo.add((y, x))
        total+=1
        for i,j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            y2, x2=y+i, x+j
            if 0<=y2<N and 0<=x2<N and y2 not in limity and x2 not in limitx and (y2, x2) not in memo:
                res.append((y2, x2))
    return max(total, 0)