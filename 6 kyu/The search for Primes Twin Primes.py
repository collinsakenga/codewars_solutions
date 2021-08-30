from gmpy2 import next_prime
def twin_prime(n):
    if n<5:
        return 0
    total=0
    start=2
    while start<n:
        prev=start
        start=next_prime(prev)
        if start-prev==2:
            total+=1
    return total