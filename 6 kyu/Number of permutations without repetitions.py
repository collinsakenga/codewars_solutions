from math import factorial
from collections import Counter
def perms(element):
    res=factorial(len(str(element)))
    for j in Counter(str(element)).values():
        res//=factorial(j)
    return res