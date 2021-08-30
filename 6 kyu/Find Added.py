from collections import Counter
def findAdded(st1, st2):
    temp1=Counter(st1)
    temp2=Counter(st2)
    res=""
    for i,j in temp2.items():
        if not temp1.get(i, None):
            res+=i*j
        elif temp2[i]>temp1[i]:
            res+=i*(j-temp1[i])
    return "".join(sorted(res))