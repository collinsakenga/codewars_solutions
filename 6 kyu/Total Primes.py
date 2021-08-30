from itertools import product
def get_total_primes(a, b):
    total=0 if a>5 else 1 if a>2 else 2
    for i in range(len(str(a)), len(str(b))+1):
        for j in product("2357", repeat=i):
            prime=int("".join(j))
            if prime%10==2 or prime%10==5 or prime<a or prime>=b:
                continue
            if is_prime(prime):
                total+=1 
    return total
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True