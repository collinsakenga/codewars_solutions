def twos_difference(lst): 
    res=[]
    check=sorted(lst)
    for i in range(len(check)):
        temp=check[i]
        for j in range(i+1, len(check)):
            if (check[j]-temp)==2:
                res.append((temp, check[j]))
            elif (check[j]-temp)>2:
                break
    return res