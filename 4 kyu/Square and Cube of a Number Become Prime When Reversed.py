import gmpy2
def memo(n):
    res=[]
    num=89
    while len(res)<n:
        num2=int(str(num**2)[::-1])
        num3=int(str(num**3)[::-1])
        if gmpy2.is_prime(num2) and gmpy2.is_prime(num3):
            res.append(num)
        num+=1
    return res
computed=memo(1000)
def sq_cub_rev_prime(n):
    return computed[n-1]
    