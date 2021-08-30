def lyrics_print(lyrics):
    res=[]
    for i in lyrics:
        temp=[]
        for j in i:
            s=""
            for char in j:
                s+=char
                res.append(temp+[s+"_"])
            temp.append(j)
    return res