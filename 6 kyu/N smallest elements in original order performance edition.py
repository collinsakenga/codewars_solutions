from collections import defaultdict
def performant_smallest(arr, n):
    table=defaultdict(int)
    for i in arr:
        table[i]+=1
    total=0
    items=[]
    for i,j in sorted(table.items(), key=lambda x: x[0]):
        temp=total
        total+=min(n-total, j)
        items.append((i, total-temp))
        if total==n:
            break
    count=0
    res=[]
    for i in arr:
        if i<items[-1][0]:
            res.append(i)
        elif i==items[-1][0] and count<items[-1][1]:
            res.append(i)
            count+=1
    return res