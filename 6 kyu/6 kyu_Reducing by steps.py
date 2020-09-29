from math import gcd


def gcdi(a, b):
    return gcd(a, b)


def lcmu(a, b):
    return abs(a*b//gcd(a, b))


def som(a, b):
    return a+b


def maxi(a, b):
    return max(a, b)


def mini(a, b):
    return min(a, b)


def oper_array(fct, arr, init):
    res = [fct(arr[0], init)]
    for i in range(1, len(arr)):
        res.append(fct(arr[i], res[-1]))
    return res
