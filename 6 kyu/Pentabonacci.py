def count_odd_pentaFib(n):
    res=[0, 1, 1, 2, 4]
    for i in range(n-4):
        res.append(sum(res[-5:]))
    return n if n<=1 else sum(1 for i in res if i%2)-1