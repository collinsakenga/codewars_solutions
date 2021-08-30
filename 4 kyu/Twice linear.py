def dbl_linear(n):
    res = [1]
    x = 0
    y = 0
    while len(res) <= n:
        if res[x]*2+1 < res[y]*3+1:
            res.append(res[x]*2+1)
            x += 1
        elif res[y]*3+1 < res[x]*2+1:
            res.append(res[y]*3+1)
            y += 1
        else:
            x += 1
    return res[n]