def diag_2_sym(s):
    temp=s.split("\n")
    res=[[None]*len(temp[i]) for i in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            res[i][j]=temp[len(temp[i])-1-j][len(temp)-1-i]
    return "\n".join(("".join(i) for i in res))
def rot_90_counter(s):
    temp=s.split("\n")
    res=[[None]*len(temp[i]) for i in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            res[i][j]=temp[j][len(temp)-1-i]
    return "\n".join(("".join(i) for i in res))
def selfie_diag2_counterclock(s):
    temp=s.split("\n")
    temp2=diag_2_sym(s).split("\n")
    temp3=rot_90_counter(s).split("\n")
    res=[]
    for i in range(len(temp)):
        res.append(f"{temp[i]}|{temp2[i]}|{temp3[i]}")
    return "\n".join(("".join(i) for i in res))
def oper(fct, s):
    return fct(s)