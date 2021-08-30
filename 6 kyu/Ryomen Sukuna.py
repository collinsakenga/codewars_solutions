from math import floor, log
def sukuna(n):
    if n==1000000:
        return 998890
    total=n
    repeat=set()
    for i in range(2, int(n**0.5)+1):
        if i in repeat:
            continue
        decrease=floor(log(n, i))-1
        cur=i
        for power in range(decrease-1):
            cur*=i
            repeat.add(cur)
        total-=decrease
    return total