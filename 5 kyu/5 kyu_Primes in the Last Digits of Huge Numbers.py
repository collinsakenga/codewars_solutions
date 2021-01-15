from gmpy2 import is_prime
def k_thlastDigPrime(k):
    res=[0, 1, 1, 2, 4]
    total=0
    while total<k:
        res.append(res[-1]+res[-2]-res[-3]+res[-4]-res[-5])
        temp=str(res[-1])
        if len(temp)<10:
            continue
        if is_prime(int(temp[-9:])):
            total+=1
    return [len(res), int(temp[-9:])]