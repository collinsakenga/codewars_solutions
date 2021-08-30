from collections import Counter
def solve(a,b):
    if len(b)>len(a):
        return 0
    count1=Counter(a)
    count2=Counter(b)
    total=0
    for i,j in count2.items():
        if not count1.get(i, 0):
            return 0
        elif j>count1.get(i, 0):
            return 0
        total+=j
    return len(a)-total