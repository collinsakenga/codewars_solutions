from collections import Counter
def solve(s):
    dict=Counter(s)
    if len(dict)==1:
        return True
    count={}
    key=0
    for i in dict.values():
        key=i
        count[i]=count.get(i, 0)+1
    if len(count)==1:
        return True if key==1 else False
    elif len(count)>=3:
        return False
    key=[]
    for i,j in count.items():
        key.append(i)
        if i==1 and j==1:
            return True
    return True if (any(i for i in count.values() if i==1)) and abs(key[0]-key[1])==1 else False
l