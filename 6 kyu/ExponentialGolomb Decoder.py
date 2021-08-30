def decoder(sequence):
    res=[]
    index=0
    while index<len(sequence):
        pre=index
        while sequence[index]=="0":
            index+=1
        diff=index-pre+1
        s=""
        for i in range(index, index+diff):
            s+=sequence[i]
        index+=diff
        res.append(int(s, 2)-1)
    return res