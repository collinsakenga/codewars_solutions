def sum_of_squares(n):
    if n**0.5==int(n**0.5):
        return 1
    num=n
    while num%4==0:
        num//=4
    if (num-7)%8==0:
        return 4
    pow=1
    increment=3
    while pow<n: 
        if (n-pow)**0.5==int((n-pow)**0.5):
            return 2
        pow, increment=pow+increment, increment+2
    return 3