from math import log
def sequence(n):
    if n<=7:
        return [0,1,3,4,9,10,12,13][n]
    num=8
    increment=8
    while num+increment<=n:
        num+=increment
        increment*=2
    return int("1"+bin(n-num)[2:].rjust(int(log(increment, 2)), "0"), 3)