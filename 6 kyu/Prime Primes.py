from gmpy2 import is_prime
from itertools import combinations
def prime_primes(N):
    res=[i for i in range(N) if is_prime(i)]
    total=length=0
    for i,j in combinations(res, 2):
        total+=i/j
        length+=1
    return (length, int(total))