from math import factorial
def choose(n,k):
    return 0 if k>n else factorial(n)//(factorial(k)*factorial(n-k))