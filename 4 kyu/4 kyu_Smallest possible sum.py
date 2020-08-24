from math import gcd


def solution(a):
    if len(set(a)) == 1:
        return a[0]*len(a)
    rec = gcd(a[0], a[1])
    for i in range(1, len(a)-1):
        rec = gcd(rec, a[i+1])
        if rec == 1:
            return len(a)
    return rec*len(a)
