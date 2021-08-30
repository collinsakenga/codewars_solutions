res=[0,1]
for i in range(3, 8000001):
    res.append(((i-1)*((res[-1]+res[-2])))%1000000007)
def solve(n):
    return res[n-1]