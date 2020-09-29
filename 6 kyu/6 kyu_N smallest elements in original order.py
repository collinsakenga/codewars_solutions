def first_n_smallest(arr, n):
    n_smallest = sorted(arr)[:n]
    if not n_smallest:
        return []
    res = []
    for i in arr:
        try:
            n_smallest.remove(i)
            res.append(i)
        except:
            pass
    return res
