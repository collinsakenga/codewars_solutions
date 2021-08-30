from math import pi, log
dict={i:j for i,j in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
def converter(n, decimals=0, base=pi):
    if n==0:
        return "0" if not decimals else "0."+"0"*decimals
    num=abs(n)
    res="-" if n<0 else ""
    pow=int(log(num, base))
    for i in range(pow, -1-decimals, -1):
        if i==-1:
            res+="."
        each=int(num/(base**i))
        res+=dict[each]
        num-=each*(base**i)
    return res