def uniq(seq): 
    index=0
    for i in range(len(seq)-1):
        if seq[i+1-index]==seq[i-index]:
            seq.pop(i-index)
            index+=1
    return seq