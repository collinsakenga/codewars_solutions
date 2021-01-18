def zero_plentiful(arr):
    total=0
    temp=[i for i,j in enumerate(arr) if j==0]
    if not temp:
        return 0
    check=[temp[0]]
    for i in range(1, len(temp)):
        if temp[i]-1==check[-1]:
            check.append(temp[i])
        else:
            if len(check)<4:
                return 0
            check=[temp[i]]
            total+=1
    return total+1 if len(check)>=4 else 0