import math
def iter_pi(epsilon):
    down=1
    res=0
    count=0
    while abs(res*4-math.pi)>epsilon:
        if count%2==0:
            res+=1/down
        else:
            res-=1/down
        count+=1
        down+=2
    return [count, round(res*4,10)]