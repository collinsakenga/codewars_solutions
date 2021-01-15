def memo():
    res=[None]*(2**20)
    for i in range(20):
        start=1
        for j in range(2**(i)-1, 2**20, 2**(i+1)):
            res[j]=start
            start=(start+1)%2
    return res
res=memo()
def paper_fold():
    return iter(res)