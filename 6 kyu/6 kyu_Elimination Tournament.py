def tourney(inp):
    solution=[inp]
    res=inp.copy()
    while len(res)>1:
        temp=[]
        if len(res)%2==0:
            for i in range(0, len(res), 2):
                temp.append(max(res[i], res[i+1]))
            res=temp.copy()
        else:
            temp2=res[-1]
            for i in range(0, len(res)-2, 2):
                temp.append(max(res[i], res[i+1]))
            res=[temp2]+temp.copy()
        solution.append(res)
    return solution