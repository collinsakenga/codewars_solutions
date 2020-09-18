def finance(n):
    start = 0
    total = 0
    for i in range(1, n+1):
        start = start+i*3
        total += start
    return total
