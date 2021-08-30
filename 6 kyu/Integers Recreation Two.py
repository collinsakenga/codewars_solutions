from math import sqrt
def prod2sum(a, b, c, d):
    a=abs(a)
    b=abs(b)
    c=abs(c)
    d=abs(d)
    num=(a**2+b**2)*(c**2+d**2)
    res=[]
    factor=int(sqrt(num)+1)
    while len(res)<2 and factor>0:
        factor-=1
        temp=sqrt(num-factor**2)
        if int(temp)==temp and [int(temp), factor][::-1] not in res:
            comp=int(temp)
            if (a*b+c*d)==comp or abs((a*b-c*d))==comp or (a*c+b*d)==comp or abs((a*c-b*d))==comp or (a*d+c*b)==comp or abs((a*d-c*b))==comp:
                if (a*b+c*d)==factor or abs((a*b-c*d))==factor or (a*c+b*d)==factor or abs((a*c-b*d))==factor or (a*d+c*b)==factor or abs((a*d-c*b))==factor:
                    res.append([comp, factor])
        if temp==0:
            break
    return res