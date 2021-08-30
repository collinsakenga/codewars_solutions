def find_opposites(seq): 
    check=set()
    res=set()
    for i in seq:
        if -i in check:
            res.add(abs(i))
        check.add(i)
    return sorted(res)