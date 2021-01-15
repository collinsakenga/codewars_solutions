def hashify(string):
    dict={}
    res=string+string[0]
    for i,j in enumerate(string):
        if dict.get(j, None):
            if isinstance(dict[j], str):
                dict[j]=list(dict[j])+[res[i+1]]
            else:
                dict[j].append(res[i+1])
        else:
            dict[j]=res[i+1]
    return dict