def arrange(strng):
    if not strng:
        return ""
    temp=strng.split()
    res=[]
    for i in range(len(temp)-1):
        if i%2==0:
            if len(temp[i])>len(temp[i+1]):
                temp[i], temp[i+1]=temp[i+1], temp[i]
            res.append(temp[i].lower())
        else:
            if len(temp[i])<len(temp[i+1]):
                temp[i], temp[i+1]=temp[i+1], temp[i]
            res.append(temp[i].upper())
    return " ".join(res+[temp[-1].upper() if len(temp)%2==0 else temp[-1].lower()])