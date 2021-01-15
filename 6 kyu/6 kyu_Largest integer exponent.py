def get_exponent(n, p):
    if p<=1:
        return None
    count=0
    while n%(p**(count+1))==0:
        count+=1
    return count