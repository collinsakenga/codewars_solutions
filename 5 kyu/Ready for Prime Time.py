from gmpy2 import next_prime
def prime(n):
    res=[]
    cur=2
    while cur<=n:
        res.append(cur)
        cur=next_prime(cur)
    return res