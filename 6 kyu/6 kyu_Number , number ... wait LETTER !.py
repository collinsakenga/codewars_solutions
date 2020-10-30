def do_math(s):
    dict={}
    res=[]
    for index,i in enumerate(s.split()):
        char, integer="", ""
        for j in i:
            if j.isalpha():
                char+=j
            else:
                integer+=j
        dict[integer]=(char, index)
        res.append(integer)
    res=sorted(res, key=lambda x: (dict[x][0], dict[x][1]))
    solution=[int(res[0])] 
    for i in range(1, len(res)):
        if (i-1)%4==0:
            solution.append(solution[-1]+int(res[i]))
        elif (i-1)%4==1:
            solution.append(solution[-1]-int(res[i]))
        elif (i-1)%4==2:
            solution.append(solution[-1]*int(res[i]))
        else:
            solution.append(solution[-1]/int(res[i]))
    return round(solution[-1])