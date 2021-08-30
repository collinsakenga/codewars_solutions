from copy import deepcopy
def frequencyDigitsInQueries(arr, queries):
    table={}
    table[-1]={i:0 for i in range(10)}
    for i,j in enumerate(arr):
        new=deepcopy(table[i-1])
        for k in j:
            new[int(k)]+=1
        table[i]=new
    res=[]
    for i,j,k in queries:
        res.append(table[j][k]-table[i-1][k])
    return res