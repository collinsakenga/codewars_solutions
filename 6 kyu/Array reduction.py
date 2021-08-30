def solve(n):
    res=[i for i in range(2, n+1)]
    remain=1
    while res[0]<len(res):
        remain+=res[0]
        res=[j for i,j in enumerate(res) if i%res[0]!=0]
    return sum(res)+remain