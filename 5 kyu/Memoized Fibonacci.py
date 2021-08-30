def fibonacci(n, res=[0,1]):
    if len(res)<=n:
        res.append(fibonacci(n-1)+fibonacci(n-2))
    return res[n]