from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    return n if n<=1 else fib(n-1)+fib(n-2)
def f(n):
    return fib(n+2)-1
    
    