from functools import reduce
def eq_dice(set_):
    product=reduce(lambda x, y: x*y, set_)
    res=helper(product, [], set())
    return len(res)-1 if (tuple(sorted(set_)) in res) else len(res)
def factors(n):
    res=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    res.add(n)
    return res
def helper(n, cur, memo):
    if n<3:
        if n==1 and len(cur)>1:
            memo.add(tuple(sorted(cur)))
        return 
    res=[i for i in factors(n) if 3<=i<=20]
    for i in res:
        helper(n//i, cur+[i], memo)
    return memo