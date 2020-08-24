def lcs(x, y):
    print(x, y)
    result = ""
    index2 = 0
    s = ""
    for i in range(0, len(x)):
        n = x[i:]
        try:
            index2 = y.index(x[i])
        except:
            continue
        while index2 < len(y):
            try:
                temp = n.index(y[index2])
                s += n[temp]
                n = n[temp+1:]
            except:
                pass
            index2 += 1
        print(s)
        if len(s) > len(result):
            result = s
        s = ""
    return result
