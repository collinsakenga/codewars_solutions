def some_but_not_all(seq, pred): 
    if all(pred(i) for i in seq):
        return False
    return any(pred(i) for i in seq)