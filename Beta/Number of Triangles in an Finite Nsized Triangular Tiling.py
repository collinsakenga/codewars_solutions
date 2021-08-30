# https://oeis.org/A002717
from math import floor
def solve(n):
    return floor(n*(n+2)*(2*n+1)//8)
