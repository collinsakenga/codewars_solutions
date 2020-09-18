def strongest_even(n, m):
    power = 0
    temp = 2
    while temp**power < m:
        power += 1
    if temp**power <= m:
        return temp**power
    elif temp**(power-1) >= n:
        return temp**(power-1)
    res = temp**(power-1)
    times = 2
    power -= 2
    while True:
        check = res
        for i in range(1, times):
            check += temp**power
            if check >= n and check <= m:
                return check
        times *= 2
        power -= 1
