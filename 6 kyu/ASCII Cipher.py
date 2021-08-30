def ascii_cipher(message, key):
    neg_flag=True if key<0 else False
    key=abs(key)
    change=-max(factorization(key)) if neg_flag else max(factorization(key))
    return "".join(chr((ord(i)+change)%128) for i in message)
def factorization(n):
    factor=2
    res=[]
    while factor*factor<=n:
        if n%factor==0:
            res.append(factor)
            n//=factor
            factor=2
        else:
            factor+=1
    res.append(n)
    return res
    