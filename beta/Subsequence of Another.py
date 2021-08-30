def subseq(needle, hay): 
    index=0
    for i in hay:
        if index<len(needle) and needle[index]==i:
            index+=1
    return index==len(needle)