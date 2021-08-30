def more_zeros(s):
    res=[]
    for j in s:
        if j in res:
            continue
        check=bin(ord(j))[2:]
        if check.count("0")>check.count("1"):
            res.append(j)
    return res