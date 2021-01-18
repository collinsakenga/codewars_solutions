def substring(strng):
    res="" 
    comp=""
    check=set()
    for i in strng:
        check.add(i)
        if len(check)>2:
            check={comp[-1], i}
            res=res if len(res)>=len(comp) else comp
            string=comp[-1]
            for j in range(len(comp)-2, -1, -1):
                if comp[j]!=comp[-1]:
                    break
                string+=comp[j]      
            comp=string+i
        else:
            comp+=i
    return res if len(res)>=len(comp) else comp