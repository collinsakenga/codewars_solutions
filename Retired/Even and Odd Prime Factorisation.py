def even_odd(n):
    return ["odd", "even"][helper(n)%2==0]
def helper(n):
    length=1
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            length+=1
            n//=factor
            factor=2
        else:
            factor+=1
    return length