from collections import Counter
from math import gcd
def has_subpattern(string):
    check=Counter(string)
    most=check.most_common()[0][1]
    least=check.most_common()[-1][1]
    if most==least:
        return "".join(sorted(k for k in check.keys()))
    factors=set()
    for v in check.values():
        factors.add(v)
    factors=list(factors)
    for i in range(1, len(factors)):
        factors[i]=gcd(factors[i], factors[i-1])
    if factors[-1]==1:
        return "".join(sorted(string))
    return "".join(sorted(k*(v//factors[-1]) for k,v in check.items()))