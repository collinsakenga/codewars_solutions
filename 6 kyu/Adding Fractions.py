from fractions import Fraction
def add_fracs(*args):
    res=Fraction()
    for i in args:
        temp=i.split("/")
        res+=Fraction(int(temp[0]), int(temp[1]))
    return str(res) if args else ""