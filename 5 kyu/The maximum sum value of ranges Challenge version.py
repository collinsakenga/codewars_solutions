from itertools import accumulate
def max_sum(a, ranges):
    res=[0]+list(accumulate(a))
    return max(res[j+1]-res[i] for i,j in ranges)