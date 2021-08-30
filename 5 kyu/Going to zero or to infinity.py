memo=[]
from math import floor
def going(n):
    if len(memo)<=n:
        temp=1
        for i in range(1,50000):
            temp*=i
            memo.append(temp)
    res=sum(memo[:n])/memo[n-1]
    if len(str(res))<=8:
        return res
    return round_down(6,res)
def round_down(place,res):
    return floor(res*10**place)/(10**place*1.0)