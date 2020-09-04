from math import gcd


def lcm(n, m):
    return n*m//gcd(n, m)


def nbr_of_laps(x, y):
    return (lcm(x, y)//x, lcm(x, y)//y)
