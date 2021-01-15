from copy import deepcopy
def remove_smallest(n, arr):
    arr=deepcopy(arr)
    count=0
    while arr and count<n:
        arr.remove(min(arr))
        count+=1
    return arr