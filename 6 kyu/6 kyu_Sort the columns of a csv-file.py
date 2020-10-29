def sort_csv_columns(csv):
    res=[None]*len(csv.split("\n")[0].split(";"))
    for i,j in enumerate(csv.split("\n")):
        for k,l in enumerate(j.split(";")):
            if not res[k]:
                res[k]=[l]
            else:
                res[k].append(l)
    temp=sorted(res, key=lambda x: (alpha(x[0])))
    string=[]
    for i in range(len(temp[0])):
        temp2=[]
        for j in range(len(temp)):
            temp2.append(temp[j][i])
        string.append(";".join(temp2))
    return "\n".join(string)
def alpha(s):
    return s.lower()