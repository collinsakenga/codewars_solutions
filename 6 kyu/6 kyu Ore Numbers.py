from fractions import Fraction
def is_ore(n):
    temp=prime(n)
    down=Fraction()
    for i in temp:
        down+=Fraction(1, i)
    res=len(temp)/down
    return True if res.denominator==1 else False
def prime(n):
    res={1, n}
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    return res