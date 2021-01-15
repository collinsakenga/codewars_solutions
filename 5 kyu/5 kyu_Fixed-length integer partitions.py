def indices(n, d):
    return sorted([list(i) for i in helper(n, d) if len(i)==n and sum(i)==d], reverse=True)
def helper(n, d, arr=[], res=set()):
    if n==0:
        if d==0: 
            res.add(tuple(arr))
        return
    for i in range(d+1):
        if i<=d:
            helper(n-1, d-i, arr+[i], res)
    return res