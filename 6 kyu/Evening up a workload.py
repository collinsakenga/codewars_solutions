from collections import deque
def split_workload(workload):
    if not workload:
        return (None, None)
    comp=abs(sum(workload))
    index=0
    Jim=deque()
    Bob=deque(workload)
    for i in range(len(workload)+1):
        if comp>abs(sum(Jim)-sum(Bob)):
            comp=abs(sum(Jim)-sum(Bob))
            index=i
        if Bob:
            Jim.append(Bob.popleft())
    return (index, comp) 
            
    