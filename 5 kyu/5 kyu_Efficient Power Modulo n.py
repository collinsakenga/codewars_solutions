from functools import reduce
def power_mod(x, y, n):
    if y<2:
        return x%n if y==1 else 1
    res=[]
    temp=None
    for i in bin(y)[2:][::-1]:
        temp=x%n if not temp else (temp**2)%n
        if i=="1":
            res.append(temp)
    return reduce(lambda x, y: x%n*y%n, res)