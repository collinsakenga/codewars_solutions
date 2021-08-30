def oddity(n):
    if n==1:
        return "odd"
    elif is_prime(n):
        return "even"
    return "odd" if str(n**0.5)[-2:]==".0" else "even"
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True