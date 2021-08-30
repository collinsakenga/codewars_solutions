from itertools import product
from gmpy2 import is_prime
numbers=sorted([i for i in product([i for i in range(100)], repeat=2)], key=lambda x: (2**x[0]*3**x[1]))
def solve(x,y):
    return sum(y>=(2**m*3**n+1)>=x and is_prime(2**m*3**n+1) for m, n in numbers)
