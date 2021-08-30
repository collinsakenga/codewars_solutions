def nth_smallest(arr, n):
    return sorted(set(arr))[n-1] if n<=len(set(arr)) else None