def find_pattern(s):
    compare=[s[i]-s[i-1] for i in range(1, len(s))]
    check=factors(len(compare))
    for i in check:
        comp=compare[:i]
        flag=True
        for j in range(0, len(compare), i):
            comp2=compare[j:j+i]
            if comp2!=comp:
                flag=False
                break
        if flag:
            return comp
def factors(n):
    res=[1]
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            res.append(i)
            res.append(n//i)
    res.append(n)
    return sorted(set(res))
    