def GCD(*args):
    res={}
    for i in args:
        factors=[(j, i//j) for j in range(1, int(i**0.5)+1) if i%j==0]
        res[i]={k for j in factors for k in j}
    possible={j for i in res.values() for j in i}
    return max(i for i in possible if all(i in j for j in res.values()))