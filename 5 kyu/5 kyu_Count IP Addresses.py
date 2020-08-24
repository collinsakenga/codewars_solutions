def ips_between(start, end):
    temp1 = start.split(".")
    temp2 = end.split(".")
    total = 0
    pow = 3
    for i in range(0, len(temp1)):
        total += (int(temp2[i])-int(temp1[i]))*(256**pow)
        pow -= 1
    return total
