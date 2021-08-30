from collections import deque
def mirrored_exponential_chunks(arr):
    if not arr:
        return []
    mid=len(arr)//2
    res=deque([[arr[mid]]]) if len(arr)%2 else deque([])
    low, high=mid, mid+1 if len(arr)%2 else mid
    length=2
    while low>0:
        res.appendleft(arr[max(low-length, 0):low])
        res.append((arr[high:min(len(arr), high+length)]))
        low, high=low-length, high+length
        length+=length
    return [i for i in res]
            
    