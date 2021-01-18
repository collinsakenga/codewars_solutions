def distance(n):
    check=1
    while check**2<n:
        check+=2
    temp=check-1
    power=(check-2)**2
    for _ in range(4):
        if n>=power and n<=power+temp:
            value=min(power+temp-n, n-power)
            break
        power+=temp
    return temp-value