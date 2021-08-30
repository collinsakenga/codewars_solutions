from itertools import permutations
from math import ceil
def count_hits_powterm (dig_list, pow_):
    highest="".join(sorted((str(i) for i in dig_list), reverse=True))
    dict={i:-1 for i in set(int("".join(j)) for i in range(len(highest)) for j in permutations(highest, i+1))}
    arr=[i**pow_ for i in range(1, ceil(int(highest)**(1/pow_)))]
    res=set()
    for i in range(len(arr)):
        total=arr[i]
        for j in range(i+1, len(arr)):
            if dict.get(total, None):
                res.add(total)
            total+=arr[j]
        if dict.get(total, None): 
            res.add(total)
    return (len(res), sorted(res))