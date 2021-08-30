def gangs(divisors,k):
    res=set()
    for i in range(1, k+1):
        res.add(helper(divisors, i))
    return len(res)
def helper(divisors, n):
    res=tuple()
    for i in divisors:
        if n%i==0:
            res+=(i, )
    return res