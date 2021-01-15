from math import gcd
def sum_mult_triangnum(n, m):
    res=[]
    multiple=0
    for i in range(n):
        res.append(1) if not res else res.append(res[-1]+i+1)
        multiple=1 if multiple==0 else lcm(res[-1], multiple)
    return m * (m + 1) // 2 * multiple
def lcm(a,b):
    return a*b//gcd(a, b)