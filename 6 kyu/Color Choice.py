from math import factorial
def checkchoose(m, n):
    if m==1:
        return 0
    start=1
    up=factorial(n)
    while start<n:
        down=factorial(start)*factorial(n-start)
        if up//down==m:
            return start
        start+=1
    return -1