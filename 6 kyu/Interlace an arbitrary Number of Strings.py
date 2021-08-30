def combine_strings(*args):
    if not args:
        return ""
    length=max(len(i) for i in args)
    res=""
    for i in range(length):
        for j in args:
            try:
                res+=j[i]
            except:
                pass
    return res