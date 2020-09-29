def get_char_count(s):
    dict = {}
    for i in s.lower():
        if not i.isalnum():
            continue
        dict[i] = dict.get(i, 0)+1
    res = {}
    for i, j in dict.items():
        if not res.get(j, None):
            res[j] = []
        res[j].append(i)
    for i in res:
        res[i] = sorted(res[i])
    return {k: v for k, v in sorted(res.items(), reverse=True)}
