from collections import Counter
def find_uniq(arr):
    dict={}
    for i in arr:
        if not i:
            continue
        dict["".join(sorted(set(i.lower())))]=dict.get("".join(sorted(set(i.lower()))), 0)+1
    return next(i for i in set(arr) if i and dict["".join(sorted(set(i.lower())))]==1)