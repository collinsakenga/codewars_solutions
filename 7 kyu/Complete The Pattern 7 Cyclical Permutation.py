from math import log
def pattern(n):
    string="".join([str(i) for i in range(1,n+1)])
    res=""
    index=0
    for i in range(n):
        if i: index+=int(log(i,10))
        res+=string[i+index:]+string[:i+index]+"\n"
    return res[:-1]