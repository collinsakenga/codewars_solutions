from functools import lru_cache
@lru_cache
def fib(n):
    return n if n<2 else fib(n-1)+fib(n-2)
def sum_fibs(n):
    return sum(j for j in (fib(i) for i in range(n+1)) if j%2==0)