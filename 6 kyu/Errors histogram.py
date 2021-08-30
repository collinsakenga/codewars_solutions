def hist(s):
    dict={}
    for i in s:
        if i in "uwxz":
            dict[i]=dict.get(i,0)+1
    res=""
    for i in "uwxz":
        if not dict.get(i, 0):
            continue
        temp=dict[i]*"*"
        temp2=" "*(6-len(str(dict[i])))
        res+=f"{i}  {dict[i]}{temp2}{temp}\r"
    return res[:-1]
    'u  11     ***********\rw  8     ********\rx  14     **************\rz  14     **************'
    'u  11    ***********\rw  8     ********\rx  14    **************\rz  14    **************'