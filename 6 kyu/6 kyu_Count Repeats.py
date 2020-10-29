def count_repeats(txt):
    res=txt[0]
    for i in txt[1:]:
        if i==res[-1]:
            continue
        res+=i
    return len(txt)-len(res)