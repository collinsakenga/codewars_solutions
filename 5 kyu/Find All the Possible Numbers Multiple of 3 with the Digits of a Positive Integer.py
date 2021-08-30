from itertools import combinations, permutations
def find_mult_3(num):
    s=str(num)
    res=set(j for i in range(len(s)) for j in combinations(s, i+1) if sum(int(k) for k in j)%3==0)
    res2=set(j for i in res for j in permutations(i, len(i)) if j[0]!="0")
    return [len(res2), max((int("".join(i)) for i in res2))]