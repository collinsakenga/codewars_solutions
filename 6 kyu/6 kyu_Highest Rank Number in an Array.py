def highest_rank(arr):
    count = 0
    highest = 0
    for i in set(arr):
        if arr.count(i) == count:
            highest = max(i, highest)
        elif arr.count(i) > count:
            count = arr.count(i)
            highest = i
    return highest
