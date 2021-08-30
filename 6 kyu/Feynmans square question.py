def count_squares(n):
    total=1
    for i in range(2, n+1):
        total+=i**2
    return total