def max_sum(arr,ranges): 
    value=float("-inf")
    for i in ranges:
        value=max(value, sum(arr[i[0]:i[1]+1]))
    return value