def revrot(strng, sz):
    if sz>len(strng) or sz<=0:
        return ""    
    res=[]
    temp=""
    for i in range(1,len(strng)+1):
        temp+=strng[i-1]
        if i%sz==0:
            res.append(temp)
            temp=""
    result=""
    for i in res:
        action=sum([int(j) for j in list(i)])
        if action%2==0:
            result+=i[::-1]
        else:
            result+=i[1:]+i[0]
    return result