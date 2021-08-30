from gmpy2 import is_prime
def prime_or_composite(n):
    return ["Composite", "Probable Prime"][is_prime(n)]