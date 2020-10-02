def rankings(arr):
    dict = {}
    rank = sorted(arr, reverse=True)
    for i, j in enumerate(rank):
        dict[j] = i+1
    return [dict[i] for i in arr]
