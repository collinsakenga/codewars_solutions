def advice(agents, n):
    agents={(i[0], i[1]) for i in agents if 0<=i[0]<n and 0<=i[1]<n}
    if n**2==len(agents):
        return []
    elif not agents:
        return [(i, j) for i in range(n) for j in range(n)]
    max_val=-1
    res=[]
    for i in range(n):
        for j in range(n):
            if (i,j) in agents:
                continue
            diff=float("inf")
            for k,l in agents: 
                diff=min(diff, distance(i, j, k, l))
                if diff<max_val: 
                    break 
            if diff>max_val:
                max_val=diff
                res=[(i, j)]  
            elif diff==max_val:
                res.append((i, j)) 
    return res
def distance(i, j, k, l):
    return abs(k-i)+abs(l-j)