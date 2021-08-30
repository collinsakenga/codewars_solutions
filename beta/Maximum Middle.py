from collections import deque
def maximum_median(arr, length):
    res=deque(arr[:length])
    ans=float("-inf")
    for i in range(length, len(arr)+1):
        ans=max(ans, res[length//2])
        if i==len(arr):
            break
        res.popleft()
        res.append(arr[i])
    return ans