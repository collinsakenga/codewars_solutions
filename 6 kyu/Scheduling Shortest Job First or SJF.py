from collections import deque
def SJF(jobs, index):
    dict={}
    for i,j in enumerate(jobs):
        if not dict.get(j, None):
            dict[j]=deque([i])
        else:
            dict[j].append(i)
    dict={k:v for k,v in sorted(dict.items(), key=lambda x: x[0])}
    total=0
    for i,j in dict.items():
        while j:
            total+=i
            if j[0]==index:
                return total
            j.popleft()