def backwards_prime(start, stop):
    res=[]
    for i in range(start, stop+1):
        if i%2==0 or i<10 or palindrome(i):
            continue
        if isprime(int(str(i)[::-1])) and isprime(i):
            res.append(i)
    return res
def palindrome(n):
    return str(n)==str(n)[::-1]
def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True