from collections import deque
def circularly_sorted(arr):
    res=deque(arr)
    compare=deque(sorted(arr))
    for i in range(len(arr)+1):
        if res==compare:
            return True
        res.append(res.popleft())
    return False