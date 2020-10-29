def reduce_pyramid(base):
    length=len(base)-1
    if length<=1:
        return sum(base)
    res=[1]
    for i in range(length):
        res.append(res[i] * (length-i) // (i+1))
    return sum(i*j for i,j in zip(base, res))