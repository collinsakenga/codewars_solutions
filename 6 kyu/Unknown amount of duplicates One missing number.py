from collections import Counter
def find_dups_miss(arr):
    res={k:v for k,v in sorted(Counter(arr).items(), key=lambda x: x[0])}
    value=[i for i in res.keys()]
    return [next((value[i]+value[i+1])//2 for i in range(0, len(value)-1) if (value[i+1]-value[i])!=1), [i for i,j in res.items() if j>1]]