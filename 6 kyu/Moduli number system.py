from functools import reduce
from math import gcd
def common(l):
    for i,j in enumerate(l):
        for k in range(i+1, len(l)):
            if gcd(j, l[k])>1:
                return True
    return False
def fromNb2Str(n, modsys):
    if reduce(lambda x, y: x*y, modsys)<=n or common(modsys):
        return "Not applicable"
    return "-"+"--".join(str(n%i) for i in modsys)+"-"
