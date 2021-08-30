from fractions import Fraction
def decompose(n):
    temp=Fraction(n)
    res=[]
    if temp.denominator==1:
        return [str(temp)] if n!="0" else []
    while temp.numerator!=1:
        res.append(f"{1}/{temp.denominator//temp.numerator+1}") if temp.denominator//temp.numerator!=0 else res.append("1")
        temp=temp-Fraction(1, temp.denominator//temp.numerator+1)
    return res+[f"{temp.numerator}/{temp.denominator}"]
    