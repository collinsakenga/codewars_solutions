from math import factorial
def nth_catalan_number(n):
    return factorial(n*2)//(factorial(n)*factorial(n))//(n+1)