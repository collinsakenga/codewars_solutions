from decimal import *
getcontext().prec = 50000
def memo():
    start=Decimal(0)
    end=Decimal(1)
    count=0
    res=[start, end]
    while count<100000:
        start, end=end, (end+start)/2
        res.append(end)
        count+=1
    return res
res=memo()
def count_sixes(n):
    return next(i for i,j in enumerate(str(res[n])[2:]) if j!="6")