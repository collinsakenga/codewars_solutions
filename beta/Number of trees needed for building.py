from math import ceil
def num_of_trees(arr, num):
    return ceil(sum(i*j for i,j in arr)/num)