def tap_code_translation(text):
    table={}
    count=0
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i!="k":
            table[i]=(count//5+1, count%5+1)
            count+=1
        else:
            table[i]=(1, 3)
    res=[]
    for i in text:
        res.append(f"{table[i][0]*'.'} {table[i][1]*'.'}")
    return " ".join(res)
            