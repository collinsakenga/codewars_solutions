def odd_one_out(s):
    temp={}
    temp2={}
    for i in s:
        temp[i]=temp.get(i, 0)+1
    res=[]
    for i in s:
        temp2[i]=temp2.get(i, 0)+1
        if temp[i]%2 and temp2[i]==temp[i]:
            res.append(i)
    return res