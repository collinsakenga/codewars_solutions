from math import factorial
def generate_diagonal(n, l):
    start=n+l-1
    res=[]
    for i in range(start, n-1, -1):
        res=[combination(i, n)]+res
    return res
def combination(large, small):
    return factorial(large)//(factorial(small)*factorial(large-small))