from itertools import accumulate
def s(m, n):
    if not m:
        return 1
    num=n
    for i in range(1, m):
        num*=(n+i)
        num//=i+1
    return num
    