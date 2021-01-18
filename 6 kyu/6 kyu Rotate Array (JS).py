from collections import deque
def rotate(arr, n):
    res=deque(arr)
    for i in range(n%len(arr)):
        res.appendleft(res.pop())
    return list(res)