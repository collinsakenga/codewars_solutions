def sel_reverse(arr,l):
    if not l:
        return arr
    res=[]
    for i in range(0, len(arr), l):
        res.extend(arr[i:i+l][::-1])
    return res