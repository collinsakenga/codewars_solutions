def prime_word(array):
    res=[]
    for i in array:
        flag=any(is_prime(ord(j)+i[1]) for j in i[0])
        res.append(1) if flag else res.append(0)
    return res
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True