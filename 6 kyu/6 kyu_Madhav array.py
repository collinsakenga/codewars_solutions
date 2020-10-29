def is_madhav_array(arr):
    if len(arr)<=1:
        return False
    low=1
    high=3
    increment=3
    compare=arr[0]
    while high<=len(arr):
        if sum(arr[low:high])!=compare:
            return False
        low, high=high, high+increment
        increment+=1
    return True if (high-increment+1)==len(arr) else False