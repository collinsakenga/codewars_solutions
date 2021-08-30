def csv_columns(csv, indices):
    temp=[i.split(",")for i in csv.split("\n")]
    index=[i for i in sorted(set(indices)) if i<len(temp[0])]
    if not index:
        return ""
    res=[]
    for i in range(len(temp)):
        string=[]
        for j in index:    
            string.append(temp[i][j])
        res.append(",".join(string))
    return "\n".join(res)