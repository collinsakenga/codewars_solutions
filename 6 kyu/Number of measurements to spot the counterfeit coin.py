from math import log
def how_many_measurements(n):
    if n<=1:
        return 0
    return int(log(n, 3)) if log(n, 3)==int(log(n, 3)) else int(log(n, 3))+1