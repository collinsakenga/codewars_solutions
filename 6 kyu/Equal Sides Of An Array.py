def find_even_index(array_num):
    compleft=0
    compright=0
    index=-1
    index2=0
    flag=False
    while True:
        for i in range(index2+1,len(array_num)):
            compright+=array_num[i]
        for j in range(index2,0,-1):
            compleft+=array_num[j-1]
        if compleft==compright:
            flag=True
            break
        if index2==len(array_num):
            break
        compleft=0
        compright=0
        index2+=1
    if flag:
        return(index2)
    else:
        return(index)