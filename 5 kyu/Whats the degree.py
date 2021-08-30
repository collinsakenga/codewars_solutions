from math import log
def degree(p):
    res=[p(2**19), p(2**20)]
    if res[0]==res[1]:
        return 0
    return round(log(res[1]/res[0], 2))