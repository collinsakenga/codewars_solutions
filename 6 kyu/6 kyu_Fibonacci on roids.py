from copy import deepcopy
def custom_fib(signature,indexes,n):
    res=deepcopy(signature)
    length=len(signature)
    for i in range(len(res), n+1):
        total=sum(res[-length+j] for j in indexes)
        res.append(total)
    return res[n]