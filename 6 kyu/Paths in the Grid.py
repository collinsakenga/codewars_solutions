from math import factorial
def number_of_routes(m, n):
    return factorial(m+n)//factorial(m)//factorial(n)