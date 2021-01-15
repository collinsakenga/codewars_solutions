from math import ceil
def even_digit_squares(a, b):
    res=[]
    for i in range(ceil(a**0.5), ceil(b**0.5)):
        if all(int(j)%2==0 for j in str(i**2)):
            res.append(i**2)
    return res+[b] if b**0.5==ceil(b**0.5) and all(int(j)%2==0 for j in str(b)) else res