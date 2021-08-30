from functools import lru_cache
def outcome(n, s, k):
    return helper(n, s, k)
def helper(n, s, k):
    if n>k or k<0:
        return 0
    elif n==0:
        return +(k==0)
    total=0
    for i in range(1, s+1):
        total+=helper(n-1, s, k-i)
    return total