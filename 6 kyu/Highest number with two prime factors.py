from math import log, ceil
def highest_biPrimefac (p1, p2, n): # p1, p2 primes and p1 < p2
    comp=ceil(log(n, p1))
    comp2=0
    res=[0,0,0]
    while comp>=1:
        comp2=int(log((n/(p1**comp)), p2)+0.0000001)
        product=(p1**comp)*(p2**comp2)
        if comp2 and product>=res[0]:
            res=[product, comp, comp2]
        comp-=1      
    return res
