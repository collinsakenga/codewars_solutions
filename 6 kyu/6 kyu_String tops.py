def tops(msg):
    res = []
    total = 2
    count = 2
    string = ""
    while total <= len(msg):
        res.append(total)
        total += 2*count+1
        count += 2
    return "".join(msg[i-1] for i in res)[::-1]
