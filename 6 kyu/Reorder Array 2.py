def reorder(a, b):
    res=[i for i in range(a)]
    length=len(res)//2
    res=[res[i:i+length] for i in range(0, len(res), length)]
    for i in range(b%length):
        res[0].insert(0, res[0].pop())
        res[1].insert(0, res[1].pop())
    return res