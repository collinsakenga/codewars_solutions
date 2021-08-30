from itertools import product
def dni_solver(dni):
    if dni[-1]!="?" and "?" not in dni:
        return [dni]
    elif dni[-1]=="?":
        return [f"{dni[:-1]}{'TRWAGMYFPDXBNJZSQVHLCKE'[int(dni[:-1])%23]}"]
    res=[]
    indexes=[i for i,j in enumerate(dni) if j=="?"]
    arr=list(dni)
    for i in product("0123456789", repeat=len(indexes)):
        for j,k in zip(indexes, i):
            arr[j]=k
        s="".join(arr)
        if int(s[:-1])%23=='TRWAGMYFPDXBNJZSQVHLCKE'.index(s[-1]):
            res.append(s)
    return res