from itertools import cycle
def max_hexagon_beam(n: int,seq: tuple):
    res=[[0]*(n*2-1) for _ in range(n*2-1)]
    rotate=cycle(seq)
    for i in range(n):
        for j in range(n+i):
            res[i][n-1-i+j]=next(rotate)
    for i in range(n-1):
        for j in range(n*2-2-i):
            res[n+i][j]=next(rotate)
    m1=max(sum(i) for i in res)
    m2=max(sum(res[j][i] for j in range(len(res[j]))) for i in range(len(res)))
    m3=max(sum(res[j][i-j] for j in range(i+1)) for i in range(n-1, len(res)))
    m4=max(sum(res[i+j][len(res)-1-j] for j in range(len(res)-i)) for i in range(1, n))
    return max(m1, m2, m3, m4)