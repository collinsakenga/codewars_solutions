def count_of_heads(initial, n, swings):
    total=initial
    factorial=1
    for i in range(1, swings+1):
        factorial*=i
        total+=+factorial*n-1
    return total