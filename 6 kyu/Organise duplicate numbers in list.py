def group(arr):
    return sorted([[i]*arr.count(i) for i in set(arr)], key=lambda x: arr.index(x[0]))