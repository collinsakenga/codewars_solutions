def solve(n):
    if n%2 and is_prime(n):
        return n
    index=0
    while index<n:
        index+=1
        if ((n-index)%2 and is_prime(n-index)):
            return n-index
        if ((n+index)%2 and is_prime(n+index)):
            return n+index
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True