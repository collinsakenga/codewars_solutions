def fcfs(processes):
    CT=TAT=WT=T=cur=0
    for i in processes:
        WT+=max(0, cur-i[0])
        cur=max(i[0], cur)+i[1]
        CT+=cur
        TAT+=cur-i[0]
        T+=i[1]
    return tuple(round(i/len(processes), 2) for i in (CT, TAT, WT, T))