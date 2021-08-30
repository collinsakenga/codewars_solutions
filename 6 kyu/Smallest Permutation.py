def min_permutation(n):
    if n==0:
        return n
    flag=True if n<0 else False
    n=str(abs(n))
    zeroes=["0"]*n.count("0")
    res=sorted([i for i in n if i!="0"], key=lambda x: x)
    return int(res[0]+"".join(zeroes)+"".join(res[1:]))*((1, -1)[flag])