def bacteria(n):
    total=0
    while n:
        n, remain=divmod(n, 2)
        total+=remain
    return total