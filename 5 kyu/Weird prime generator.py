from math import gcd
def count_ones(n):  
    res=[7]
    for i in range(2, n+1):
        res.append(res[-1]+ gcd(res[-1], i))
    pairs=[res[i]-res[i-1] for i in range(1, len(res))]
    return pairs.count(1)+1
def max_pn(n):
    res=[7]
    i=2
    diff=set()
    while len(diff)<n:
        res.append(res[-1]+ gcd(res[-1], i))
        i+=1
        if (res[-1]-res[-2])!=1:
            diff.add(res[-1]-res[-2])
    return max(diff)
def an_over_average(n):
    return 3