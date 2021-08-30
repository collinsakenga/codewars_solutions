def sol_equa(n):
    rec=factors(n)
    res=[]
    for i in rec:
        check=sum(i)
        if check%2==0:
            x, y=check//2, (check//2-i[0])//2
            if (x - 2*y) * (x + 2*y) == n:
                res.append([x, y])
    return res
def factors(n):
    results = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            results.append([i,n//i])
    return results