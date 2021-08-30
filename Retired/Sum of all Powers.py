def product(n):
    return 1 if n==0 else n**n+product(n-1)