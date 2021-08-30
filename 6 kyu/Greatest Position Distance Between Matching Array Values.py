def greatest_distance(arr):
    dict={}
    for i,j in enumerate(arr):
        if dict.get(j, None)==None:
            dict[j]=[i]
        else:
            dict[j].append(i)
    return max(i[-1]-i[0] for i in dict.values())