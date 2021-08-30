from itertools import product
def reg_sum_hits(n, s):
    dict={}
    for i in product(list(range(1, s+1)), repeat=n):
        dict[sum(i)]=dict.get(sum(i), 0)+1
    return [[i, j] for i,j in dict.items()]