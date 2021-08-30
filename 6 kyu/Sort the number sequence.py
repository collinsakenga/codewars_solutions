def sort_sequence(sequence):
    res=[]
    arr=[]
    for i in sequence:
        arr.append(i)
        if i==0:
            res.append(sorted(arr[:-1])+[0])
            arr=[]
    return [j for i in sorted(res, key=lambda list: sum(list)) for j in i]