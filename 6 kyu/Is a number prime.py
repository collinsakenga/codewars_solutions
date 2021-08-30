from math import sqrt
def is_prime(num):
    if num<=1:
        return False
    else:
        sq_root=int(sqrt(num))
        for modulus in range(2,sq_root+1):
            if num%modulus==0:
                return False
    return True