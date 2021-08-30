res=[0,1]
for i in range(100000):
    res.append(res[-1]+res[-2])
def fib(n):
    return res[n-1]