def find_wrong_way_cow(field):
    dict={}
    for i,j in enumerate(field):
        for k in range(len(j)-2):
            comp="".join(j[k:k+3])
            if not (comp=="cow" or comp=="woc"):
                continue
            if not dict.get(comp, None):
                dict[comp]=[[k, i]] if j[k]=="c" else [[k+2, i]]
            else:
                dict[comp].append([k, i]) if j[k]=="c" else dict[comp].append([k+2, i])
    for j in dict.values():
        if len(j)==1:
            return j[0]
    length=len(field[0])
    for i in range(length):
        for j in range(len(field)-2):
            comp=field[j][i]+field[j+1][i]+field[j+2][i]+"1"
            if not (comp=="cow1" or comp=="woc1"):
                continue
            if not dict.get(comp, None):
                dict[comp]=[[i, j]] if comp[0]=="c" else [[i, j+2]]
            else:
                dict[comp].append([i, j]) if comp[0]=="c" else dict[comp].append([i, j+2])
    for j in dict.values():
        if len(j)==1:
            return j[0]