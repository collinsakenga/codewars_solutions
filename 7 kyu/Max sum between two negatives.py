def max_sum_between_two_negatives(arr):
    index=[i for i,j in enumerate(arr) if j<0]
    if len(index)<=1:
        return -1
    return max(sum(arr[index[i-1]:index[i]+1])-arr[index[i-1]]-arr[index[i]] for i in range(1, len(index)))