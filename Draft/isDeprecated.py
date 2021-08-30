from math import gcd
def count_pieces(n, m):
    return n+m-gcd(n, m)