from itertools import product
def memo():
    res=[0]
    for i in range(6):
        for j in (p for p in product("0123456789", repeat=i+1) if p[0]!="0"):
            temp="".join(j)
            res.append(int(temp+temp[-2::-1]))
            res.append(int(temp+temp[::-1]))
    return sorted(res)
res=memo()
def find_reverse_number(n):
    return res[n-1]