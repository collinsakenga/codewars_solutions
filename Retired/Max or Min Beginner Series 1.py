def max_or_min(arr):
    try:
        return min(arr) if sum(arr)%2 else max(arr)
    except:
        return "INVALID INPUT"