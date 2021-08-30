from math import ceil
def ab(a, b):
    return ceil(sum(int(i) for i in str(a))/sum(int(i) for i in str(b)))