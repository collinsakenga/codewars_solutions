def de_nico(key,msg):
    dict=[]
    for i in key:
        dict.append([i])
    for i,j in enumerate(msg):
        dict[i%len(dict)].append(j)
    for i in range(len(dict)):
        dict[i]=[dict[i][:1]]+[dict[i][1:]]
    string="".join(sorted(key))
    res=[]
    for i in range(len(dict)):
        res.append(dict[string.index(dict[i][0][0])][1])
    solution=""
    maxlen=0
    for i in res:
        maxlen=max(len(i), maxlen)
    for i in range(maxlen):
        for j in range(len(res)):
            try:
                solution+=res[j][i]
            except:
                pass
    return solution.rstrip()