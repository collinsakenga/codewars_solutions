def how_many_times(a, b):
    if a==b:
        return a
    larger=max(a, b)
    smaller=min(a, b)
    return sum(smaller>=i for i in factors(larger-smaller))
def factors(n):
    res={1, n}
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    return sorted(res)