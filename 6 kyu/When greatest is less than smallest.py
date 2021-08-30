from math import gcd
def greatest(x, y, n):
    num=lcm(x, y)*(n//lcm(x, y))
    return 0 if num==n else num
    
def smallest(x, y, n):
    return lcm(x, y)*(n//lcm(x, y)+1)
    
def lcm(n, m):
    return n*m//gcd(n, m)