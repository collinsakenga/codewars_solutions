def derivative(eq):
    res={}
    item=""
    for i,j in enumerate(eq+"-"):
        if (i==0 and j=="-") or j not in "+-":
            item+=j
        else:
            if item.startswith("-"):
                res[item.replace("-", "")]="-"
            else:
                res[item.replace("+", "")]="+"
            item=j
    solution=[]
    for i,j in res.items():
        temp=i.split("^")
        if len(temp)==2:
            if temp[1]=="2":
                solution.append(j+str(int(temp[0][:temp[0].index("x")] or "1")*int(temp[1]))+"x")
            else:
                solution.append(j+str(int(temp[0][:temp[0].index("x")] or "1")*int(temp[1]))+"x^"+str(int(temp[1])-1))
        elif len(temp)==1:
            solution.append(j+"0") if "x" not in i else solution.append(j+(i[:i.index("x")] or "1"))
    if solution[-1]=="-0" or solution[-1]=="+0":
        solution.pop()
    return "".join(solution).lstrip("+") or "0" 