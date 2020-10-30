from collections import Counter
def vertical_histogram_of(s):
    dict = Counter(i for i in s if i.isupper())
    if not dict:
        return ""
    length = dict.most_common()[0][1]
    temp = {k: v for k, v in sorted(dict.items(), key=lambda x: x[0])}
    res = [[" "]*(len(temp)) for i in range(length+1)]
    for i, (k, v) in enumerate(temp.items()):
        res[-1][i] = k
        for j in range(len(res)-1-v, len(res)-1):
            res[j][i] = "*"
    return "\n".join(" ".join(i).rstrip() for i in res)