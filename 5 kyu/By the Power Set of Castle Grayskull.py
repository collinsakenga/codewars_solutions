from itertools import combinations
def power(a):
    if not a: return [[]]
    temp=[]
    for i in range(1,len(a)+1):
        temp.append(list(j) for j in combinations(a, i))
    return [[]]+[j for i in temp for j in i]