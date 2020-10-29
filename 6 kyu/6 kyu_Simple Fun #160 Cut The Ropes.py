from collections import Counter
def cut_the_ropes(arr):
    temp={k:v for k,v in sorted(Counter(arr).items(), key=lambda x: (x[0]))}
    res=[len(arr)]
    for j in temp.values():
        res.append(res[-1]-j)
    return res[:-1]