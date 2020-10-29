def expanded_form(num):
    temp=str(num)
    zero=len(temp.split(".")[0])-1
    down="10"
    res=[]
    for i in temp.split(".")[0]:
        if i!="0":
            res.append(i+"0"*zero)
        zero-=1
    for i in temp.split(".")[1]:
        if i!="0":
            res.append(f"{i}/{down}")
        down+="0"
    return " + ".join(res)