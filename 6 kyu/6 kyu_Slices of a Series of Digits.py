def series_slices(digits, n):
    if n>len(digits):
        raise Exception()
    res=[]
    for i in range(0, len(digits)-n+1):
        res.append([int(j) for j in digits[i:i+n]])
    return res