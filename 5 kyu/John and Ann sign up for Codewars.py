from functools import lru_cache
@lru_cache(maxsize=None)
def helper1(n):
    if n==0:
        return 0
    return n-helper2(helper1(n-1))
@lru_cache(maxsize=None)
def helper2(n):
    if n==0:
        return 1
    return n-helper1(helper2(n-1))
def john(n):
    return [helper1(i) for i in range(n)]

def ann(n):
    return [helper2(i) for i in range(n)]
    
def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))