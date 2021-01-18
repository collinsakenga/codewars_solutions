def cycle(sequence):
    dict={}
    for i,j in enumerate(sequence):
        if dict.get(j, -1)<0:
            dict[j]=i
        else:
            return [dict[j], i] if not dict[j] else [dict[j], i-1]
    return []