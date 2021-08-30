from itertools import permutations
from gmpy2 import is_prime
memo={i: (True if is_prime(i) else False) for i in range(10, 100001)}
def permutational_primes(n_max, k_perms):
    res=[]  
    search={}
    for i in range(10, n_max+1):
        if not memo[i] or search.get(i, None):
            continue
        temp=str(i)     
        count=0
        primes=set()
        for j in set(permutations(str(i))):
            if count>k_perms:
                break
            num="".join(j)
            if num==temp or num[0]=="0":
                continue
            num=int(num)
            if num<n_max and memo[num]:
                count+=1
                primes.add(num)
        if count==k_perms:
            for p in primes:
                search[p]=p
            res.append(i)
    if not res:
        return [0,0,0]
    return [len(res), min(res), max(res)]