def wheat_from_chaff(values):
    last=len(values)-1
    for i, j in enumerate(values):
        if j<0:
            continue
        rec=last
        while values[last]>=0:
            last-=1
        if i>=last:
            break
        values[last], values[i]=values[i], values[last]
        if rec==last:
            last-=1
    return values