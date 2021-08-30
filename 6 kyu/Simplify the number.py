def simplify(number):
    multiply="1"+"0"*(len(str(number))-1)
    res=[]
    for i in str(number):
        if i!="0":
            res.append(f"{i}*{multiply}") if multiply!="1" else res.append(f"{i}")
        multiply=multiply[:-1]
    return "+".join(res)