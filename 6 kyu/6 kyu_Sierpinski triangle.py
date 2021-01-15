from copy import deepcopy
def sierpinski(n):
    res=[' * ', '* *']
    for i in range(2, n+1):
        temp1=[" "*(2**(i-1))+j+" "*(2**(i-1)) for j in res]
        temp2=[j+" "+j for j in res]
        res=deepcopy(temp1+temp2)
    return "\n".join(res)