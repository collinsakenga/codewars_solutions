def modified_sum(a, n):
    total = 0
    for i in range(len(a)):
        total += a[i]**n
        total -= a[i]
    return total
