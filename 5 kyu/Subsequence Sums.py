from itertools import accumulate
from collections import Counter
def subsequence_sums(arr, s):
    res=list(accumulate(arr))
    table=Counter(res)
    total=0
    for i in res:
        table[i]-=1
        total+=table[i+s]
    return total+res.count(s)