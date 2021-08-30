res=[3,8]
for i in range(500000):
    res.append((2*(res[-1]+res[-2]))%1000000007)
def blind_number(n):
    return res[n-1]