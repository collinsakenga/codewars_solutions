def max_sequence(arr):
    total=0
    record=0
    for i in range(len(arr)):
        total+=arr[i]
        if total<0:
            total=0
        if total>record:
            record=total
    return record