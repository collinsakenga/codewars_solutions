def proofread(string):
    res = string.lower().split(".")
    for i, j in enumerate(res):
        if not j:
            continue
        res[i] = j.split()
        for k, l in enumerate(res[i]):
            res[i][k] = l.replace("ie", "ei")
        res[i][0] = res[i][0].capitalize()
        res[i] = " ".join(res[i])
    return ". ".join(res).rstrip(" ")
