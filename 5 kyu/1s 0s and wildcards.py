def possibilities(param):
    check=[]
    for i,j in enumerate(param):
        if j=="?":
            check.append(i)
    temp=list(param)
    result=[]
    res=generate(param.count("?"),"",[])
    for i in res:
        for j,k in enumerate(i):
            temp[check[j]]=k           
        result.append("".join(temp))
    return result
def generate(len, solution, res):
    if len==0:
        res.append(solution)
    else:
        generate(len-1, solution+"0",res)
        generate(len-1, solution+"1",res)
    return res