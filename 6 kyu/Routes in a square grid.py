from math import factorial
def routes(n):
    if n<=0:
        return 0
    return (factorial(n*2)//(factorial(n)**2))