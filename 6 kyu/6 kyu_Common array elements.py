from collections import Counter
def common(a,b,c):
    temp1, temp2, temp3=Counter(a), Counter(b), Counter(c)
    total=0
    for i in set(a+b+c):
        total+=min(temp1.get(i, 0), temp2.get(i, 0), temp3.get(i, 0))*i
    return total