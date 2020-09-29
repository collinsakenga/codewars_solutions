def index_equals_value(arr):
    start = 0
    end = len(arr)-1
    res = []
    while start <= end:
        mid = (start+end)//2
        if mid == arr[mid]:
            res.append(mid)
            end = mid-1
        elif arr[mid] > mid:
            end = mid-1
        elif arr[mid] < mid:
            start = mid+1
    return min(res) if res else -1
