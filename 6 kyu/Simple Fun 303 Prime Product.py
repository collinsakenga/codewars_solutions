def prime_product(n):
    low=n//2
    high=(n+1)//2
    while low>=0 and high<=n:
        if is_prime(low) and is_prime(high):
            return low*high
        low-=1
        high+=1
    return 0
def is_prime(n):
    if n<=1 or (n!=2 and n%2==0) or (n!=3 and n%3==0):
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True