from math import ceil
def has_two_cube_sums(n):
    if n<=1:
        return False
    length=ceil(n**(1/3))+1
    dict={i**3:i for i in range(length)}
    res=set()
    for i in range(length):
        if dict.get(n-i**3) and dict.get(i**3):
            res.add(n-i**3)
            res.add(i**3)
        if len(res)>=4:
            return True
    return False