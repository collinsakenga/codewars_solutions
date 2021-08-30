def even_odd(arr):
    total=0
    for i,j in enumerate(arr):
        if i%2==1:
            total*=j
        else:
            total+=j
    return total