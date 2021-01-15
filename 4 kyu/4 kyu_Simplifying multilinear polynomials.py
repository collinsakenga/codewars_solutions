def simplify(poly):
    dict={}
    temp=""
    flag=True
    for j in (poly+"+"):
        if j in "+-":
            if not temp:
                flag=True if j=="+" else False
                continue
            digits=int(temp[:next(i for i,k in enumerate(temp) if not k.isdigit())] or "1")
            temp="".join(sorted(temp))
            variable=temp if digits==1 else temp[len(str(digits)):]
            dict[variable]=dict.get(variable, 0)+(digits if flag else -digits)
            temp=""
            flag=True if j=="+" else False
        else:
            temp+=j
    res=sorted({k:v for k,v in dict.items() if v!=0}.items(), key=lambda x:(len(x[0]), x[0]))
    polynomial=""
    for i,j in enumerate(res):
        polynomial+=("+" if j[1]>0 else "-")+("" if abs(j[1])==1 else str(abs(j[1])))+j[0]
    return polynomial.lstrip("+")