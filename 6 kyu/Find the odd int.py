def find_it(seq):
    for index in seq:
        if seq.count(index)%2!=0:
            return index
