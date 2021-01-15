from collections import Counter
from gmpy2 import is_prime
def gen_prime():
    dict={}
    count=0
    for i in range(2, 10001):
        if is_prime(i):
            dict[i]=count
            count+=1
    return dict
primes=gen_prime()
code={1: '()', 2: '(())', 3: '(.())', 4: '((()))', 5: '(..())', 6: '(()())', 7: '(...())', 8: '((.()))', 9: '(.(()))', 10: '(().())', 11: '(....())', 12: '((())())', 13: '(.....())'}
def puzzle(integer):
    if integer<=1:
        return "." if integer==0 else "()"
    res=[]
    temp=sorted(Counter(prime_factorization(integer)).items(), key=lambda x: -x[0])
    for i,j in enumerate(temp):
        if i==0:
            res=["."]*(primes[j[0]]+1)
            res[-1]=code[j[1]]
        else:
            res[primes[j[0]]]=code[j[1]]
    return "("+"".join(res)+")"
def prime_factorization(n):
    res=[]
    factor=2
    while factor*factor<=n:
        if n%factor==0:
            n//=factor
            res.append(factor)
            factor=2
        else:
            factor+=1
    return res+[n]