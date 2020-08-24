from math import sqrt, log, floor


def isPP(n):
    logx = 2
    max = floor(sqrt(n))+1
    comp = floor(log(n, logx))+1
    while True:
        for i in range(logx, max):
            for j in range(2, comp):
                if i**j == n:
                    return [i, j]
        if comp == 2:
            return None
        logx += 1
        max = floor(n**(1/logx))+1
        comp = floor(log(n, logx))+1
