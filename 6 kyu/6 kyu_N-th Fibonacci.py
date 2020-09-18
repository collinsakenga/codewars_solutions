def nth_fib(n):
    return fib(n-2) if n != 1 else 0


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fib(n-1)+fib(n-2)
