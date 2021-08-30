def find_in_array(seq, predicate): 
    for i,j in enumerate(seq):
        if predicate(j, i):
            return i
    return -1