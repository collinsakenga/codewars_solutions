def count_inversions(array):
    total=0
    while True:
        flag=True
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                array[i], array[i+1]=array[i+1], array[i]
                flag=False
                break
        if flag:
            break
        total+=1
    return total