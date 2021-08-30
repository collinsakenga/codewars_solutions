def equal(s):
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    return equal(s[1:-1])
def memo():
    first=int(50000000**0.5)
    palin=set()
    for i in range(first, 0, -1):
        total=i**2
        n=i-1
        while total<=100000000 and n>0:
            total+=n**2
            if equal(str(total)):
                palin.add(total)
            n-=1
    return sorted(palin)
res=memo()
def values(n):    
    return sum(n>=i for i in res)