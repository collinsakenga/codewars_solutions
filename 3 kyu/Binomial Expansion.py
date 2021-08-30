import re
from math import factorial
def expand(expr):
    power=expr.split("^")
    if power[1]=="0":
        return "1"
    start=int(power[1])
    power[0]=power[0][1:-1]
    flag1=True if power[0][0]!="-" else False
    if not flag1: power[0]=power[0][1:]
    flag2=True if "+" in power[0] else False
    plus_minus="+" if (flag1 and flag2) else "-" if (not flag1 and not flag2) else ""
    if (not flag1 and not flag2 and start%2==0): plus_minus="+"
    coefficient=re.split("[+-]", power[0])
    letter=coefficient[0][-1]
    coefficient[0]="1" if len(coefficient[0])==1 else coefficient[0][:-1]
    for i,j in enumerate(coefficient):
        coefficient[i]=int(j)
    res=""
    rec=start
    while start>=0:
        product=combination(rec, start)*coefficient[0]**(start)*coefficient[1]**(rec-start)
        if product==1 and start!=0:
            product=""
        if plus_minus:
            res+=f"{plus_minus}{product}{letter}^{start}" if start>1 else f"{plus_minus}{product}{letter}" if start==1 else f"{plus_minus}{product}"
        else:
            temp="+" if (not flag1 and start%2==0) else "+" if (not flag2 and (rec-start)%2==0) else "-"
            res+=f"{temp}{product}{letter}^{start}" if start>1 else f"{temp}{product}{letter}" if start==1 else f"{temp}{product}"
        start-=1
    return res[1:] if res[0]=="+" else res
def combination(n, c):
    return factorial(n)//(factorial(c)*factorial(n-c))