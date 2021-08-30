from math import log
def count_nines(n):
    res=[]
    start=1
    for i in range(100):
        res.append(start*(10**i))
        start+=1
    power=int(log(n, 10))
    n=str(n)
    total=n[-1]=="9"
    while power:
        total+=res[power-1]*(int(n)//(10**power))
        total+=int(n[1:] or "0")+1 if n[0]=="9" else 0
        n=n[1:]
        power-=1
    return total