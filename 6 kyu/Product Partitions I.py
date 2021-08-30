def prod_int_part(n):
    res=helper(n, [], set())
    return [len(res), [] if not res else list(res[0])]
def factorization(n):
    res=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    res.add(n)
    return sorted(res)
def helper(n, cur, memo):
    if n==1:
        if len(cur)>1:
            memo.add(tuple(sorted(cur)))
        return
    res=factorization(n)
    for i in res: 
        helper(n//i, cur+[i], memo)
    return sorted(memo, key=lambda x: -len(x))