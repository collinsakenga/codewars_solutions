from collections import deque
def roundRobin(jobs, slice, index):
    res=deque(i for i in jobs)
    total=0
    count=0
    while True:
        value=res.popleft()
        total+=min(value, slice)
        value-=min(value, slice)
        if value==0 and count%len(jobs)==index:
            break
        count+=1
        res.append(value)
    return total