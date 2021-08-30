def solve(arr):
    arr.sort()
    if arr[0]!=1: return 1
    rec=arr[0]
    for i in range(len(arr)-1):
        if arr[i+1]>(rec+1): 
            return rec+1
        rec+=arr[i+1]
    return rec+1