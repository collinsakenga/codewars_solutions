from math import factorial
def nth_perm(n,d):
    string=list("0123456789"[:d])
    num=d
    res=""
    while num:
        index=(n-1)//factorial(num-1)
        res+=string[index]
        string.pop(index)
        n-=index*(factorial(num-1))
        num-=1
    return res