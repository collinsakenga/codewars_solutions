from itertools import zip_longest
def ternary(a, c):
    res=[]
    for power,(i, j) in enumerate(zip_longest(transform(a), transform(c), fillvalue=0)):
        res.append(str((j-i)%3))
    return int("".join(res[::-1]) or "0", 3)
def transform(n):
    res=[]
    while n:
        res.append(n%3)
        n//=3
    return res