def move_zeros(array):
    total=0
    temp=array.copy()
    for i in range(len(array)):
        if array[i]==0 and type(array[i])!=bool:
            temp.pop(i-total)
            total+=1
    return temp+[0]*total