from math import gcd
from itertools import combinations


def proper_fractions(n):
    res = prime(n)
    if not res:
        return n-1
    temp = res.copy()
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if res[j] % res[i] == 0:
                temp[j] = 0
    temp = [i for i in temp if i != 0]
    common = 0
    for i in temp:
        common += n//i
    index = 2
    while index < len(temp)+1:
        final = combinations(temp, index)
        for i in final:
            flag = lcm(i[1], i[0])
            for j in range(2, len(i)):
                flag = lcm(flag, i[j])
            common += n//flag if index % 2 == 1 else -n//flag
        index += 1
    return n-common


def prime(n):
    res = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            if i == n//i:
                continue
            res.append(n//i)
    return res


def lcm(n, m):
    return n*m//gcd(n, m)
