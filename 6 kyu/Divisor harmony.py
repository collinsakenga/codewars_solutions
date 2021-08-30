def solve(a,b):
    dict={}
    for i in range(max(a, 1), b):
        temp=factors(i)
        dict[sum(temp)/i]=dict.get(sum(temp)/i, [])+[i]
    return sum(j[0] for j in dict.values() if len(j)>1)
def factors(n):
    res={1, n}
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    return res