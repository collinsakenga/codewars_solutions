def nearest_larger(arr, i):
    check=arr[i]
    left=0
    right=len(arr)-1
    for j in range(1, max(right-i, i+left)+1):
        if i-j>=left and arr[i-j]>check:
            return i-j
        if i+j<=right and arr[i+j]>check:
            return i+j
    return -1