def halving_sum(n):
    divide = 2
    total = 0
    while n != 0:
        total += n
        n = int(n/divide)
    return total
